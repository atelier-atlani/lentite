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
En cas d'échec de validation, le rapport d'erreurs est réinjecté à l'agent
Synthèse, deux itérations maximum, puis échec propre avec logs.

Logs — un fichier JSON par appel d'agent (tâche 2.6), dans
pipeline/analyses/<analysis_id>/logs/, versionnés avec le YAML produit
(traces de production, pas des vues dérivées — contrairement aux exports
du graphe).

Clé API lue exclusivement depuis la variable d'environnement
ANTHROPIC_API_KEY — jamais acceptée en argument CLI, jamais codée en dur.

Usage:
    python3 orchestrateur.py <texte_source.txt> <analysis_id> [--model MODELE]

Avertissement (plan_action_002 séquence 2, tâche 2.4) — ce module est codé
et sa plomberie interne vérifiée par substitution (agent factice, sans appel
réseau) ; aucune exécution sur texte réel n'est faite dans ce lot, c'est
l'objet de la tâche 2.7.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Protocol

import yaml
from pydantic import ValidationError

from schemas import M01Analysis

DEFAULT_MODEL = "claude-sonnet-5"
MAX_ITERATIONS = 2
AGENTS_DIR = Path(__file__).parent / "agents" / "fonctionnels"

# Ordre du pipeline linéaire — les trois premiers agents s'exécutent une
# fois ; l'agent Synthèse boucle jusqu'à MAX_ITERATIONS sur échec de
# validation (réinjection du rapport d'erreurs).
PRIOR_AGENTS = [
    ("charite", "prompt_charite_v1_0.md"),
    ("vulnerabilites", "prompt_vulnerabilites_v1_0.md"),
    ("chaines_causales", "prompt_chaines_causales_v1_0.md"),
]
SYNTHESE_AGENT = ("synthese", "prompt_synthese_v1_0.md")


# ============================================================================
# PORT HEXAGONAL — abstraction de l'appel au modèle de langage
# ============================================================================


class AgentCaller(Protocol):
    """Port — un appelant conforme reçoit (modèle, prompt complet) et
    retourne (réponse_brute, usage_tokens). Le cœur du pipeline ne connaît
    que cette interface, jamais le SDK concret."""

    def __call__(self, model: str, prompt: str) -> tuple[str, dict]: ...


class AnthropicAgentCaller:
    """Adaptateur SDK Anthropic direct (tâche 2.4). Import du SDK différé
    au constructeur — un objet de ce type n'est instancié que pour une
    exécution réelle (tâche 2.7), jamais pour les tests de plomberie."""

    def __init__(self) -> None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY absente de l'environnement. La clé API n'est "
                "jamais acceptée autrement — pas d'argument CLI, pas de valeur "
                "codée en dur (discipline tâche 2.4)."
            )
        import anthropic

        self._client = anthropic.Anthropic(api_key=api_key)

    def __call__(self, model: str, prompt: str) -> tuple[str, dict]:
        # 8192 s'est révélé insuffisant à l'exécution réelle (tâche 2.7) — l'agent
        # Synthèse recopie l'intégralité des fragments précédents, ce qui tronque
        # la réponse en fin de YAML sur un discours de taille réelle. Relevé à
        # 16000 (valeur empirique constatée suffisante, pas une limite doctrinale).
        response = self._client.messages.create(
            model=model,
            max_tokens=16000,
            messages=[{"role": "user", "content": prompt}],
        )
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
    précédents + rapport d'erreurs le cas échéant (réinjection Synthèse).
    Déterministe et intégralement journalisé (tâche 2.6) — rien de ce que
    reçoit l'agent n'est implicite."""
    parts = [prompt_content, "\n\n---\n\n## TEXTE SOURCE\n\n", source_text]
    for name, frag in fragments.items():
        parts.append(
            f"\n\n---\n\n## SORTIE DE L'AGENT {name.upper()} (à ne jamais modifier)\n\n"
            f"```yaml\n{yaml.safe_dump(frag, allow_unicode=True, sort_keys=False)}```\n"
        )
    if failure_report:
        parts.append(
            "\n\n---\n\n## RAPPORT D'ERREURS validate.py (itération précédente)\n\n"
            f"{failure_report}\n"
        )
    return "".join(parts)


def parse_yaml_fragment(raw_response: str) -> dict:
    """Extrait le premier bloc ```yaml ... ``` de la réponse brute d'un
    agent. Ne tente aucune correction ni complétion du contenu reçu."""
    if "```yaml" in raw_response:
        block = raw_response.split("```yaml", 1)[1].split("```", 1)[0]
    else:
        block = raw_response
    return yaml.safe_load(block) or {}


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
    travail de Charité (text_span, speech_acts, presuppositions)."""
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
        reponse_brute, usage = agent_caller(model, full_prompt)
        record = AgentCallRecord(
            agent_name, version, model, horodatage, 1, full_prompt, reponse_brute, usage
        )
        log_paths.append(write_agent_log(analysis_dir, n, record))
        try:
            fragments[agent_name] = parse_yaml_fragment(reponse_brute)
        except yaml.YAMLError as e:
            # Aucune boucle de réinjection pour les trois premiers agents
            # (seul Synthèse en dispose, plan_action_002 tâche 2.4) — échec
            # propre immédiat avec logs plutôt qu'un plantage non contrôlé.
            return OrchestrationResult(
                False, None, {}, 1, log_paths,
                f"YAML mal formé produit par l'agent {agent_name} : {e}",
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
        reponse_brute, usage = agent_caller(model, full_prompt)
        record = AgentCallRecord(
            synthese_name, synthese_version, model, horodatage, iteration,
            full_prompt, reponse_brute, usage,
        )
        log_paths.append(write_agent_log(analysis_dir, n, record))

        try:
            synthese_fragment = parse_yaml_fragment(reponse_brute)
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
        except yaml.YAMLError as e:
            # Un YAML mal formé (souvent une réponse tronquée par max_tokens,
            # constaté à l'exécution réelle tâche 2.7) est traité comme un
            # échec réinjectable à Synthèse, au même titre qu'une erreur de
            # validation Pydantic — l'agent peut corriger sur la base du
            # message d'erreur, dans la même limite de deux itérations.
            failure_report = f"YAML mal formé ou tronqué produit par Synthèse : {e}"
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
        yaml_path.write_text(
            yaml.safe_dump(result.candidate, allow_unicode=True, sort_keys=False), encoding="utf-8"
        )
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
