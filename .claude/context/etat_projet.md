# L'Entité — État du projet

*Document de cache contextuel pour pré-chargement en début de session par toutes les instances IA. Vue compacte et factuelle de l'état courant. Mise à jour à chaque évolution majeure. Pour navigation détaillée — `README.md` à la racine du projet et `journal/lentite_journal.md`.*

---

## Date de référence

**12 juillet 2026.** Phase 0 (codage) close. Phase 1 en cours (`plan_action_003.md`, dossier zéro rétrospectif) — cas sélectionné (décision 006) : la réforme des retraites 2023, arc complet (amont documentaire 2019-2022 jusqu'aux réactions immédiates de juin 2023). T0 bornage : `date_connaissance ≤ 2023-06-30`. T1 (confrontation) : 1er septembre 2023 – 31 décembre 2025, sous scellé jusqu'à la séquence D.

---

## Séquence B (constitution des corpus) — CLOSE

`corpus/dossier_zero/T0/` — **30 sources**, front matter complet (type selon politique de corpus v1, provenance, intégrité, dates bitemporelles), un commit par source. Répartition par acteur (inventaire vérifié le 11 juillet 2026) :

- **Gouvernement** — robustement couvert (8 sources : Delevoye 2019, conférence de financement 2020, adresse Macron Covid, présentation Borne 10 janvier 2023, étude d'impact PLFRSS, verbatim officiel du 49.3, réaction Borne à la décision CC, loi promulguée).
- **Syndicats** — CGT (4 sources), FO (1, 2020 seulement), CFDT (1, Berger 5 avril), intersyndicale collective (3).
- **Oppositions parlementaires** — RN, LFI, LR : chacun une source primaire dédiée (lot B.2-ter) en plus des citations enchâssées dans le verbatim du 49.3.
- **Expertise/contrôle** — Conseil constitutionnel (2 sources) + rapport annuel COR 2022 (lot B.2-ter, comble un gap identifié après B.2-bis).
- Source complémentaire du Dirigeant (note CAEPS) intégrée selon la procédure standard, sans traitement privilégié.

18/30 candidats de la liste d'arbitrage B.1 restent non couverts (détail : `.claude/logs/log_session_003_lot_B2_final.md`) — gap documenté, pas comblé silencieusement. Lots B.2, B.2-bis (verbatim 49.3 corrigé après dépôt d'un mauvais fichier ; contradiction des saisines CC résolue), B.2-ter (COR + 3 oppositions).

---

## Séquence C (production du dossier, régime T0 strict) — EN COURS

**C.1 — M01 automatiques sur les discours structurants.** Cible du plan : 3-5 discours. **5 M01 produits à ce jour**, cible atteinte :

| M01 | Source | Intégrité | Corrections humaines |
|---|---|---|---|
| Borne, 10 janvier 2023 | presse (source T0 dégradée) | `uncertain` | 1 (métadonnée) |
| Borne, 49.3, 16 mars 2023 | verbatim officiel | `certified` | 1 (métadonnée) |
| CGT, 2 mars 2023 | communiqué | `partial` | 2 (rupture de clôture de corpus) |
| LFI, 30 janvier 2023 | communiqué | `partial` | 1 (rupture de clôture de corpus) |
| RN, 3 mai 2023 | communiqué | `partial` | 2 (rupture de clôture de corpus, dont une pseudo-citation fabriquée) |

Tous validés sans réinjection (4 appels d'agent chacun). **Motif structurel repéré sur le lot C.1-bis** : tendance de l'agent Chaînes causales/Synthèse à injecter une connaissance générale hors du texte source fourni (rupture de la clôture de corpus par discours), plus marquée sur les sources courtes (communiqués) que sur le verbatim officiel — point à surveiller sur les M01 suivants, matière possible pour un audit dédié.

**C.2 (M03 comparatif multi-acteurs), C.3 (bloc omissions), C.4 (synthèse du dossier)** — non engagées.

**C.5 (chiffrage de la boucle humaine, mesure 1)** — premier point de données obtenu (voir ci-dessous), pas encore consolidé sur l'ensemble de la séquence.

---

## Mesures acquises

- **Mesure 1 (C.5, chiffrage de la boucle humaine)** — établie par le Dirigeant sur le lot C.1 (les deux M01 Borne) : **30 minutes de lecture attentive par M01, en lecteur adverse ; zéro correction de fond**, seules corrections = métadonnées. Production automatique mesurée par horodatage des logs d'agents : 2 à 3 minutes par M01 selon les cinq analyses produites à ce jour. **Ratio production/validation ≈ 1:10.** Extrapolation dossier complet : ordre de grandeur de 6-10h humaines de validation, hors constitution de corpus. Marquée **quatrième rendement empirique du projet** (journal, entrée du 12 juillet 2026), aux côtés de l'asymétrie de datation 21/36, l'alerte intentionnalité 80-83% (gelée, test discriminant sur ce dossier), et la discipline `not_yet_observed` observée en production. Établie sur échantillon par le Dirigeant, pas recalculée à chaque pièce par l'Implementer (les corrections du lot C.1-bis, plus substantielles que celles de C.1, n'ont pas encore été chronométrées par un humain réel).
- **Coût machine d'une passe M01** — stable autour de 2-3 minutes, 4 appels d'agent, aucune réinjection sur les 5 analyses produites dans le dossier zéro.

---

## Documents candidats v2.2 (hors canon)

`dev/candidats_v2_2/` — fondation épistémologique + backlog doctrinal pipeline, sous moratoire jusqu'à clôture du dossier zéro (`plan_action_003` E.4). Aucune modification de schéma ni de doctrine v2.1 canonique. Matière retenue (items backlog, refus motivés, notes de vigilance, graphe abductif Phase 3) versée au journal, entrée du 12 juillet 2026.

---

## Points en attente d'action du Dirigeant

- **Feu vert pour le prochain lot de séquence C** — C.1 ayant atteint sa fourchette cible (5 M01 sur 3-5 prévus), le plan indique C.2 (M03 comparatif multi-acteurs) comme étape suivante, mais aucun lot n'a été explicitement engagé au-delà de C.1-bis.
- **Décision sur les 18/30 candidats non couverts de la liste B.1** — rouvrir la constitution de corpus (nouveau lot B.x) ou considérer la séquence B close en l'état.
- **Examen des documents candidats v2.2** — reporté par construction jusqu'à la clôture du dossier zéro (E.4), pas une action immédiate.
- **Reportés depuis la clôture de Phase 0** (non bloquants pour la Phase 1, mais toujours ouverts) — trace du re-test d'onboarding par un tiers réellement indépendant ; relecture juridique du CLA, requise avant la première PR externe.

---

## Prochaine action exacte au retour

Attendre l'instruction du Dirigeant pour le prochain lot de séquence C (vraisemblablement C.2 — M03 comparatif multi-acteurs — puisque C.1 a atteint sa fourchette cible de 3-5 M01) plutôt que d'engager un nouveau lot de sa propre initiative.

---

## Documents canoniques (navigation)

— *Plan actif* — `.claude/plans/plan_action_003.md`.
— *Décision du cas* — `.claude/decisions/decision_006_cas_dossier_zero.md`.
— *Corpus T0* — `corpus/dossier_zero/T0/` (30 sources) ; liste d'arbitrage `corpus/dossier_zero/candidats_T0_lot_B1.md`.
— *Analyses M01* — `pipeline/analyses/M01_*_AUTO_v1/`.
— *Journal méthodologique* — `journal/lentite_journal.md`.
— *Notes de fin de lot* — `.claude/logs/log_session_003_lot_*.md`.

---

*État du projet — mis à jour le 12 juillet 2026 (reprise de contexte, séquence C en cours). Prochaine mise à jour attendue à la clôture de C.2 ou au prochain feu vert du Dirigeant.*
