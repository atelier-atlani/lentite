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
| Analyses M01 sur cas réels | 5 produites |
| Application M03 sur cas réel | 1 à 4 acteurs (canonique courante) + 1 à 3 acteurs (archivée) |
| Pipeline opérationnel minimal | Pydantic v2.13 + validateurs CLI |
| Tests négatifs pipeline | 3/3 confirment que les contraintes mordent |
| Critique externe formalisée | 1 examinée, partiellement intégrée (v2.1.1) |
| Méthodologie de codage | v1 produite, en attente décisions Phase 0 |

**Huit volets opérationnels — tous au statut canonique ou validé.** Le projet est éprouvé transversalement. La doctrine v2.1.1 est stable. La méthodologie de codage est documentée pour permettre le passage au système opérationnel complet.

---

## 3. Architecture du projet

```
lentite/
├── README.md                          ← ce fichier
├── doctrine/
│   ├── v2/                            ← obsolète, conservée par discipline du journal
│   └── v2.1/                          ← canonique courante
├── analyses/
│   ├── cas_jouets/
│   ├── m01/                           ← 5 analyses M01 v2.1
│   └── m03/                           ← application M03 v2.1 à 4 acteurs
├── pipeline/                          ← couche d'exécution opérationnelle (minimale)
├── coordination/
├── journal/                           ← journal méthodologique général
└── dev/                               ← couche méthodologique de développement (nouveau)
    └── methodologie_codage_v1.md
```

Cinq couches distinctes — doctrine, analyses, pipeline, coordination/journal, méthodologie de développement (nouveau volet ajouté à mai 2026).

---

## 4. Documents canoniques v2.1.1 — référence courante

**Couche A.** `doctrine/v2.1/charte_v2_1.md`.

**Couche B.** `doctrine/v2.1/gabarit_v2_1.md` + `doctrine/v2.1/gabarit_v2_1_1_revision_mineure.md`.

**Couche C.** `doctrine/v2.1/methode_01_v2_1.md` et `doctrine/v2.1/methode_03_v2_1.md`.

**Couche méthodologique de développement (nouveau).** `dev/methodologie_codage_v1.md` — plan de codage avec phases, disciplines, décisions structurantes, premier livrable concret.

---

## 5. Analyses produites

### Cas-jouets canoniques (`analyses/cas_jouets/`)

| Cas | Type | Statut |
|---|---|---|
| 1 — Simple | sophisme certain + omission structurelle | validé |
| 2 — Sans cible | Fabius vœux Conseil constitutionnel | validé |
| 3 — Substantiel | Lecornu DPG 14 octobre 2025 | validé |
| 4 — Adversarial | Ciotti réponse à DPG | validé |
| 5 — Écart réel | `never_observed` | validé |
| 6 — Écart par contrainte | `prevented_by_constraint` | validé |

### Analyses M01 v2.1 sur cas réels (`analyses/m01/`)

| Analyse | Locuteur | Régime | Mode | Pattern V.3 saillant |
|---|---|---|---|---|
| Fabius | Président Conseil constitutionnel | sobre | applicable_complete | `observed_as_announced` × 2 |
| Ciotti | Président groupe UDR | adversarial | applicable_vigilance_adversariale | V.3 vide motivé |
| Lecornu | Premier ministre | substantiel | applicable_complete | `broken_explicitly` + motivation |
| Vallaud | Président groupe Socialistes | pivot | applicable_degraded | `observed_otherwise` × 3 |
| Panot | Présidente groupe LFI | adversarial | applicable_vigilance_adversariale | `never_observed` + `not_yet_observed` |

### Applications M03 v2.1 (`analyses/m03/`)

| Application | Acteurs | Cas saillants | Statut |
|---|---|---|---|
| Séquence retraites octobre 2025 — *référence canonique courante* | Lecornu / Ciotti / Vallaud / Panot | 7 cas saillants | validé à 4 acteurs |
| Séquence retraites octobre 2025 — *archive du journal* | Lecornu / Ciotti / Vallaud | 4 cas saillants | conservé par discipline |

**Extension immédiatement possible** — application à 5 acteurs (Wauquiez ou Bardella ou Philippe).

---

## 6. Pipeline opérationnel

**Localisation.** `pipeline/`. Lire `pipeline/README.md` pour usage détaillé.

**Pré-requis.** Python 3.11+, Pydantic 2.13+, PyYAML.

**Composants.**

— `schemas.py` (39 modèles Pydantic v2 selon gabarit v2.1 section 11) + `schemas_m03.py` (22 modèles selon M03 v2.1).

— `validate.py` (CLI validateur M01) + `validate_m03.py` (CLI validateur M03).

— `analyses/*.yaml` (huit YAML M01-M validés + un YAML M03-M à 4 acteurs validé).

— `tests/*.yaml` (trois YAML défaillants validant les contraintes mordantes).

**Note importante.** Ce pipeline est *minimal* — il valide les YAML produits par analyses humaines. Le système opérationnel complet (qui produirait automatiquement les analyses à partir de textes sources) est en attente de codage. Voir `dev/methodologie_codage_v1.md`.

---

## 7. Travaux en cours et tâches suivantes

### Tâche immédiate identifiée

**Décisions structurantes Phase 0 codage** (5 décisions documentées dans la méthodologie de codage v1). Sans ces décisions, le codage substantiel ne peut commencer.

### Audits en cours d'accumulation

**`intentionality_bias_audit` (gabarit v2.1.1).** 5 analyses M01 sur cas réels accumulées. Premier audit possible après 5 analyses supplémentaires.

**`hypothesis_gap_audit` (gabarit v2.1.1).** 8 analyses (5 cas réels + 3 cas-jouets) + 1 application M03 à 4 acteurs. Premier audit possible après 12-22 analyses supplémentaires.

### Tâches reportées

— Phases 1-4 de la méthodologie de codage.

— Extension M03 à 5 acteurs.

— Instanciation M02 (lecture indiciaire).

— Autres méthodes du catalogue (M04 à M08).

— Refonte v3 (après accumulation et retour d'expérience).

---

## 8. Décisions politiques pendantes

— Licence open source (Apache 2.0 recommandé, ou MIT, ou AGPL).

— Modèle de distribution (distribution duale recommandée, ou open source complet, ou closed transitoire).

— Premier groupe Mode 1 (analystes).

— Trajectoire de financement Mode 3.

Ces décisions sont structurantes pour la Phase 0 du codage. Détails dans `dev/methodologie_codage_v1.md` section 8.

---

## 9. Navigation rapide

**Comprendre la doctrine** — `doctrine/v2.1/charte_v2_1.md` → `doctrine/v2.1/gabarit_v2_1.md` + révision mineure → l'une des méthodes.

**Voir des analyses concrètes** — `analyses/m01/analyse_fabius_v2_1.md` (sobre) → `analyses/m01/analyse_ciotti_v2_1.md` (adversarial) → `analyses/m03/m03_application_retraites_octobre_2025_4acteurs_v2_1.md` (comparative à 4 acteurs).

**Exécuter le pipeline** — `pipeline/README.md`. `pip install --break-system-packages pydantic pyyaml`. `python3 pipeline/validate.py --all`.

**Critiquer la doctrine** — `analyses/cas_jouets/` + `pipeline/tests/`. Critique externe précédente examinée dans `doctrine/v2.1/gabarit_v2_1_1_revision_mineure.md`.

**Démarrer le codage** — `dev/methodologie_codage_v1.md`. Cinq décisions structurantes à prendre avant Phase 0.

**Première prise en main** — ce README → la charte → le gabarit → la méthodologie de codage. Quatre à six heures de lecture pour une compréhension solide.

---

## 10. Maintenance et versioning

**Conventions de versioning.** Majeure (v2 → v3) — refonte qui invalide la rétrocompatibilité. Mineure (v2.1 → v2.1.1) — évolution interne compatible.

**Catégories d'entrée canoniques au journal.** `method_evolution`, `case_execution`, `failure_pattern`, `typology_audit`, `intentionality_bias_audit` (v2.1.1), `hypothesis_gap_audit` (v2.1.1).

**Discipline de séparation sortie humaine / journal méthodologique.** Sortie M01-H lisible non-analyste séparée du méta-discours méthodologique.

**Discipline anti-cumul des documents de coordination.** Un seul document canonique par transition. Archivage au journal des précédents.

---

## Métadonnées du README

- *Version du README* : 1.1
- *Date d'édition* : 17 mai 2026
- *Modification depuis 1.0* — intégration de l'extension M03 v2.1 à 4 acteurs comme référence canonique courante, de l'analyse Panot v2.1, de la méthodologie de codage v1 comme nouveau volet. Métriques actualisées (5 analyses M01 + 1 M03 à 4 acteurs).
- *État du projet à la date* : doctrine v2.1.1 stable, méthodologie de codage produite, en attente décisions Phase 0 pour démarrage du codage substantiel.
- *Prochaine révision attendue* : après décisions Phase 0 codage et début Phase 1.

---

*Document factuel. Pas de récit du projet. Pour l'histoire et les frictions du développement, consulter `journal/journal.md`. Pour le plan de codage, consulter `dev/methodologie_codage_v1.md`.*
