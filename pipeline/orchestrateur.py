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
tâche 2.5) : Charité → Vulnérabilités → Chaînes causales → Synthèse →
assemblage YAML → validation (schemas.M01Analysis, cœur de validate.py).

Réinjection routée par agent propriétaire (lot 2.9, correctif final Phase 0
prescrit en Reviewer, complète revue_002.md §4) — en cas d'échec de
validation, chaque erreur est attribuée à l'agent dont le fragment contient
le champ fautif (`route_validation_errors`) et réinjectée à cet agent
seulement, jamais systématiquement à Synthèse comme au lot 2.8. Budget
global de trois appels de réinjection par passe, partagé entre les agents
qui en ont besoin (pas trois par agent) — au-delà, échec propre avec logs.
Une erreur dont le chemin ne correspond à aucun agent connu (bug
d'orchestrateur, jamais un défaut d'agent) interrompt immédiatement la
passe sans consommer le budget de réinjection.

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
REINJECTION_BUDGET = 3
AGENTS_DIR = Path(__file__).parent / "agents" / "fonctionnels"

# Ordre du pipeline linéaire — chaque agent voit les fragments des agents
# qui le précèdent dans cet ordre, jamais ceux qui le suivent (y compris en
# réinjection — la réinjection rejoue le même contexte que l'appel initial
# de l'agent, plus le rapport d'erreurs qui lui est propre). Prompts v2.1
# pour Vulnérabilités et Chaînes causales depuis le lot 2.9 (champs
# bitemporels requis, cf. pipeline/agent_schemas.py) ; v2.0 inchangés pour
# Charité et Synthèse (aucun champ bitemporel dans leur périmètre).
PIPELINE_ORDER = ["charite", "vulnerabilites", "chaines_causales", "synthese"]
AGENT_PROMPT_FILES = {
    "charite": "prompt_charite_v2_0.md",
    "vulnerabilites": "prompt_vulnerabilites_v2_1.md",
    "chaines_causales": "prompt_chaines_causales_v2_1.md",
    "synthese": "prompt_synthese_v2_0.md",
}

# Table de routage des erreurs de validation vers l'agent propriétaire du
# champ fautif (lot 2.9, revue_002.md §4 point 3) — voir route_validation_errors.
_CHARITE_TOP_FIELDS = {"execution_mode", "execution_mode_note", "enonciation", "charity_reconstruction"}
_CHARITE_UNIT_FIELDS = {"unit_id", "text_span", "speech_acts", "presuppositions"}
_VULNERABILITES_UNIT_FIELDS = {"argumentative_vulnerabilities", "omissions", "inferred_function"}
_CHAINES_CAUSALES_TOP_FIELDS = {
    "upstream_causal_chain",
    "downstream_causal_chains",
    "discourse_action_gaps_on_thematic_objects",
    "observable_effects_on_targeted_objects",
    "historiographies",
}
_SYNTHESE_TOP_FIELDS = {"epistemic_synthesis", "null_results"}

# Erreur racine (model_validator sur M01Analysis, `loc` vide) — le chemin
# précis du champ fautif n'est pas structuré par Pydantic, il est encodé en
# texte dans le message de `validate_bitemporal_when_durci` (schemas.py).
# Cette expression en extrait chaque chemin entre guillemets pour permettre
# le routage par agent, plutôt que de réinjecter le message brut à un agent
# arbitraire.
_BITEMPORAL_MISSING_PATH = re.compile(
    r"'((?:units\[[^\]]+\]\.(?:argumentative_vulnerabilities|omissions)\[\d+\])"
    r"|(?:discourse_action_gaps_on_thematic_objects\[[^\]]+\])"
    r"|(?:observable_effects_on_targeted_objects\[[^\]]+\]))'"
)


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
    routée par agent propriétaire depuis le lot 2.9, jamais systématiquement
    à Synthèse). Déterministe et intégralement journalisé (tâche 2.6) — rien
    de ce que reçoit l'agent n'est implicite."""
    parts = [prompt_content, "\n\n---\n\n## TEXTE SOURCE\n\n", source_text]
    for name, frag in fragments.items():
        parts.append(
            f"\n\n---\n\n## SORTIE DE L'AGENT {name.upper()} (à ne jamais modifier)\n\n"
            f"```json\n{json.dumps(frag, ensure_ascii=False, indent=2)}\n```\n"
        )
    if failure_report:
        parts.append(
            "\n\n---\n\n## RAPPORT D'ERREURS validate.py (te concernant, "
            "réinjecté après une tentative précédente)\n\n"
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


def route_validation_errors(e: ValidationError) -> tuple[dict[str, list[str]], list[str]]:
    """Attribue chaque erreur de `M01Analysis.model_validate` à l'agent
    propriétaire du champ fautif (lot 2.9, revue_002.md §4 point 3).

    Retourne (routées, non_routables) — `routées` associe un nom d'agent à
    la liste des lignes d'erreur (formatées comme `format_validation_errors`)
    qui lui reviennent ; `non_routables` liste les erreurs dont le chemin ne
    correspond à aucun agent connu (bug d'orchestrateur — champ défaulté par
    `run_pipeline` lui-même, ou validateur imprévu — jamais un défaut d'agent
    à corriger par réinjection). Un appelant qui reçoit une liste
    `non_routables` non vide doit arrêter la passe immédiatement, sans
    consommer de budget de réinjection sur une hypothèse de routage non
    fondée.

    Deux cas de figure par erreur :
    - `loc` non vide (erreur de champ standard) — routée par le premier
      segment du chemin, avec un traitement spécial pour `units[i].<champ>`
      (le sous-champ à l'index 2 distingue Charité de Vulnérabilités).
    - `loc` vide (erreur racine — `model_validator` sur `M01Analysis`) — le
      chemin précis n'est pas structuré par Pydantic dans ce cas ; extrait du
      texte du message pour les validateurs connus (`validate_bitemporal_
      when_durci`, qui peut référencer des champs de Vulnérabilités ET de
      Chaînes causales dans un seul message — d'où le double routage
      possible d'une même erreur brute)."""
    routed: dict[str, list[str]] = {}
    unroutable: list[str] = []

    def add(owner: str, line: str) -> None:
        routed.setdefault(owner, []).append(line)

    for err in e.errors():
        loc = err["loc"]
        line = f"[{err['type']}] {'.'.join(str(x) for x in loc)}: {err['msg']}"

        if loc:
            first = loc[0]
            if first == "units":
                subfield = loc[2] if len(loc) >= 3 else None
                if subfield in _VULNERABILITES_UNIT_FIELDS:
                    add("vulnerabilites", line)
                else:
                    # Sous-champ de Charité (text_span, speech_acts, ...), ou
                    # erreur au niveau de l'unité entière (unit_id manquant,
                    # etc.) — dans les deux cas, c'est Charité qui produit la
                    # structure de l'unité elle-même.
                    add("charite", line)
            elif first in _CHARITE_TOP_FIELDS:
                add("charite", line)
            elif first in _CHAINES_CAUSALES_TOP_FIELDS:
                add("chaines_causales", line)
            elif first in _SYNTHESE_TOP_FIELDS:
                add("synthese", line)
            else:
                # Champs défaultés par l'orchestrateur (method_id, source,
                # ...) ou tout autre chemin imprévu — aucun agent à blâmer.
                unroutable.append(line)
            continue

        # Erreur racine — extraire les chemins embarqués dans le message.
        msg = err["msg"]
        paths = _BITEMPORAL_MISSING_PATH.findall(msg)
        if paths:
            by_owner: dict[str, list[str]] = {}
            for p in paths:
                if "argumentative_vulnerabilities" in p or ".omissions[" in p:
                    by_owner.setdefault("vulnerabilites", []).append(p)
                elif (
                    "discourse_action_gaps_on_thematic_objects" in p
                    or "observable_effects_on_targeted_objects" in p
                ):
                    by_owner.setdefault("chaines_causales", []).append(p)
            for owner, owner_paths in by_owner.items():
                add(
                    owner,
                    "[value_error] bitemporalité manquante (gabarit_version="
                    "2.1-durci-seq1) sur : " + ", ".join(owner_paths),
                )
        elif "v.3" in msg.lower() or "discourse_action_gaps" in msg.lower():
            # validate_v3_efficiency_block_coherence — le correctif porte sur
            # discourse_action_gaps_on_thematic_objects, produit par Chaînes
            # causales.
            add("chaines_causales", f"[value_error] : {msg}")
        else:
            unroutable.append(f"[value_error] : {msg}")

    return routed, unroutable


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
    agent_calls_used: int
    log_paths: list[Path] = field(default_factory=list)
    failure_report: str | None = None


def _prior_fragments(fragments: dict[str, dict], agent_name: str) -> dict[str, dict]:
    """Fragments des agents qui précèdent `agent_name` dans l'ordre linéaire
    (`PIPELINE_ORDER`), déjà produits. Utilisé aussi bien pour l'appel
    initial d'un agent que pour sa réinjection — un agent réinjecté revoit
    exactement le même contexte amont que lors de son appel initial, jamais
    les fragments des agents qui le suivent (pipeline toujours linéaire,
    lot 2.9, revue_002.md §4 point 3)."""
    idx = PIPELINE_ORDER.index(agent_name)
    return {name: fragments[name] for name in PIPELINE_ORDER[:idx] if name in fragments}


def _call_agent(
    agent_name: str,
    source_text: str,
    fragments: dict[str, dict],
    agent_caller: AgentCaller,
    model: str,
    analysis_dir: Path,
    log_paths: list[Path],
    n: int,
    call_index: int,
    failure_report: str | None,
) -> tuple[dict | None, str | None]:
    """Appelle un agent (initial ou réinjection), journalise l'appel, parse
    sa réponse JSON. Retourne (fragment, None) en cas de succès,
    (None, message_erreur) sinon — jamais les deux à la fois."""
    prompt_content, version = load_prompt(AGENT_PROMPT_FILES[agent_name])
    full_prompt = assemble_prompt(
        prompt_content, source_text, _prior_fragments(fragments, agent_name), failure_report
    )
    horodatage = datetime.now(timezone.utc).isoformat()
    reponse_brute, usage = agent_caller(model, full_prompt, AGENT_OUTPUT_MODELS[agent_name])
    record = AgentCallRecord(
        agent_name, version, model, horodatage, call_index, full_prompt, reponse_brute, usage
    )
    log_paths.append(write_agent_log(analysis_dir, n, record))
    try:
        return parse_json_fragment(reponse_brute), None
    except json.JSONDecodeError as e:
        # Défense en profondeur — output_config.format (lot 2.8) réduit
        # fortement le risque de JSON malformé, il ne l'élimine pas
        # complètement (cf. parse_json_fragment). Échec propre immédiat pour
        # cet appel plutôt qu'un plantage non contrôlé ; ne consomme pas le
        # budget de réinjection différemment d'un échec de validation — les
        # deux sont des échecs d'appel d'agent au même titre.
        return None, f"JSON mal formé produit par l'agent {agent_name} : {e}"


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
    cette responsabilité.

    Réinjection routée par agent (lot 2.9) — après la passe initiale (un
    appel par agent, dans l'ordre linéaire), toute erreur de validation est
    attribuée à son agent propriétaire (`route_validation_errors`) et
    réinjectée à cet agent seul, jamais systématiquement à Synthèse. Budget
    global de `REINJECTION_BUDGET` appels de réinjection par passe, partagé
    entre tous les agents qui en ont besoin — si un tour nécessite de
    corriger deux agents, il consomme deux unités de budget, pas une par
    agent. Une erreur non routable (chemin ne correspondant à aucun agent
    connu) interrompt la passe immédiatement, sans consommer de budget."""
    log_paths: list[Path] = []
    fragments: dict[str, dict] = {}
    call_counts: dict[str, int] = dict.fromkeys(PIPELINE_ORDER, 0)
    n = 0

    # Passe initiale — un appel par agent, dans l'ordre linéaire.
    for agent_name in PIPELINE_ORDER:
        n += 1
        call_counts[agent_name] += 1
        fragment, err = _call_agent(
            agent_name, source_text, fragments, agent_caller, model,
            analysis_dir, log_paths, n, call_counts[agent_name], None,
        )
        if err:
            return OrchestrationResult(False, None, {}, n, log_paths, err)
        fragments[agent_name] = fragment

    def build_candidate() -> dict:
        candidate = merge_fragments(
            fragments.get("charite", {}),
            fragments.get("vulnerabilites", {}),
            fragments.get("chaines_causales", {}),
            fragments.get("synthese", {}),
        )
        candidate.setdefault("method_id", "M01_ANALYSE_RHETORIQUE")
        candidate.setdefault("method_version", "2.1")
        candidate.setdefault("gabarit_version", "2.1-durci-seq1")
        candidate.setdefault("analysis_id", analysis_id)
        candidate.setdefault("execution_date", date.today().isoformat())
        candidate.setdefault("source", source_metadata)
        return candidate

    candidate = build_candidate()
    try:
        analysis = M01Analysis.model_validate(candidate)
        return OrchestrationResult(True, analysis, candidate, n, log_paths)
    except ValidationError as e:
        last_error = e

    budget = REINJECTION_BUDGET
    while budget > 0:
        routed, unroutable = route_validation_errors(last_error)
        if unroutable:
            return OrchestrationResult(
                False, None, candidate, n, log_paths,
                "Erreur(s) non routable(s) vers un agent propriétaire — échec "
                "immédiat, budget de réinjection non consommé (bug "
                "d'orchestrateur probable, pas un défaut d'agent) :\n"
                + "\n".join(unroutable),
            )
        for agent_name, error_lines in routed.items():
            if budget <= 0:
                break
            n += 1
            call_counts[agent_name] += 1
            fragment, err = _call_agent(
                agent_name, source_text, fragments, agent_caller, model,
                analysis_dir, log_paths, n, call_counts[agent_name],
                "\n".join(error_lines),
            )
            budget -= 1
            if err:
                return OrchestrationResult(False, None, candidate, n, log_paths, err)
            fragments[agent_name] = fragment

        candidate = build_candidate()
        try:
            analysis = M01Analysis.model_validate(candidate)
            return OrchestrationResult(True, analysis, candidate, n, log_paths)
        except ValidationError as e:
            last_error = e

    return OrchestrationResult(
        False, None, candidate, n, log_paths,
        f"Budget de réinjection ({REINJECTION_BUDGET}) épuisé. Dernier rapport :\n"
        + format_validation_errors(last_error),
    )


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
        print(f"✓ Validation réussie en {result.agent_calls_used} appel(s) d'agent — {yaml_path}")
        return 0

    print(
        f"❌ Échec après {result.agent_calls_used} appel(s) d'agent. Logs : "
        f"{', '.join(str(p) for p in result.log_paths)}",
        file=sys.stderr,
    )
    print(result.failure_report, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
