#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""
L'Entité — Audits du gabarit v2.1/v2.1.1 comme parcours du graphe cognitif.

Trois audits canoniques (gabarit v2.1 section 16, étendu par la révision
v2.1.1) :
  - intentionality_bias_audit — fréquence des hypothèses intentionnelles
    dominantes. Fenêtre roulante de 10 analyses, seuil d'alerte 80%.
  - hypothesis_gap_audit — distribution des écarts hypothèses. Fenêtre
    roulante de 20-30 analyses, concentration surveillée sur [0.18, 0.22].
  - typology_audit — recensement mécanique de l'usage des typologies
    ouvertes du gabarit (charte v2.1 section 6.6). Le jugement d'ancrage
    empirique (maintenue / requalifiée / supprimée) reste humain.

Usage:
    python3 audits.py <intentionality_bias_audit|hypothesis_gap_audit|typology_audit>
    python3 audits.py --all
"""

from __future__ import annotations
import argparse
import statistics
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import networkx as nx

from graph_builder import build_graph

INTENTIONALITY_WINDOW = 10
INTENTIONALITY_ALERT_THRESHOLD = 0.8

HYPOTHESIS_GAP_WINDOW = (20, 30)
HYPOTHESIS_GAP_CONCENTRATION_BAND = (0.18, 0.22)
# Friction — seuil non spécifié par la doctrine, voir note dans le rapport.
HYPOTHESIS_GAP_CONCENTRATION_ALERT_THRESHOLD = 0.5

TEMPORAL_PATTERN_CANONICAL = [
    "not_yet_observed", "never_observed", "observed_later", "observed_otherwise",
    "observed_by_other_actor", "prevented_by_constraint", "broken_explicitly",
    "observed_as_announced", "partially_observed",
]


def _sorted_analyses(g: nx.MultiDiGraph) -> list[tuple[str, dict]]:
    analyses = [(n, a) for n, a in g.nodes(data=True) if a.get("kind") == "analysis"]
    analyses.sort(key=lambda x: (x[1].get("execution_date", ""), x[0]))
    return analyses


def run_intentionality_bias_audit(g: nx.MultiDiGraph) -> str:
    analyses = _sorted_analyses(g)
    window = analyses[-INTENTIONALITY_WINDOW:]
    lines = [
        "# Audit — intentionality_bias_audit",
        "",
        f"*Fenêtre roulante : {INTENTIONALITY_WINDOW} analyses (gabarit v2.1.1 section 16). "
        f"Seuil d'alerte : {INTENTIONALITY_ALERT_THRESHOLD:.0%} de dominante intentionnelle.*",
        "",
    ]
    if len(analyses) < INTENTIONALITY_WINDOW:
        lines += [
            f"**Avertissement.** Corpus actuel ({len(analyses)} analyses) sous la taille "
            f"nominale de la fenêtre ({INTENTIONALITY_WINDOW}). Audit exécuté sur l'ensemble "
            "disponible, à titre informatif — pas le « premier audit » officiel au sens du "
            "gabarit, qui attend l'accumulation complète (cf. `journal/lentite_journal.md`).",
            "",
        ]

    rows = []
    dominant_intentional_count = 0
    ties: list[str] = []
    for aid, _ in window:
        hyps = [attrs for n, attrs in g.nodes(data=True)
                if attrs.get("kind") == "hypothesis" and g.has_edge(aid, n)]
        if not hyps:
            continue
        max_conf = max(h["confidence"] for h in hyps)
        dominants = [h for h in hyps if h["confidence"] == max_conf]
        dominant_types = sorted({h["hyp_type"] for h in dominants})
        is_intentional = dominant_types == ["intentional"]
        if len(dominants) > 1 and len(dominant_types) > 1:
            ties.append(aid)
        if is_intentional:
            dominant_intentional_count += 1
        rows.append((aid, max_conf, dominant_types, len(dominants) > 1))

    n = len(rows)
    ratio = dominant_intentional_count / n if n else 0.0
    lines += [
        f"Analyses examinées : {n}",
        f"Hypothèse dominante intentionnelle : {dominant_intentional_count}/{n} ({ratio:.0%})",
        "",
        "| Analyse | Confidence dominante | Type(s) dominant(s) | Égalité |",
        "|---|---|---|---|",
    ]
    for aid, conf, types, tied in rows:
        lines.append(f"| {aid} | {conf:.2f} | {', '.join(types)} | {'oui' if tied else 'non'} |")
    lines.append("")

    if ratio >= INTENTIONALITY_ALERT_THRESHOLD:
        lines.append(
            f"**ALERTE** — {ratio:.0%} ≥ seuil {INTENTIONALITY_ALERT_THRESHOLD:.0%}. "
            "Examen méthodologique à envisager (gabarit v2.1.1)."
        )
    else:
        lines.append(f"Pas d'alerte — {ratio:.0%} < seuil {INTENTIONALITY_ALERT_THRESHOLD:.0%}.")

    if len(analyses) > len(window):
        full_count = 0
        full_n = 0
        for aid, _ in analyses:
            hyps = [attrs for n, attrs in g.nodes(data=True)
                    if attrs.get("kind") == "hypothesis" and g.has_edge(aid, n)]
            if not hyps:
                continue
            full_n += 1
            max_conf = max(h["confidence"] for h in hyps)
            if sorted({h["hyp_type"] for h in hyps if h["confidence"] == max_conf}) == ["intentional"]:
                full_count += 1
        full_ratio = full_count / full_n if full_n else 0.0
        excluded = [aid for aid, _ in analyses[: len(analyses) - len(window)]]
        lines += [
            "",
            f"**Friction — ordonnancement de la fenêtre roulante.** Toutes les analyses du corpus "
            f"partagent le même `execution_date` (production par lot) ; aucune donnée de date de "
            f"production individuelle n'existe pour ordonner une vraie « fenêtre roulante ». Le tri "
            "de repli (execution_date puis identifiant alphabétique) exclut arbitrairement "
            f"{len(excluded)} analyse(s) du calcul ci-dessus : {', '.join(excluded)}. Sur "
            f"l'ensemble du corpus ({full_n} analyses, sans fenêtre), le ratio est {full_ratio:.0%} "
            f"({full_count}/{full_n}) — même verdict d'alerte que ci-dessus, mais ce ne sera pas "
            "toujours le cas sur un corpus futur. Signalé plutôt que masqué par le tri de repli.",
        ]

    if ties:
        lines += [
            "",
            f"**Friction — égalités de confidence.** {len(ties)} analyse(s) présentent une égalité "
            "de confidence maximale entre hypothèses de types différents (dominance non tranchée) : "
            f"{', '.join(ties)}. La doctrine ne spécifie pas de règle de départage pour ce cas ; "
            "ces analyses sont exclues du numérateur « dominante intentionnelle » par choix "
            "conservateur, signalé ici plutôt qu'arbitré silencieusement.",
        ]

    lines += [
        "",
        "**Note d'interprétation.** Le type `non_intentional_or_moderate` (`pipeline/schemas.py`) "
        "n'a pas de définition doctrinale dédiée pour cet audit ; il est traité comme non-intentionnel "
        "(il ne correspond jamais littéralement à `intentional`). Signalé comme interprétation de "
        "l'implémentation, pas comme règle doctrinale établie.",
    ]
    return "\n".join(lines)


def run_hypothesis_gap_audit(g: nx.MultiDiGraph) -> str:
    analyses = _sorted_analyses(g)
    lo, hi = HYPOTHESIS_GAP_WINDOW
    band_lo, band_hi = HYPOTHESIS_GAP_CONCENTRATION_BAND
    lines = [
        "# Audit — hypothesis_gap_audit",
        "",
        f"*Fenêtre roulante : {lo}-{hi} analyses (gabarit v2.1.1 section 16). Critère documenté "
        "(`analyses/cas_jouets/lentite_cas_jouets_1_5_6_v2_1.md`, bilan transversal) : concentration "
        f"excessive de l'écart hypothèses dans la bande [{band_lo}, {band_hi}].*",
        "",
    ]
    if len(analyses) < lo:
        lines += [
            f"**Avertissement.** Corpus actuel ({len(analyses)} analyses) sous la taille "
            f"nominale de la fenêtre ({lo}-{hi}). Audit exécuté sur l'ensemble disponible, à "
            "titre informatif — pas le « premier audit » officiel au sens du gabarit.",
            "",
        ]

    gaps = [(aid, a["hypothesis_gap"], a["hypothesis_status"])
            for aid, a in analyses if "hypothesis_gap" in a]
    values = [v for _, v, _ in gaps]
    n = len(values)
    lines.append(f"Analyses examinées : {n}")
    if n:
        lines += [
            f"Écart moyen : {statistics.mean(values):.3f}",
            f"Écart médian : {statistics.median(values):.3f}",
            f"Min / Max : {min(values):.2f} / {max(values):.2f}",
        ]
    lines.append("")

    lines += ["### Distribution par statut (convention 6.7)", "", "| Statut | Effectif | Part |", "|---|---|---|"]
    status_counts = Counter(s for _, _, s in gaps)
    for status in ("zone_of_indetermination", "uncertain_dominance", "clear_dominance"):
        c = status_counts.get(status, 0)
        lines.append(f"| {status} | {c} | {c / n:.0%} |" if n else f"| {status} | 0 | — |")
    lines.append("")

    in_band = [aid for aid, v, _ in gaps if band_lo <= v <= band_hi]
    ratio_band = len(in_band) / n if n else 0.0
    lines += [
        f"### Concentration dans la bande [{band_lo}, {band_hi}]",
        "",
        f"{len(in_band)}/{n} analyses ({ratio_band:.0%}) — " + (", ".join(in_band) if in_band else "(aucune)"),
        "",
        "| Analyse | Écart | Statut |",
        "|---|---|---|",
    ]
    for aid, v, s in gaps:
        lines.append(f"| {aid} | {v:.2f} | {s} |")
    lines.append("")

    if ratio_band >= HYPOTHESIS_GAP_CONCENTRATION_ALERT_THRESHOLD:
        lines.append(
            f"**ALERTE (seuil interprété)** — {ratio_band:.0%} ≥ "
            f"{HYPOTHESIS_GAP_CONCENTRATION_ALERT_THRESHOLD:.0%} dans la bande de concentration."
        )
    else:
        lines.append(
            f"Pas d'alerte sur ce seuil interprété — {ratio_band:.0%} < "
            f"{HYPOTHESIS_GAP_CONCENTRATION_ALERT_THRESHOLD:.0%}."
        )

    lines += [
        "",
        "**Friction — seuils d'alerte non spécifiés par la doctrine.** Le gabarit v2.1.1 et sa "
        "documentation dérivée (README §9) mentionnent « trois seuils d'alerte » pour cet audit sans "
        "jamais les définir textuellement dans un document doctrinal. Le seul critère explicite "
        "retrouvé (`lentite_cas_jouets_1_5_6_v2_1.md`) est la concentration dans la bande "
        f"[{band_lo}, {band_hi}] — implémenté ci-dessus avec un seuil d'alerte de "
        f"{HYPOTHESIS_GAP_CONCENTRATION_ALERT_THRESHOLD:.0%} choisi par cette implémentation, non "
        "spécifié par le gabarit, signalé ici plutôt qu'arbitré silencieusement. Les deux autres "
        "seuils annoncés ne sont pas implémentés faute de définition retrouvée — cœur interprétable "
        "seulement, par consigne du lot.",
    ]
    return "\n".join(lines)


def run_typology_audit(g: nx.MultiDiGraph) -> str:
    lines = [
        "# Audit — typology_audit",
        "",
        "*Recensement mécanique de l'usage des typologies ouvertes du gabarit (charte v2.1 "
        "section 6.6, ancrage empirique). Le jugement de maintien, requalification ou suppression "
        "d'une catégorie reste humain — cet audit produit le constat factuel d'usage, pas la "
        "décision.*",
        "",
    ]

    def census(title: str, values, canonical: list[str] | None = None) -> list[str]:
        counts = Counter(values)
        block = [f"### {title}", ""]
        if not counts:
            block += ["*Aucune occurrence dans le corpus actuel.*", ""]
            return block
        block += ["| Valeur | Occurrences |", "|---|---|"]
        for val, c in counts.most_common():
            block.append(f"| {val} | {c} |")
        if canonical:
            unused = sorted(set(canonical) - set(counts))
            if unused:
                block += ["", f"*Valeurs canoniques jamais observées dans ce corpus* : {', '.join(unused)}"]
        block.append("")
        return block

    pattern_types = [d["pattern_type"] for _, _, d in g.edges(data=True) if d.get("type") == "ECART"]
    lines += census("Patterns temporels (`TemporalPattern`, M01, bloc V.3)",
                     pattern_types, canonical=TEMPORAL_PATTERN_CANONICAL)

    effect_types_m01 = [d["effect_type"] for _, _, d in g.edges(data=True)
                         if d.get("type") == "EFFET" and d.get("method") == "M01_ANALYSE_RHETORIQUE"]
    lines += census("Effets observables M01 (`ObservableEffectType`, schéma fermé)", effect_types_m01)

    effect_types_m03 = [d["effect_type"] for _, _, d in g.edges(data=True)
                         if d.get("type") == "EFFET" and d.get("method") == "M03_ANALYSE_COMPARATIVE_MULTI_ACTEURS"]
    lines += [
        "*M03 `effect` est un champ texte libre (`str`), pas un enum contraint par schéma — "
        "recensement fourni à titre de matière pour un futur typology_audit M03, distinct du "
        "gabarit M01.*",
        "",
    ]
    lines += census("Effets observables M03 (texte libre, non contraint par schéma)", effect_types_m03)

    regimes = [d["regime"] for _, _, d in g.edges(data=True) if d.get("type") == "POSITION_EPISTEMIQUE"]
    lines += census("Régimes épistémiques M03 (`EpistemicMatrixRegime`)", regimes)

    statuses = [d["status"] for _, _, d in g.edges(data=True) if d.get("type") == "VISE" and "status" in d]
    lines += census("Statuts d'objet visé M03 (`TargetedObjectStatus`)", statuses)

    vuln_levels = [a["level"] for _, a in g.nodes(data=True) if a.get("kind") == "vulnerabilite"]
    lines += census("Niveaux de vulnérabilité (`VulnerabilityLevel`, M01)", vuln_levels)

    omission_levels = [a["level"] for _, a in g.nodes(data=True) if a.get("kind") == "omission"]
    lines += census("Niveaux d'omission (`OmissionLevel`, M01)", omission_levels)

    lines.append(
        "**Friction — portée du recensement.** Ce parcours de graphe ne voit que ce qui est encodé "
        "dans les schémas Pydantic (YAML validés). Les candidats de typologie signalés narrativement "
        "dans les analyses markdown (par exemple `never_observed_by_actor_removal` sur Barnier, "
        "`amplification_temporaire_terminee_par_chute` sur Bayrou) ne sont pas visibles depuis le "
        "graphe — ils vivent en texte libre dans `analyses/m01/*.md`, hors du YAML structuré. Un "
        "typology_audit complet au sens du gabarit (charte v2.1 section 6.6) demande une lecture "
        "humaine de ces candidats narratifs en complément de ce recensement mécanique."
    )
    return "\n".join(lines)


AUDITS = {
    "intentionality_bias_audit": run_intentionality_bias_audit,
    "hypothesis_gap_audit": run_hypothesis_gap_audit,
    "typology_audit": run_typology_audit,
}


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("audit", nargs="?", choices=list(AUDITS), help="Nom de l'audit à exécuter")
    parser.add_argument("--all", action="store_true", help="Exécute les trois audits")
    parser.add_argument(
        "--analyses-dir", type=Path, default=Path(__file__).parent / "analyses",
        help="Répertoire des YAML sources (défaut : pipeline/analyses/)",
    )
    parser.add_argument(
        "--export-dir", type=Path, default=Path(__file__).parent.parent / "exports" / "audits",
        help="Répertoire d'export (défaut : exports/audits/, non versionné)",
    )
    args = parser.parse_args()

    if not args.all and not args.audit:
        parser.error("préciser un audit (voir --help) ou --all")

    g = build_graph(args.analyses_dir)
    args.export_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    names = list(AUDITS) if args.all else [args.audit]
    for name in names:
        report = AUDITS[name](g)
        out_path = args.export_dir / f"{name}_{timestamp}.md"
        out_path.write_text(report, encoding="utf-8")
        print(f"✓ {name} → {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
