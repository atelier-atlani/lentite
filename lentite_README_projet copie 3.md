# L'Entité — README

*État des lieux du projet à mai 2026. Point d'entrée pour la navigation, l'archivage et la reprise. Document factuel — il référence les sources doctrinales sans les dupliquer.*

---

## 1. Qu'est-ce que L'Entité

L'Entité est une infrastructure d'enquête forensique sur le réel produit par actions humaines, fondée sur le dévoilement (*aletheia*). Phrase-cœur — *la vérité est dans la qualité du chemin*. Figure — l'enquêteur forensique.

Trois modes — *Mode 1* (éclairage médiatique d'analystes), *Mode 2* (conseiller du prince, distribution restreinte), *Mode 3* (chat public à finalité auto-pédagogique). Quatre engagements de l'ADN — refus de confondre dit/fait/produit/voulu, observation située déclarée, ligne fine entre naïveté et paranoïa, refus de présupposer la chaîne causale.

Pour la doctrine complète, lire `doctrine/v2.1/charte_v2_1.md`.

---

## 2. État courant — mai 2026

| Volet | État |
|---|---|
| Couche A (charte) | v2.1 canonique |
| Couche B (gabarit) | v2.1 + révision mineure v2.1.1 |
| Couche C (méthodes) | M01 v2.1 + M03 v2.1 |
| Cas-jouets canoniques | 6/6 instanciés |
| Analyses M01 sur cas réels | **7 produites** |
| Applications M03 sur cas réels | **2 produites** |
| Pipeline opérationnel minimal | Pydantic v2.13 + validateurs CLI |
| YAML validés au pipeline | **10 M01 + 2 M03** |
| Tests négatifs pipeline | 3/3 confirment que les contraintes mordent |
| Critique externe formalisée | 1 examinée, partiellement intégrée (v2.1.1) |
| Méthodologie de codage | v1 produite, **Phase 0 en attente de décisions** |

**Consolidation doctrinale substantielle.** Le projet est éprouvé transversalement sur sept analyses M01 cas réels et deux applications M03. La doctrine v2.1.1 est stable. *La consolidation est jugée suffisante pour engager la Phase 0 du codage.*

---

## 3. Architecture du projet

```
lentite/
├── README.md                          ← ce fichier
├── doctrine/v2.1/                     ← canonique courante
├── analyses/
│   ├── cas_jouets/
│   ├── m01/                           ← 7 analyses M01 v2.1 sur cas réels
│   └── m03/                           ← 2 applications M03 v2.1
├── pipeline/                          ← couche d'exécution opérationnelle (minimale)
├── coordination/
├── journal/                           ← journal méthodologique général
└── dev/                               ← couche méthodologique de développement
    └── methodologie_codage_v1.md
```

---

## 4. Documents canoniques v2.1.1

**Couche A.** `doctrine/v2.1/charte_v2_1.md`.

**Couche B.** `doctrine/v2.1/gabarit_v2_1.md` + `doctrine/v2.1/gabarit_v2_1_1_revision_mineure.md`.

**Couche C.** `doctrine/v2.1/methode_01_v2_1.md` et `doctrine/v2.1/methode_03_v2_1.md`.

**Couche méthodologique de développement.** `dev/methodologie_codage_v1.md`.

---

## 5. Analyses produites

### Cas-jouets canoniques

| Cas | Type | Statut |
|---|---|---|
| 1 — Simple | sophisme certain + omission structurelle | validé |
| 5 — Écart réel | `never_observed` | validé |
| 6 — Écart par contrainte | `prevented_by_constraint` | validé |

### Analyses M01 v2.1 sur cas réels

| Analyse | Locuteur | Date discours | Régime | Mode | Pattern V.3 saillant |
|---|---|---|---|---|---|
| Fabius | Président Conseil constitutionnel | janvier 2026 | sobre | applicable_complete | `observed_as_announced` × 2 |
| Ciotti | Président groupe UDR | oct 2025 | adversarial | applicable_vigilance_adversariale | V.3 vide motivé |
| Lecornu | Premier ministre | oct 2025 | substantiel | applicable_complete | `broken_explicitly` + motivation |
| Vallaud | Président groupe Socialistes | oct 2025 | pivot | applicable_degraded | `observed_otherwise` × 3 |
| Panot | Présidente groupe LFI | oct 2025 | adversarial | applicable_vigilance_adversariale | `never_observed` + `not_yet_observed` |
| Bayrou | Premier ministre | janv 2025 | substantiel | applicable_complete | 3 patterns différents |
| **Barnier** | **Premier ministre** | **oct 2024** | **substantiel — censuré** | **applicable_complete** | **4 patterns différents — couverture la plus large** |

### Applications M03 v2.1

| Application | Acteurs | Cas saillants | Statut |
|---|---|---|---|
| Séquence retraites octobre 2025 — *référence sur retraites* | Lecornu / Ciotti / Vallaud / Panot | 7 cas saillants | validé à 4 acteurs |
| **Séquence Bayrou-Barnier-Lecornu — *référence sur gouvernement minoritaire*** | **Barnier / Bayrou / Lecornu** | **7 cas saillants** | **validé à 3 acteurs PM successifs** |

*Deux applications M03 sur deux problématiques distinctes* — controverse thématique (retraites) et controverse méthodologique (gouvernement minoritaire). La méthode M03 v2.1 est éprouvée transversalement.

---

## 6. Pipeline opérationnel minimal

**Pré-requis.** Python 3.11+, Pydantic 2.13+, PyYAML.

**Composants.** `schemas.py` + `schemas_m03.py`. `validate.py` + `validate_m03.py`. 10 YAML M01-M validés + 2 YAML M03-M validés. 3 YAML tests négatifs.

**Note.** Pipeline *minimal* — valide les YAML produits par analyses humaines. Système opérationnel complet (production automatique d'analyses à partir de textes sources) en attente de codage. Voir `dev/methodologie_codage_v1.md`.

---

## 7. Travaux en cours et tâches suivantes

### Verrou stratégique identifié

**Décisions structurantes Phase 0 codage (5 décisions documentées dans la méthodologie de codage v1).** La consolidation doctrinale est désormais jugée suffisante. Le verrou est doctrinalement débloqué, le verrou est désormais *les décisions de Phase 0*.

### Audits en cours d'accumulation

— `intentionality_bias_audit` : 7/10 analyses M01 cas réels. Premier audit possible après 3 analyses supplémentaires.

— `hypothesis_gap_audit` : 10/20-30 analyses M01 + 2 applications M03. Premier audit possible après 10-20 analyses supplémentaires.

— `typology_audit` ouvert sur *deux candidats* — `amplification_temporaire_terminee_par_chute` (révélé par Bayrou) et `never_observed_by_actor_removal` (révélé par Barnier et M03 Bayrou-Barnier-Lecornu).

### Tâches reportées

— Phases 1-4 de la méthodologie de codage.

— Extension M03 à séquence Sánchez Espagne (test de généralisation hors France des découvertes 3.11 enrichie, 3.12, 3.13).

— Instanciation M02 lecture indiciaire (selon recommandation critique externe Gemini 2.C).

— Instanciation M04 triangulation historiographique (test critique de la portée structurelle des découvertes méthodologiques).

— Refonte v3 (après accumulation et retour d'expérience Phase 1-4 codage).

---

## 8. Décisions politiques pendantes

— Cinq décisions structurantes Phase 0 codage (orchestration multi-agents, persistance graphe, persistance journal, licence, modèle de distribution).

— Premier groupe Mode 1 (analystes).

— Trajectoire de financement Mode 3.

Détails dans `dev/methodologie_codage_v1.md` sections 4 et 8.

---

## 9. Navigation rapide

**Comprendre la doctrine** — charte → gabarit + révision mineure → l'une des méthodes.

**Voir des analyses concrètes** — Fabius (sobre) → Ciotti (adversarial) → Bayrou et Lecornu et Barnier (trois PM successifs, comparaison directe) → M03 Bayrou-Barnier-Lecornu (comparative méthodologique) → M03 retraites octobre 2025 à 4 acteurs (comparative thématique).

**Exécuter le pipeline** — `pipeline/README.md`. `pip install --break-system-packages pydantic pyyaml`. `python3 pipeline/validate.py --all`.

**Démarrer le codage** — `dev/methodologie_codage_v1.md`. Cinq décisions structurantes à prendre avant Phase 0.

**Première prise en main** — ce README → charte → gabarit → méthodologie de codage. Quatre à six heures de lecture pour compréhension solide.

---

## 10. Maintenance et versioning

**Conventions de versioning.** Majeure — refonte invalidant rétrocompatibilité. Mineure — évolution interne compatible.

**Disciplines.** Séparation sortie humaine / journal méthodologique. Anti-cumul des documents. Patterns observés vs fabriqués. Friction productive du pipeline traitée par typology_audit, jamais par modification ad hoc.

---

## Métadonnées du README

- *Version du README* : 1.3
- *Date d'édition* : 17 mai 2026
- *Modification depuis 1.2* — intégration de l'analyse Barnier v2.1 (septième M01 sur cas réel, unique PM censuré du corpus, couverture typologique la plus large) ; intégration de l'application M03 v2.1 Bayrou-Barnier-Lecornu (deuxième application M03, problématique méthodologique) ; métriques actualisées (10 YAML M01 + 2 M03 au pipeline) ; deuxième candidat typology_audit inscrit (`never_observed_by_actor_removal`) ; *consolidation doctrinale jugée substantielle — verrou stratégique désormais les 5 décisions Phase 0 codage*.

---

*Document factuel. Pour l'histoire et les frictions, `journal/journal.md`. Pour le plan de codage, `dev/methodologie_codage_v1.md`.*
