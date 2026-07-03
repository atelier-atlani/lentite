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
| Analyses M01 sur cas réels | **6 produites** |
| Application M03 sur cas réel | 1 à 4 acteurs (canonique courante) + 1 à 3 acteurs (archivée) |
| Pipeline opérationnel minimal | Pydantic v2.13 + validateurs CLI |
| YAML validés au pipeline | **9 M01 + 1 M03** |
| Tests négatifs pipeline | 3/3 confirment que les contraintes mordent |
| Critique externe formalisée | 1 examinée, partiellement intégrée (v2.1.1) |
| Méthodologie de codage | v1 produite, en attente décisions Phase 0 |

**Huit volets opérationnels — tous au statut canonique ou validé.** Le projet est éprouvé transversalement. La doctrine v2.1.1 est stable.

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
│   ├── m01/                           ← 6 analyses M01 v2.1 sur cas réels
│   └── m03/                           ← application M03 v2.1 à 4 acteurs
├── pipeline/                          ← couche d'exécution opérationnelle (minimale)
├── coordination/
├── journal/                           ← journal méthodologique général
└── dev/                               ← couche méthodologique de développement
    └── methodologie_codage_v1.md
```

Cinq couches distinctes.

---

## 4. Documents canoniques v2.1.1 — référence courante

**Couche A.** `doctrine/v2.1/charte_v2_1.md`.

**Couche B.** `doctrine/v2.1/gabarit_v2_1.md` + `doctrine/v2.1/gabarit_v2_1_1_revision_mineure.md`.

**Couche C.** `doctrine/v2.1/methode_01_v2_1.md` et `doctrine/v2.1/methode_03_v2_1.md`.

**Couche méthodologique de développement.** `dev/methodologie_codage_v1.md`.

---

## 5. Analyses produites

### Cas-jouets canoniques (`analyses/cas_jouets/`)

| Cas | Type | Statut |
|---|---|---|
| 1 — Simple | sophisme certain + omission structurelle | validé |
| 2 — Sans cible | Fabius vœux Conseil constitutionnel | validé |
| 3 — Substantiel | Lecornu DPG | validé |
| 4 — Adversarial | Ciotti réponse à DPG | validé |
| 5 — Écart réel | `never_observed` | validé |
| 6 — Écart par contrainte | `prevented_by_constraint` | validé |

### Analyses M01 v2.1 sur cas réels (`analyses/m01/`)

| Analyse | Locuteur | Régime | Mode | Pattern V.3 saillant |
|---|---|---|---|---|
| Fabius | Président Conseil constitutionnel | sobre | applicable_complete | `observed_as_announced` × 2 |
| Ciotti | Président groupe UDR | adversarial | applicable_vigilance_adversariale | V.3 vide motivé |
| Lecornu | Premier ministre (octobre 2025) | substantiel | applicable_complete | `broken_explicitly` + motivation |
| Vallaud | Président groupe Socialistes | pivot | applicable_degraded | `observed_otherwise` × 3 |
| Panot | Présidente groupe LFI | adversarial | applicable_vigilance_adversariale | `never_observed` + `not_yet_observed` |
| **Bayrou** | **Premier ministre (janvier 2025)** | **substantiel** | **applicable_complete** | **`observed_as_announced` × 3, `observed_otherwise`, `never_observed` × 2** |

### Applications M03 v2.1 (`analyses/m03/`)

| Application | Acteurs | Cas saillants | Statut |
|---|---|---|---|
| Séquence retraites octobre 2025 — *référence canonique courante* | Lecornu / Ciotti / Vallaud / Panot | 7 cas saillants | validé à 4 acteurs |
| Séquence retraites octobre 2025 — *archive du journal* | Lecornu / Ciotti / Vallaud | 4 cas saillants | conservé par discipline |

**Extensions immédiatement possibles** — M03 retraites octobre 2025 à 5 acteurs (Wauquiez, Bardella ou Philippe) ; M03 séquence Bayrou-Barnier-Lecornu (trois PM successifs en gouvernement minoritaire, test de la découverte 3.11).

---

## 6. Pipeline opérationnel

**Localisation.** `pipeline/`. Lire `pipeline/README.md` pour usage détaillé.

**Pré-requis.** Python 3.11+, Pydantic 2.13+, PyYAML.

**Composants.** `schemas.py` (39 modèles M01) + `schemas_m03.py` (22 modèles M03). `validate.py` + `validate_m03.py`. 9 YAML M01-M validés + 1 YAML M03-M à 4 acteurs validé. 3 YAML tests négatifs validants.

**Note importante.** Pipeline *minimal* — valide les YAML produits par analyses humaines. Système opérationnel complet en attente de codage. Voir `dev/methodologie_codage_v1.md`.

---

## 7. Travaux en cours et tâches suivantes

### Tâche immédiate identifiée

**Décisions structurantes Phase 0 codage** (5 décisions documentées dans la méthodologie de codage v1).

### Audits en cours d'accumulation

**`intentionality_bias_audit` (gabarit v2.1.1).** 6 analyses M01 sur cas réels accumulées. Premier audit possible après 4 analyses supplémentaires.

**`hypothesis_gap_audit` (gabarit v2.1.1).** 9 analyses M01 (6 cas réels + 3 cas-jouets) + 1 application M03 à 4 acteurs. Premier audit possible après 11-21 analyses supplémentaires.

**`typology_audit` ouvert (depuis mai 2026).** Candidat d'extension typologique sur `amplification_temporaire_terminee_par_chute` détecté lors de la validation Bayrou v2.1. Examen à déclencher après accumulation de 2-3 cas externes (Rocard 1988-1991, Juppé 1995-1996, autres PM minoritaires).

### Tâches reportées

— Phases 1-4 de la méthodologie de codage.

— Extension M03 retraites octobre 2025 à 5 acteurs.

— Extension M03 séquence Bayrou-Barnier-Lecornu (test découverte 3.11).

— Instanciation M02 (lecture indiciaire).

— Refonte v3 (après accumulation et retour d'expérience).

---

## 8. Décisions politiques pendantes

— Licence open source (Apache 2.0 recommandé).
— Modèle de distribution (distribution duale recommandée).
— Premier groupe Mode 1 (analystes).
— Trajectoire de financement Mode 3.

Détails dans `dev/methodologie_codage_v1.md` section 8.

---

## 9. Navigation rapide

**Comprendre la doctrine** — charte → gabarit + révision mineure → l'une des méthodes.

**Voir des analyses concrètes** — Fabius (sobre) → Ciotti (adversarial) → Bayrou et Lecornu (substantiel comparable, deux PM successifs) → M03 à 4 acteurs (comparative).

**Exécuter le pipeline** — `pipeline/README.md`. `pip install --break-system-packages pydantic pyyaml`. `python3 pipeline/validate.py --all`.

**Critiquer la doctrine** — `analyses/cas_jouets/` + `pipeline/tests/`. Critique externe précédente examinée dans `doctrine/v2.1/gabarit_v2_1_1_revision_mineure.md`.

**Démarrer le codage** — `dev/methodologie_codage_v1.md`. Cinq décisions structurantes à prendre avant Phase 0.

**Première prise en main** — ce README → charte → gabarit → méthodologie de codage. Quatre à six heures de lecture pour compréhension solide.

---

## 10. Maintenance et versioning

**Conventions de versioning.** Majeure — refonte invalidant rétrocompatibilité. Mineure — évolution interne compatible.

**Catégories d'entrée canoniques au journal.** `method_evolution`, `case_execution`, `failure_pattern`, `typology_audit`, `intentionality_bias_audit` (v2.1.1), `hypothesis_gap_audit` (v2.1.1).

**Disciplines.** Séparation sortie humaine / journal méthodologique. Anti-cumul des documents de coordination. Patterns observés vs fabriqués (charte v2.1 section 6.6).

---

## Métadonnées du README

- *Version du README* : 1.2
- *Date d'édition* : 17 mai 2026
- *Modification depuis 1.1* — intégration de l'analyse Bayrou v2.1 comme sixième M01 sur cas réel ; métriques actualisées (9 YAML M01 au pipeline + 1 M03 à 4 acteurs) ; nouveau audit `typology_audit` ouvert sur `amplification_temporaire_terminee_par_chute` ; extensions M03 envisagées documentées (5 acteurs sur retraites, ou séquence Bayrou-Barnier-Lecornu).
- *État du projet à la date* : doctrine v2.1.1 stable ; consolidation doctrinale renforcée par Bayrou v2.1 ; méthodologie de codage v1 produite ; en attente décisions Phase 0 pour démarrage codage substantiel.

---

*Document factuel. Pour l'histoire et les frictions, `journal/journal.md`. Pour le plan de codage, `dev/methodologie_codage_v1.md`.*
