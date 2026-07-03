# L'Entité — Grille de calibration des degrés de confiance v1

*Licence : CC BY 4.0.*

*Document couche B — gabarit v2.1. Version de démarrage (plan_action_002 séquence 1, tâche 1.4). Spécifie la grille de calibration et le protocole inter-annotateurs ; l'exécution du protocole n'est pas couverte par ce document — hors périmètre de ce lot.*

---

## 1. Objet

Ce document fixe une grille de lecture qualitative à quatre degrés (faible/modéré/fort/établi) pour le score numérique `confidence` (0,0–1,0) déjà défini par le gabarit v2.1 (section 6.7 et `pipeline/schemas.py`), promeut les trois cas-jouets 1, 5 et 6 en cas-étalons officiels de cette grille, et spécifie — sans l'exécuter — un protocole inter-annotateurs de mesure d'écart.

**Avertissement terminologique.** Le degré « établi » de cette grille qualifie un score de `confidence` élevé sur une inférence ou une hypothèse — ce n'est *pas* le statut épistémique « fait établi » des trois statuts de la charte v2.1. Un fait établi n'est pas noté sur l'échelle 0–1 ; il est vérifiable indépendamment sans construction inférentielle. Confondre les deux reviendrait à traiter une confidence comme une vérité — pattern d'échec déjà recensé (`confidence_treated_as_truth`, journal méthodologique de M01, gabarit v2.1 section 16).

## 2. Grille à quatre degrés

| Degré | Plage numérique | Lecture |
|---|---|---|
| Faible | 0,00 – 0,39 | Hypothèse concurrente parmi d'autres, aucune ne domine ; ou inférence à prémisse fragile. |
| Modéré | 0,40 – 0,59 | Hypothèse ou inférence plausible, non disqualifiée, mais concurrencée de près — cohérent avec la zone d'indétermination du gabarit (écart ≤ 0,2 entre 1ère et 2ème hypothèse, convention 6.7). |
| Fort | 0,60 – 0,84 | Inférence ou hypothèse dominante avec argumentation développée, defeaters identifiés et non disqualifiants, mais confirmation indépendante encore partielle. |
| Établi | 0,85 – 1,00 | Confidence maximale disponible sur une inférence/hypothèse — chronologie ou mécanisme publiquement documentable rendant l'alternative peu crédible. Reste une inférence, pas un fait établi au sens de la charte (voir avertissement §1). |

Ces plages sont un point de départ déclaratif, pas un résultat statistique — elles seront révisées si le protocole inter-annotateurs (§4) documente un désaccord systématique sur les frontières.

## 3. Cas-étalons — cas-jouets 1, 5, 6

Les trois cas-jouets fictifs construits (gabarit v2.1 section 14 ; `analyses/cas_jouets/lentite_cas_jouets_1_5_6_v2_1.md` ; YAML `pipeline/analyses/cas_jouet_{1,5,6}_*.yaml`) sont promus cas-étalons officiels de la présente grille — ils couvrent des paramètres construits et documentés, contrairement aux cas réels où les valeurs de confidence dépendent d'une matière première non contrôlée.

| Cas-étalon | Objet | Confidence | Degré (§2) | Écart / statut 6.7 |
|---|---|---|---|---|
| Cas 1 — simple | Inférence — attribution causale instrumentalisée | 0,90 | Établi | — |
| Cas 1 — simple | Hyp. A intentionnelle (dominante) | 0,85 | Établi | Écart 0,40 (A−D) → uncertain_dominance |
| Cas 1 — simple | Hyp. D non intentionnelle (2e) | 0,45 | Modéré | |
| Cas 5 — écart réel | Hyp. B non intentionnelle (dominante) | 0,55 | Modéré | Écart 0,10 (B−C) → zone_of_indetermination |
| Cas 5 — écart réel | Hyp. C non intentionnelle (2e) | 0,45 | Modéré | |
| Cas 6 — écart contrainte | Hyp. A intentionnelle (dominante) | 0,50 | Modéré | Écart 0,10 (A−B) → zone_of_indetermination |
| Cas 6 — écart contrainte | Hyp. B intentionnelle (2e) | 0,40 | Modéré | |

*Lecture.* Sur les trois cas-étalons actuels, aucune valeur ne descend sous 0,40 ni ne dépasse 0,90. C'est une limite déclarée de cette version — les cas-étalons ne couvrent pas encore la bande « faible » (0,00–0,39) de la grille. Un cas-jouet supplémentaire calibré pour produire une hypothèse dominante faible est une extension recommandée pour une v2 de cette grille, hors périmètre du présent lot.

## 4. Protocole inter-annotateurs (spécification — exécution hors périmètre de ce lot)

**Objectif.** Mesurer l'écart entre les degrés de confidence attribués par l'annotateur original d'une analyse et un second annotateur re-codant indépendamment, pour évaluer la reproductibilité de la grille §2.

**Sélection des analyses.** Deux analyses existantes parmi le corpus des 12 YAML validés (`pipeline/analyses/`). Le choix des deux analyses précises est un arbitrage d'exécution, non fixé par ce document.

**Second annotateur.** Le co-dirigeant, ou une instance Claude isolée n'ayant accès ni à l'analyse originale ni à ses attributions de confidence — seulement au discours source et au contexte factuel documenté.

**Déroulement.**

1. Le second annotateur reçoit le discours source et le contexte factuel (sans le YAML M01-M original, sans ses valeurs de `confidence`).
2. Il produit ses propres attributions de confidence sur les mêmes objets d'analyse identifiés par l'analyse originale — mêmes unités, mêmes hypothèses concurrentes déclarées. Le protocole mesure l'écart de *calibration*, pas l'écart d'*identification* des objets.
3. Pour chaque paire de valeurs comparables (`confidence` originale, `confidence` du second annotateur sur le même objet), calcul de l'écart absolu simple `|confidence_originale − confidence_second_annotateur|`.
4. Écart moyen sur l'ensemble des paires comparées, rapporté par analyse puis agrégé sur les deux analyses.

**Mesure d'écart simple — pas de statistique inférentielle.** Version de démarrage : moyenne des écarts absolus, sans test de significativité ni coefficient d'accord inter-annotateurs (Cohen's kappa ou équivalent) — volontairement hors périmètre à ce stade.

**Seuils de lecture proposés (à valider par l'exécution).** Écart moyen < 0,10 — calibration cohérente. Écart moyen 0,10–0,20 — calibration à surveiller, pas d'action immédiate. Écart moyen > 0,20 — friction à consigner au journal, révision de la grille §2 à envisager.

**Non-exécution assumée.** Ce protocole n'est pas exécuté dans le présent lot — son exécution suppose la disponibilité d'un second annotateur (co-dirigeant ou instance isolée), non réunie à ce stade (`plan_action_002.md` §4 tâche 1.4 : « l'exécution du protocole n'est pas dans ce plan »).

---

*Grille de calibration v1 — version de démarrage, `plan_action_002.md` séquence 1 tâche 1.4. Cas-étalons limités aux trois cas-jouets 1/5/6 ; protocole spécifié mais non exécuté.*
