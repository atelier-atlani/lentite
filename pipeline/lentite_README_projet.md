# L'Entité — README

*État des lieux du projet à mai 2026. Point d'entrée pour la navigation, l'archivage et la reprise. Document factuel — il référence les sources doctrinales sans les dupliquer.*

---

## 1. Qu'est-ce que L'Entité

L'Entité est une infrastructure d'enquête forensique sur le réel produit par actions humaines, fondée sur le dévoilement (*aletheia*). Phrase-cœur — *la vérité est dans la qualité du chemin*. Figure — l'enquêteur forensique.

Le projet se déploie en trois modes — *Mode 1* (éclairage médiatique d'analystes), *Mode 2* (conseiller du prince, distribution restreinte), *Mode 3* (chat public à finalité auto-pédagogique). Quatre engagements de l'ADN — refus de confondre dit/fait/produit/voulu, observation située déclarée, ligne fine entre naïveté et paranoïa, refus de présupposer la chaîne causale.

Pour la doctrine complète, lire `doctrine/v2.1/charte_v2_1.md`. Le présent README ne se substitue pas à la doctrine.

---

## 2. État courant — mai 2026

| Volet | État |
|---|---|
| Couche A (charte) | v2.1 canonique |
| Couche B (gabarit) | v2.1 + révision mineure v2.1.1 |
| Couche C (méthodes) | M01 v2.1 + M03 v2.1 |
| Cas-jouets canoniques | 6/6 instanciés |
| Analyses M01 sur cas réels | 4 produites |
| Application M03 sur cas réel | 1 produite (séquence retraites octobre 2025) |
| Pipeline opérationnel | Pydantic v2.13 + validateurs CLI |
| Tests négatifs pipeline | 3/3 confirment que les contraintes mordent |
| Critique externe formalisée | 1 examinée, partiellement intégrée (v2.1.1) |

**Sept volets opérationnels — tous au statut canonique ou validé.** Le projet est éprouvé transversalement. La doctrine v2.1.1 est stable.

---

## 3. Architecture du projet

```
lentite/
├── README.md                          ← ce fichier
├── doctrine/                          ← couches A, B, C
│   ├── v2/                            ← obsolète, conservée par discipline du journal
│   └── v2.1/                          ← canonique courante
├── analyses/                          ← production analytique
│   ├── cas_jouets/                    ← fixtures de calibration
│   ├── m01/                           ← analyses individuelles
│   └── m03/                           ← applications comparatives
├── pipeline/                          ← couche d'exécution opérationnelle
│   ├── schemas.py + schemas_m03.py
│   ├── validate.py + validate_m03.py
│   ├── analyses/*.yaml + tests/*.yaml
│   └── README.md (pipeline)
├── coordination/                      ← documents de coordination (peu nombreux)
└── journal/                           ← journal méthodologique général
```

Quatre couches distinctes — doctrine, analyses, pipeline, coordination/journal. Chacune avec sa discipline propre. La doctrine est versionnée par majeure et mineure ; les analyses référencent la doctrine sans la dupliquer ; le pipeline est code Python + YAML, isolable et exécutable ; le journal trace les évolutions.

---

## 4. Documents canoniques v2.1.1 — référence courante

**Couche A.** `doctrine/v2.1/charte_v2_1.md` — quatre engagements de l'ADN, trois modes opérationnels, deux dimensions de l'objet (réel des actes + récits politiques structurants), doctrine sur les patterns observés vs fabriqués (section 6.6), primauté de l'inférence sur les patterns.

**Couche B.** `doctrine/v2.1/gabarit_v2_1.md` + `doctrine/v2.1/gabarit_v2_1_1_revision_mineure.md`. Grammaire des méthodes — 16 sections normatives, sept patterns temporels avec ancrage empirique (dont `broken_explicitly` v2.1), bloc V refondé en quatre sous-blocs, schéma Pydantic enrichi. La révision mineure v2.1.1 ajoute deux catégories d'audit au journal — `intentionality_bias_audit` et `hypothesis_gap_audit`.

**Couche C.** `doctrine/v2.1/methode_01_v2_1.md` (analyse rhétorique d'un discours public) et `doctrine/v2.1/methode_03_v2_1.md` (analyse comparative multi-acteurs sur même controverse). Quatorze étapes pour chaque méthode, avec spécifications opérationnelles et critères d'évaluation.

---

## 5. Analyses produites

### Cas-jouets canoniques (`analyses/cas_jouets/`)

| Cas | Type | Statut |
|---|---|---|
| 1 — Simple | sophisme certain + omission structurelle (discours fictif construit) | validé |
| 2 — Sans cible | Fabius vœux Conseil constitutionnel 8 janvier 2024 (cas réel) | validé |
| 3 — Substantiel | Lecornu DPG 14 octobre 2025 (cas réel) | validé |
| 4 — Adversarial | Ciotti réponse à DPG 14 octobre 2025 (cas réel) | validé |
| 5 — Écart réel | `never_observed` (discours fictif construit) | validé |
| 6 — Écart par contrainte | `prevented_by_constraint` (discours fictif construit) | validé |

### Analyses M01 v2.1 sur cas réels (`analyses/m01/`)

| Analyse | Locuteur | Régime | Mode | Pattern V.3 saillant |
|---|---|---|---|---|
| Fabius | Président Conseil constitutionnel | sobre | applicable_complete | `observed_as_announced` × 2 |
| Ciotti | Président groupe UDR | adversarial | applicable_vigilance_adversariale | V.3 vide motivé |
| Lecornu | Premier ministre | substantiel | applicable_complete | `broken_explicitly` + motivation |
| Vallaud | Président groupe Socialistes | pivot | applicable_degraded | `observed_otherwise` × 3 |
| Panot | Présidente groupe LFI | adversarial | applicable_vigilance_adversariale | `never_observed` + `not_yet_observed` |

Cinq cas réels couvrant tous les régimes documentés du gabarit v2.1. Les analyses sont matière première pour les applications M03 ultérieures et alimentent la fenêtre roulante des audits inscrits au gabarit v2.1.1.

### Applications M03 v2.1 (`analyses/m03/`)

| Application | Séquence | Acteurs | Cas saillants | Statut |
|---|---|---|---|---|
| Séquence retraites octobre 2025 | 6-16 octobre 2025 + effets à mai 2026 | Lecornu / Ciotti / Vallaud | 4 cas saillants identifiés | validé à 3 acteurs |

**Extension immédiatement possible** — l'application peut être étendue à quatre acteurs avec ajout de Panot dont l'analyse M01 v2.1 est produite. Tâche identifiée comme suivante (voir section 7).

---

## 6. Pipeline opérationnel

**Localisation.** `pipeline/`. Lire `pipeline/README.md` pour usage détaillé.

**Pré-requis.** Python 3.11+, Pydantic 2.13+, PyYAML.

**Composants.**

— `schemas.py` (39 modèles Pydantic v2 selon gabarit v2.1 section 11) + `schemas_m03.py` (22 modèles selon M03 v2.1 section 11).

— `validate.py` (CLI validateur M01) + `validate_m03.py` (CLI validateur M03).

— `analyses/*.yaml` (huit YAML analyses M01-M validés + un YAML application M03-M validé).

— `tests/*.yaml` (trois YAML défaillants délibérément + validation que les contraintes mordent).

**Usage rapide.**

```bash
# Validation d'une analyse M01
python3 validate.py analyses/fabius_v2_1.yaml

# Validation transversale toutes analyses M01
python3 validate.py --all

# Validation application M03
python3 validate_m03.py analyses/m03_retraites_octobre_2025_v2_1.yaml
```

**Contraintes validées par tests négatifs.**

1. `broken_explicitly` exige `public_motivation_invoked` non null (gabarit v2.1 section 6.6).

2. Bloc V.3 vide si et seulement si locuteur non-efficient sur tous les objets thématiques (gabarit v2.1 section 13 critère 7).

3. Convention 6.7 — `hypothesis_gap ≤ 0.2` requiert `zone_of_indetermination`, etc. (gabarit v2.1 section 6.7).

Les trois tests négatifs sont rejetés par le pipeline avec message d'erreur référençant la section du gabarit violée.

---

## 7. Travaux en cours et tâches suivantes

### Tâche immédiate identifiée

**Extension de M03 v2.1 application à quatre acteurs** — Lecornu / Ciotti / Vallaud / Panot sur la séquence retraites octobre 2025. La matière première est désormais disponible (quatre M01 v2.1 produits). Production attendue — refonte du markdown `analyses/m03/` à quatre acteurs, YAML M03-M étendu, revalidation pipeline. Volume estimé 8000-9000 mots + YAML.

### Audits en cours d'accumulation

**`intentionality_bias_audit` (gabarit v2.1.1).** Surveille la fréquence des hypothèses intentionnelles dominantes. Seuil d'alerte 80%. Fenêtre roulante de 10 analyses. *Actuellement 5 analyses M01 sur cas réels accumulées. Premier audit possible après 5 analyses supplémentaires.*

**`hypothesis_gap_audit` (gabarit v2.1.1).** Surveille la distribution des écarts hypothèses. Trois seuils d'alerte. Fenêtre roulante de 20-30 analyses. *Actuellement 8 analyses (5 cas réels + 3 cas-jouets) accumulées. Premier audit possible après 12-22 analyses supplémentaires.*

### Tâches reportées (à plus long terme)

— *Pipeline génération M01-P automatique* — appel LLM léger à partir d'un M01-M validé pour produire la sortie publique avec validation par schéma (longueur, présence des cinq éléments, absence de termes évaluatifs non marqués).

— *Pipeline d'audit des typologies* — détection automatique des nouveaux types d'effets observables, vulnérabilités, ou patterns dans les analyses entrantes, pour examen périodique selon la charte v2.1 section 6.6.

— *Export vers graphe cognitif* — sérialiseur YAML → graphe (Neo4j ou PostgreSQL+AGE selon décision technique).

— *Routing automatique par `method_id`* dans `validate.py` (au lieu de validateurs séparés M01/M03).

— *Autres méthodes du catalogue* — M02 (lecture indiciaire Ginzburg, prioritaire selon la critique externe), M04 (triangulation historiographique), M05-M08 (à spécifier).

---

## 8. Décisions politiques pendantes

Inscrites dans la charte v2.1 section 9.2 comme négociables. Relèvent du choix du porteur principal (Seb).

— *Licence open source*. Options canoniques — MIT (permissive), Apache 2.0 (avec protection brevets), AGPL (copyleft fort). Décision à prendre avant publication v3.

— *Modèle d'accès Mode 2 distribution restreinte*. Périmètre du groupe restreint, conditions d'admission, modalités d'audit, durée d'embargo des analyses.

— *Premier groupe Mode 1 (analystes)*. Composition initiale, profils recherchés, format de collaboration.

— *Trajectoire de financement Mode 3 (chat public)*. Modèle économique du service public ou semi-public, partenaires institutionnels possibles, conditions de gratuité.

---

## 9. Navigation rapide

**Si vous voulez comprendre la doctrine** — lire dans l'ordre `doctrine/v2.1/charte_v2_1.md` (couche A), puis `doctrine/v2.1/gabarit_v2_1.md` + révision mineure v2.1.1 (couche B), puis l'une des méthodes (M01 ou M03 selon intérêt).

**Si vous voulez voir des analyses concrètes** — commencer par `analyses/m01/analyse_fabius_v2_1.md` (cas sobre) pour la lisibilité, puis `analyses/m01/analyse_ciotti_v2_1.md` (cas adversarial) pour la complexité, puis `analyses/m03/m03_application_retraites_octobre_2025_v2_1.md` pour l'application comparative.

**Si vous voulez exécuter le pipeline** — aller dans `pipeline/`, suivre `pipeline/README.md`. Installation rapide — `pip install --break-system-packages pydantic pyyaml`, puis `python3 pipeline/validate.py --all`.

**Si vous voulez critiquer la doctrine** — examiner les fixtures `analyses/cas_jouets/` et les tests négatifs `pipeline/tests/`. Les contraintes mordantes sont documentées dans le pipeline. La réponse à une critique externe précédente est consignée dans `doctrine/v2.1/gabarit_v2_1_1_revision_mineure.md`.

**Si vous prenez en main le projet pour la première fois** — lire ce README, puis la charte, puis le gabarit, puis lancer le pipeline sur les analyses pour voir la validation en action. La doctrine est dense — quatre à six heures de lecture pour une compréhension solide.

---

## 10. Maintenance et versioning

**Conventions de versioning** (gabarit section 1).

— *Majeure* (v2 → v3) — refonte qui invalide la rétrocompatibilité des sorties. Le passage v2 → v2.1 n'aurait pas été une majeure si la stratification de l'efficience par objet et les chaînes causales amont/aval n'avaient pas modifié structurellement le schéma des sorties.

— *Mineure* (v2.1 → v2.1.1) — évolution interne compatible. La révision v2.1.1 ne modifie aucune contrainte normative existante, elle étend le dispositif de surveillance.

**Catégories d'entrée canoniques au journal** (gabarit section 16, étendu par v2.1.1).

1. `method_evolution` — passages de version, frictions identifiées, corrections intégrées.

2. `case_execution` — exécutions notables, cas-jouets rejoués, rejeux comparatifs.

3. `failure_pattern` — recensement des erreurs de raisonnement identifiées au fil des analyses (patterns de gouvernance du projet, distincts des typologies analytiques).

4. `typology_audit` — examen périodique des typologies opératoires selon le critère d'ancrage empirique (charte v2.1 section 6.6).

5. `intentionality_bias_audit` (v2.1.1) — surveillance de la fréquence des hypothèses intentionnelles dominantes.

6. `hypothesis_gap_audit` (v2.1.1) — surveillance de la distribution des écarts hypothèses concurrentes.

**Discipline de séparation sortie humaine / journal méthodologique** (gabarit v2.1 section 9.0). La sortie humaine M01-H est conçue pour lecteur informé non-analyste, allégée du méta-discours. Le méta-discours méthodologique va au journal séparé, pas à la sortie humaine.

**Discipline anti-cumul des documents de coordination.** Les documents de coordination (transition v2 → v2.1 par exemple) sont conservés à l'unité, pas empilés en versions successives. Quand un document de coordination est produit dans une nouvelle transition, l'ancien est archivé au journal et le nouveau remplace.

---

## Métadonnées du README

- *Version du README* : 1.0
- *Date d'édition* : 17 mai 2026
- *État du projet à la date* : v2.1.1 doctrinalement stable, pipeline opérationnel, 5 analyses M01 sur cas réels + 1 application M03 + 6 cas-jouets canoniques + 3 tests négatifs validés
- *Prochaine révision attendue* : après extension M03 à 4 acteurs ou après accumulation de nouvelles analyses substantielles

---

*Document factuel. Pas de récit du projet. Pour l'histoire et les frictions du développement, consulter `journal/journal.md`. Pour les décisions doctrinales, lire la charte v2.1. Pour les choix opérationnels, lire le gabarit v2.1 et sa révision mineure v2.1.1.*
