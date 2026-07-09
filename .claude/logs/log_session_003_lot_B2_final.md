# Note de fin de lot — plan_action_003, séquence B, lot B.2

*Mode opérationnel : Implementer. Plan référencé : `.claude/plans/plan_action_003.md` §5 (séquence B), sur la base de `decision_006_cas_dossier_zero.md` et de l'arbitrage B.1 (`corpus/dossier_zero/candidats_T0_lot_B1.md`). Cette note **supersède** `log_session_003_lot_B2.md` (note interimaire écrite lors d'une interruption par limite d'usage de session, reprise depuis).*

---

## Sources ingérées — 25 fichiers, un commit chacun

`corpus/dossier_zero/T0/` contient désormais 25 sources, toutes vérifiées individuellement contre le bornage `date_connaissance ≤ 2023-06-30` au moment de l'écriture de chaque front matter.

### Amont documentaire (A)
1. `2019-07-18_rapport-delevoye.md` (T0-AMONT-01, A1) — `partial`.
2. `2017-09-22_ordonnance-penibilite.md` (T0-PENIBILITE-01) — `partial`.
3. `2017-09-22_rapport-president-ordonnance-penibilite.md` (T0-PENIBILITE-02) — `partial`.

### Conférence de financement 2020 (sourcing fin, priorité explicite du lot)
4. `2020-01-24_conseil-ministres-conference-financement.md` (T0-CONF-FIN-01) — `partial` (403 sur récupération directe).
5. `2020-01-30_declaration-installation-conference-financement.md` (T0-CONF-FIN-02) — `partial`.
6. `2020-01-17_fo-reponse-courrier-pm.md` (T0-CONF-FIN-03) — `partial`, citation directe confirmée (Yves Veyrier).
7. `2020-01-14_cgt-reponse-courrier-pm.md` (T0-CONF-FIN-04) — `partial`, citations Philippe Martinez.
8. `2020-03-16_macron-adresse-francais-covid19.md` (T0-CONF-FIN-05) — `partial`, citation directe confirmée.

### Alternatives de financement écartées (2023)
9. `2023-01-18_cgt-financer-retraites-salaires.md` (T0-ALT-FIN-01) — `partial`.
10. `2023-03-02_cgt-autre-reforme-retraites.md` (T0-ALT-FIN-02) — `partial`.
11. `2023-02-13_cgt-services-publics-financement.md` (T0-ALT-FIN-03) — `partial`, **friction** : guillemets imbriqués inhabituels, fidélité verbatim non garantie.

### Séquence d'adoption (B)
12. `2023-01-11_communique-intersyndical-premier-appel.md` (T0-ADOPTION-09, B3) — `uncertain`, url non_documente.
13. `2023-01-23_plfrss-dossier-legislatif.md` (T0-ADOPTION-01) — `partial`, **contradiction interne signalée** (mention d'une intervention CC au 21 mars, non retenue comme fiable).
14. `2023-02-15_an-compte-rendu-seance-csg.md` (T0-ADOPTION-02) — `partial`.
15. `2023-01-10_borne-presentation-reforme-retraites.md` (T0-ADOPTION-03, B1) — `uncertain`, cinq échecs de récupération directe, contenu de substitution (presse).
16. `2023-03-16_borne-declaration-49-3.md` (T0-ADOPTION-04, B10) — `uncertain`, citations rendues en anglais par l'outil (traduction signalée, pas verbatim français).
17. `2023-03-20_motions-censure-rejetees.md` (T0-ADOPTION-08, B11+B12 fusionnées) — `partial`, résultat du vote confirmé (278/287, 9 voix), contenu du débat non comblé.
18. `2023-03-20_2023-03-23_saisines-conseil-constitutionnel.md` (T0-ADOPTION-07, B13-B15 fusionnées) — `uncertain`, **contradiction non résolue entre deux récupérations**, `date_fait` non_documente ; **saisine présidentielle du candidat B15 original non confirmée par aucune source**.
19. `2023-04-14_cc-decision-2023-849-dc.md` (T0-ADOPTION-05, B16) — `partial`, source autonome (auparavant seulement mentionnée par renvoi).
20. `2023-04-14_loi-2023-270-promulguee.md` (T0-ADOPTION-06, B18) — `partial`, **divergence non vérifiée** sur la liste des régimes spéciaux concernés (RATP/EDF au 10 janvier vs transports/magistrats/CESE dans ce résumé).
21. `2023-04-05_berger-declaration-premiere-ministre.md` (T0-ADOPTION-10, B7) — `partial`.

### Réactions immédiates (C)
22. `2023-04-14_borne-reaction-decision-cc.md` (T0-REACTION-01, C1) — `uncertain`.
23. `2023-04-14_intersyndicale-reaction-decision-cc.md` (T0-REACTION-02, C2) — `uncertain`.
24. `2023-05-01_mobilisation-intersyndicale.md` (T0-REACTION-03, C4) — `uncertain`, documente l'annonce, pas le déroulement de la journée.

### Source complémentaire du Dirigeant
25. `2023-03-14_caeps-note-2023-07-deficit-retraites.md` (T0-CAEPS-2023-07) — intégrée selon la procédure standard, sans traitement particulier ni commentaire de fiabilité privilégié ou défavorable, conformément à l'instruction explicite. Type `statistique` (déduit de la forme), intégrité `uncertain` (document remis sans URL).

## Dates résolues vs `non_documente`

- **Résolues avec un degré de confiance raisonnable** : la quasi-totalité des 25 sources porte un `date_fait` précis et vérifié (au moins par recoupement entre deux récupérations indépendantes pour les cas les plus sensibles : décision CC du 14 avril confirmée à la fois par la décision elle-même et par le dossier législatif ; résultat du vote du 20 mars confirmé par une source de presse spécifique).
- **`date_fait` non_documente** : une seule entrée — `2023-03-20_2023-03-23_saisines-conseil-constitutionnel.md` — faute de pouvoir établir une date unique fiable pour chaque saisine individuelle à partir de deux récupérations contradictoires. Traité en friction explicite, pas en date inventée.
- **`url` non_documente** : deux entrées — le communiqué intersyndical du 11 janvier (B3) et la note CAEPS (source du Dirigeant, sans URL par nature).

## État de l'omission conférence de financement (inchangé depuis la note interimaire, réévalué — pas de nouvelle source touchant ce point dans la suite du lot)

- **`pouvoir_agir`** — suffisamment sourcé (sources T0-CONF-FIN-01/02).
- **`opportunité` (datée)** — partiellement sourcée : la fenêtre initiale (30 janvier-fin avril 2020) est bien datée ; **insuffisant pour toute affirmation sur une opportunité de relance 2020-2023** — aucune source ingérée dans ce lot (y compris les ajouts de cette reprise de session) ne documente ce second segment. Friction maintenue, non résolue.
- **`cloture_corpus`** — non applicable à ce stade (renseignée à l'assertion d'omission, séquence C.3).
- **`explications_innocentes`** — suffisamment sourcée pour au moins une alternative (T0-CONF-FIN-05 : pandémie invoquée publiquement + retrait syndical antérieur documenté par la source elle-même).

**Verdict inchangé** : sourcing insuffisant spécifiquement pour la période 2020-2023 (absence de relance documentée) ; l'épisode initial de 2020 est bien fondé. Signalé en friction, pas forcé.

## Correspondance avec les 30 candidats arbitrés en B.1 — décompte exact, recompté mécaniquement (convention `conventions.md` §6.10)

Sur les 30 candidats arbitrés, **16 sont couverts avec un degré de confiance raisonnable** (dont 3 par fusion explicite de plusieurs candidats en une seule source — B11+B12, B13+B14), **14 ne le sont pas** :

- **Couverts** : A1, A5, B1, B3, B7, B9 (partiel — CSG seulement, pas l'ensemble des débats visés par B9), B10, B11, B12 (partiel — résultat du vote couvert, contenu de l'intervention non), B13 (partiel), B14 (partiel), B16, B18, C1, C2, C4 (partiel — annonce seulement, pas le déroulement).
- **Non couverts, gap signalé plutôt que comblé par supposition** :
  - **A2** (projet de loi système universel 2020), **A3** (étude d'impact 2020), **A4** (volet pénibilité de la réforme par points 2019-2020 — distinct de l'ordonnance pénibilité 2017 déjà ingérée sous T0-PENIBILITE-01/02, qui documente un épisode antérieur et différent), **A6** (issue de la conférence de financement, ~janvier 2021 — distinct de la suspension Covid de mars 2020 déjà documentée ; aucune source sur ce point précis, cohérent avec la friction déjà signalée sur l'omission), **A7** (rapport COR 2022).
  - **B2** (dossier de presse 10 janvier), **B4** (texte initial PLFRSS), **B5** (étude d'impact PLFRSS), **B6** (avis Conseil d'État), **B8** (interventions Philippe Martinez sélectionnées — distinctes des citations CGT déjà présentes dans T0-ALT-FIN-01/02, qui portent sur le financement, pas une sélection d'interventions dédiée), **B15** (saisine par le Président de la République — explicitement **non confirmée** par les sources consultées, voir T0-ADOPTION-07), **B17** (décision(s) RIP du Conseil constitutionnel).
  - **C3** (couverture de presse recoupée du 14 avril, ≥ deux médias indépendants — exigence de recoupement de la politique de corpus v1 §2.2 non remplie dans ce lot), **C5** (réactions des oppositions à la décision du CC — une tentative de recherche a échoué, résultats hors sujet portant sur une affaire judiciaire sans rapport avec 2023, écartés sans forcer une source non pertinente).

Ce gap de 14 candidats sur 30 est concentré sur deux familles : (i) les pièces institutionnelles nécessitant un accès direct fiable à `assemblee-nationale.fr` / `legifrance.gouv.fr` (études d'impact, avis, comptes rendus détaillés), domaines ayant montré un pattern de blocage répété (403, pages vides) tout au long de ce lot ; (ii) les pièces nécessitant une sélection éditoriale fine (B8, C5) que ce lot n'a pas eu le temps de trancher avec un sourcing fiable.

## Frictions structurelles à noter pour la suite

- **Pattern de blocage `info.gouv.fr` / `vie-publique.fr` / `assemblee-nationale.fr`** — récurrent sur l'ensemble du lot, touchant au moins 4 sources structurantes (conférence de financement, discours du 10 janvier, déclaration 49.3, débat du 20 mars). Récupération manuelle par le Dirigeant recommandée en priorité pour les deux discours `uncertain` (T0-ADOPTION-03, T0-ADOPTION-04) avant tout usage comme `source_text` M01.
- **Traduction non signalée par l'outil de récupération** — au moins une source (T0-ADOPTION-04) a vu des citations françaises rendues en anglais par le modèle intermédiaire de récupération, sans avertissement — nécessite une vigilance systématique sur ce point pour toute source de presse anglophone-adjacente à l'avenir.
- **Contradictions non résolues entre récupérations indépendantes** — deux cas distincts (dates du Conseil constitutionnel autour du 21 mars ; identité de l'auteur de la saisine RIP du 20 mars) où deux tentatives de sourcing se contredisent. Ni l'une ni l'autre n'est tranchée arbitrairement — signalées comme friction, à lever par vérification directe contre la source primaire.

## Modifications de code / documents

- `corpus/dossier_zero/T0/` — 25 fichiers markdown au total (11 nouveaux dans cette reprise de session, 14 déjà ingérés avant l'interruption), front matter complet, un commit par source.
- `.claude/logs/log_session_003_lot_B2_final.md` — cette note, superséde la note interimaire.

Lot B.2 clos sur cet état — 25 fichiers ingérés dans `corpus/dossier_zero/T0/` couvrant 16 des 30 candidats arbitrés en B.1 (dont 3 par fusion explicite), 14 candidats non couverts et documentés ci-dessus comme gap plutôt que comblés par supposition, aucune invention pour combler les manques. Arrêt conforme à l'instruction.
