# L'Entité — README

*État des lieux du projet à juillet 2026. Point d'entrée pour la navigation, l'archivage et la reprise. Document factuel — il référence les sources doctrinales sans les dupliquer.*

---

## 1. Qu'est-ce que L'Entité

L'Entité est une infrastructure d'enquête forensique sur le réel produit par actions humaines, fondée sur le dévoilement (*aletheia*). Phrase-cœur — *la vérité est dans la qualité du chemin*. Figure — l'enquêteur forensique.

Le projet se déploie en trois modes — *Mode 1* (éclairage médiatique d'analystes), *Mode 2* (conseiller du prince, distribution restreinte), *Mode 3* (chat public à finalité auto-pédagogique). Quatre engagements de l'ADN — refus de confondre dit/fait/produit/voulu, observation située déclarée, ligne fine entre naïveté et paranoïa, refus de présupposer la chaîne causale.

Pour la doctrine complète, lire `doctrine/V2.1/lentite_charte_v2_1.md`. Le présent README ne se substitue pas à la doctrine.

---

## 2. État courant — juillet 2026

| Volet | État |
|---|---|
| Couche A (charte) | v2.1 canonique |
| Couche B (gabarit) | v2.1 + révision mineure v2.1.1 |
| Couche C (méthodes) | M01 v2.1 + M03 v2.1 |
| Cas-jouets canoniques | 6/6 instanciés |
| Analyses M01 sur cas réels | 7 produites (Fabius, Ciotti, Lecornu, Vallaud, Panot, Bayrou, Barnier) |
| Applications M03 sur cas réels | 2 produites (retraites octobre 2025 à 4 acteurs, Bayrou-Barnier-Lecornu) |
| Pipeline de validation | Pydantic v2 — validateur M03-M opérationnel ; validateur M01-M **à restaurer** (séquence 2, tâche 2.1) |
| Tests négatifs pipeline | 3/3 confirment que les contraintes mordent |
| Décisions structurantes Phase 0 (codage) | 5/5 prises le 3 juillet 2026 — voir `.claude/decisions/` |
| Dépôt git | initialisé le 3 juillet 2026 — jalon 1 (dépôt privé) de la décision 005 |
| Licence | tri-partition posée (décision 004) — `LICENSE`, `LICENSES/`, en-têtes SPDX, voir section 6 |
| Hygiène du dépôt (séquence 0, `plan_action_002.md`) | en cours d'exécution |

**Cinq décisions structurantes de codage prises, hygiène du dépôt en cours.** La doctrine v2.1.1 reste stable et n'a fait l'objet d'aucune révision pendant la Phase 0 du codage (moratoire, voir `.claude/plans/plan_action_002.md` §5).

---

## 3. Architecture du projet

```
lentite/
├── lentite_README_projet.md           ← ce fichier
├── LICENSE                            ← AGPL-3.0 (licence par défaut du dépôt)
├── LICENSES/                          ← AGPL-3.0, Apache-2.0, CC-BY-SA-4.0 (textes intégraux)
├── doctrine/                          ← couches A, B, C
│   ├── V2/                            ← obsolète, conservée par discipline du journal
│   └── V2.1/                          ← canonique courante
├── analyses/                          ← production analytique (Markdown, licence CC BY-SA 4.0)
│   ├── cas_jouets/                    ← fixtures de calibration
│   ├── m01/                           ← analyses individuelles
│   └── m03/                           ← applications comparatives
├── pipeline/                          ← couche d'exécution opérationnelle
│   ├── schemas.py + schemas_m03.py    ← Apache 2.0
│   ├── validate_m03.py                ← Apache 2.0 (validate.py M01 à restaurer)
│   ├── agents/                        ← prompts d'agents versionnés — AGPL-3.0-only
│   ├── analyses/*.yaml                ← YAML M01-M/M03-M validés — CC BY-SA 4.0
│   ├── tests/*.yaml                   ← tests négatifs — Apache 2.0
│   └── lentite_README_projet.md (pipeline)
├── dev/                                ← méthodologie de développement du projet lui-même
│   ├── lentite_methodologie_codage_v1.md
│   └── lentite_methodologie_workflow_collaboratif_ia_v1.md
├── gouvernance/                       ← CLA et documents de gouvernance
│   └── CLA.md
├── archives/                          ← strates génétiques datées, non canoniques
│   ├── observatrice_complet_2026-05/  ← prototype antérieur, prompts cannibalisés vers pipeline/agents/
│   └── structure_lentite_2026-07-01.rtf
├── coordination/                      ← documents de coordination (peu nombreux)
├── journal/                           ← journal méthodologique général
└── .claude/                           ← workflow collaboratif IA (plans, décisions, contexte de session)
```

Couches distinctes — doctrine, analyses, pipeline, dev, gouvernance, coordination/journal, archives. Chacune avec sa discipline propre. La doctrine est versionnée par majeure et mineure ; les analyses référencent la doctrine sans la dupliquer ; le pipeline est code Python + YAML, isolable et exécutable ; le journal trace les évolutions ; les archives conservent les strates génétiques du projet sans les faire concourir avec le canon courant.

**Racine minimale.** Depuis la tâche 0.7 de `plan_action_002.md`, seuls `README`, `LICENSE`, `LICENSES/` et des répertoires sont admis à la racine — convention inscrite à `conventions.md` §6.7. Aucun document de travail, aucune copie, aucun fichier orphelin n'y séjourne.

---

## 4. Documents canoniques v2.1.1 — référence courante

**Couche A.** `doctrine/V2.1/lentite_charte_v2_1.md` — quatre engagements de l'ADN, trois modes opérationnels, deux dimensions de l'objet (réel des actes + récits politiques structurants), doctrine sur les patterns observés vs fabriqués (section 6.6), primauté de l'inférence sur les patterns.

**Couche B.** `doctrine/V2.1/lentite_gabarit_v2_1.md` + `doctrine/V2.1/lentite_revisions_v2_1.md` (révision mineure v2.1.1). Grammaire des méthodes — 16 sections normatives, sept patterns temporels avec ancrage empirique (dont `broken_explicitly` v2.1), bloc V refondé en quatre sous-blocs, schéma Pydantic enrichi. La révision mineure v2.1.1 ajoute deux catégories d'audit au journal — `intentionality_bias_audit` et `hypothesis_gap_audit`.

**Couche C.** `doctrine/V2.1/lentite_methode_01_v2_1.md` (analyse rhétorique d'un discours public) et `doctrine/V2.1/lentite_methode_03_v2_1.md` (analyse comparative multi-acteurs sur même controverse). Quatorze étapes pour chaque méthode, avec spécifications opérationnelles et critères d'évaluation.

**Méthodologie de développement** (distincte de la doctrine analytique). `dev/lentite_methodologie_codage_v1.md` — cinq phases de codage avec critères d'acceptation, cinq décisions structurantes de Phase 0 (toutes prises, voir `.claude/decisions/`). `dev/lentite_methodologie_workflow_collaboratif_ia_v1.md` — workflow de collaboration entre modes IA (Architecte, Implementer, Reviewer, Maintainer, Cowork), matérialisé dans `.claude/`.

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

### Analyses M01 v2.1 sur cas réels (`analyses/m01/` + `analyses/cas_jouets/` pour Ciotti)

| Analyse | Locuteur | Régime | Pattern V.3 saillant |
|---|---|---|---|
| Fabius | Président Conseil constitutionnel | sobre | `observed_as_announced` × 2 |
| Ciotti | Président groupe UDR | adversarial | V.3 vide motivé |
| Lecornu | Premier ministre | substantiel | `broken_explicitly` + motivation |
| Vallaud | Président groupe Socialistes | pivot | `observed_otherwise` × 3 |
| Panot | Présidente groupe LFI | adversarial | `never_observed` + `not_yet_observed` |
| Bayrou | Premier ministre (janv. 2025) | substantiel | 3 patterns différents |
| Barnier | Premier ministre (oct. 2024, censuré) | substantiel | 4 patterns différents (couverture la plus large) |

Sept cas réels couvrant tous les régimes documentés du gabarit v2.1. Les analyses sont matière première pour les applications M03 et alimentent la fenêtre roulante des audits inscrits au gabarit v2.1.1.

### Applications M03 v2.1 (`analyses/m03/`)

| Application | Séquence | Acteurs | Statut |
|---|---|---|---|
| Séquence retraites octobre 2025 (4 acteurs) | 6-16 octobre 2025 + effets à mai 2026 | Lecornu / Ciotti / Vallaud / Panot | canonique courante |
| ~~Séquence retraites octobre 2025 (3 acteurs)~~ | 6-16 octobre 2025 | Lecornu / Ciotti / Vallaud | **supersédée par la version 4 acteurs (juillet 2026)** — conservée pour traçabilité |
| Séquence Bayrou-Barnier-Lecornu | gouvernement minoritaire, 2024-2025 | Barnier / Bayrou / Lecornu | validé |

Le YAML M03-M correspondant à la version 3 acteurs a été retiré de `pipeline/analyses/` — seul le YAML 4 acteurs y est maintenu, conformément à la discipline anti-cumul (`conventions.md` §6.1).

---

## 6. Pipeline opérationnel

**Localisation.** `pipeline/`. Lire `pipeline/lentite_README_projet.md` pour usage détaillé (document hérité, non encore resynchronisé — voir avertissement en section 9).

**Pré-requis.** Python 3.11+, Pydantic 2.13+, PyYAML.

**Composants.**

— `schemas.py` (modèles Pydantic v2 selon gabarit v2.1 section 11) + `schemas_m03.py` (extension M03 v2.1 section 11). Licence Apache 2.0.

— `validate_m03.py` (CLI validateur M03). Licence Apache 2.0. **`validate.py` (validateur M01) n'existe pas encore** — restauration prévue tâche 2.1 de `plan_action_002.md`, par dérivation de `validate_m03.py` sur `schemas.py`.

— `agents/` — cinq prompts cannibalisés du prototype `lentite_observatrice_complet/` (contradicteur, analyste discours, économiste, juriste, sociologue). Non encore adaptés à la doctrine v2.1.1 ni aux schémas durcis (tâche 2.5). Licence AGPL-3.0-only.

— `analyses/*.yaml` (douze YAML d'analyses M01-M/M03-M validés, CC BY-SA 4.0) + `tests/*.yaml` (trois YAML défaillants délibérément, Apache 2.0, validation que les contraintes mordent).

**Usage actuellement disponible.**

```bash
# Validation d'une analyse M03 (seul validateur CLI opérationnel à ce jour)
python3 pipeline/validate_m03.py pipeline/analyses/m03_retraites_octobre_2025_4acteurs_v2_1.yaml
```

Il n'existe à ce jour ni option `--all` ni validateur M01 CLI — ces capacités sont prévues en séquence 2 de `plan_action_002.md` (`validate.py`, `graph_builder.py`, audits en CLI, orchestrateur).

**Contraintes validées par tests négatifs.**

1. `broken_explicitly` exige `public_motivation_invoked` non null (gabarit v2.1 section 6.6).

2. Bloc V.3 vide si et seulement si locuteur non-efficient sur tous les objets thématiques (gabarit v2.1 section 13 critère 7).

3. Convention 6.7 — `hypothesis_gap ≤ 0.2` requiert `zone_of_indetermination`, etc. (gabarit v2.1 section 6.7).

Les trois tests négatifs sont rejetés par le pipeline avec message d'erreur référençant la section du gabarit violée.

---

## 7. Licences

Tri-partition par classe d'artefacts, décidée le 3 juillet 2026 (`.claude/decisions/decision_004_licence.md`) et matérialisée dans ce dépôt.

| Classe d'artefacts | Périmètre (répertoires) | Licence |
|---|---|---|
| Spécification / standard | `pipeline/schemas.py`, `pipeline/schemas_m03.py`, `pipeline/validate*.py`, `pipeline/tests/`, doctrine couche B (`doctrine/`) | Apache 2.0 (code) + CC BY 4.0 (documents de spécification) |
| Moteur (orchestration) | `pipeline/agents/`, `pipeline/orchestrateur.py` et modules d'orchestration à venir, `graph_builder.py` à venir | AGPL-3.0, copyright détenu intégralement par le porteur |
| Productions analytiques | `analyses/`, `pipeline/analyses/` | CC BY-SA 4.0 |

`LICENSE` à la racine porte le texte intégral AGPL-3.0 (licence par défaut du dépôt). `LICENSES/` contient les trois textes intégraux (`AGPL-3.0.txt`, `Apache-2.0.txt`, `CC-BY-SA-4.0.txt`). Chaque fichier de code porte un en-tête `SPDX-License-Identifier` ; chaque YAML/Markdown d'analyse porte sa mention de licence en tête de fichier ou en commentaire.

**Contribution externe.** Toute contribution au périmètre AGPL est conditionnée à la signature préalable du CLA (`gouvernance/CLA.md`, projet non encore validé juridiquement) — condition bloquante, décision 004 §7.

---

## 8. Distribution

Modèle dual à trois jalons conditionnels, décidé le 3 juillet 2026 (`.claude/decisions/decision_005_modele_distribution.md`).

**Jalon 1 — Privé structuré (en cours).** Dépôt `atelier-atlani/lentite`, hygiène en cours d'exécution (`plan_action_002.md` séquence 0). Accès Dirigeant + co-dirigeant, ce dernier sous CLA préalable sur le périmètre AGPL.

**Jalon 2 — Passage public du cœur (non atteint).** Conditionné à (a) dossier zéro rétrospectif livré, validé au pipeline et relu par deux lecteurs externes, et (b) relecture juridique de la responsabilité éditoriale effectuée et intégrée à la charte. Le périmètre spec/gabarit peut passer public dès ce jalon, ou avant par décision légère.

**Jalon 3 — Ouverture commerciale Mode 2 (non atteint).** Postérieure au jalon 2 — licence commerciale séparée.

Le Mode 3 (chat public) reste hors scope de cette décision, report doctrinal maintenu.

---

## 9. Travaux en cours et tâches suivantes

### Séquence 0 (hygiène et fondation) — en cours

Exécution de `plan_action_002.md` séquence 0 — git init, purge des doublons, cannibalisation d'`observatrice_complet/`, licences, README, CLA, conventions. **Non fait à ce stade** — resynchronisation de `pipeline/lentite_README_projet.md` (document hérité, distinct du présent fichier, décrivant encore l'état de mai 2026) ; test d'onboarding à froid (tiers clone et valide une analyse sans autre aide) non encore mené.

### Séquences suivantes

**Séquence 1 — durcissement du gabarit couche B.** Bloc omission durci, bitemporalité minimale, politique de corpus v1, grille de calibration. Revalidation du corpus (douze YAML) sous le gabarit durci.

**Séquence 2 — prototype pipeline.** `validate.py` M01 restauré, `graph_builder.py` (YAML → NetworkX → exports), trois audits du gabarit en CLI, orchestrateur minimal (texte source → 4 agents → YAML → validation), test de bout en bout étalonné sur un texte source réel.

### Audits en cours d'accumulation

**`intentionality_bias_audit` (gabarit v2.1.1).** Fenêtre roulante de 10 analyses, seuil d'alerte 80%. 7/10 analyses M01 sur cas réels accumulées — premier audit possible après 3 analyses supplémentaires.

**`hypothesis_gap_audit` (gabarit v2.1.1).** Fenêtre roulante de 20-30 analyses, trois seuils d'alerte. 10/20-30 analyses (7 cas réels + 2 applications M03 + cas-jouets) accumulées.

### Tâches reportées (à plus long terme)

— *Pipeline génération M01-P automatique*, *pipeline d'audit des typologies*, *routing automatique par `method_id`*, *autres méthodes du catalogue* (M02 prioritaire, M04-M08). Voir `dev/lentite_methodologie_codage_v1.md` et `.claude/plans/plan_action_002.md` pour le séquencement détaillé.

---

## 10. Décisions politiques pendantes

Les cinq décisions structurantes de codage (orchestration, persistance graphe, persistance journal, licence, distribution) sont **prises** — voir `.claude/decisions/`. Décisions politiques hors codage encore pendantes, relevant du choix du porteur principal (Seb) :

— *Premier groupe Mode 1 (analystes)*. Composition initiale, profils recherchés, format de collaboration.

— *Trajectoire de financement Mode 3 (chat public)*. Modèle économique du service public ou semi-public, partenaires institutionnels possibles, conditions de gratuité.

— *Modalités précises du CLA*. Mécanisme de signature (CLA-bot ou signature manuelle), relecture juridique — voir `gouvernance/CLA.md` §5.

---

## 11. Navigation rapide

**Si vous voulez comprendre la doctrine** — lire dans l'ordre `doctrine/V2.1/lentite_charte_v2_1.md` (couche A), puis `doctrine/V2.1/lentite_gabarit_v2_1.md` + `lentite_revisions_v2_1.md` (couche B), puis l'une des méthodes (M01 ou M03 selon intérêt).

**Si vous voulez voir des analyses concrètes** — commencer par `analyses/m01/lentite_analyse_fabius_v2_1.md` (cas sobre) pour la lisibilité, puis `analyses/cas_jouets/lentite_cas_jouet_4_ciotti_v2_1.md` (cas adversarial) pour la complexité, puis `analyses/m03/lentite_m03_application_retraites_octobre_2025_4acteurs_v2_1.md` pour l'application comparative.

**Si vous voulez exécuter le pipeline** — aller dans `pipeline/`, installer les dépendances (`pip install --break-system-packages pydantic pyyaml`), puis valider une analyse M03 (`python3 pipeline/validate_m03.py pipeline/analyses/<fichier>.yaml`). Le validateur M01 n'est pas encore disponible.

**Si vous voulez critiquer la doctrine** — examiner les fixtures `analyses/cas_jouets/` et les tests négatifs `pipeline/tests/`. Les contraintes mordantes sont documentées dans le pipeline.

**Si vous prenez en main le projet pour la première fois** — lire ce README, puis la charte, puis le gabarit, puis lancer le pipeline sur une analyse M03 pour voir la validation en action. La doctrine est dense — quatre à six heures de lecture pour une compréhension solide.

---

## 12. Maintenance et versioning

**Conventions de versioning** (gabarit section 1).

— *Majeure* (v2 → v3) — refonte qui invalide la rétrocompatibilité des sorties.

— *Mineure* (v2.1 → v2.1.1) — évolution interne compatible.

**Catégories d'entrée canoniques au journal** (gabarit section 16, étendu par v2.1.1) — `method_evolution`, `case_execution`, `failure_pattern`, `typology_audit`, `intentionality_bias_audit`, `hypothesis_gap_audit`.

**Journal — persistance et front matter** (décision 003). Le journal méthodologique général et les journaux de méthodes sont des fichiers markdown versionnés dans git, en régime append-only physique. Chaque entrée porte un front matter YAML minimal (`date`, `type`, `refs`). Voir `conventions.md` §7 pour la convention complète et `.claude/decisions/decision_003_persistance_journal.md`.

**Discipline de séparation sortie humaine / journal méthodologique** (gabarit v2.1 section 9.0). La sortie humaine M01-H est conçue pour lecteur informé non-analyste, allégée du méta-discours.

**Discipline anti-cumul des documents de coordination.** Les documents de coordination sont conservés à l'unité, pas empilés en versions successives.

**Discipline de racine minimale** (`conventions.md` §6.7, depuis juillet 2026). Seuls `README`, `LICENSE`, `LICENSES/` et des répertoires à la racine.

---

## Métadonnées du README

- *Version du README* : 2.0
- *Date d'édition* : 3 juillet 2026 (resynchronisation, tâche 0.5 de `plan_action_002.md`)
- *État du projet à la date* : cinq décisions structurantes de codage prises, dépôt git initialisé, séquence 0 (hygiène) en cours d'exécution, 7 analyses M01 + 2 applications M03 + 6 cas-jouets canoniques
- *Prochaine révision attendue* : à la clôture de la séquence 0 (test d'onboarding à froid) ou après la séquence 1 (durcissement du gabarit)

---

*Document factuel. Pas de récit du projet. Pour l'histoire et les frictions du développement, consulter `journal/lentite_journal.md`. Pour les décisions doctrinales, lire la charte v2.1. Pour les décisions structurantes de codage, lire `.claude/decisions/`.*
