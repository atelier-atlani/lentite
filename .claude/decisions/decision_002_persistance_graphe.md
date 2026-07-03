# Décision 002 — Persistance du graphe cognitif

*Décision structurante Phase 0 du codage. Prise en délibération avec sparring partner (Claude.ai, Mode Architecte/sparring). Référence : `plan_action_001.md` §4.2. Append-only — toute révision fera l'objet d'une nouvelle décision référençant celle-ci.*

*Méta-information.*
- Date de décision : 3 juillet 2026.
- Décideur : Seb (Dirigeant).
- Statut : validée.
- Décisions liées : cohérente avec 004 (licences Apache 2.0/BSD des composants retenus) ; conditionne 003 (le principe fichiers-source-de-vérité s'y applique symétriquement) ; contraint 001 (l'orchestration écrit des YAML validés, jamais directement dans le graphe).

---

## 1. Contexte

Le graphe cognitif est la mémoire structurée de L'Entité : nœuds (Acteurs, Propositions, Objets thématiques, Objets visés, Unités argumentatives, Cadres, Effets) et arêtes typées (`ArenaRelationType` et autres) issus des analyses M01 et M03. À juillet 2026, le corpus validé compte sept analyses M01, deux applications M03 et trois cas-jouets — soit un volume de l'ordre de quelques centaines de nœuds et arêtes, appelé à croître d'une dizaine d'analyses avec le dossier zéro rétrospectif. La persistance existante de fait est constituée des fichiers YAML validés par les schémas Pydantic (`schemas.py`, `schemas_m03.py`), destinés au versionnage git.

## 2. Problème

Le plan d'action 001 posait la question comme un choix de moteur de base de données. La délibération a reformulé le problème un cran plus haut : qui est la source de vérité ? Une base de graphe alimentée directement (par humain ou par agent) crée un état non auditable ligne à ligne, non diffable, non signable — en contradiction avec la doctrine (traçabilité P7, auditabilité comme contrainte constitutive). Par ailleurs, choisir et opérer un serveur de base de données pour un volume de quelques centaines d'éléments constitue de l'infrastructure avant le besoin, contraire à l'anti-tâche du plan (« la décision bonne pour le projet maintenant, pas l'optimale en théorie »).

## 3. Options examinées

**Option A — PostgreSQL + Apache AGE immédiat** (recommandation préliminaire du plan).
Cible techniquement correcte (versatilité SQL + Cypher, licence Apache 2.0 cohérente avec la décision 004). Mais prématurée : coût d'installation, d'opération et de maintenance dès la Phase 0 pour un volume qui ne le justifie pas ; écosystème AGE encore étroit (visualisation pauvre, communauté restreinte) ; et surtout, ne répond pas à la question de la source de vérité — une base alimentée directement resterait non auditable.

**Option B — Principe fichiers-source-de-vérité + graphe dérivé** (retenue).
Les YAML validés dans git sont l'unique source de vérité. Le graphe est une vue dérivée, reconstructible à tout moment par rejeu du corpus. Implémentation Phase 0-1 : module `graph_builder.py` ingérant les YAML validés vers NetworkX (Python pur, licence BSD, zéro serveur), avec exports GraphML/JSON pour visualisation et audits. Bascule vers PostgreSQL + AGE sur seuils documentés (§7).

**Option C — Neo4j Community.**
Écartée : GPLv3 gérable en composant serveur non modifié, mais politique de pricing Enterprise hostile à terme, et aucun apport à l'échelle actuelle que l'option B ne fournisse.

## 4. Critères de décision

- Auditabilité : chaque assertion du graphe doit remonter à un fichier commité, daté, diffable (doctrine P7).
- Réversibilité : le choix d'outil de graphe doit pouvoir être défait sans migration de données.
- Discipline anti-corruption : aucune écriture directe dans le graphe — humains et agents produisent des YAML qui passent le validateur, puis sont ingérés.
- Proportionnalité : pas d'infrastructure avant le besoin (anti-tâche du plan d'action 001 §5).
- Cohérence de licences avec la décision 004 (NetworkX BSD, PostgreSQL/AGE Apache 2.0 : conformes).

## 5. Décision retenue

**Option B**, en deux volets indissociables :

**Volet 1 — Principe architectural** (permanent, indépendant de tout outil).
Les fichiers YAML validés et versionnés dans git sont la source de vérité unique du graphe cognitif. Le graphe est une vue dérivée, jetable et reconstructible par rejeu intégral du corpus. Aucune écriture directe dans le graphe n'est autorisée, par aucun acteur humain ou logiciel.

**Volet 2 — Implémentation séquencée.**
- Phase 0-1 : `graph_builder.py` (YAML validés → NetworkX), exports GraphML/JSON, visualisation via Gephi ou vue web légère. Les audits du gabarit (`intentionality_bias_audit`, `hypothesis_gap_audit`, `typology_audit`) sont implémentés comme parcours du graphe NetworkX.
- Phase ultérieure : bascule vers PostgreSQL + Apache AGE lorsque les seuils du §7 sont franchis. La migration se réduit à pointer l'ingesteur vers Postgres et rejouer le corpus — conséquence directe du volet 1.

## 6. Motif principal

Le principe fichiers-source-de-vérité transforme le choix de moteur de graphe, décision lourde et engageante, en décision légère et réversible — tout en satisfaisant mieux la doctrine qu'aucune base de données : l'auditabilité est native (git), la corruption structurellement impossible (validateur en unique porte d'entrée), la réversibilité totale (le graphe se jette et se reconstruit). C'est la matérialisation technique de la phrase-cœur du projet : la vérité est dans la qualité du chemin — ici, le chemin de chaque assertion jusqu'à son commit d'origine.

## 7. Conditions de révision

Bascule vers PostgreSQL + Apache AGE (cible confirmée, sauf réexamen) lorsque l'un de ces seuils est franchi et documenté au journal :

- Corpus dépassant ~50 analyses validées, ou temps de rejeu complet excédant 60 secondes sur machine de développement.
- Besoin de requêtes concurrentes multi-utilisateurs (déploiement Mode 1 en service).
- Besoin de requêtes croisées SQL + graphe pour les audits statistiques, non couvrables raisonnablement en NetworkX/pandas.

Réexamen du choix AGE lui-même si, au moment de la bascule, l'écosystème AGE a régressé (maintenance, compatibilité versions PostgreSQL) — alternatives à évaluer alors : Oxigraph/RDF si le besoin de raisonnement formel a mûri (cf. horizon neurosymbolique de la doctrine), Neo4j si les contraintes de licence sont réévaluées.

## 8. Conséquences immédiates

- La décision 003 (persistance journal) hérite du même principe : git append-only comme source de vérité, index dérivé — l'option A du plan devient l'évidence cohérente.
- La décision 001 (orchestration) est contrainte : les agents produisent des YAML candidats soumis au validateur ; aucun agent n'écrit dans le graphe. Le graphe est en lecture seule pour l'orchestration.
- `plan_action_002.md` devra spécifier `graph_builder.py` (ingestion YAML → NetworkX, exports, premiers audits comme parcours de graphe).
- Dépendances à ajouter au prototype : `networkx` (BSD). Aucune infrastructure serveur en Phase 0-1.
- Renforce l'urgence de l'hygiène git : le principe fichiers-source-de-vérité présuppose un repo — `git init` sur `lentité/` est un prérequis bloquant du prototype.
- Inscription au journal méthodologique général comme entrée 8.7 (numérotation du plan d'action 001 §6).

---

*Décision 002 v1.0 — 3 juillet 2026. Append-only.*
