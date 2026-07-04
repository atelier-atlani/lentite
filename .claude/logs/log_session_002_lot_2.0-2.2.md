# Log de session — plan_action_002, lot {2.0–2.2}

*Mode opérationnel : Implementer. Plan référencé : `.claude/plans/plan_action_002.md` §4 séquence 2. Tâche 2.0 est un arbitrage Architecte préliminaire, insérée avant 2.1/2.2 tels que numérotés dans le plan d'origine.*

---

## Tâches accomplies

**2.0 — Extension de la bitemporalité à M03 (arbitrage Architecte).** `pipeline/schemas_m03.py` importe désormais `GabaritVersion`/`NON_RENSEIGNE`/`BitemporalDate` de `schemas.py` (pas de duplication). Champ `gabarit_version` ajouté à `M03Analysis`. `date_fait`/`date_connaissance` ajoutés sur quatre modèles, choisis par parallélisme avec le périmètre M01 de la tâche 1.2 — `EpistemicCell`, `TargetedObjectCell` (cellules des deux matrices, cœur analytique de M03), `ActorObservableEffect` (analogue direct de `ObservableEffect`), `InvalidatedPrediction` (analogue direct de `DiscourseActGap`). Validateur conditionnel symétrique à celui de `M01Analysis`. Le bloc omission M03 reste explicitement hors scope, comme demandé — `M03Analysis` n'a pas d'équivalent `Omission`, question doctrinale renvoyée au Reviewer.

Test négatif M03 créé (`pipeline/tests/negatif_m03_bitemporalite_manquante_gabarit_durci.yaml`, fixture minimale à 3 acteurs), rejeté avec erreur ciblée ; contre-vérification positive effectuée.

Les 2 YAML M03 amendés (mêmes règles que le lot 1.5 — sourcé, aucune invention, un commit par fichier) :
- `epistemic_position_matrix` / `targeted_objects_matrix` — `date_fait` dérivé mécaniquement de la date d'énonciation du M01 lié par acteur (déjà présente au corpus, aucune invention). 18+21 cellules (fichier 3 acteurs), 24+32 cellules (fichier 4 acteurs) — 100% réel par construction.
- `comparative_downstream_chains` / `invalidated_predictions` — sourcing par entrée, dates explicites dans le texte ou renvoi documenté à l'amendement 1.5 du M01 correspondant quand le même événement y est déjà daté (précédent Vallaud du lot 1.5, étendu ici de façon symétrique) ; `non_documente` sinon.

**2.1 — `validate.py` M01.** Restauré par dérivation directe de `validate_m03.py` — même structure (chargement YAML, rapport d'erreurs Pydantic détaillé, rapport de succès, code retour 0/1). Rapport de succès adapté aux blocs M01 (énonciation, objets, unités, écarts V.3, effets V.4, historiographies, synthèse épistémique, résultats nuls). Vérifié sur les 10 YAML M01 positifs (code 0) et les 5 tests négatifs M01 (code 1).

README racine mis à jour — toute mention « validate.py absent » retirée (§2, §6.2, §6.3, §11), usage documenté. `pipeline/lentite_README_projet.md` **fusionné** (choix signalé, alternative resynchronisation examinée et écartée) — réduit à un pointeur vers le README racine §6, pour ne pas reconstituer un second document vivant sur le même sujet après une première dérive déjà documentée au journal (friction d'onboarding).

**2.2 — `graph_builder.py`.** Ingestion de tous les YAML valides de `pipeline/analyses/` (M01-M et M03-M, dispatch par préfixe `method_id`) → graphe `networkx.MultiDiGraph` unique. Nœuds typés (`analysis`, `person`, `objet_thematique`, `objet_vise`, `proposition`, `controverse`, `unite`, `vulnerabilite`, `omission`) ; arêtes typées portant les attributs épistémiques sur les assertions durcies en 1.2/2.0 (source, confiance, méthode, `date_fait`/`date_connaissance`). Les identifiants de personne (`speaker.id` / `actor_id`) ne sont pas namespacés par analyse — un acteur réel présent à la fois en M01 et en M03 (ex. `MICHEL_BARNIER`) fusionne son nœud, produisant le pont M01↔M03 (arête `M01_LIE`) qui matérialise le graphe cognitif de la décision 002.

Exports `exports/graphe.graphml` + `exports/graphe.json`, déjà couverts par `.gitignore` (aucune modification nécessaire). Reconstruction intégrale vérifiée déterministe sur deux exécutions successives (JSON identique). Corpus complet ingéré sans erreur — 121 nœuds, 291 arêtes.

`networkx==3.6.1` ajouté à `requirements.txt` (version installée et confirmée fonctionnelle, même discipline que pydantic/PyYAML lors de l'onboarding).

## Frictions et choix d'implémentation signalés

1. **Périmètre des 4 modèles M03 durcis (2.0).** Choix analogue à celui documenté au lot {1.1–1.2} pour M01 — `BenefitAsymmetry` et `CrossMatrixCase` laissés hors périmètre (synthèse/agrégat, pas assertion atomique), cohérent avec le traitement de `Historiography`/`Hypothesis` en M01. Non tranché par le plan explicitement, documenté ici.
2. **Sourcing cross-fichier étendu (2.0).** Le précédent du lot 1.5 (Vallaud, un seul cas) est généralisé ici à plusieurs entrées M03 dont le fait décrit est manifestement le même événement déjà daté dans le M01 correspondant (ex. conclave Bayrou 26/06/2025, censure Barnier 4/12/2024). Chaque réutilisation est commentée en ligne dans le YAML amendé pour rester auditable.
3. **Fusion plutôt que resynchronisation de `pipeline/lentite_README_projet.md` (2.1).** Décision explicitement signalée dans les deux README concernés et dans ce log — alternative de resynchronisation intégrale examinée et écartée, le document ayant déjà dérivé une première fois malgré son statut de document vivant distinct.
4. **Portée du graphe (2.2).** Prototype scopé aux structures et assertions déjà durcies (parallélisme avec 1.2/2.0) — `arena_structure`, `interpretive_frames`, `asymmetries_of_benefit`, `epistemic_synthesis` (hypothèses) ne sont pas représentés comme nœuds/arêtes dans cette version. Extension possible si le Reviewer ou l'usage des audits (tâche 2.3) le demande.
5. **`--all` non implémenté sur les validateurs.** Le plan ne le demande pas explicitement pour 2.1 (seule l'interface `python validate.py <fichier>` est spécifiée) ; l'ancien `pipeline/lentite_README_projet.md` (état de mai 2026, fusionné) mentionnait un `--all` qui n'a jamais été vérifié comme existant. Non implémenté ici, signalé au README comme capacité restante.

## État des tests

12/12 YAML positifs (10 M01 + 2 M03) valident sous `gabarit_version=2.1-durci-seq1`. 6/6 tests négatifs rejetés (3 M01 préexistants + 2 M01 du lot {1.1–1.2} + 1 M03 nouveau de ce lot). `validate.py` et `validate_m03.py` vérifiés en CLI sur l'ensemble du corpus (codes retour 0/1 corrects). `graph_builder.py` vérifié sans erreur sur le corpus complet, reconstruction déterministe confirmée.

## Modifications de code / documents

- `pipeline/schemas_m03.py` — bitemporalité étendue (tâche 2.0).
- `pipeline/tests/negatif_m03_bitemporalite_manquante_gabarit_durci.yaml` — nouveau.
- `pipeline/analyses/m03_bayrou_barnier_lecornu_v2_1.yaml`, `m03_retraites_octobre_2025_4acteurs_v2_1.yaml` — amendés.
- `pipeline/validate.py` — nouveau (restauré).
- `lentite_README_projet.md` — mis à jour (2.1, puis 2.2).
- `pipeline/lentite_README_projet.md` — réduit à un pointeur.
- `pipeline/graph_builder.py` — nouveau.
- `requirements.txt` — `networkx==3.6.1` ajouté.

## État du système

Séquence 2 en cours — tâches 2.0, 2.1, 2.2 faites. Restent 2.3 (audits en CLI), 2.4-2.6 (orchestrateur, prompts, format de log), 2.7 (étalonnage bout en bout). L'écart au §9 du plan signalé aux lots précédents (séquence 0 non formellement close) reste ouvert, indépendant de l'avancement de la séquence 2.

## Recommandations pour la suite

- Tâche 2.3 (audits) pourra s'appuyer directement sur `graph_builder.py` — les trois audits du gabarit (`intentionality_bias_audit`, `hypothesis_gap_audit`, `typology_audit`) sont spécifiés comme des parcours de graphe NetworkX par le plan.
- Décision à prendre avant ou pendant 2.4 : le graphe doit-il être étendu aux blocs actuellement hors périmètre (arena_structure, hypothèses, asymétries) si les audits en ont besoin.
- Le point ouvert sur le bloc omission M03 (hors scope de 2.0, renvoyé au Reviewer) reste à trancher indépendamment de la séquence 2.

---

*Commits de ce lot : voir historique git, préfixes `feat(schemas)` / `feat(analyses)` / `test(pipeline)` / `feat(pipeline)` / `docs(readme)`.*
