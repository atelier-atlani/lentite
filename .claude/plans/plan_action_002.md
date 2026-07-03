# Plan d'action 002 — Prototype technique Phase 0

*Deuxième plan d'action du workflow `.claude/`. Produit en Mode Architecte (Claude.ai). Spécifie le prototype technique de la Phase 0, en cohérence avec les cinq décisions structurantes classées dans `.claude/decisions/` (entrées 8.6–8.10 du journal méthodologique général).*

*Méta-information.*
- Date de production : 3 juillet 2026.
- Mode opérationnel : Architecte.
- Mode cible d'exécution : Implementer (Claude Code, Sonnet 4.6) pour les séquences techniques ; Dirigeant pour les actes de gouvernance (création repo, CLA) ; Cowork pour les opérations de classement.
- Plans référencés : `plan_action_001.md` (clos — cinq décisions prises le 3 juillet 2026).
- Plan suivant attendu : `plan_action_003.md` (dossier zéro rétrospectif) après revue du prototype par Mode Reviewer.

*Hypothèse de travail déclarée.* Ce plan a été produit avec le contexte intégral de la session de délibération (cinq décisions, audit d'arborescence du 3 juillet, plan de reprise en quatre phases) mais sans relecture de `etat_projet.md` et `conventions.md`. L'Implementer vérifie en tâche 0.0 que rien dans `conventions.md` ne contredit le présent plan ; toute contradiction est remontée avant exécution, pas arbitrée silencieusement.

---

## 1. Contexte

Les cinq décisions structurantes sont prises et documentées :

| Décision | Choix | Conséquence directe pour ce plan |
|---|---|---|
| 001 Orchestration | Custom Python minimal, pipeline linéaire 4 agents, logs JSON par appel, bascule langgraph sur critères | Spécifier l'orchestrateur, le format de log, `pipeline/agents/` |
| 002 Persistance graphe | Fichiers-source-de-vérité ; graphe NetworkX dérivé ; bascule AGE sur seuils | Spécifier `graph_builder.py` + audits comme parcours de graphe |
| 003 Persistance journal | Git + markdown append-only + front matter YAML | Convention à inscrire dans `conventions.md` ; pas d'indexeur |
| 004 Licence | Tri-partition Apache/CC BY (spec) + AGPL (moteur) + CC BY-SA (analyses) | Structure `LICENSES/` + en-têtes SPDX dès le prototype |
| 005 Distribution | Duale, trois jalons ; jalon 1 = repo privé structuré | La phase d'hygiène est le jalon 1 — première séquence de ce plan |

Trois décisions (002, 003, 005) convergent vers le même prérequis bloquant : le dépôt git n'existe pas encore. L'audit du 3 juillet a par ailleurs constaté : doublons non purgés à la racine (3 copies README, 2 copies journal, analyses dupliquées), `validate.py` M01 référencé par le README mais absent, dossier `lentite_observatrice_complet/` non statué, README daté de mai désynchronisé.

Enfin, quatre chantiers de couche B issus du plan de reprise conditionnent le schéma avant tout dossier réel : bloc omission durci, bitemporalité minimale, politique de corpus, calibration des degrés de confiance. Ils sont intégrés à ce plan (séquence 1) car les exécuter après le prototype imposerait une revalidation coûteuse de tout le corpus.

## 2. Objectif

**Livrer un dépôt privé assaini (jalon 1) contenant un gabarit durci et un prototype de pipeline complet** : texte source → quatre agents → YAML candidat → validation → graphe dérivé — avec traçabilité intégrale par artefacts, démontré sur au moins un texte source réel.

## 3. Critères d'acceptation

- [ ] **Repo** : `atelier-atlani/lentite` privé existe ; arborescence canonique assainie ; test d'onboarding à froid réussi (un tiers — instance Claude vierge — clone, lit le seul README, et parvient à valider une analyse existante sans autre aide).
- [ ] **Licences** : `LICENSE` racine (AGPL-3.0), dossier `LICENSES/` (3 textes), en-têtes SPDX sur tous les fichiers source, section Licences du README explicitant la partition par répertoire.
- [ ] **Gabarit durci** : les quatre chantiers de couche B implémentés dans les schémas Pydantic avec au moins un test négatif chacun ; les 12 YAML existants (9 analyses + 3 cas-jouets) revalident, amendements documentés au journal.
- [ ] **Pipeline** : `validate.py` M01 restauré ; `graph_builder.py` opérationnel (YAML → NetworkX → exports GraphML + JSON) ; les trois audits du gabarit implémentés comme parcours de graphe et exécutables en CLI.
- [ ] **Orchestrateur** : produit, sur au moins un texte source réel, un YAML M01-M qui passe `validate.py` (retry borné ≤ 2), avec un artefact de log JSON complet par appel d'agent.
- [ ] **Étalonnage** : la sortie automatique sur ce texte est comparée à l'analyse manuelle validée correspondante ; écarts documentés au journal (sans jugement de conformité à ce stade — c'est une donnée pour le Reviewer).
- [ ] **Gouvernance** : CLA co-dirigeant rédigé et versionné (`gouvernance/CLA.md`) avant toute PR externe.
- [ ] **Journal** : chaque séquence close = une entrée au journal (front matter conforme décision 003).

## 4. Spécification par séquences

### Séquence 0 — Hygiène et fondation (jalon 1 de la décision 005)

*Exécutant : Claude Code (opérations fichiers + git), Dirigeant (création du repo GitHub privé, secrets).*

- **0.0 Vérification préalable.** Lire `conventions.md` et `etat_projet.md` ; signaler toute contradiction avec ce plan avant de poursuivre.
- **0.1 Git.** `git init` sur `lentité/` (ou clone du repo distant créé par le Dirigeant), `.gitignore` (artefacts Python, `.env`, exports dérivés du graphe — les vues dérivées ne se versionnent pas, décision 002), commit initial de l'état canonique **avant toute purge** (l'état pré-assainissement doit être le premier commit : auditabilité de l'assainissement lui-même).
- **0.2 Purge et rapatriement.** Suppression des copies (`README copie*`, `journal copie*`) ; déplacement des analyses orphelines de la racine vers `analyses/` et `pipeline/analyses/` selon leur nature ; un commit par opération logique, messages explicites.
- **0.3 Cannibalisation d'`observatrice_complet/`.** Extraction des prompts réutilisables (contradicteur, analystes spécialisés) vers `pipeline/agents/` en fichiers markdown versionnés, avec en-tête indiquant origine et date ; déplacement du reste vers `archives/observatrice_complet_2026-05/` ; entrée au journal actant la décision de statut (cannibalisé + archivé).
- **0.4 Licences.** `LICENSE` racine, `LICENSES/`, en-têtes SPDX (`# SPDX-License-Identifier: AGPL-3.0-only` pour `pipeline/` hors schémas ; `Apache-2.0` pour `schemas*.py`, `validate*.py` ; les analyses portent leur mention CC dans leur front matter).
- **0.5 README.** Resynchronisation : arborescence réelle, section Licences, section Distribution (trois jalons), date réelle, suppression des références mortes.
- **0.6 CLA.** Rédaction de `gouvernance/CLA.md` (cession ou licence exclusive des contributions sur le périmètre AGPL au porteur, référence décision 004 §7). *Le Dirigeant valide ce texte avant merge — une relecture juridique reste recommandée avant la première signature effective.*
- **0.7 Conventions.** Ajout à `conventions.md` : convention de front matter du journal (décision 003), convention de commit, règle « une séquence close = une entrée journal ».

**Critère de sortie** : test d'onboarding à froid réussi (cf. §3). **Anti-tâche** : ne rien coder de nouveau dans cette séquence.

### Séquence 1 — Durcissement du gabarit (couche B)

*Exécutant : Claude Code. Chaque tâche = schéma + test négatif + revalidation du corpus.*

- **1.1 Bloc omission durci.** Dans `schemas.py`/`schemas_m03.py`, l'assertion d'omission exige quatre champs obligatoires : `pouvoir_agir` (référence documentée à la compétence/capacité), `opportunite` (datée), `cloture_corpus` (déclaration explicite du corpus dans lequel l'absence est constatée, avec date de clôture), `explications_innocentes` (liste non vide d'alternatives examinées avec statut). Test négatif : une omission sans clôture de corpus doit échouer.
- **1.2 Bitemporalité minimale.** Deux champs par assertion : `date_fait` (quand le fait a eu lieu) et `date_connaissance` (quand il est entré au corpus). Optionnels avec défaut explicite `non_renseigne` pour ne pas invalider brutalement l'existant — mais **obligatoires pour toute analyse nouvelle** (validation conditionnelle sur un champ de version de gabarit). Test négatif associé.
- **1.3 Politique de corpus v1.** Document `doctrine/V2.1/lentite_politique_corpus_v1.md` : typologie des sources (officielle, journalistique, statistique, militante, académique) avec qualification de fiabilité déclarée, règle d'extension tracée (toute source ajoutée en cours d'enquête = entrée au journal de méthode), lien formel avec le champ `cloture_corpus` de 1.1. Une à deux pages — version de démarrage, pas traité.
- **1.4 Grille de calibration.** Les trois cas-jouets promus cas-étalons officiels des degrés de confiance dans un document `doctrine/V2.1/lentite_calibration_confiance_v1.md` ; protocole inter-annotateurs spécifié (re-codage de deux analyses existantes par un second annotateur — co-dirigeant ou instance Claude isolée sans accès aux attributions — mesure d'écart simple). *L'exécution du protocole n'est pas dans ce plan (elle exige le second annotateur) ; seule sa spécification l'est.*
- **1.5 Revalidation du corpus.** Les 12 YAML revalident sous le gabarit durci ; chaque amendement nécessaire est commité individuellement et consigné (une entrée journal de synthèse pour la séquence, listant les frictions).

**Critère de sortie** : suite de tests complète verte (positifs + négatifs), corpus intégralement revalidé.

### Séquence 2 — Prototype pipeline

*Exécutant : Claude Code.*

- **2.1 `validate.py` M01.** Restauration par dérivation de `validate_m03.py` sur `schemas.py`. CLI homogène : `python validate.py <fichier.yaml>` → rapport structuré (erreurs Pydantic lisibles), code retour exploitable par l'orchestrateur.
- **2.2 `graph_builder.py`.** Ingestion de tous les YAML validés de `pipeline/analyses/` → graphe NetworkX (nœuds et arêtes typés conformément aux schémas, attributs épistémiques portés par les arêtes : source, confiance, méthode, dates de 1.2) ; exports `exports/graphe.graphml` et `exports/graphe.json` (non versionnés — vues dérivées) ; reconstruction intégrale à chaque exécution (pas d'état incrémental — décision 002, le rejeu est le mécanisme).
- **2.3 Audits.** Les trois audits du gabarit (`intentionality_bias_audit`, `hypothesis_gap_audit`, `typology_audit`) implémentés comme parcours du graphe NetworkX, exécutables : `python audits.py <nom_audit>` → rapport markdown horodaté dans `exports/audits/` (non versionné ; s'il doit être conservé, il est cité au journal).
- **2.4 Orchestrateur minimal (`pipeline/orchestrateur.py`).** Architecture hexagonale légère : le cœur (schémas, validation, graph_builder) n'importe rien de l'orchestration. Pipeline linéaire : texte source → Charité → Vulnérabilités → Chaînes causales → Synthèse → assemblage YAML → `validate.py` ; en cas d'échec de validation, le rapport d'erreurs est réinjecté à l'agent Synthèse, deux itérations maximum, puis échec propre avec logs. Prompts chargés depuis `pipeline/agents/*.md` (adaptés en 2.5). SDK Anthropic direct ; modèle par défaut Sonnet (cohérence coût du workflow), paramétrable.
- **2.5 Adaptation des prompts d'agents.** Les prompts cannibalisés en 0.3 sont alignés sur la doctrine v2.1.1 et sur les schémas durcis de la séquence 1 (chaque agent connaît le fragment de schéma qu'il alimente). Chaque prompt est un fichier versionné avec numéro de version propre.
- **2.6 Format de l'artefact de log.** Par appel d'agent, un fichier `pipeline/analyses/<analyse>/logs/<n>_<agent>_<horodatage>.json` contenant : `agent`, `version_prompt`, `modele`, `horodatage_iso`, `iteration`, `prompt_complet`, `reponse_brute`, `usage_tokens`. Le dossier d'une analyse produite automatiquement contient son YAML **et** ses logs — versionnés ensemble (les logs d'analyses sont des traces de production, pas des vues dérivées : ils se versionnent, contrairement aux exports du graphe).
- **2.7 Test de bout en bout étalonné.** Exécution de l'orchestrateur sur le texte source d'une analyse M01 existante (proposition : Lecornu ou Fabius — au choix du Dirigeant selon disponibilité du texte source original). Production du YAML automatique, validation, puis document d'écarts `exports/etalonnage_001.md` comparant sortie automatique et analyse manuelle validée : éléments communs, manqués, ajoutés, divergences de degré de confiance. **Sans jugement de conformité** — c'est la matière première du Mode Reviewer.

**Critère de sortie** : critères d'acceptation §3 lignes pipeline, orchestrateur et étalonnage satisfaits.

## 5. Anti-tâches

- *Ne pas installer* de framework d'orchestration (langgraph — critères de bascule non atteints, décision 001 §7), *ni* de base de données (seuils non atteints, décision 002 §7).
- *Ne pas coder* l'indexeur de journal (décision 003 §8 — besoin non avéré).
- *Ne pas écrire* dans le graphe ni au journal depuis l'orchestrateur ou les agents (décisions 002/003) — les agents produisent des fichiers candidats, l'humain commit.
- *Ne pas commencer* le dossier zéro rétrospectif — c'est `plan_action_003.md`, après revue du prototype.
- *Ne rien publier* — jalon 2 non atteint (décision 005) ; le repo reste privé.
- *Ne pas réviser la doctrine* (moratoire) : toute friction doctrinale rencontrée est consignée au journal avec son niveau, et attend la fin du dossier zéro.
- *Ne pas optimiser* : pas de parallélisation, pas de cache d'appels, pas de gestion d'erreurs au-delà du retry borné spécifié.

## 6. Output attendu

- Repo `atelier-atlani/lentite` privé, assaini, licencié, conforme aux critères §3.
- Gabarit durci (séquence 1) avec corpus revalidé.
- Prototype pipeline complet (séquence 2) démontré sur un texte réel avec étalonnage.
- `exports/etalonnage_001.md` + entrées journal des trois séquences.
- **Rapport d'implémentation** (`.claude/logs/rapport_implementation_002.md`) rédigé par l'Implementer à destination du Mode Reviewer : ce qui a été fait, les frictions, les écarts au plan et leurs motifs.

## 7. Modèle recommandé et répartition

- **Claude Code (Sonnet 4.6)** : séquences 0 (hors création repo), 1, 2 — en lots d'une session chacun au maximum : {0.1–0.2}, {0.3–0.7}, {1.1–1.2}, {1.3–1.4}, {1.5}, {2.1–2.2}, {2.3}, {2.4–2.6}, {2.7}. Chaque lot se termine par des commits propres et une note de lot.
- **Dirigeant** : création du repo GitHub privé + gestion de la clé API (variable d'environnement, jamais commitée) + validation du CLA + choix du texte source d'étalonnage (2.7).
- **Cowork** : classement de ce plan dans `.claude/plans/`, entrées journal.
- **Mode Reviewer (Claude.ai)** : à la fin, sur la base du rapport d'implémentation et de `etalonnage_001.md` — produit la revue et prépare `plan_action_003.md` (dossier zéro).

## 8. Estimation

- Séquence 0 : 1 à 2 sessions Claude Code (une demi-journée cumulée).
- Séquence 1 : 3 sessions (schémas + tests + revalidation).
- Séquence 2 : 4 à 5 sessions (dont l'adaptation des prompts, poste le plus incertain).
- Coût API : modéré — développement sur Sonnet ; le test 2.7 consomme quelques dizaines de milliers de tokens par itération d'agent.
- Délai recommandé : séquence 0 sous une semaine (elle débloque tout, y compris l'onboarding du co-dirigeant) ; l'ensemble sous quatre semaines compte tenu des créneaux disponibles (PSQ en build parallèle jusqu'à mi-août).

## 9. Discipline d'exécution

- *Une séquence à la fois, dans l'ordre.* La séquence 1 ne commence pas avant le critère de sortie de la 0 ; idem 1 → 2.
- *Un lot = une session = des commits propres.* Aucun chantier ouvert entre deux sessions.
- *Toute friction au journal*, avec front matter conforme (décision 003), sans révision doctrinale à chaud (moratoire).
- *L'Implementer ne prend aucune décision structurante.* Tout choix non couvert par ce plan ou par les cinq décisions est remonté (note dans le rapport d'implémentation, ou interruption du lot si bloquant).
- *Le premier commit précède la première purge* (0.1) — l'assainissement lui-même doit être auditable.

---

*Plan d'action 002 v1.0 — produit le 3 juillet 2026 par Mode Architecte. À placer dans `.claude/plans/plan_action_002.md`. Prochain plan attendu — `plan_action_003.md` (dossier zéro rétrospectif) après revue du prototype par Mode Reviewer.*
