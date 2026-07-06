# Étalonnage 001 — comparaison sortie automatique vs analyse manuelle canonique

*Texte source : Déclaration de Politique Générale de Sébastien Lecornu, Assemblée nationale, 14 octobre 2025 (`corpus/lecornu_dpg_20251014.md`). Sortie automatique : `pipeline/analyses/M01_LECORNU_DPG_20251014_AUTO_v1/M01_LECORNU_DPG_20251014_AUTO_v1.yaml`, produite le 5 juillet 2026 en 4 appels d'agent sans réinjection (lot 2.9). Analyse manuelle canonique : `pipeline/analyses/lecornu_v2_1.yaml`, produite le 17 mai 2026. Comparaison strictement factuelle — écarts et convergences constatés, sans jugement de conformité (matière du Mode Reviewer, conformément à l'instruction du lot).*

---

## 0. Différence de base d'information — préalable factuel

Avant toute comparaison de contenu, une différence structurelle entre les deux analyses conditionne plusieurs écarts ci-dessous : l'analyse manuelle a été produite le 17 mai 2026, sept mois après le discours, avec une recherche documentaire sur les événements survenus depuis (vote du 12 novembre 2025, usage du 49.3 le 19 janvier 2026, etc.). La sortie automatique a été produite à partir du seul texte du discours (`corpus/lecornu_dpg_20251014.md`), sans document de contexte externe sur les suites effectivement observées. Les deux analyses ne disposent donc pas de la même base d'information factuelle pour les blocs qui portent sur des observations postérieures au discours (V.3, V.4, chaînes causales avales) — signalé une fois ici, valable pour les sections 3 et 4 ci-dessous.

## 1. Objets thématiques et objets visés

### 1.1 Objets thématiques

| Manuelle (3 objets) | Automatique (7 objets) |
|---|---|
| OT1 — suspension réforme retraites | obj_retraites — suspension réforme retraites (+ conférence retraites) |
| OT2 — renoncement 49.3 | obj_49_3 — renoncement 49.3 et partage du pouvoir avec le Parlement |
| OT3 — programme de méthode (gouvernement de mission) | *(recoupe obj_49_3 et obj_decentralisation, non isolé comme objet distinct)* |
| — | obj_crise_multiple — crises multiples et changement de monde |
| — | obj_budget — budget de l'État, déficit, fiscalité |
| — | obj_decentralisation — partage du pouvoir avec les collectivités locales |
| — | obj_outremer — Nouvelle-Calédonie, Outre-mer, Corse |
| — | obj_urgences_diverses — sécurité, immigration, éducation, santé, fin de vie |

**Constat factuel.** Les deux objets thématiques centraux de l'analyse manuelle (retraites, 49.3) sont retrouvés par l'automatique. L'objet manuel OT3 (« programme de méthode ») n'a pas d'équivalent isolé dans l'automatique — le thème de méthode y est distribué entre `obj_49_3` et `obj_decentralisation`. L'automatique couvre en plus quatre objets thématiques absents de la sélection manuelle (crises multiples, budget, outre-mer, urgences diverses) — la sélection manuelle est restreinte aux trois objets porteurs de la lecture stratégique retenue (négociation avec le PS pour la survie du gouvernement), tandis que l'automatique couvre l'intégralité des thèmes développés dans le texte, sans présupposer laquelle sert une stratégie de survie parlementaire.

### 1.2 Objets visés

| Manuelle (3 objets, lecture stratégique) | Automatique (5 objets, lecture textuelle) |
|---|---|
| OV1 — survie immédiate du gouvernement face à la censure (conf. 0,85) | — |
| OV2 — détacher le PS de la coalition de censure (conf. 0,80) | — |
| OV3 — maintenir la confiance des marchés financiers (conf. 0,75) | — |
| — | tgt_opposants_degagistes — opposants au changement / « dégagisme » (conf. 0,70) |
| — | tgt_partis_opposition — oppositions parlementaires (conf. 0,65) |
| — | tgt_grandes_fortunes — grandes fortunes et optimisation fiscale (conf. 0,85) |
| — | tgt_fraudeurs — fraudeurs sociaux et fiscaux (conf. 0,85) |
| — | tgt_predecesseur_bercy — pratique antérieure centrée sur Bercy (conf. 0,55) |

**Constat factuel.** Aucun recoupement direct entre les deux listes d'objets visés — les deux analyses opèrent des visées de nature différente. La manuelle identifie des cibles stratégiques de la négociation politique inter-institutionnelle (le PS, les marchés, la survie du gouvernement lui-même), déduites du contexte politique externe (motion de censure du 16 octobre). L'automatique identifie des cibles rhétoriques internes au texte (catégories désignées ou visées par les formulations du discours — dégagistes, oppositions, grandes fortunes, fraudeurs, pratique bercyenne antérieure), sans mobiliser le contexte de la motion de censure comme grille de lecture. Aucun objet visé n'est commun aux deux ensembles.

## 2. Unités argumentatives

L'analyse manuelle ne comporte aucune unité structurée (`units` absent du fichier canonique) — elle opère à un niveau agrégé (objets, chaînes causales, synthèse) sans découpage du discours en unités numérotées. L'automatique produit 18 unités (u1 à u18, non continu — u13, u15 absents des vulnérabilités/omissions listées mais présents dans le fichier), portant 17 vulnérabilités argumentatives (aucune de niveau `certain`, réparties entre `probable` et `possible`), 4 omissions, et 2 fonctions inférées. **Aucune comparaison unité-à-unité n'est possible** — c'est un écart de granularité entre les deux analyses, pas un écart de contenu comparable terme à terme.

## 3. Chaînes causales amont/aval et engagements V.3

### 3.1 Chaîne amont

| Manuelle (4 éléments) | Automatique (7 éléments) |
|---|---|
| Démission Lecornu I (6 octobre 2025) | Crise parlementaire (absence de majorité absolue) |
| Fragmentation parlementaire post-dissolution 2024 | Crises multiples entremêlées |
| Demande PS-CFDT de suspension depuis 2023 | Réforme des retraites 2023 et tensions suscitées |
| Échecs gouvernementaux antérieurs (Barnier, Bayrou) | Demande CFDT (gel de l'âge de départ) |
| — | Élections municipales et présidentielle 2027 |
| — | Fin des accords de Nouméa / accord de Bougival |
| — | Contrainte institutionnelle (49.3 politiquement risqué) |

**Constat factuel.** Deux éléments se recoupent thématiquement (demande CFDT/PS sur les retraites ; contexte de fragmentation parlementaire). L'élément manuel le plus spécifique aux événements externes au discours (« démission Lecornu I le 6 octobre 2025 ») n'a pas d'équivalent automatique — le texte du discours ne mentionne pas cet événement nommément, l'automatique ne peut le produire sans invention (cohérent avec l'interdiction du prompt Charité). L'automatique documente en plus des éléments présents dans le texte mais absents de la sélection manuelle (Nouvelle-Calédonie, élections à venir).

### 3.2 Chaînes causales avales

| Manuelle (OV1, OV2 — 2 chaînes) | Automatique (tgt_grandes_fortunes, tgt_fraudeurs, tgt_predecesseur_bercy — 3 chaînes) |
|---|---|
| Non-censure du PS le 16 octobre (observée) | Mobilisation de lobbies patronaux (plausible, non observée) |
| Alignement du groupe socialiste (observé, sourcé Vallaud 14/10) | Amendements parlementaires (plausible, non observée) |
| — | Adoption accélérée du projet de loi fraudes (plausible) |
| — | Tensions cabinet PM / administration Bercy (plausible) |

**Constat factuel.** Les objets visés étant disjoints (section 1.2), les chaînes avales portent sur des objets différents et ne sont pas comparables terme à terme. La manuelle rapporte des conséquences déjà **observées** au moment de sa rédaction (`observable_to_date` renseigné) ; l'automatique, faute de contexte documentaire externe, rapporte exclusivement des conséquences **plausibles non observées** (`observable_to_date: null` sur les deux entrées consultées) — cohérent avec le constat de la section 0.

### 3.3 Engagements V.3 (`discourse_action_gaps_on_thematic_objects`)

| Objet | Manuelle — pattern | Automatique — pattern (objet correspondant) |
|---|---|---|
| Retraites | `observed_as_announced` (suspension votée 12/11/2025, sourcée) | `not_yet_observed` (obj_retraites) |
| 49.3 | `broken_explicitly` (49.3 utilisé le 19/01/2026 malgré l'engagement, sourcé) | `not_yet_observed` (obj_49_3) |
| Méthode | `partially_observed` | *(pas d'objet thématique isolé correspondant)* |
| Budget | — | `not_yet_observed` (obj_budget) |
| Décentralisation | — | `not_yet_observed` (obj_decentralisation) |

**Constat factuel.** Les deux analyses couvrent les mêmes deux objets centraux (retraites, 49.3) mais avec des patterns nécessairement différents : la manuelle documente un écart réellement observé et sourcé (`broken_explicitly` sur le 49.3, avec citation et date du 19 janvier 2026) parce qu'elle dispose de l'information postérieure ; l'automatique assigne `not_yet_observed` aux quatre objets couverts, ce qui est la seule valeur cohérente avec l'absence de tout contexte documentaire sur les suites du discours (section 0) — l'automatique ne peut pas, et ne prétend pas, savoir si les engagements ont été tenus.

### 3.4 Effets observables sur les objets visés

Manuelle : 3 effets renseignés, tous avec date et description sourcée (motion rejetée, suspension votée, absence de crise des marchés). Automatique : **liste vide** (`observable_effects_on_targeted_objects: []`) — cohérent avec l'absence de contexte documentaire externe (section 0) et avec les objets visés disjoints (section 1.2, aucun des objets visés automatiques n'a d'effet observable documentable dans le seul texte du discours).

## 4. Hypothèses concurrentes, confidences et grille de calibration

Rappel de la grille de calibration (`doctrine/V2.1/lentite_calibration_confiance_v1.md`) : faible [0,00–0,39[, modéré [0,40–0,59], fort [0,60–0,84], établi [0,85–1,00].

| | Manuelle | Automatique |
|---|---|---|
| Nombre d'hypothèses | 4 | 4 |
| Hypothèse dominante | « négociation politique aboutie pour suspension contre non-censure » — intentionnelle, conf. 0,85 (**établi**) | « cadrage du discours (dichotomies, minimisation des contraintes) » — intentionnelle, conf. 0,45 (**modéré**) |
| Deuxième hypothèse | « stratégie à horizon présidentiel 2027 » — intentionnelle, conf. 0,65 (**fort**) | « renoncement 49.3 = adaptation contrainte » — non_intentional_or_moderate, conf. 0,55 (**modéré**) |
| `hypothesis_gap` | 0,20 | 0,10 |
| `hypothesis_status` | `zone_of_indetermination` (à la borne) | `zone_of_indetermination` |
| Bande la plus basse représentée | modéré (0,45 et 0,50) | faible (0,3) |
| Bande la plus haute représentée | établi (0,85) | modéré (0,55) |

**Constat factuel.** Les deux analyses aboutissent au même statut (`zone_of_indetermination`), mais par des profils de confidence very différents : la manuelle place son hypothèse dominante en bande « établi » (0,85) avec un écart de 0,20 — à la limite supérieure de la zone d'indétermination ; l'automatique place sa dominante en bande « modéré » (0,45) avec un écart de 0,10 — nettement à l'intérieur de la zone. L'automatique n'atteint la bande « établi » sur aucune de ses quatre hypothèses ; son maximum est 0,55. Les hypothèses elles-mêmes portent sur des objets différents : la manuelle teste des lectures de la stratégie de négociation politique externe (censure, PS, horizon 2027) ; l'automatique teste des lectures internes au texte (fonction du cadrage rhétorique, adaptation contrainte vs authentique). Aucune hypothèse n'est formulée de façon suffisamment proche entre les deux analyses pour un appariement direct.

## 5. Autres constats factuels

- **Historiographies.** Manuelle : 2 (Vème République parlementarisée ; tradition du compromis démocratique). Automatique : 3, dont une commune de fond — la doctrine gaulliste de rééquilibrage Parlement/Gouvernement, mobilisée par les deux analyses via la même idée générale, mais sourcée nommément par l'automatique (citation attribuée à Michel Debré, absente de la sélection manuelle) et une historiographie supplémentaire propre à l'automatique (cadre du « dégagisme », `mobilization_type: lexical_marginal`, `consensus_level_mobilized: disqualified`) sans équivalent manuel.
- **`null_results`.** Manuelle : 5 sophismes probables/possibles, 0 certain. Automatique : 9 sophismes probables/possibles (comptage cohérent avec les 17 vulnérabilités des 18 unités, aucune de niveau `certain`), 0 certain. Les deux analyses convergent sur l'absence de sophisme de niveau `certain`.
- **Reconstruction charitable.** Les deux reformulations centrent l'argument sur la nécessité, pour un gouvernement minoritaire, de proposer des concessions de méthode et de fond pour éviter la paralysie — convergence de fond, formulations indépendantes.
- **Omissions.** Manuelle : bloc omission non peuplé (`Omission` absent du fichier canonique — cohérent avec le constat du lot 1.5, aucune analyse du corpus initial n'avait de bloc omission structuré). Automatique : 4 omissions structurées, chacune avec les quatre champs du bloc durci (`pouvoir_agir`, `opportunite`, `cloture_corpus`, `explications_innocentes`) — pas de comparaison possible faute d'équivalent manuel, mais l'automatique produit ici une structuration que le corpus manuel existant n'avait pas encore appliquée à ce texte.

## 6. Synthèse des écarts pour le Mode Reviewer

Sans jugement de conformité, les catégories d'écarts observées sont :

1. **Granularité** — la manuelle est une lecture stratégique sélective (3 thèmes, 3 cibles), l'automatique une lecture exhaustive et unitaire (7 thèmes, 5 cibles, 18 unités). Écart de méthode d'analyse, pas de désaccord factuel sur un même objet.
2. **Base d'information** — la manuelle intègre 7 mois de suites documentées, l'automatique n'a que le texte du discours. Tous les écarts sur V.3/V.4/chaînes avales en découlent mécaniquement, pas d'une capacité différente à observer un même fait disponible.
3. **Angle des objets visés** — stratégique/externe (manuelle) vs textuel/interne (automatique), aucun recoupement direct.
4. **Profil de confidence** — l'automatique reste systématiquement plus prudent (maximum 0,55 contre 0,85 pour la manuelle), sans que cela change le statut final (`zone_of_indetermination` dans les deux cas).
5. **Structuration nouvelle** — l'automatique produit un bloc omission et un découpage en unités que l'analyse manuelle existante n'avait pas produits pour ce texte.
