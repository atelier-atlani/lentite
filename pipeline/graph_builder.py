#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""
L'Entité — Construction du graphe cognitif à partir du corpus validé.

Ingère tous les YAML valides de pipeline/analyses/ (M01-M et M03-M),
construit un graphe NetworkX unique (nœuds et arêtes typés conformément
aux schémas, attributs épistémiques portés par les arêtes — source,
confiance, méthode, dates), et l'exporte en GraphML + JSON dans exports/.

Reconstruction intégrale à chaque exécution — pas d'état incrémental
(décision 002 : les fichiers-source sont la source de vérité, le graphe
est une vue dérivée, non versionnée).

Usage:
    python3 graph_builder.py [--analyses-dir DIR] [--export-dir DIR]
"""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

import networkx as nx
import yaml
from pydantic import ValidationError

from schemas import M01Analysis
from schemas_m03 import M03Analysis


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _add_node(g: nx.MultiDiGraph, node_id: str, **attrs: object) -> None:
    clean = {k: v for k, v in attrs.items() if v is not None}
    if g.has_node(node_id):
        g.nodes[node_id].update(clean)
    else:
        g.add_node(node_id, **clean)


def _add_edge(g: nx.MultiDiGraph, u: str, v: str, edge_type: str, **attrs: object) -> None:
    clean = {k: v for k, v in attrs.items() if v is not None}
    g.add_edge(u, v, type=edge_type, **clean)


def add_m01_analysis(g: nx.MultiDiGraph, analysis: M01Analysis) -> None:
    """Nœuds et arêtes pour une analyse M01 — gabarit v2.1 section 11."""
    aid = analysis.analysis_id
    _add_node(
        g,
        aid,
        kind="analysis",
        method_id=analysis.method_id,
        method_version=analysis.method_version,
        gabarit_version=analysis.gabarit_version.value,
        execution_date=str(analysis.execution_date),
        execution_mode=analysis.execution_mode.value,
    )

    speaker = analysis.enonciation.speaker
    _add_node(g, speaker.id, kind="person", name=speaker.name, role=speaker.role_at_date)
    _add_edge(
        g, speaker.id, aid, "ENONCE",
        date=str(analysis.enonciation.date), method=analysis.method_id,
    )

    for ot in analysis.enonciation.thematic_objects:
        oid = f"{aid}::{ot.object_id}"
        _add_node(g, oid, kind="objet_thematique", label=ot.label,
                   efficiency_status=ot.efficiency_status.value)
        _add_edge(g, aid, oid, "ABORDE", method=analysis.method_id)

    for ov in analysis.enonciation.targeted_objects:
        oid = f"{aid}::{ov.object_id}"
        _add_node(g, oid, kind="objet_vise", label=ov.label,
                   efficiency_status=ov.efficiency_status.value)
        _add_edge(
            g, speaker.id, oid, "VISE",
            confidence=ov.inference_confidence,
            source="; ".join(ov.grounded_in) or None,
            method=analysis.method_id,
        )

    for unit in analysis.units:
        uid = f"{aid}::{unit.unit_id}"
        _add_node(g, uid, kind="unite", text_span=unit.text_span[:200])
        _add_edge(g, aid, uid, "CONTIENT", method=analysis.method_id)
        for j, vuln in enumerate(unit.argumentative_vulnerabilities):
            vid = f"{uid}::vuln::{j}"
            _add_node(g, vid, kind="vulnerabilite", vuln_type=vuln.type, level=vuln.level.value)
            _add_edge(
                g, uid, vid, "PRESENTE",
                confidence=vuln.confidence,
                date_fait=str(vuln.date_fait), date_connaissance=str(vuln.date_connaissance),
                method=analysis.method_id,
            )
        for j, omission in enumerate(unit.omissions):
            oid2 = f"{uid}::omission::{j}"
            _add_node(
                g, oid2, kind="omission", missing_element=omission.missing_element,
                level=omission.level.value, pouvoir_agir=omission.pouvoir_agir,
            )
            _add_edge(
                g, uid, oid2, "OMET",
                confidence=omission.confidence,
                date_fait=str(omission.date_fait), date_connaissance=str(omission.date_connaissance),
                method=analysis.method_id,
            )

    for gap in analysis.discourse_action_gaps_on_thematic_objects:
        oid = f"{aid}::{gap.thematic_object_id}"
        _add_node(g, oid, kind="objet_thematique")
        _add_edge(
            g, oid, speaker.id, "ECART",
            pattern_type=gap.pattern_type.value,
            date_fait=str(gap.date_fait), date_connaissance=str(gap.date_connaissance),
            source=gap.source_reference, method=analysis.method_id,
        )

    for effect in analysis.observable_effects_on_targeted_objects:
        oid = f"{aid}::{effect.targeted_object_id}"
        _add_node(g, oid, kind="objet_vise")
        _add_edge(
            g, oid, speaker.id, "EFFET",
            effect_type=effect.effect_type.value,
            date_fait=str(effect.date_fait), date_connaissance=str(effect.date_connaissance),
            source=effect.source_reference, method=analysis.method_id,
        )

    if analysis.epistemic_synthesis:
        s = analysis.epistemic_synthesis
        _add_node(
            g, aid,
            hypothesis_gap=s.hypothesis_gap, hypothesis_status=s.hypothesis_status.value,
        )
        for i, hyp in enumerate(s.competing_hypotheses):
            hid = f"{aid}::hyp::{i}"
            _add_node(g, hid, kind="hypothesis", hyp_type=hyp.type.value,
                       confidence=hyp.confidence, label=hyp.label[:150])
            _add_edge(g, aid, hid, "HYPOTHESE", method=analysis.method_id)


def add_m03_analysis(g: nx.MultiDiGraph, analysis: M03Analysis) -> None:
    """Nœuds et arêtes pour une analyse M03 — extension M03 v2.1 section 11."""
    aid = analysis.analysis_id
    _add_node(
        g,
        aid,
        kind="analysis",
        method_id=analysis.method_id,
        method_version=analysis.method_version,
        gabarit_version=analysis.gabarit_version.value,
        execution_date=str(analysis.execution_date),
        execution_mode=analysis.execution_mode.value,
    )

    cid = f"{aid}::controversy"
    _add_node(g, cid, kind="controverse", object=analysis.controversy.object[:200],
               temporal_sequence=analysis.controversy.temporal_sequence)
    _add_edge(g, aid, cid, "PORTE_SUR", method=analysis.method_id)

    for actor in analysis.actors:
        _add_node(g, actor.actor_id, kind="person", name=actor.name, role=actor.role_at_date)
        _add_edge(g, actor.actor_id, aid, "PARTICIPE", method=analysis.method_id)
        if actor.m01_analysis_id:
            _add_edge(g, actor.actor_id, actor.m01_analysis_id, "M01_LIE",
                       method=analysis.method_id)

    for prop in analysis.structuring_propositions:
        pid = f"{aid}::{prop.proposition_id}"
        _add_node(g, pid, kind="proposition", label=prop.label)
        _add_edge(g, aid, pid, "STRUCTURE", method=analysis.method_id)

    for cell in analysis.epistemic_position_matrix:
        pid = f"{aid}::{cell.proposition}"
        _add_edge(
            g, cell.actor, pid, "POSITION_EPISTEMIQUE",
            regime=cell.regime.value, confidence=cell.confidence,
            date_fait=str(cell.date_fait), date_connaissance=str(cell.date_connaissance),
            source=cell.source_citation, method=analysis.method_id,
        )

    for cell in analysis.targeted_objects_matrix:
        oid = f"{aid}::{cell.object}"
        _add_node(g, oid, kind="objet_vise", label=cell.label)
        _add_edge(
            g, cell.actor, oid, "VISE",
            status=cell.status.value, confidence=cell.confidence,
            date_fait=str(cell.date_fait), date_connaissance=str(cell.date_connaissance),
            source="; ".join(cell.grounded_in) or None, method=analysis.method_id,
        )

    for chain in analysis.comparative_downstream_chains:
        for effect in chain.observable_effects:
            oid = f"{aid}::{effect.object}"
            _add_node(g, oid, kind="objet_vise")
            _add_edge(
                g, oid, chain.actor, "EFFET",
                effect_type=effect.effect, description=effect.description[:200],
                date_fait=str(effect.date_fait), date_connaissance=str(effect.date_connaissance),
                method=analysis.method_id,
            )

    for pred in analysis.invalidated_predictions:
        _add_edge(
            g, pred.actor, aid, "PREDICTION_INVALIDEE",
            predicted=pred.predicted[:200], pattern_type=pred.pattern_type,
            date_fait=str(pred.date_fait), date_connaissance=str(pred.date_connaissance),
            source=pred.source_citation, method=analysis.method_id,
        )

    if analysis.epistemic_synthesis:
        s = analysis.epistemic_synthesis
        _add_node(
            g, aid,
            hypothesis_gap=s.hypothesis_gap, hypothesis_status=s.hypothesis_status.value,
        )
        for i, hyp in enumerate(s.competing_hypotheses):
            hid = f"{aid}::hyp::{i}"
            _add_node(g, hid, kind="hypothesis", hyp_type=hyp.type.value,
                       confidence=hyp.confidence, label=hyp.label[:150])
            _add_edge(g, aid, hid, "HYPOTHESE", method=analysis.method_id)


def _levenshtein(a: str, b: str) -> int:
    """Distance d'édition simple (insertion/suppression/substitution, coût 1)."""
    if a == b:
        return 0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        curr = [i] + [0] * len(b)
        for j, cb in enumerate(b, start=1):
            cost = 0 if ca == cb else 1
            curr[j] = min(prev[j] + 1, curr[j - 1] + 1, prev[j - 1] + cost)
        prev = curr
    return prev[-1]


def report_near_duplicate_identifiers(g: nx.MultiDiGraph, threshold: int = 2) -> list[str]:
    """Convention §2.5 (conventions.md) — identifiants d'acteur/locuteur globaux,
    non namespacés par analyse. Une divergence de graphie (typo, variante) casse
    silencieusement la fusion de nœuds M01/M03 dans le graphe. Signale toute paire
    d'identifiants `person` distincts à distance d'édition <= threshold."""
    person_ids = sorted(n for n, attrs in g.nodes(data=True) if attrs.get("kind") == "person")
    findings = []
    for i, a in enumerate(person_ids):
        for b in person_ids[i + 1 :]:
            d = _levenshtein(a, b)
            if 0 < d <= threshold:
                findings.append(f"  • {a!r} ~ {b!r} (distance d'édition = {d})")
    return findings


def build_graph(analyses_dir: Path) -> nx.MultiDiGraph:
    """Ingère tous les YAML de analyses_dir. Les fichiers qui ne valident
    pas contre leur schéma sont ignorés et signalés — seuls les YAML
    validés entrent dans le graphe."""
    g: nx.MultiDiGraph = nx.MultiDiGraph()
    for path in sorted(analyses_dir.glob("*.yaml")):
        data = load_yaml(path)
        method_id = str(data.get("method_id", ""))
        try:
            if method_id.startswith("M03"):
                add_m03_analysis(g, M03Analysis.model_validate(data))
            else:
                add_m01_analysis(g, M01Analysis.model_validate(data))
        except ValidationError as e:
            print(f"⚠ {path.name} — ignoré, {e.error_count()} erreur(s) de validation",
                  file=sys.stderr)
    return g


def export_graph(g: nx.MultiDiGraph, export_dir: Path) -> tuple[Path, Path]:
    export_dir.mkdir(parents=True, exist_ok=True)
    graphml_path = export_dir / "graphe.graphml"
    json_path = export_dir / "graphe.json"

    nx.write_graphml(g, graphml_path)

    data = nx.node_link_data(g, edges="edges")
    json_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, default=str), encoding="utf-8"
    )
    return graphml_path, json_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--analyses-dir", type=Path, default=Path(__file__).parent / "analyses",
        help="Répertoire des YAML sources (défaut : pipeline/analyses/)",
    )
    parser.add_argument(
        "--export-dir", type=Path, default=Path(__file__).parent.parent / "exports",
        help="Répertoire d'export (défaut : exports/, non versionné)",
    )
    args = parser.parse_args()

    g = build_graph(args.analyses_dir)
    graphml_path, json_path = export_graph(g, args.export_dir)

    print(f"Graphe reconstruit — {g.number_of_nodes()} nœuds, {g.number_of_edges()} arêtes")
    print(f"Export GraphML : {graphml_path}")
    print(f"Export JSON    : {json_path}")

    near_duplicates = report_near_duplicate_identifiers(g)
    print()
    if near_duplicates:
        print("⚠ Quasi-doublons d'identifiants d'acteur détectés (conventions.md §2.5) :")
        print("\n".join(near_duplicates))
    else:
        print("✓ Aucun quasi-doublon d'identifiant d'acteur détecté (conventions.md §2.5).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
