# Décision 003 — Persistance du journal méthodologique

*Décision structurante Phase 0 du codage. Prise en délibération avec sparring partner (Claude.ai, Mode Architecte/sparring). Référence : `plan_action_001.md` §4.3. Append-only — toute révision fera l'objet d'une nouvelle décision référençant celle-ci.*

*Méta-information.*
- Date de décision : 3 juillet 2026.
- Décideur : Seb (Dirigeant).
- Statut : validée.
- Décisions liées : application directe du principe fichiers-source-de-vérité établi par la décision 002 ; cohérente avec 004 (aucune contrainte de licence) ; contraint 001 (les agents n'écrivent pas au journal — seul le Dirigeant ou un processus validé par lui produit des entrées).

---

## 1. Contexte

Le journal méthodologique général et les journaux propres aux méthodes constituent la trace de l'évolution doctrinale et décisionnelle de L'Entité : entrées datées, append-only, requises pour les audits doctrinaux et la reprise de contexte entre sessions. À juillet 2026, le journal existe (`lentite_journal.md`, ~21 Ko) en markdown, tenu manuellement, avec deux mois de pratique effective. Les entrées 8.6 à 8.10 sont réservées aux cinq décisions structurantes de la Phase 0.

## 2. Problème

Comment persister les entrées de journal de façon (a) strictement append-only, (b) datée, (c) lisible humainement — critère qualifié d'essentiel pour l'audit doctrinal par le plan d'action 001 — et (d) requêtable si un besoin d'audit indexé émerge, sans créer de couplage avec la persistance du graphe ni de migration de format injustifiée ?

## 3. Options examinées

**Option A-stricte — Git + JSON structuré indexé** (recommandation préliminaire du plan).
Versioning natif, requêtabilité via index séparé. Mais impose une migration du journal existant (markdown → JSON) et sacrifie la lisibilité humaine directe — le JSON se lit via outils, pas en ouvrant le fichier. Le gain de requêtabilité ne répond à aucun besoin identifié : les trois audits du gabarit v2.1.1 (`intentionality_bias_audit`, `hypothesis_gap_audit`, `typology_audit`) portent sur le graphe cognitif, couvert par la décision 002, non sur le journal.

**Option A-amendée — Git + markdown append-only + front matter YAML léger** (retenue).
Le journal reste en markdown, format de sa pratique effective. Chaque entrée porte un front matter YAML minimal (date, type d'entrée, références aux décisions/analyses concernées) qui la rend parsable par script trivial le jour où un besoin d'index émerge. L'index, s'il advient, est dérivé et jetable — application symétrique du principe de la décision 002.

**Option B — Base de données avec event sourcing.**
Écartée : contredit le principe fichiers-source-de-vérité (décision 002), couple le journal à l'infrastructure du graphe, sacrifie la lisibilité humaine native.

**Option C — Hybride Git + DB d'index.**
Écartée comme décision : c'est une voie d'évolution, pas un choix initial. Elle reste ouverte via le front matter (condition de révision §7), sans duplication de données aujourd'hui.

## 4. Critères de décision

- Discipline append-only structurellement respectée (git : chaque entrée est un commit ; toute réécriture est visible au diff).
- Lisibilité humaine native — critère essentiel du plan, décisif pour l'audit doctrinal et l'onboarding (co-dirigeant, comité de lecture futur).
- Continuité avec la pratique réelle : deux mois de journal markdown existant, zéro migration.
- Réversibilité : capacité d'indexation future sans engagement présent.
- Cohérence architecturale avec la décision 002 (fichiers-source-de-vérité, vues dérivées).

## 5. Décision retenue

**Option A-amendée** :

- Le journal méthodologique général et les journaux de méthodes sont des fichiers markdown versionnés dans git, en régime append-only physique : les entrées s'ajoutent exclusivement en fin de fichier, dans l'ordre chronologique d'écriture. La numérotation logique (ex. 8.6–8.10 réservées) n'autorise aucune insertion ni réordonnancement — un numéro logique peut être écrit hors ordre, jamais inséré dans le corps existant.
- Chaque nouvelle entrée porte un front matter YAML minimal en bloc de code ou en en-tête d'entrée : `date`, `type` (décision | révision doctrinale | friction | audit | reprise), `refs` (décisions, analyses, plans concernés). Les entrées antérieures ne sont pas rétrofittées (append-only).
- Toute structure de requête (index, extraction, tableau de bord) est dérivée des fichiers par script, reconstructible, jamais source de vérité.
- Seul le Dirigeant — ou un processus explicitement validé par lui — écrit au journal. Les agents de l'orchestration (décision 001 à venir) n'y ont pas accès en écriture.

## 6. Motif principal

Le journal est un document de lecture, pas une donnée : le format doit servir l'humain qui audite, le front matter servant la machine qui indexera peut-être. L'A-amendée optimise la pratique réelle du projet (markdown, deux mois d'usage) là où l'A-stricte optimisait un besoin hypothétique — conformément à l'anti-tâche du plan d'action 001 : la décision bonne pour le projet maintenant, pas l'optimale en théorie. La réversibilité est totale : le front matter est une convention de rédaction à coût nul qui ouvre l'indexation future sans l'engager.

## 7. Conditions de révision

- **Besoin d'index avéré** : si des requêtes récurrentes sur le journal (fréquence hebdomadaire ou intégration aux audits) apparaissent, production d'un script d'indexation dérivé (markdown + front matter → JSON/SQLite). Ceci n'est pas une révision de la décision mais son application (§5, structure dérivée) ; à consigner au journal comme simple friction résolue.
- **Croissance du journal au-delà de la maniabilité d'un fichier unique** (~150 Ko ou navigation devenue coûteuse) : partition en fichiers par période ou par domaine (journal général, journaux de méthodes), régime append-only inchangé — nouvelle décision légère référençant celle-ci.
- **Écriture agentique** : si l'orchestration (décision 001) fait émerger un besoin d'entrées produites par agents (ex. audit automatique consigné), définition préalable d'un type d'entrée dédié et d'une validation humaine avant commit — nouvelle décision requise, celle-ci l'interdisant par défaut.

## 8. Conséquences immédiates

- Migration : aucune. Le journal existant est conforme ; seules les entrées futures adoptent le front matter.
- Vérification ponctuelle : contrôler que l'insertion de l'entrée 8.7 (décision 002) a bien été faite en append physique et non par réordonnancement du fichier — si réécriture il y a eu, la consigner comme friction au journal (sans réécrire à nouveau : append-only).
- `plan_action_002.md` : prévoir la convention de front matter dans `conventions.md` (`.claude/context/`), et le squelette du script d'indexation en anti-tâche explicite (ne pas le coder avant besoin avéré).
- Renforce le prérequis git : le régime append-only n'est vérifiable qu'au diff — `git init` sur `lentité/` reste bloquant pour le prototype.
- Inscription au journal méthodologique général comme entrée 8.8 (numérotation du plan d'action 001 §6).

---

*Décision 003 v1.0 — 3 juillet 2026. Append-only.*
