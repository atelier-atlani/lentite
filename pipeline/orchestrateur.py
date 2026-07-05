#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""
L'Entité — Orchestrateur du pipeline M01 (texte source → YAML M01-M validé).

Architecture hexagonale légère (décision 001) : ce module importe le cœur
(schemas.py) ; le cœur n'importe jamais l'orchestration. L'appel au modèle
de langage est isolé derrière le port `AgentCaller` — l'adaptateur concret
(`AnthropicAgentCaller`) est le seul point de dépendance au SDK Anthropic ;
`run_pipeline` accepte n'importe quel objet conforme au port, ce qui permet
de tester la plomberie de retry/log sans appel réseau réel.

Pipeline linéaire à quatre agents fonctionnels (pipeline/agents/fonctionnels/,
tâche 2.5, prompts v2.0 depuis le lot 2.8) : Charité → Vulnérabilités →
Chaînes causales → Synthèse → assemblage YAML → validation
(schemas.M01Analysis, cœur de validate.py). En cas d'échec de validation, le
rapport d'erreurs est réinjecté à l'agent Synthèse, deux itérations maximum,
puis échec propre avec logs.

Sortie structurée JSON par agent (lot 2.8, correctif structurel prescrit par
`.claude/reviews/revue_002.md` §4 point 1) — chaque agent produit un JSON
conforme à son fragment de schéma (pipeline/agent_schemas.py), contraint
côté serveur par `output_config.format` du SDK Anthropic. Le modèle n'écrit
plus lui-même de YAML : la génération de texte libre en YAML nu était la
cause structurelle de l'échec du lot 2.7 (prose française contenant des
deux-points ou des citations, rompant la syntaxe de scalaires non
guillemetés — trois occurrences indépendantes, cf. rapport_implementation_002
§3 et revue_002.md §2.3). La conversion JSON→YAML est désormais mécanique,
faite par l'orchestrateur lui-même (`dump_yaml_forcing_quotes`), jamais par
le modèle.

Logs — un fichier JSON par appel d'agent (tâche 2.6), dans
pipeline/analyses/<analysis_id>/logs/, versionnés avec le YAML produit
(traces de production, pas des vues dérivées — contrairement aux exports
du graphe). Le champ `reponse_brute` contient désormais le JSON brut de
l'agent (auparavant du YAML potentiellement mal formé) — une trace plus
fidèle de l'échange réel avec le modèle.

Clé API lue exclusivement depuis la variable d'environnement
ANTHROPIC_API_KEY — jamais acceptée en argument CLI, jamais codée en dur.

Usage:
    python3 orchestrateur.py <texte_source.txt> <analysis_id> [--model MODELE]

Constat empirique (lot 2.8, exécution réelle) — `output_config.format`
réduit fortement mais n'élimine pas le risque de JSON syntaxiquement
malformé (virgule finale avant crochet/accolade fermante, observée deux
fois indépendamment sur l'agent Charité) ; `parse_json_fragment` répare
mécaniquement cette classe d'erreur avant analyse JSON.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Protocol

import yaml
from pydantic import BaseModel, ValidationError

from schemas import M01Analysis
from agent_schemas import AGENT_OUTPUT_MODELS

DEFAULT_MODEL = "claude-sonnet-5"
MAX_ITERATIONS = 2
AGENTS_DIR = Path(__file__).parent / "agents" / "fonctionnels"

# Ordre du pipeline linéaire — les trois premiers agents s'exécutent une
# fois ; l'agent Synthèse boucle jusqu'à MAX_ITERATIONS sur échec de
# validation (réinjection du rapport d'erreurs). Prompts v2.0 (lot 2.8) —
# sortie JSON structurée, schéma de sortie dans pipeline/agent_schemas.py.
PRIOR_AGENTS = [
    ("charite", "prompt_charite_v2_0.md"),
    ("vulnerabilites", "prompt_vulnerabilites_v2_0.md"),
    ("chaines_causales", "prompt_chaines_causales_v2_0.md"),
]
SYNTHESE_AGENT = ("synthese", "prompt_synthese_v2_0.md")


# ============================================================================
# PORT HEXAGONAL — abstraction de l'appel au modèle de langage
# ============================================================================


class AgentCaller(Protocol):
    """Port — un appelant conforme reçoit (modèle, prompt complet, schéma de
    sortie structurée de l'agent) et retourne (réponse_brute JSON, usage_tokens).
    Le cœur du pipeline ne connaît que cette interface, jamais le SDK concret."""

    def __call__(self, model: str, prompt: str, output_schema: type[BaseModel]) -> tuple[str, dict]: ...


class AnthropicAgentCaller:
    """Adaptateur SDK Anthropic direct (tâche 2.4, sortie JSON structurée
    depuis le lot 2.8). Import du SDK différé au constructeur — un objet de
    ce type n'est instancié que pour une exécution réelle, jamais pour les
    tests de plomberie."""

    def __init__(self) -> None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY absente de l'environnement. La clé API n'est "
                "jamais acceptée autrement — pas d'argument CLI, pas de valeur "
                "codée en dur (discipline tâche 2.4)."
            )
        import anthropic
        from anthropic.resources.messages.messages import transform_schema

        self._client = anthropic.Anthropic(api_key=api_key)
        self._transform_schema = transform_schema

    def __call__(self, model: str, prompt: str, output_schema: type[BaseModel]) -> tuple[str, dict]:
        # thinking désactivé explicitement : sur claude-sonnet-5, omettre le
        # paramètre active le raisonnement étendu adaptatif par défaut (à la
        # différence d'Opus 4.7/4.8). Constaté à l'exécution réelle tâche 2.7 —
        # sur un prompt long (discours source intégral inclus), le modèle a pu
        # consacrer la totalité du budget de sortie au bloc de raisonnement
        # interne, laissant zéro token pour la réponse attendue. Les agents
        # fonctionnels sont des tâches d'extraction déterministe suivant une
        # procédure prescrite par le prompt — le raisonnement du modèle n'y
        # apporte rien, donc coupé plutôt que budgété.
        #
        # max_tokens=64000 en streaming : nécessaire même une fois thinking
        # coupé — la réponse Charité seule sur un discours réel a atteint
        # stop_reason="max_tokens" à 16000 tokens (tâche 2.7). Le streaming
        # est requis par le SDK au-delà d'environ 16000 tokens de sortie en
        # mode non-streaming (garde-fou contre les timeouts HTTP).
        #
        # output_config.format (lot 2.8, revue_002.md §4 point 1) : contraint
        # fortement la sortie vers du JSON conforme au schéma de l'agent —
        # élimine la classe d'erreur diagnostiquée au lot 2.7 (YAML nu mal
        # formé par le modèle, conflit prose-riche/YAML-nu). Constat empirique
        # du lot 2.8 : ne garantit pas pour autant l'absence de toute
        # malformation JSON (virgule finale observée deux fois indépendamment
        # sur l'agent Charité, réparée mécaniquement par `parse_json_fragment`
        # plutôt que traitée comme un échec). `transform_schema` est un
        # utilitaire interne du SDK (anthropic==0.116.0, version épinglée) qui
        # assainit le schéma JSON généré par Pydantic (contraintes non
        # supportées par l'API — minLength, minItems, minimum/maximum —
        # déplacées en description) ; utilisé ici plutôt que la méthode
        # publique `messages.parse()` parce que celle-ci force une requête
        # non-streaming côté transport (vérifié empiriquement), ce qui
        # déclenche le même garde-fou de timeout à max_tokens=64000.
        schema = self._transform_schema(output_schema)
        with self._client.messages.stream(
            model=model,
            max_tokens=64000,
            thinking={"type": "disabled"},
            output_config={"format": {"type": "json_schema", "schema": schema}},
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            response = stream.get_final_message()
        text = "".join(block.text for block in response.content if block.type == "text")
        usage = {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
        }
        return text, usage


# ============================================================================
# LOGS — tâche 2.6
# ============================================================================


@dataclass
class AgentCallRecord:
    """Contenu exact de l'artefact de log par appel d'agent (tâche 2.6)."""

    agent: str
    version_prompt: str
    modele: str
    horodatage_iso: str
    iteration: int
    prompt_complet: str
    reponse_brute: str
    usage_tokens: dict


def write_agent_log(analysis_dir: Path, n: int, record: AgentCallRecord) -> Path:
    """Écrit pipeline/analyses/<analyse>/logs/<n>_<agent>_<horodatage>.json.
    Versionné avec le YAML de l'analyse — trace de production, pas une vue
    dérivée (contrairement aux exports du graphe, décision 002)."""
    logs_dir = analysis_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    horodatage_fichier = record.horodatage_iso.replace(":", "").replace("-", "")
    path = logs_dir / f"{n}_{record.agent}_{horodatage_fichier}.json"
    path.write_text(
        json.dumps(
            {
                "agent": record.agent,
                "version_prompt": record.version_prompt,
                "modele": record.modele,
                "horodatage_iso": record.horodatage_iso,
                "iteration": record.iteration,
                "prompt_complet": record.prompt_complet,
                "reponse_brute": record.reponse_brute,
                "usage_tokens": record.usage_tokens,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return path


# ============================================================================
# ASSEMBLAGE DES PROMPTS ET DES FRAGMENTS
# ============================================================================


def load_prompt(filename: str) -> tuple[str, str]:
    """Charge un prompt versionné. Retourne (contenu, version) — la version
    est extraite du nom de fichier, convention prompt_<agent>_vX_Y.md."""
    content = (AGENTS_DIR / filename).read_text(encoding="utf-8")
    stem = filename.removesuffix(".md")
    version = "v" + stem.rsplit("_v", 1)[-1]
    return content, version


def assemble_prompt(
    prompt_content: str,
    source_text: str,
    fragments: dict[str, dict],
    failure_report: str | None = None,
) -> str:
    """Assemble le prompt complet envoyé à l'agent — contenu du fichier de
    prompt + texte source + sorties déjà produites par les agents
    précédents (en JSON depuis le lot 2.8 — format d'échange machine natif,
    cf. revue_002.md §2.3) + rapport d'erreurs le cas échéant (réinjection
    Synthèse). Déterministe et intégralement journalisé (tâche 2.6) — rien
    de ce que reçoit l'agent n'est implicite."""
    parts = [prompt_content, "\n\n---\n\n## TEXTE SOURCE\n\n", source_text]
    for name, frag in fragments.items():
        parts.append(
            f"\n\n---\n\n## SORTIE DE L'AGENT {name.upper()} (à ne jamais modifier)\n\n"
            f"```json\n{json.dumps(frag, ensure_ascii=False, indent=2)}\n```\n"
        )
    if failure_report:
        parts.append(
            "\n\n---\n\n## RAPPORT D'ERREURS validate.py (itération précédente)\n\n"
            f"{failure_report}\n"
        )
    return "".join(parts)


_TRAILING_COMMA = re.compile(r",(\s*[\]}])")


def parse_json_fragment(raw_response: str) -> dict:
    """Parse la réponse JSON brute d'un agent.

    Constat empirique du lot 2.8, à l'exécution réelle sur le corpus Lecornu :
    `output_config.format` contraint fortement la sortie de l'agent Charité
    vers un JSON conforme au schéma, mais ne garantit pas en pratique
    l'absence de virgule finale avant une accolade ou un crochet fermant —
    observé deux fois indépendamment, à chaque fois en fin de liste
    `speech_acts` d'une unité (`json.JSONDecodeError: Expecting property name
    enclosed in double quotes`), avec un volume de sortie très inférieur au
    plafond de tokens (donc pas une troncature). C'est une classe d'erreur
    strictement syntaxique et non ambiguë — contrairement au conflit
    prose-riche/YAML-nu du lot 2.7 (défaut de contenu textuel), une virgule
    finale n'a qu'une seule correction possible, sans invention de contenu.
    Réparée mécaniquement avant l'analyse JSON plutôt que traitée comme un
    échec d'agent — la reformulation « sinon consigne de format stricte +
    parsing » de `revue_002.md` §4 point 1 anticipait explicitement que le
    mécanisme de sortie structurée seul pourrait ne pas suffire."""
    return json.loads(_TRAILING_COMMA.sub(r"\1", raw_response)) or {}


def merge_fragments(
    charite: dict, vulnerabilites: dict, chaines_causales: dict, synthese: dict
) -> dict:
    """Fusionne les quatre fragments en un candidat unique.

    Les clés de premier niveau produites par Charité (enonciation,
    charity_reconstruction, units, execution_mode, execution_mode_note),
    Chaînes causales (upstream_causal_chain, downstream_causal_chains,
    discourse_action_gaps_on_thematic_objects, observable_effects_on_
    targeted_objects, historiographies) et Synthèse (epistemic_synthesis,
    null_results) sont disjointes — fusion directe. Seule `units` reçoit
    un traitement particulier : l'agent Vulnérabilités complète les unités
    déjà découpées par Charité (mêmes `unit_id`) plutôt que d'en produire
    une liste concurrente — un simple remplacement de clé perdrait le
    travail de Charité (text_span, speech_acts, presuppositions).

    Depuis le lot 2.8, le fragment Synthèse ne contient plus que ses deux
    propres blocs (epistemic_synthesis, null_results) — il ne recopie plus
    l'intégralité des sorties précédentes (revue_002.md §2.3, §4 point 2) :
    l'assemblage complet est désormais uniquement la responsabilité de cette
    fonction, jamais partagée avec le modèle."""
    candidate: dict = dict(charite)

    vuln_units_by_id = {u["unit_id"]: u for u in vulnerabilites.get("units", [])}
    merged_units = []
    for unit in candidate.get("units", []):
        extra = vuln_units_by_id.get(unit["unit_id"], {})
        merged_units.append({**unit, **{k: v for k, v in extra.items() if k != "unit_id"}})
    candidate["units"] = merged_units

    candidate.update(chaines_causales)
    candidate.update(synthese)
    return candidate


def format_validation_errors(e: ValidationError) -> str:
    lines = []
    for err in e.errors():
        loc = ".".join(str(x) for x in err["loc"])
        lines.append(f"[{err['type']}] {loc}: {err['msg']}")
    return "\n".join(lines)


# ============================================================================
# SÉRIALISATION YAML — conversion JSON→YAML mécanique (lot 2.8)
# ============================================================================

# Caractères indicateurs YAML en tête/fin de scalaire — risque d'ambiguïté
# de parsing si le style n'est pas explicitement forcé.
_YAML_INDICATOR_CHARS = set("-?:,[]{}#&*!|>'\"%@`")

_YAML_RESERVED_WORDS = {"true", "false", "null", "yes", "no", "~", "none", "on", "off"}


def _string_needs_forced_quoting(s: str) -> bool:
    """Heuristique de quotage forcé (lot 2.8, revue_002.md §4 point 2). PyYAML
    choisit déjà un style sûr par défaut pour du texte produit par du code
    (contrairement au YAML nu produit à la main par un modèle, cause de
    l'échec du lot 2.7) — cette fonction rend ce choix explicite et
    vérifiable par un test dédié plutôt que de s'y fier silencieusement.

    Quote si la chaîne : est vide ; contient un deux-points suivi d'un espace
    ou se termine par un deux-points (rupture de scalaire en mapping) ;
    contient un dièse précédé d'un espace ou commence par un dièse
    (commentaire) ; contient un saut de ligne ; commence ou finit par un
    caractère indicateur YAML ou une espace ; est un mot réservé YAML
    (true/false/null/...) ; ou ressemble à un nombre (préserve le typage
    chaîne)."""
    if s == "":
        return True
    if ": " in s or s.endswith(":"):
        return True
    if " #" in s or s.startswith("#"):
        return True
    if "\n" in s:
        return True
    if s[0] in _YAML_INDICATOR_CHARS or s[0].isspace() or s[-1].isspace():
        return True
    if s.lower() in _YAML_RESERVED_WORDS:
        return True
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False


class _ForcedQuoteDumper(yaml.SafeDumper):
    """Dumper YAML dédié — seul le représentant de chaîne est modifié par
    rapport à SafeDumper, le reste (dict, list, int, float, bool, None) est
    hérité tel quel."""


def _represent_str_forcing_quotes(dumper: yaml.SafeDumper, data: str) -> yaml.ScalarNode:
    style = '"' if _string_needs_forced_quoting(data) else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


_ForcedQuoteDumper.add_representer(str, _represent_str_forcing_quotes)


def dump_yaml_forcing_quotes(data: dict) -> str:
    """Sérialise en YAML avec guillemetage forcé des chaînes ambiguës (lot
    2.8, revue_002.md §4 point 2) — remplace le rôle de génération YAML
    auparavant tenu par le modèle lui-même (source du conflit prose-riche/
    YAML-nu diagnostiqué au lot 2.7, requalifié par la revue en défaut
    structurel, pas en simple discipline de formatage). C'est désormais la
    seule fonction du dépôt qui écrit le YAML final d'une analyse produite
    automatiquement."""
    return yaml.dump(data, Dumper=_ForcedQuoteDumper, allow_unicode=True, sort_keys=False)


# ============================================================================
# ORCHESTRATION
# ============================================================================


@dataclass
class OrchestrationResult:
    success: bool
    analysis: M01Analysis | None
    candidate: dict
    iterations_used: int
    log_paths: list[Path] = field(default_factory=list)
    failure_report: str | None = None


def run_pipeline(
    source_text: str,
    analysis_id: str,
    analysis_dir: Path,
    agent_caller: AgentCaller,
    source_metadata: dict,
    model: str = DEFAULT_MODEL,
) -> OrchestrationResult:
    """Pipeline linéaire complet. `agent_caller` est injecté — n'importe
    quel objet conforme au port `AgentCaller` convient, réel ou substitué.

    `source_metadata` (champ `source` du gabarit — `text_id`, `provenance`,
    `integrity_status`) est fourni par l'appelant, jamais halluciné par un
    agent : c'est une métadonnée sur l'entrée de l'orchestrateur lui-même,
    pas un contenu inféré du texte. Paramètre obligatoire plutôt que
    silencieusement défaulté, pour que l'appelant assume explicitement
    cette responsabilité."""
    log_paths: list[Path] = []
    fragments: dict[str, dict] = {}
    n = 0

    for agent_name, prompt_file in PRIOR_AGENTS:
        n += 1
        prompt_content, version = load_prompt(prompt_file)
        full_prompt = assemble_prompt(prompt_content, source_text, fragments)
        horodatage = datetime.now(timezone.utc).isoformat()
        reponse_brute, usage = agent_caller(model, full_prompt, AGENT_OUTPUT_MODELS[agent_name])
        record = AgentCallRecord(
            agent_name, version, model, horodatage, 1, full_prompt, reponse_brute, usage
        )
        log_paths.append(write_agent_log(analysis_dir, n, record))
        try:
            fragments[agent_name] = parse_json_fragment(reponse_brute)
        except json.JSONDecodeError as e:
            # Aucune boucle de réinjection pour les trois premiers agents
            # (seul Synthèse en dispose, plan_action_002 tâche 2.4) — échec
            # propre immédiat avec logs plutôt qu'un plantage non contrôlé.
            # Ce chemin reste atteignable en pratique (lot 2.8, cf. la note
            # de parse_json_fragment — virgule finale non couverte par la
            # réparation automatique, ou toute autre malformation JSON) —
            # output_config.format réduit fortement le risque, il ne
            # l'élimine pas complètement.
            return OrchestrationResult(
                False, None, {}, 1, log_paths,
                f"JSON mal formé produit par l'agent {agent_name} : {e}",
            )

    synthese_name, synthese_file = SYNTHESE_AGENT
    synthese_prompt_content, synthese_version = load_prompt(synthese_file)
    failure_report: str | None = None
    candidate: dict = {}

    for iteration in range(1, MAX_ITERATIONS + 1):
        n += 1
        full_prompt = assemble_prompt(
            synthese_prompt_content, source_text, fragments, failure_report
        )
        horodatage = datetime.now(timezone.utc).isoformat()
        reponse_brute, usage = agent_caller(model, full_prompt, AGENT_OUTPUT_MODELS[synthese_name])
        record = AgentCallRecord(
            synthese_name, synthese_version, model, horodatage, iteration,
            full_prompt, reponse_brute, usage,
        )
        log_paths.append(write_agent_log(analysis_dir, n, record))

        try:
            synthese_fragment = parse_json_fragment(reponse_brute)
            candidate = merge_fragments(
                fragments.get("charite", {}),
                fragments.get("vulnerabilites", {}),
                fragments.get("chaines_causales", {}),
                synthese_fragment,
            )
            candidate.setdefault("method_id", "M01_ANALYSE_RHETORIQUE")
            candidate.setdefault("method_version", "2.1")
            candidate.setdefault("gabarit_version", "2.1-durci-seq1")
            candidate.setdefault("analysis_id", analysis_id)
            candidate.setdefault("execution_date", date.today().isoformat())
            candidate.setdefault("source", source_metadata)

            analysis = M01Analysis.model_validate(candidate)
            return OrchestrationResult(True, analysis, candidate, iteration, log_paths)
        except json.JSONDecodeError as e:
            # Défense en profondeur — voir la note équivalente ci-dessus pour
            # les trois premiers agents. Traité comme réinjectable à Synthèse
            # au même titre qu'une erreur de validation Pydantic.
            failure_report = f"JSON mal formé produit par Synthèse : {e}"
            candidate = {}
            if iteration == MAX_ITERATIONS:
                return OrchestrationResult(
                    False, None, candidate, iteration, log_paths, failure_report
                )
        except ValidationError as e:
            failure_report = format_validation_errors(e)
            if iteration == MAX_ITERATIONS:
                return OrchestrationResult(
                    False, None, candidate, iteration, log_paths, failure_report
                )

    raise AssertionError("unreachable — MAX_ITERATIONS couvre toutes les itérations de la boucle")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source_text", type=Path, help="Fichier texte source")
    parser.add_argument("analysis_id", type=str, help="Identifiant d'analyse (convention 2.3)")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help=f"Modèle (défaut : {DEFAULT_MODEL})")
    parser.add_argument(
        "--analyses-dir", type=Path, default=Path(__file__).parent / "analyses",
        help="Répertoire racine des analyses (défaut : pipeline/analyses/)",
    )
    args = parser.parse_args()

    source_text = args.source_text.read_text(encoding="utf-8")
    analysis_dir = args.analyses_dir / args.analysis_id
    analysis_dir.mkdir(parents=True, exist_ok=True)

    # Métadonnée sur l'entrée de l'orchestrateur lui-même — jamais confiée à
    # un agent. integrity_status="uncertain" par défaut : l'ingestion
    # automatisée ne certifie rien, seule une vérification humaine documentée
    # justifierait "certified" ou "partial" (Source, pipeline/schemas.py).
    source_metadata = {
        "text_id": args.analysis_id,
        "provenance": str(args.source_text),
        "integrity_status": "uncertain",
    }

    agent_caller = AnthropicAgentCaller()
    result = run_pipeline(
        source_text, args.analysis_id, analysis_dir, agent_caller, source_metadata, args.model
    )

    if result.success:
        yaml_path = analysis_dir / f"{args.analysis_id}.yaml"
        yaml_path.write_text(dump_yaml_forcing_quotes(result.candidate), encoding="utf-8")
        print(f"✓ Validation réussie en {result.iterations_used} itération(s) — {yaml_path}")
        return 0

    print(
        f"❌ Échec après {result.iterations_used} itération(s). Logs : "
        f"{', '.join(str(p) for p in result.log_paths)}",
        file=sys.stderr,
    )
    print(result.failure_report, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
