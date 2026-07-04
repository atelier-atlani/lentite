#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
L'Entité — Validateur CLI des analyses M01-M selon le gabarit v2.1.

Usage:
    python3 validate.py <fichier.yaml>
"""

from __future__ import annotations
import sys
from pathlib import Path
import yaml
from pydantic import ValidationError

from schemas import M01Analysis


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


def format_success_report(analysis: M01Analysis, path: Path) -> str:
    lines = [
        f"✓ VALIDATION RÉUSSIE — {path.name}",
        "",
        f"Méthode    : {analysis.method_id} v{analysis.method_version}",
        f"Analyse    : {analysis.analysis_id}",
        f"Mode       : {analysis.execution_mode.value}",
        f"Gabarit    : {analysis.gabarit_version.value}",
        "",
        "ÉNONCIATION",
        "─" * 60,
        f"Locuteur   : {analysis.enonciation.speaker.name} "
        f"({analysis.enonciation.speaker.role_at_date[:50]})",
        f"Date       : {analysis.enonciation.date}",
        f"Genre      : {analysis.enonciation.genre}",
        f"Charge     : affective={analysis.enonciation.affective_charge.value} "
        f"éthique={analysis.enonciation.ethical_charge.value}",
        "",
        "OBJETS",
        "─" * 60,
    ]
    for ot in analysis.enonciation.thematic_objects:
        lines.append(f"  • [OT] {ot.object_id}: {ot.label[:70]} ({ot.efficiency_status.value})")
    for ov in analysis.enonciation.targeted_objects:
        lines.append(
            f"  • [OV] {ov.object_id}: {ov.label[:70]} "
            f"(confidence={ov.inference_confidence:.2f}, {ov.efficiency_status.value})"
        )

    n_vulns = sum(len(u.argumentative_vulnerabilities) for u in analysis.units)
    n_omissions = sum(len(u.omissions) for u in analysis.units)
    lines.append("")
    lines.append("UNITÉS ARGUMENTATIVES")
    lines.append("─" * 60)
    lines.append(
        f"Unités analysées : {len(analysis.units)} "
        f"({n_vulns} vulnérabilités, {n_omissions} omissions)"
    )

    lines.append("")
    lines.append("ÉCARTS DISCOURS / ACTE (bloc V.3)")
    lines.append("─" * 60)
    if analysis.discourse_action_gaps_on_thematic_objects:
        for gap in analysis.discourse_action_gaps_on_thematic_objects:
            lines.append(f"  • {gap.thematic_object_id}: pattern={gap.pattern_type.value}")
    else:
        lines.append("  (vide)")

    lines.append("")
    lines.append("EFFETS OBSERVABLES (bloc V.4)")
    lines.append("─" * 60)
    if analysis.observable_effects_on_targeted_objects:
        for effect in analysis.observable_effects_on_targeted_objects:
            lines.append(
                f"  • {effect.targeted_object_id}: {effect.effect_type.value} "
                f"— {effect.description[:60]}"
            )
    else:
        lines.append("  (vide)")

    lines.append("")
    lines.append("HISTORIOGRAPHIES")
    lines.append("─" * 60)
    lines.append(f"Mobilisées : {len(analysis.historiographies)}")

    if analysis.epistemic_synthesis:
        s = analysis.epistemic_synthesis
        lines.append("")
        lines.append("SYNTHÈSE ÉPISTÉMIQUE")
        lines.append("─" * 60)
        lines.append(f"Hypothèses concurrentes : {len(s.competing_hypotheses)}")
        lines.append(f"Écart hypothèses        : {s.hypothesis_gap:.2f}")
        lines.append(f"Statut                  : {s.hypothesis_status.value}")

    if analysis.null_results:
        n = analysis.null_results
        lines.append("")
        lines.append("RÉSULTATS NULS")
        lines.append("─" * 60)
        lines.append(f"Sophismes certains          : {n.fallacies_certain}")
        lines.append(f"Sophismes probables/possibles : {n.fallacies_probable_or_possible}")
        lines.append(f"Omissions intentionnelles prouvées : {n.intentional_omissions_proved}")

    lines.append("")
    lines.append("CONFORMITÉ M01 v2.1 ✓")
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
        analysis = M01Analysis.model_validate(data)
    except ValidationError as e:
        print(format_validation_errors(e, path))
        return 1

    print(format_success_report(analysis, path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
