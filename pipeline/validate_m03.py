#!/usr/bin/env python3
"""
L'Entité — Validateur CLI des analyses M03-M selon le gabarit v2.1.

Usage:
    python3 validate_m03.py <fichier.yaml>
"""

from __future__ import annotations
import sys
from pathlib import Path
import yaml
from pydantic import ValidationError

from schemas_m03 import M03Analysis


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def format_validation_errors(e: ValidationError, path: Path) -> str:
    lines = [
        f"❌ ÉCHEC DE VALIDATION — {path.name}",
        "",
        f"Nombre d'erreurs : {e.error_count()}",
        "",
        "Erreurs détaillées :",
        "─" * 60,
    ]
    for i, err in enumerate(e.errors(), 1):
        loc = ".".join(str(x) for x in err["loc"])
        msg = err["msg"]
        err_type = err["type"]
        lines.append(f"{i}. [{err_type}]")
        lines.append(f"   Localisation : {loc}")
        lines.append(f"   Message      : {msg}")
        if "input" in err:
            input_repr = repr(err["input"])
            if len(input_repr) > 120:
                input_repr = input_repr[:117] + "..."
            lines.append(f"   Valeur reçue : {input_repr}")
        lines.append("")
    return "\n".join(lines)


def format_success_report(analysis: M03Analysis, path: Path) -> str:
    lines = [
        f"✓ VALIDATION RÉUSSIE — {path.name}",
        "",
        f"Méthode    : {analysis.method_id} v{analysis.method_version}",
        f"Analyse    : {analysis.analysis_id}",
        f"Mode       : {analysis.execution_mode.value}",
        "",
        "CONTROVERSE",
        "─" * 60,
        f"Objet      : {analysis.controversy.object[:80]}",
        f"Séquence   : {analysis.controversy.temporal_sequence}",
        f"Fenêtre    : {analysis.controversy.date_range[0]} → {analysis.controversy.date_range[1]}",
        "",
        "ACTEURS",
        "─" * 60,
    ]
    for actor in analysis.actors:
        lines.append(f"  • {actor.actor_id}: {actor.name} ({actor.role_at_date[:50]})")
        lines.append(f"      ← analyse M01 référencée : {actor.m01_analysis_id}")

    lines.append("")
    lines.append("MATRICES v2.1")
    lines.append("─" * 60)
    n_propositions = len(analysis.structuring_propositions)
    n_actors = len(analysis.actors)
    n_epistemic_cells = len(analysis.epistemic_position_matrix)
    n_targeted_cells = len(analysis.targeted_objects_matrix)
    expected_epistemic = n_actors * n_propositions
    lines.append(f"Propositions structurantes      : {n_propositions}")
    lines.append(
        f"Matrice positions épistémiques  : {n_epistemic_cells} cellules "
        f"(attendu max {expected_epistemic})"
    )
    lines.append(f"Matrice objets visés            : {n_targeted_cells} cellules")
    lines.append(f"Cas saillants identifiés        : {len(analysis.cross_matrix_salient_cases)}")
    for case in analysis.cross_matrix_salient_cases:
        lines.append(f"  • [{case.type.value}] {case.description[:75]}")

    lines.append("")
    lines.append("CADRES INTERPRÉTATIFS")
    lines.append("─" * 60)
    for frame in analysis.interpretive_frames:
        lines.append(f"  • {frame.frame_label}")
        lines.append(
            f"      ancrage empirique ({len(frame.empirical_grounding)} cas) — "
            f"consensus={frame.consensus_level.value}"
        )

    lines.append("")
    lines.append("CHAÎNES CAUSALES AVAL COMPARÉES (v2.1)")
    lines.append("─" * 60)
    for chain in analysis.comparative_downstream_chains:
        lines.append(f"  • {chain.actor}: {len(chain.observable_effects)} effets observés")

    lines.append("")
    lines.append("ASYMÉTRIES ET PRÉDICTIONS (v2.1)")
    lines.append("─" * 60)
    lines.append(f"Asymétries de bénéfice identifiées    : {len(analysis.asymmetries_of_benefit)}")
    lines.append(f"Prédictions invalidées documentées    : {len(analysis.invalidated_predictions)}")
    for pred in analysis.invalidated_predictions:
        lines.append(f"  • {pred.actor}: pattern={pred.pattern_type}")
        lines.append(f"      prédit: {pred.predicted[:70]}")

    if analysis.epistemic_synthesis:
        s = analysis.epistemic_synthesis
        lines.append("")
        lines.append("SYNTHÈSE ÉPISTÉMIQUE")
        lines.append("─" * 60)
        lines.append(f"Hypothèses concurrentes : {len(s.competing_hypotheses)}")
        lines.append(f"Écart hypothèses        : {s.hypothesis_gap:.2f}")
        lines.append(f"Statut                  : {s.hypothesis_status.value}")

    lines.append("")
    lines.append("CONFORMITÉ M03 v2.1 ✓")
    return "\n".join(lines)


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1

    path = Path(args[0])
    if not path.exists():
        print(f"Fichier introuvable : {path}")
        return 1

    try:
        data = load_yaml(path)
    except yaml.YAMLError as e:
        print(f"YAML mal formé : {e}")
        return 1

    try:
        analysis = M03Analysis.model_validate(data)
    except ValidationError as e:
        print(format_validation_errors(e, path))
        return 1

    print(format_success_report(analysis, path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
