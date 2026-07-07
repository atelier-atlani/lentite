# L'Entité — Stack technique

*Document dérivé (communication/pilotage). Les décisions `.claude/decisions/` et le plan `plan_action_002.md` font foi. Destinataire premier : contributeur technique entrant. Prérequis de contribution : lecture du document maître (00) + signature du CLA (`gouvernance/CLA.md`) avant toute PR sur le périmètre AGPL.*

*Version 1.0 — 4 juillet 2026. Licence CC BY 4.0.*

---

## 1. Le principe avant la stack

Toute l'architecture découle d'un principe unique (décision 002), qu'il faut comprendre avant de lire le reste :

> **Les fichiers YAML validés et versionnés dans git sont la seule source de vérité. Tout le reste — graphe, index, exports, rapports — est une vue dérivée, jetable, reconstructible par rejeu intégral. Personne (humain ou agent) n'écrit dans une vue dérivée.**

Corollaires : pas de base de données tant que les seuils ne sont pas atteints ; pas d'état incrémental ; la migration d'outil est toujours un simple re-pointage de l'ingesteur ; l'audit d'une assertion remonte toujours à un commit.

## 2. Flux de données

```
texte source ──► [orchestrateur : 4 agents séquentiels] ──► YAML candidat
                  Charité → Vulnérabilités →                     │
                  Chaînes causales → Synthèse                    ▼
                  (1 log JSON par appel)              [validate.py / validate_m03.py]
                                                        échec → retry (≤2) → échec propre
                                                        succès ▼
                                            YAML validé, commité (SOURCE DE VÉRITÉ)
                                                               │ rejeu intégral
                                                               ▼
                                            [graph_builder.py] ──► NetworkX
                                                               │        │
                                              exports/graphe.graphml    ▼
                                              exports/graphe.json   [audits.py]
                                              (non versionnés)      → rapports markdown horodatés
```

L'humain intervient à deux endroits exactement : le commit du YAML validé (rien n'entre dans la source de vérité sans lui) et l'arbitrage des frictions.

## 3. Composants

| Composant | Rôle | Licence | État (4 juil. 2026) |
|---|---|---|---|
| `pipeline/schemas.py` (641+ l.) | Modèles Pydantic v2 M01 — le gabarit doctrinal rendu mécanique : omission à 4 champs obligatoires, defeaters exigés, bitemporalité, sentinelles NON_RENSEIGNE/NON_DOCUMENTE | Apache 2.0 | Durci (séq. 1) |
| `pipeline/schemas_m03.py` | Modèles M03 (comparatif multi-acteurs), réutilise GabaritVersion/sentinelles | Apache 2.0 | Bitemporalité étendue (2.0) ; omission M03 = question doctrinale ouverte |
| `pipeline/validate.py`, `validate_m03.py` | CLI de validation — rapport lisible, codes retour 0/1 | Apache 2.0 | Opérationnels |
| `pipeline/tests/` | Tests négatifs : YAML qui *doivent* échouer avec l'erreur ciblée — la preuve que les contraintes mordent | Apache 2.0 | 6 négatifs verts (+12 positifs) |
| `pipeline/graph_builder.py` | YAML validés → graphe NetworkX ; arêtes portant source/confiance/méthode/dates ; fusion des acteurs M01/M03 par identifiant ; reconstruction déterministe | AGPL-3.0 | Opérationnel — 121 nœuds, 291 arêtes, pont M01↔M03 (`M01_LIE`) |
| `pipeline/audits.py` | Les 3 audits du gabarit comme parcours de graphe (CLI) | AGPL-3.0 | Lot 2.3 en cours |
| `pipeline/orchestrateur.py` | Pipeline linéaire 4 agents, SDK Anthropic direct, retry borné, architecture hexagonale (le cœur ignore l'orchestration) | AGPL-3.0 | Lot 2.4–2.6 à venir |
| `pipeline/agents/*.md` | Prompts d'agents versionnés (jamais en dur dans le code) — rôles fonctionnels + postes disciplinaires hérités du prototype de mai | AGPL-3.0 | Matériau présent, adaptation au gabarit durci à venir (2.5) |
| `pipeline/analyses/*/logs/*.json` | Artefact par appel d'agent : prompt complet, réponse brute, modèle, horodatage, tokens, itération. Versionnés (traces de production, pas vues dérivées) | — | Format spécifié (plan §4, 2.6) |

## 4. Environnement

- **Python ≥ 3.10 (3.11 recommandé)** — le code utilise la syntaxe d'union PEP 604 (`X | None`). Symptôme d'une version trop ancienne : `TypeError: unsupported operand type(s) for |`. Sur macOS, le `python3` par défaut est souvent 3.9 : nommer l'interpréteur (`python3.11`) ou créer un venv avec lui.
- **Installation** : `python3.11 -m pip install -r requirements.txt` (forme `python -m pip` obligatoire — élimine l'ambiguïté pip/pip3 et les flags non portables).
- **Dépendances épinglées** : `pydantic==2.13.4`, `PyYAML==6.0.3`, `networkx==3.6.1` (+ SDK Anthropic au lot 2.4). Aucun framework d'orchestration, aucune base de données — c'est un choix documenté, pas un oubli (§5).
- **Secrets** : clé API Anthropic en variable d'environnement, jamais commitée (`.gitignore` couvre `.env`).
- **Vérification rapide** : la commande « ça marche si » du README §6.1.

## 5. Ce qu'on n'installe PAS, et quand ça changera

Les deux absences les plus visibles sont des décisions datées avec critères de bascule explicites — les contester sans nouvelle donnée est un non-sujet ; les franchir sans documenter la bascule est une violation :

| Absent | Cible de bascule | Critères (l'un suffit, documenté au journal) | Décision |
|---|---|---|---|
| Base de graphe | PostgreSQL + Apache AGE | > ~50 analyses ou rejeu > 60 s ; requêtes concurrentes multi-utilisateurs (Mode 1 service) ; requêtes croisées SQL+graphe pour audits statistiques | 002 §7 |
| Framework d'orchestration | langgraph (MIT) | Topologie non linéaire avérée : parallélisation d'agents (ex. boucle multi-postes), branchements conditionnels, état persistant inter-sessions, boucles dialectiques > 2 tours | 001 §7 |

En cas de bascule, deux invariants survivent : les logs JSON par appel (indépendants de l'orchestration) et le principe source-de-vérité (la migration du graphe = re-pointer l'ingesteur et rejouer).

## 6. Conventions de contribution

- **CLA d'abord** : aucune PR sur le périmètre AGPL sans CLA signé (condition du droit de double licence, décision 004 — bloquante, pas négociable).
- **Racine minimale** : README, LICENSE, LICENSES/, requirements.txt et répertoires — rien d'autre (`conventions.md` §6.7).
- **Un commit par opération logique**, messages explicites ; pas d'amend après push ; `main` protégée (pas de force-push) — c'est la garantie technique de l'append-only.
- **Journal** : markdown append-only physique, front matter YAML (date, type, refs) ; les entrées de clôture sont réservées aux séquences ; les agents n'écrivent jamais au journal.
- **Identifiants d'acteurs** : format unique `prenom_nom`, désambiguïsation documentée (convention en cours d'inscription, lot 2.3) — condition de validité de la fusion des nœuds du graphe.
- **SPDX par fichier** : `Apache-2.0` (schémas, validateurs, tests), `AGPL-3.0-only` (moteur), mention CC dans les front matters d'analyses.
- **Toute friction au journal, aucun arbitrage silencieux** : un choix non couvert par un plan ou une décision se signale, ne se tranche pas seul.
- **Moratoire doctrinal** : aucune révision de la charte avant la fin du dossier zéro — les frictions doctrinales s'inscrivent et attendent.

## 7. Sécurité — état et dette assumée

Traité : secrets hors repo, repo privé (jalon 1), append-only vérifiable au diff, validation mécanique en unique porte d'entrée de la source de vérité. **Dette assumée et datée** : la robustesse du pipeline d'ingestion face à des sources hostiles (injection de prompt via documents piégés) n'est pas encore traitée — test adversarial minimal prévu au dossier zéro (plan de reprise, axe 7), isolation contenu/instruction à spécifier à ce moment. Toute contribution sur l'orchestrateur doit garder cette échéance en tête : ne rien construire qui rende cette isolation plus difficile.

## 8. Parcours d'onboarding technique

1. Lire le document maître (00) — 20 minutes.
2. Cloner, suivre le README §6.1, valider une analyse existante (c'est le test d'onboarding à froid — il est réputé passer ; s'il échoue, c'est un bug d'onboarding à signaler, pas une erreur de l'entrant).
3. Reconstruire le graphe (`graph_builder.py`), regarder `exports/graphe.json`.
4. Casser un test négatif : modifier un YAML de `pipeline/tests/`, vérifier que le validateur le rejette avec l'erreur ciblée — c'est le geste qui fait comprendre le projet mieux que toute doc.
5. Exercice de calibration : re-coder deux analyses existantes en aveugle (protocole `doctrine/V2.1/lentite_calibration_confiance_v1.md`) — l'onboarding méthodologique *est* la première mesure inter-annotateurs du projet.
6. Signer le CLA. Première PR.

---

*Document 02 v1.0 — 4 juillet 2026. Emplacement cible : `communication/02_stack_technique.md`.*
