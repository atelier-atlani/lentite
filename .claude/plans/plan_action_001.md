# Plan d'action 001 — Phase 0 du codage — Cinq décisions structurantes

*Premier plan d'action du workflow `.claude/`. Produit en Mode Architecte (Claude.ai Opus 4.7). Adressé à Seb pour prise de cinq décisions structurantes avant engagement du codage substantiel de L'Entité.*

*Méta-information.*
- Date de production : 17 mai 2026.
- Mode opérationnel : Architecte.
- Mode cible d'exécution : Délibération humaine (Seb) — pas exécution IA classique.
- Plan référencé suivant attendu : `plan_action_002.md` (production du prototype technique Phase 0 après décisions prises).

---

## 1. Contexte

Le projet L'Entité a atteint à mai 2026 un état de consolidation doctrinale substantielle — sept analyses M01 sur cas réels, deux applications M03, trois cas-jouets, trois tests négatifs au pipeline. La doctrine v2.1.1 est stable. Le pipeline opérationnel minimal valide des analyses produites manuellement, mais le système opérationnel complet — production automatique d'analyses à partir de textes sources avec orchestration multi-agents — reste à coder.

La méthodologie de codage v1 (`dev/methodologie_codage_v1.md`) a identifié *cinq critères de maturité* pour engager le codage substantiel. *Quatre sur cinq sont satisfaits* — doctrine stable, méthodes éprouvées, schéma de validation opérationnel, ressources techniques disponibles. *Le cinquième critère — décisions architecturales structurantes — reste à valider.* C'est l'objet de ce plan d'action.

Le verrou stratégique du projet à mai 2026 est donc la prise de *cinq décisions structurantes* qui définissent l'architecture technique cible. Sans ces décisions, le codage substantiel (Phase 1 — pipeline monolithique texte → analyse M01-M) ne peut commencer rigoureusement.

Ce plan est *le premier cycle réel* de la méthode de workflow collaboratif IA mise en place dans `.claude/`. Il éprouve simultanément (a) la prise de décisions structurantes pour le codage, (b) la méthode de travail elle-même.

---

## 2. Objectif

**Prise par Seb des cinq décisions structurantes de la Phase 0 du codage**, avec documentation de chaque décision dans un fichier dédié dans `.claude/decisions/` selon le format du template `template_decision_structurante.md`.

---

## 3. Critères d'acceptation

- [ ] Cinq fichiers de décision produits dans `.claude/decisions/` —
  - `decision_001_orchestration_multi_agents.md`
  - `decision_002_persistance_graphe.md`
  - `decision_003_persistance_journal.md`
  - `decision_004_licence.md`
  - `decision_005_modele_distribution.md`
- [ ] Chaque décision respecte le format standardisé du template (huit sections — contexte, problème, options examinées, critères de décision, décision retenue, motif principal, conditions de révision, conséquences immédiates).
- [ ] Pour chaque décision, *option retenue avec motif explicite*.
- [ ] Pour chaque décision, *conditions de révision documentées*.
- [ ] Cohérence transversale des cinq décisions (les choix se renforcent ou ne se contredisent pas — par exemple, choisir AGPL + open source intégral est cohérent, mais Apache 2.0 + closed transitoire l'est moins).

---

## 4. Décisions à prendre

### 4.1 Décision 001 — Orchestration multi-agents

**Question.** Quel framework utiliser pour orchestrer l'architecture multi-agents anonymisés mentionnée dans la couche d'exécution v2 (à formaliser en v2.1.1) — quatre agents spécialisés selon la doctrine v2.1 (Charité, Vulnérabilités, Chaînes causales, Synthèse) ?

**Options examinées.**

*Option A — langgraph (LangChain Inc.).*
- Avantages : framework dédié à l'orchestration de graphes d'agents, écosystème mûr (sorti 2024, adopté par communauté), lisibilité du graphe d'exécution, support natif des LLM Anthropic via SDK.
- Inconvénients : couplage avec l'écosystème LangChain, courbe d'apprentissage si non familier, dépendance externe à maintenir à jour.
- Coût : faible (open source MIT).

*Option B — Custom Python.*
- Avantages : contrôle maximal sur l'orchestration, pas de dépendance externe, transparence totale pour audit, alignement parfait avec les besoins spécifiques de L'Entité.
- Inconvénients : effort de développement significatif, risque de réinventer la roue, maintenance à charge du projet.
- Coût : élevé en temps de développement initial, faible en runtime.

*Option C — LangChain agents (versions antérieures à langgraph).*
- Avantages : maturité, écosystème large.
- Inconvénients : architecture moins explicite que langgraph, considéré comme "legacy" par l'éditeur lui-même.
- Coût : faible.

**Critères de décision.**
- Lisibilité du graphe d'agents (essentielle pour transparence du projet L'Entité).
- Maintenance et stabilité de l'écosystème.
- Effort initial de développement vs effort de maintenance.
- Capacité d'audit (les décisions des agents doivent être traçables).

**Recommandation préliminaire — Option A (langgraph).** Motif — la lisibilité explicite du graphe d'agents est cohérente avec la discipline de transparence du projet, l'écosystème est désormais mûr et stable, et le couplage avec LangChain peut être limité à la couche d'orchestration sans contamination du cœur métier (architecture hexagonale). L'option Custom (B) est conservée comme option de repli si langgraph s'avère insuffisamment transparent à l'usage.

### 4.2 Décision 002 — Persistance graphe cognitif

**Question.** Quel système de persistance utiliser pour le graphe cognitif — nœuds (Acteurs, Propositions, Objets thématiques, Objets visés, Unités argumentatives, Cadres, Effets) et arêtes (relations typées selon `ArenaRelationType` et autres) issus des analyses M01 et M03 ?

**Options examinées.**

*Option A — Neo4j Community Edition.*
- Avantages : mature (depuis 2007), requêtes Cypher puissantes et lisibles, écosystème graphe le plus large, outils de visualisation natifs.
- Inconvénients : licence GPLv3 pour Community Edition (impose copyleft fort sur les modifications) ; restrictions Enterprise sur replication, sharding au-delà d'une certaine taille ; modèle de prix Enterprise contraignant à terme.
- Coût : gratuit en Community, contraintes futures si scale.

*Option B — PostgreSQL + Apache AGE.*
- Avantages : PostgreSQL est largement déployé et maintenu, Apache AGE (Apache Graph Extension) ajoute le support Cypher à PostgreSQL, licence Apache 2.0 (permissive), versatilité SQL + graphe dans le même système.
- Inconvénients : écosystème moins mûr que Neo4j (AGE est plus récent), outils de visualisation moins matures, performance graphe peut-être en-dessous de Neo4j sur très grands volumes.
- Coût : gratuit.

*Option C — Stockage hybride (fichiers + index).*
- Avantages : simplicité, lisibilité humaine des données.
- Inconvénients : requêtes graphe complexes difficiles, performance limitée.
- Coût : faible.

**Critères de décision.**
- Compatibilité avec licence open source permissive (Apache 2.0 cible préliminaire — voir décision 004).
- Versatilité (capacité à faire à la fois requêtes SQL et graphe).
- Effort d'adoption pour l'équipe.
- Pérennité de l'écosystème.

**Recommandation préliminaire — Option B (PostgreSQL + Apache AGE).** Motif — la cohérence de licence avec le projet (Apache 2.0 préférable à GPLv3), la versatilité SQL + graphe pour les besoins mixtes du projet (analyses, journal indexé, requêtes statistiques pour audits), et l'écosystème PostgreSQL plus stable à long terme. Neo4j (A) est conservée comme option si AGE s'avère insuffisamment mature à l'usage et si les contraintes GPLv3 sont acceptables.

### 4.3 Décision 003 — Persistance du journal méthodologique

**Question.** Comment persister les entrées du journal méthodologique général et des journaux propres aux méthodes — append-only, datées, requêtables, lisibles humainement ?

**Options examinées.**

*Option A — Git + JSON structuré indexé.*
- Avantages : versioning natif via Git, lisibilité humaine des fichiers JSON, indexation périodique pour requêtes (par exemple Elasticsearch ou index custom), cohérence avec la pratique Git existante du projet.
- Inconvénients : requêtes ad hoc moins immédiates qu'une base de données, index à maintenir séparément.
- Coût : faible (Git + script d'indexation).

*Option B — Base de données avec event sourcing (par exemple PostgreSQL avec table append-only).*
- Avantages : requêtable directement, intégration native avec le graphe cognitif (décision 002), atomicité des écritures.
- Inconvénients : moins lisible humainement (sauf via outils), couplage avec la décision 002, complexité de migration.
- Coût : modéré.

*Option C — Hybride Git pour traces humaines + DB pour index.*
- Avantages : lisibilité humaine + requêtabilité.
- Inconvénients : duplication des données, synchronisation à maintenir.
- Coût : modéré.

**Critères de décision.**
- Discipline append-only respectée (le journal ne se modifie pas).
- Lisibilité humaine (essentielle pour audit doctrinal).
- Capacité à supporter les audits inscrits au gabarit v2.1.1 (`intentionality_bias_audit`, `hypothesis_gap_audit`, `typology_audit`).
- Cohérence avec la pratique Git du projet.

**Recommandation préliminaire — Option A (Git + JSON structuré indexé).** Motif — la lisibilité humaine native de Git (chaque entrée est un commit signable et auditable), la cohérence avec la doctrine append-only du projet, et l'indexation séparée qui permet d'exposer les audits sans couplage rigide avec la base de données du graphe. L'Option C (hybride) reste une voie d'évolution si les besoins de requête deviennent intensifs.

### 4.4 Décision 004 — Licence open source

**Question.** Quelle licence appliquer au code source de L'Entité — détermine les modalités de réutilisation, de modification, de distribution commerciale, et la stratégie de protection.

**Options examinées.**

*Option A — MIT.*
- Avantages : permissive maximale, adoption la plus large possible, simplicité juridique.
- Inconvénients : pas de protection contre l'appropriation propriétaire (un acteur peut forker, modifier, et vendre en closed-source sans contribuer en retour) ; pas de protection brevets.

*Option B — Apache 2.0.*
- Avantages : permissive avec protection brevets explicite (un contributeur ne peut pas attaquer en brevets sur sa contribution), large adoption en entreprise, compatibilité avec la plupart des autres licences.
- Inconvénients : aucun copyleft (un acteur peut réutiliser sans contribuer en retour).

*Option C — AGPLv3.*
- Avantages : copyleft fort (les modifications utilisées en service en ligne doivent être partagées), protection contre l'appropriation propriétaire.
- Inconvénients : adoption plus limitée en entreprise (certaines politiques internes interdisent AGPL), incompatibilité avec certains autres écosystèmes.

**Critères de décision.**
- Volonté politique du projet (engagement à la transparence vs adoption la plus large).
- Modèle économique cible (open source pur, distribution duale, freemium).
- Alignement avec la philosophie L'Entité (transparence, dévoilement, vérité partagée).
- Précédents dans l'écosystème AI open source.

**Recommandation préliminaire — Option B (Apache 2.0).** Motif — équilibre entre permissivité (adoption large possible, y compris commerciale) et protection (clause brevets explicite). Cohérent avec les outils utilisés (PostgreSQL + AGE en Apache 2.0). Cohérent avec un modèle de distribution duale (code source ouvert, service Mode 2 sous contrat séparé). Option C (AGPL) reste pertinente si volonté politique forte d'imposer le partage des modifications utilisées en service, mais réduirait l'adoption.

### 4.5 Décision 005 — Modèle de distribution

**Question.** Comment distribuer L'Entité aux différents publics — analystes (Mode 1), distribution restreinte (Mode 2), chat public (Mode 3) ?

**Options examinées.**

*Option A — Open source complet dès le départ.*
- Avantages : transparence maximale, communauté ouverte, alignement philosophique fort avec L'Entité.
- Inconvénients : pas de modèle économique direct, dépendance aux contributions volontaires et subventions, risque de fork compétitif.

*Option B — Distribution duale.*
- Avantages : code source public (Phase 2+), accès au service Mode 2 sous contrat ou abonnement, modèle économique viable, philosophie préservée (le code est ouvert, le service est contractuel).
- Inconvénients : complexité juridique de la dualité, risque de critiques sur la "monétisation" du service.

*Option C — Closed transitoire (open source à maturité).*
- Avantages : protège l'avantage compétitif pendant phase opérationnelle initiale, modèle économique direct.
- Inconvénients : contredit l'engagement de transparence, retarde l'écosystème, risque de "vendor lock-in" perçu.

**Critères de décision.**
- Alignement philosophique avec L'Entité.
- Viabilité économique.
- Vitesse d'adoption par les analystes (Mode 1).
- Articulation avec la décision 004 (licence).

**Recommandation préliminaire — Option B (Distribution duale).** Motif — préserve l'engagement de transparence (code source public sous Apache 2.0 dès Phase 2), permet un modèle économique viable via le service Mode 2 sous contrat, et reste cohérent avec la trajectoire entrepreneuriale du porteur (Studio ee). Option A (open source complet) reste possible si financement par subventions / fondations est sécurisé. Option C (closed transitoire) est rejetée — incompatible avec la philosophie du projet.

---

## 5. Anti-tâches

- *Ne pas commencer le codage substantiel* (Phase 1 pipeline monolithique) avant que les cinq décisions soient prises et documentées.
- *Ne pas surdéterminer chaque décision par anticipation des suivantes*. Chaque décision est examinée sur ses propres critères, puis la cohérence transversale est vérifiée.
- *Ne pas confondre Recommandation préliminaire et décision finale*. Les recommandations préliminaires sont des points de départ pour la délibération, pas des conclusions imposées.
- *Ne pas chercher la décision optimale en théorie* — chercher la décision *bonne pour le projet à mai 2026* avec les ressources et la trajectoire actuels.

---

## 6. Output attendu

- *Cinq fichiers de décision* produits dans `.claude/decisions/` selon le format du template `template_decision_structurante.md`.
- *Décisions communiquées en retour à Mode Architecte* (session suivante de Claude.ai) pour validation de cohérence transversale et production de `plan_action_002.md` (prototype technique Phase 0).
- *Inscription au journal méthodologique général* des cinq décisions comme entrées 8.6, 8.7, 8.8, 8.9, 8.10 (à la prochaine révision du journal).

---

## 7. Modèle recommandé

- *Délibération de Seb* (pas de modèle IA en exécution directe pour ce plan).
- *Optionnel — Claude.ai Opus 4.7 (Mode Architecte) en sparring partner* sur une ou plusieurs décisions si tu veux examiner plus en profondeur des options ou en discuter avant de trancher. Une session de discussion par décision est possible.

---

## 8. Estimation

- *Durée* — variable selon ton temps de délibération. Estimation conservative — 2-4 heures cumulées pour cinq décisions, avec ou sans sparring partner.
- *Coût marginal* — faible (peu d'API si pas de sparring partner ; modéré si plusieurs sessions de discussion avec Claude.ai).
- *Délai recommandé* — décisions prises sous une semaine pour ne pas perdre la dynamique du projet.

---

## 9. Discipline d'exécution

- *Une décision à la fois.* Pas de production simultanée des cinq décisions — chacune mérite délibération.
- *Premières décisions plus structurantes pour les suivantes.* Recommandation d'ordre — décision 004 (licence) en premier car elle conditionne 002, 003, 005 ; ensuite 002 (persistance graphe), 003 (persistance journal), 005 (distribution), 001 (orchestration) qui est la plus technique et la moins liée aux autres.
- *Documenter même les décisions évidentes.* Le format est exhaustif pour permettre l'audit et la révision ultérieure.
- *Append-only sur les décisions.* Une décision validée n'est pas modifiée — si révision nécessaire, nouvelle décision avec référence à la précédente.

---

*Plan d'action 001 v1.0 — produit le 17 mai 2026 par Mode Architecte. À placer dans `.claude/plans/plan_action_001.md`. Prochain plan attendu — `plan_action_002.md` (prototype technique Phase 0) après prise des décisions.*
