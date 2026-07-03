# Log de session — plan_action_002, lot {1.1–1.2}

*Mode opérationnel : Implementer. Plan référencé : `.claude/plans/plan_action_002.md` §4 séquence 1.*

---

## Tâches accomplies

**1.1 — Bloc omission durci.** Dans `pipeline/schemas.py`, le modèle `Omission` exige désormais quatre champs obligatoires en plus de ceux existants :
- `pouvoir_agir: str` (min_length=1) — référence documentée à la compétence/capacité d'agir.
- `opportunite: Opportunite` — nouveau modèle imbriqué (`description`, `date`).
- `cloture_corpus: ClotureCorpus` — nouveau modèle imbriqué (`corpus_declare`, `date_cloture`).
- `explications_innocentes: list[ExplicationInnocente]` (min_length=1) — nouveau modèle imbriqué (`description`, `statut` typé par le nouvel enum `ExplicationInnocenteStatut` : `examinee`/`ecartee`/`retenue`).

Test négatif : `pipeline/tests/negatif_omission_sans_cloture_corpus.yaml` — omission avec les trois autres champs présents mais `cloture_corpus` absent. Échec confirmé : `[missing] units.0.omissions.0.cloture_corpus: Field required`.

**1.2 — Bitemporalité minimale.** Ajout d'une sentinelle `NON_RENSEIGNE = "non_renseigne"` et d'un type `BitemporalDate = date | Literal["non_renseigne"]`. Champs `date_fait` et `date_connaissance` (défaut `non_renseigne`) ajoutés sur les modèles d'assertion suivants : `Vulnerability`, `Omission`, `DiscourseActGap`, `ObservableEffect` (voir *Frictions* ci-dessous sur le choix du périmètre).

Nouveau champ racine `gabarit_version: GabaritVersion = GabaritVersion.V2_1` sur `M01Analysis`, avec deuxième valeur `V2_1_DURCI_SEQ1 = "2.1-durci-seq1"`. Nouveau validateur `validate_bitemporal_when_durci` : si `gabarit_version=2.1-durci-seq1`, toute assertion couverte doit avoir `date_fait` et `date_connaissance` renseignés (≠ `non_renseigne`), sinon erreur listant précisément les chemins fautifs.

Test négatif : `pipeline/tests/negatif_bitemporalite_manquante_gabarit_durci.yaml` — `gabarit_version=2.1-durci-seq1` avec une vulnérabilité laissée à son défaut `non_renseigne`. Échec confirmé, message ciblé référençant la tâche 1.2 et le chemin exact (`units[U1].argumentative_vulnerabilities[0]`).

## Frictions et choix d'implémentation non entièrement spécifiés par le plan

Deux points où le plan laisse une marge d'interprétation, signalés ici plutôt qu'arbitrés silencieusement (discipline §9 du plan) :

1. **Périmètre des modèles couverts par la bitemporalité.** Le plan dit « deux champs par assertion » sans lister les modèles concernés. Choix retenu — limiter au périmètre minimal des assertions empiriques déjà typées par confidence/évidence dans le gabarit v2.1 : `Vulnerability` (5.4), `Omission` (5.5), `DiscourseActGap` (9.5), `ObservableEffect` (9.5). Cohérent avec le titre « bitemporalité **minimale** ». Non couverts dans ce lot — `UpstreamElement`, `PlausibleConsequence`, `Historiography`, `Inference`, `Hypothesis`, `TargetedObject`. Extension possible en 1.5 ou séquence ultérieure si le Reviewer juge le périmètre insuffisant.

2. **`schemas_m03.py` non modifié.** La tâche 1.1 nomme explicitement `schemas.py`/`schemas_m03.py`, mais `M03Analysis` n'importe ni n'utilise `Omission` — aucun changement n'y était nécessaire pour 1.1. Pour 1.2, le plan ne nomme aucun fichier ; par discipline de lot minimal, la bitemporalité n'a pas été étendue aux modèles d'assertion propres à M03 (`EpistemicCell`, `TargetedObjectCell`, `InvalidatedPrediction`, `BenefitAsymmetry`, etc.). Question ouverte pour l'Architecte/Reviewer — étendre `gabarit_version` + bitemporalité à `M03Analysis` dans un lot dédié, ou laisser M03 hors périmètre du durcissement séquence 1.

3. **Nommage `gabarit_version`.** Valeur `"2.1-durci-seq1"` choisie délibérément distincte des vraies versions mineures de doctrine (`2.1`, `2.1.1`) pour ne pas laisser croire à une révision de la doctrine couche B elle-même (moratoire en vigueur, §5 du plan) — c'est un indicateur interne au schéma/pipeline, pas un numéro de version doctrinale.

## État des tests

- 12/12 YAML existants (9 analyses + 3 cas-jouets) revalidés sans modification — aucune régression (vérification, pas la revalidation formelle du lot 1.5).
- 3/3 tests négatifs préexistants toujours rejetés comme attendu.
- 2/2 nouveaux tests négatifs (1.1, 1.2) rejetés avec erreur ciblée.
- Contre-vérification positive — les deux cas ci-dessus passent la validation une fois les champs manquants correctement renseignés.
- Vérification manuelle via `python3.11 -c "..."` (import direct de `schemas.M01Analysis`), pas de CLI — `validate.py` M01 n'existe pas encore (restauration prévue tâche 2.1). Aucun harnais de test automatisé (pytest) créé dans ce lot — hors périmètre, cohérent avec l'absence d'infrastructure de test existante pour M01.

## Modifications de code

- `pipeline/schemas.py` — +121/-1 lignes. Nouveaux enums `ExplicationInnocenteStatut`, `GabaritVersion` ; nouveaux modèles `Opportunite`, `ClotureCorpus`, `ExplicationInnocente` ; modèle `Omission` durci ; champs bitemporels sur 4 modèles ; champ `gabarit_version` + validateur conditionnel sur `M01Analysis` ; `__all__` mis à jour.
- `pipeline/tests/negatif_omission_sans_cloture_corpus.yaml` — nouveau.
- `pipeline/tests/negatif_bitemporalite_manquante_gabarit_durci.yaml` — nouveau.
- **Aucune modification** aux 12 YAML existants dans `pipeline/analyses/` (hors périmètre de ce lot — lot 1.5).
- `schemas_m03.py` non touché (voir Frictions point 2).

## État du système

Corpus des 12 analyses intact et validant. Contraintes 1.1 et 1.2 opérationnelles et mordantes. Séquence 1 non close — restent 1.3 (politique de corpus), 1.4 (grille de calibration), 1.5 (revalidation formelle du corpus + entrée journal de synthèse de séquence).

## Recommandations pour la suite

- Lot suivant `{1.3–1.4}` peut démarrer indépendamment.
- Lot `1.5` devra explicitement décider, pour les 12 YAML existants, s'ils reçoivent `gabarit_version` (implicitement `"2.1"` par défaut — aucune action requise) ou si certains doivent être promus au gabarit durci a posteriori.
- Trancher les deux points de friction ci-dessus (périmètre M03, extension du périmètre bitemporel) avant ou pendant 1.5.

---

*Commits de ce lot : voir historique git, préfixe `feat(schemas)` / `test(pipeline)`.*
