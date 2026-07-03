# L'Entité — Résumé de la doctrine v2.1.1

*Document de cache contextuel pour pré-chargement en début de session par toutes les instances IA (Architecte, Implementer, Reviewer, Maintainer). Synthèse minimale de la doctrine canonique courante. Pour les détails — consulter `doctrine/v2.1/charte_v2_1.md` et `doctrine/v2.1/gabarit_v2_1.md`.*

---

## Identité du projet

**L'Entité** — infrastructure d'enquête forensique sur le réel produit par actions humaines, fondée sur le dévoilement (*aletheia*).

*Phrase-cœur* — la vérité est dans la qualité du chemin.
*Figure* — l'enquêteur forensique.

## Trois modes opérationnels

— *Mode 1* — éclairage médiatique d'analystes (distribution publique, finalité informative).
— *Mode 2* — conseiller du prince (distribution restreinte sous contrat, finalité décisionnelle).
— *Mode 3* — chat public auto-pédagogique (finalité éducative).

## Quatre engagements de l'ADN

1. Refus de confondre dit / fait / produit / voulu.
2. Observation située déclarée.
3. Ligne fine entre naïveté et paranoïa.
4. Refus de présupposer la chaîne causale.

## Architecture en trois couches

— *Couche A — charte.* Principes, ADN, ontologie. `doctrine/v2.1/charte_v2_1.md`.
— *Couche B — gabarit.* Schéma normatif des sorties d'analyse, 16 sections. `doctrine/v2.1/gabarit_v2_1.md` + révision mineure v2.1.1.
— *Couche C — méthodes.* Procédures opérationnelles d'analyse. `M01` (analyse rhétorique d'un discours) et `M03` (analyse comparative multi-acteurs) instanciées en v2.1.

## Principes méthodologiques saillants

— *Stratification de l'efficience par objet.* Toute analyse distingue *objets thématiques* (formellement énoncés) et *objets visés* (stratégiquement inférés). Efficience qualifiée par objet, trois valeurs — `efficient`, `efficient_partiel`, `non_efficient`.

— *Patterns observés vs fabriqués.* Patterns ancrés empiriquement par 2-3 cas externes documentables → légitimes. Patterns fabriqués a priori sans ancrage → à requalifier en inférences. L'inférence reste première sur tout pattern.

— *Sept patterns temporels du gabarit v2.1* (sous-bloc V.3) — `not_yet_observed`, `never_observed`, `observed_later`, `observed_otherwise`, `observed_by_other_actor`, `prevented_by_constraint`, `broken_explicitly`. Le pattern `broken_explicitly` exige `public_motivation_invoked` non null.

— *Trois statuts épistémiques* (synthèse) — *faits établis*, *inférences* (avec confidence et premise), *hypothèses concurrentes* (avec écart hypothèses et statut — `zone_of_indetermination`, `uncertain_dominance`, `clear_dominance`). Convention 6.7 — écart ≤ 0,2 → indétermination, 0,2 < écart ≤ 0,4 → dominance incertaine, écart > 0,4 → dominance claire.

— *Quatre opérateurs épistémiques distincts* — K (savoir factif), B (croyance), Affirme (acte de langage), Prétend_savoir (claim factif contestable).

— *Trois omissions distinctes* — *structurelle* (par contrainte de genre), *stratégique probable* (avec defeaters), *intentionnelle non prouvée*.

## Quatre modes d'exécution

— `applicable_complete` — verbatim accessible, mode normal.
— `applicable_degraded` — verbatim partiel, vigilance accrue.
— `applicable_vigilance_adversariale` — locuteur adversarial, charge éthique élevée, vigilance critique.
— `not_applicable` — méthode non exécutable en l'état (motiver le refus).

## Trois sorties obligatoires par analyse M01

— *M01-H* (sortie humaine) — lisible non-analyste, sans méta-discours méthodologique.
— *M01-M* (sortie machine) — YAML conforme au schéma Pydantic, validé par pipeline.
— *M01-P* (sortie publique) — résumé 150-300 mots avec cinq éléments structurels.

Plus journal méthodologique séparé pour le méta-discours.

## Disciplines transversales

— *Discipline anti-cumul.* Un seul document canonique par version. Versions antérieures archivées au journal, pas accumulées en parallèle.

— *Discipline de séparation H/M/P.* Pas de mélange entre sortie humaine, machine, publique. Méta-discours méthodologique séparé.

— *Discipline du typology_audit.* Pas de modification ad hoc de typologie. Friction productive → inscription au typology_audit pour examen ultérieur si confirmation par 2-3 cas externes.

— *Discipline append-only sur les journaux.* Entrées datées, jamais supprimées, révisions par nouvelles entrées.

## Découvertes méthodologiques transversales accumulées (état mai 2026)

1. Clivage stabilité/rupture transversal aux clivages thématiques.
2. CFDT pivot transversal de légitimation, à trois modes d'actualisation (déclarative / procédurale / court-circuit législatif).
3. Engagements parlementaires à seuil structurellement sous-déterminés.
4. Asymétries de bénéfice révélant la structure profonde.
5. Distinction mobilisation thématique / lexicale-marginale d'une historiographie.
6. Sept patterns temporels avec ancrage empirique.
7. Discipline anti-cumul des documents de coordination (failure pattern de gouvernance).
8. Test décisif du pipeline opérationnel — friction productive → typology_audit.
9. Division durable de la gauche post-rupture NUPES.
10. Régime adversarial — pattern d'effets observables asymétriques.
11. Typologie ternaire des stratégies de PM minoritaire (frontalité substantive / procéduralisation / concession substantielle).
12. Corrélation inverse concession-durée.
13. Apprentissage séquentiel inter-acteurs sous contrainte parlementaire constante.

Pour détails de chaque découverte — `journal/journal.md`.

## Pipeline opérationnel minimal

Pydantic v2.13 + validateurs CLI. 10 YAML M01 + 2 YAML M03 + 3 tests négatifs validés. Pipeline *minimal* — valide les YAML produits par analyses humaines, ne génère pas automatiquement les analyses depuis textes sources. Codage du système opérationnel complet en attente (Phase 0 décisions structurantes).

## Audits inscrits au gabarit v2.1.1

— `typology_audit` — deuxième audit ouvert sur deux candidats (`amplification_temporaire_terminee_par_chute`, `never_observed_by_actor_removal`).
— `intentionality_bias_audit` — 7/10 analyses M01 cas réels accumulées.
— `hypothesis_gap_audit` — 10/20-30 analyses + 2 applications M03.

---

*Résumé v1.0 — créé le 17 mai 2026. À mettre à jour à chaque évolution doctrinale majeure ou trimestriellement.*
