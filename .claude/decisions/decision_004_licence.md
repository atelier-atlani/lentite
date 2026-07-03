# Décision 004 — Licence

*Décision structurante Phase 0 du codage. Prise en délibération avec sparring partner (Claude.ai, Mode Architecte/sparring). Référence : `plan_action_001.md` §4.4. Append-only — toute révision fera l'objet d'une nouvelle décision référençant celle-ci.*

*Méta-information.*
- Date de décision : 3 juillet 2026.
- Décideur : Seb (Dirigeant).
- Statut : validée.
- Décisions liées : conditionne 005 (distribution) ; compatible avec 002 (persistance graphe) quelle que soit l'option retenue.

---

## 1. Contexte

Le projet L'Entité atteint le seuil du codage substantiel (Phase 1 — pipeline monolithique texte → analyse M01-M). La doctrine v2.1.1 est stable, le pipeline de validation opérationnel. La charte (couche A, §8) impose déjà une contrainte : cœur Mode 1 open source, Mode 2 sous distribution restreinte avec traçabilité. Le choix de licence détermine les modalités de réutilisation, de modification, de distribution commerciale et la stratégie de protection du projet.

Le projet vise en outre, à moyen terme, un débouché de type « standard » : le gabarit (couche B) et ses schémas de validation comme format ouvert de claim défaisable, exportable au-delà du scope politique (conformité déclarative, audit décisionnel, dossier probatoire).

## 2. Problème

Une licence unique ne peut pas satisfaire simultanément deux objectifs contradictoires du projet :

- **Diffusion maximale du gabarit** comme standard — exige une licence permissive, car un format dont l'implémentation de référence est sous copyleft ne sera pas adopté par des tiers.
- **Protection du moteur contre la capture propriétaire** — exige un copyleft fort de type réseau, car sous licence permissive un tiers peut forker le pipeline et opérer son propre service Mode 2 en concurrence directe, sans obligation de contribution. Ce scénario contredit frontalement le refus doctrinal de « l'asymétrie de l'instrument stratégique » (charte §8.2) et affaiblit le modèle de distribution duale pressenti (décision 005).

Le problème est donc reformulé : non pas « quelle licence pour L'Entité », mais « quelle licence pour chaque classe d'artefacts produits par L'Entité ».

## 3. Options examinées

**Option A — Apache 2.0 unique** (recommandation préliminaire du plan d'action 001).
Adoption maximale, protection brevets explicite, simplicité juridique. Mais aucune protection du moteur : la capture propriétaire du pipeline par un acteur commercial reste licite et probable en cas de succès. L'argument de cohérence avec les dépendances (PostgreSQL + AGE en Apache 2.0) est nul : la compatibilité de licence est unidirectionnelle, un projet AGPL peut s'appuyer sur des briques Apache/MIT.

**Option B — AGPL-3.0 unique.**
Protection maximale du moteur (obligation de republication des modifications opérées en service). Mais tue la diffusion du gabarit comme standard : contamination copyleft inacceptable pour les adopteurs tiers du format.

**Option C — Tri-partition par classe d'artefacts** (retenue).
- *Spécification et schémas* (couche B : gabarit, `schemas.py`, `schemas_m03.py`, validateurs) : **Apache 2.0** pour le code, **CC BY 4.0** pour les documents de spécification.
- *Pipeline et orchestration* (moteur : ingestion, agents, graphe, synthèse) : **AGPL-3.0**, copyright détenu intégralement par le porteur, préservant le droit de double licence commerciale pour le Mode 2.
- *Analyses produites* (dossiers M01/M03, sorties Mode 1) : **CC BY-SA 4.0** — citables et réutilisables, dérivés maintenus ouverts.

## 4. Critères de décision

- Alignement philosophique : refus de l'asymétrie, transparence, auditabilité publique du Mode 1 (charte §1, §8).
- Viabilité du modèle économique dual : le Mode 2 sous contrat doit rester un droit exclusif défendable.
- Diffusion du gabarit comme standard potentiel (actif transversal du portefeuille).
- Précédents éprouvés dans l'écosystème : le modèle AGPL + double licence commerciale est le mécanisme documenté de Neo4j, Grafana, MongoDB (pré-SSPL) — l'AGPL ne bloque pas le business, elle crée la raison de contracter.
- Public réel du Mode 1 (journalistes, chercheurs, analystes) : utilisateurs du service et lecteurs d'analyses, non intégrateurs de code — la friction AGPL en entreprise ne frappe pas ce public.

## 5. Décision retenue

**Option C — tri-partition.**

| Classe d'artefacts | Périmètre | Licence |
|---|---|---|
| Spécification / standard | Gabarit couche B, schémas Pydantic, validateurs CLI, documentation du format | Apache 2.0 (code) + CC BY 4.0 (spec) |
| Moteur | Pipeline d'ingestion, orchestration multi-agents, graphe cognitif, synthèse | AGPL-3.0, copyright unique porteur |
| Productions analytiques | Dossiers M01/M03 publiés en Mode 1 | CC BY-SA 4.0 |

Matérialisation dans le repo : fichier `LICENSE` racine (AGPL-3.0 par défaut), `LICENSES/` avec les trois textes, en-tête SPDX par fichier (`SPDX-License-Identifier`), section « Licences » du README explicitant la partition par répertoire.

## 6. Motif principal

La tri-partition est la seule option qui satisfait simultanément les deux objectifs stratégiques : diffusion du gabarit comme standard (permissif là où l'adoption est le but) et protection du moteur contre la capture propriétaire (copyleft réseau là où se concentre la valeur défendable). Elle matérialise en droit la séparation des couches que la doctrine impose déjà en architecture — la licence suit la doctrine au lieu de la contredire.

## 7. Conditions de révision

- **Contribution externe au pipeline** : avant acceptation de la première PR externe sur le périmètre AGPL, mise en place obligatoire d'un CLA (contributor license agreement) ou d'un DCO avec cession, faute de quoi le droit de double licence Mode 2 est perdu. Cette condition est bloquante et devra être vérifiée à l'onboarding de tout contributeur, y compris le co-dirigeant AXON-1.
- **Décollage du standard** : si le gabarit est adopté par des tiers au point de justifier une gouvernance neutre, migration possible de la spécification vers une fondation ou un organisme de standardisation — nouvelle décision référençant celle-ci.
- **Blocage d'adoption documenté** : si trois prospects Mode 1/Mode 2 qualifiés refusent explicitement pour motif AGPL sur une période de douze mois, réexamen de la licence moteur (candidats : double licence élargie, BSL avec fenêtre de conversion).
- **Incompatibilité de dépendance** : si une dépendance critique du pipeline s'avère incompatible AGPL, arbitrage documenté (remplacement de la dépendance prioritaire sur le changement de licence).

## 8. Conséquences immédiates

- La décision 005 (distribution) peut retenir le modèle dual en cohérence : cœur public AGPL, service Mode 2 sous licence commerciale séparée.
- La décision 002 (persistance graphe) n'est pas contrainte : PostgreSQL + AGE (Apache 2.0) comme Neo4j Community (GPLv3, utilisé non modifié comme composant serveur) restent compatibles.
- `plan_action_002.md` devra inclure la mise en place de la structure `LICENSES/` + SPDX dès le prototype.
- Le repo `lentite` doit exister (git) avant toute publication — dépendance vers la phase d'hygiène déjà identifiée.
- Inscription au journal méthodologique général comme entrée 8.9 (numérotation du plan d'action 001 §6).

---

*Décision 004 v1.0 — 3 juillet 2026. Append-only.*
