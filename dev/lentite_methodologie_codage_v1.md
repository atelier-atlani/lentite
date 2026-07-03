# Méthodologie de codage du projet L'Entité

*Document de plan pour le passage du projet documentaire au système opérationnel complet. Répond aux deux questions structurantes — quand commencer à coder, comment procéder. Adressé au porteur principal du projet. Document factuel et opérationnel.*

---

## 1. État actuel du codage

**Ce qui existe déjà.** Pipeline minimal Python (~4500 lignes au total) en `pipeline/` du projet archivé :

— `schemas.py` (39 modèles Pydantic v2 pour M01 v2.1) — schéma normatif des sorties machine M01-M.
— `schemas_m03.py` (22 modèles Pydantic v2 pour M03 v2.1) — schéma normatif des sorties machine M03-M.
— `validate.py` et `validate_m03.py` — validateurs CLI avec rapports structurés et messages d'erreur référençant les sections du gabarit.
— Huit YAML M01-M validés + un YAML M03-M à 4 acteurs validé.
— Trois YAML de tests négatifs validés (contraintes critiques mordantes confirmées).

**Ce qui manque pour le système opérationnel complet.**

— *Orchestration multi-agents* — implémentation des quatre agents anonymisés mentionnés dans la couche d'exécution v2 (à réécrire en v2.1.1).
— *Persistance* — graphe cognitif + journal versionné. Choix technique non encore fait (Neo4j vs PostgreSQL+AGE).
— *Pipelines d'inférence* — appels LLM orchestrés pour produire M01-M, M03-M, M01-P depuis textes sources. Le pipeline actuel valide les YAML *à partir d'analyses humaines manuelles*, pas à partir de production automatique.
— *Module Elenchus* d'examen de la requête (étape préalable à toute application de méthode, charte v2.1 section 7).
— *Interfaces* — selon mode opérationnel (Mode 1 analystes, Mode 2 distribution restreinte, Mode 3 chat public).
— *Gestion des régimes d'exécution* (`applicable_complete`, `applicable_degraded`, `applicable_vigilance_adversariale`, `not_applicable`).
— *Tests d'intégration* — actuellement tests unitaires de validation, pas tests de pipeline complet texte → analyse.

Le pipeline actuel représente probablement 5 à 10% du codage nécessaire pour le système opérationnel complet.

---

## 2. Critères de maturité pour commencer le codage

Cinq critères. Cocher avant chaque phase.

**Critère 1 — Doctrine suffisamment stable.** Le code ne doit pas être réécrit à chaque révision majeure de la doctrine. *État* — doctrine v2.1.1 stable, refonte majeure v3 reportée à après accumulation d'analyses. ✓

**Critère 2 — Méthodes principales éprouvées.** Les méthodes que le code instrumente doivent avoir été éprouvées sur cas réels. *État* — M01 v2.1 éprouvée sur cinq cas réels et trois cas-jouets, M03 v2.1 éprouvée sur une application à quatre acteurs. ✓

**Critère 3 — Schéma de validation opérationnel.** Le pipeline doit pouvoir valider les sorties produites par le code. *État* — schemas Pydantic + validateurs existants et testés. ✓

**Critère 4 — Décisions architecturales structurantes prises.** Avant codage d'une brique structurante, la décision technique doit être prise et documentée. *État* — *partiellement*. Décisions prises — Python 3.11+, Pydantic 2.13+, API Anthropic. Décisions non prises — modèle d'orchestration multi-agents (langgraph, custom, autre), choix graphe (Neo4j vs PostgreSQL+AGE), modèle de persistance du journal (Git + JSON, base de données, hybride), modèle de licence, modèle de distribution.

**Critère 5 — Ressources techniques disponibles.** Équipe (peut être un dev seul), budget API LLM, infrastructure de déploiement. *État* — à confirmer par Seb selon trajectoire entrepreneuriale.

**Verdict sur le démarrage.** Trois critères sur cinq satisfaits. Les critères 4 et 5 demandent décisions explicites. *Recommandation* — Phase 0 (préparation, prises de décision, prototype technique de validation) peut commencer immédiatement. Phases 1 et suivantes attendent les décisions de la Phase 0.

---

## 3. Réponse à la question — quand commencer à coder

**Maintenant pour la Phase 0** (préparation, décisions architecturales, prototype technique minimal). Conditions satisfaites — doctrine stable, méthodes éprouvées, schéma de validation opérationnel.

**Après Phase 0 pour les Phases 1-4** (architecture multi-agents, persistance avancée, interfaces, déploiement). Conditions à satisfaire — décisions architecturales prises et documentées.

**Pas avant accumulation supplémentaire pour la Phase 5** (refonte v3 — génération M01-P automatique, audit typologies automatique, graphe cognitif intégré). Conditions à satisfaire — accumulation de 15-25 analyses M01 supplémentaires pour audits inscrits au gabarit v2.1.1, plus retour d'expérience opérationnel des Phases 1-4.

**Logique.** Le codage commence quand la doctrine est mûre, jamais avant. Le projet a investi six mois (estimation à partir des dates documentées) dans la doctrine et les analyses validantes. Cet investissement est la condition de robustesse du code à venir. Le codage prématuré aurait demandé refonte successive à chaque révision doctrinale — perte de temps massive.

---

## 4. Séquence des phases recommandée

### Phase 0 — Préparation (1-2 semaines)

*Objectif* — prendre les décisions structurantes, préparer environnement et outils, produire un prototype technique de validation. Sans Phase 0, le risque de réécriture en cours de Phase 1 est élevé.

*Livrables*.

— *Document "Couche d'exécution v2.1.1"* qui remplace la couche d'exécution v2 obsolète. Spécifie l'architecture technique cible avec décisions arrêtées sur orchestration multi-agents, choix graphe, modèle de persistance, modèle de licence, modèle de distribution.

— *Prototype technique minimal de pipeline complet* — un script Python qui prend un texte source en entrée, applique un appel LLM unique, produit une analyse M01-M conforme au schéma Pydantic, sans orchestration multi-agents ni persistance. Vise à valider que la chaîne *texte → analyse M01-M validée* fonctionne techniquement. Aucune ambition d'analyse réellement opérationnelle — c'est un *spike technique* pour confirmer la faisabilité.

— *Plan de codage détaillé Phase 1-4* avec estimations temporelles, livrables, critères d'acceptation, dépendances.

*Décisions à prendre.*

— *Orchestration multi-agents.* Options examinées — (a) langgraph (graphe d'agents avec routage explicite, écosystème mûr), (b) custom (orchestrateur Python pur, contrôle maximal, complexité de développement), (c) langchain agents (mature mais plus opaque). *Recommandation préliminaire* — langgraph pour la lisibilité du graphe d'agents et l'écosystème mûr, custom seulement si contrainte forte de transparence et d'audit.

— *Persistance du graphe cognitif.* Options examinées — (a) Neo4j Community (mature, requêtes Cypher, écosystème mûr, mais licence GPLv3 pour la version communautaire et restrictions enterprise), (b) PostgreSQL + Apache AGE (open source plus permissif, SQL + Cypher hybride, écosystème moins mûr). *Recommandation préliminaire* — PostgreSQL + AGE pour la cohérence avec licence open source du projet si retenue, et la versatilité SQL + graphe.

— *Persistance du journal.* Options examinées — (a) Git pur (versioning natif, lisibilité humaine, mais difficile à requêter), (b) base de données avec event sourcing (requêtable, plus complexe), (c) hybride Git + index requêtable. *Recommandation préliminaire* — Git + JSON structuré pour les entrées du journal, indexé périodiquement pour requêtes. Bénéficie de la traçabilité native de Git et reste lisible humainement, cohérent avec la doctrine du journal append-only.

— *Modèle de licence.* Options examinées — (a) MIT (permissive maximale), (b) Apache 2.0 (permissive avec protection brevets), (c) AGPL (copyleft fort, force le partage des modifications utilisées en service). *Recommandation préliminaire* — Apache 2.0 pour permettre l'usage commercial et académique tout en protégeant contre l'extraction des contributions par brevet. AGPL si volonté politique forte de garantir le partage des modifications.

— *Modèle de distribution.* Options examinées — (a) open source complet dès le départ (Modes 1, 2, 3 publiquement accessibles), (b) distribution duale (code source public, accès Mode 2 restreint contractuellement), (c) closed pendant phase opérationnelle, open source au moment de la maturité. *Recommandation préliminaire* — distribution duale. Le code source est public dès Phase 2, l'accès au service Mode 2 (analyses approfondies, contextes sensibles) reste sous contrat ou abonnement. Cohérent avec la charte v2.1 section 8.2.

*Outillage à mettre en place.*

— Git repository avec branches structurées (`main`, `develop`, `feature/*`).
— Environnement Python 3.11+ avec virtualenv.
— Pytest pour tests unitaires et tests d'intégration.
— Pre-commit hooks pour formatage (black, ruff, mypy).
— GitHub Actions ou GitLab CI pour CI/CD minimaliste.
— Anthropic SDK Python configuré avec API key.
— Pour Seb spécifiquement — utiliser Claude Code en CLI pour développement assisté (déjà documenté dans les mémoires comme outil de prédilection).

### Phase 1 — Pipeline texte → analyse M01-M validée avec agent unique (3-5 semaines)

*Objectif* — produire une chaîne complète qui transforme un texte source en analyse M01-M validée, avec un agent LLM unique (pas encore multi-agents). Valide la faisabilité fonctionnelle de bout en bout.

*Livrables.*

— *Module Elenchus* d'examen de la requête (charte v2.1 section 7). Vérifications mécaniques — identifiabilité du locuteur, intégrité du texte, mesure de surcharge contextuelle, détection lexicale de termes des cadres disqualifiés. Pré-verdict sur le mode d'exécution.

— *Pipeline M01 v2.1 monolithique* — script Python qui (a) reçoit un texte source, (b) appelle Elenchus, (c) appelle l'API Anthropic avec prompt complet du gabarit, (d) parse la réponse YAML, (e) valide contre `schemas.py`, (f) sauvegarde en fichier YAML + génère la version M01-H markdown.

— *Tests d'intégration* sur les cinq cas réels existants (Fabius, Ciotti, Lecornu, Vallaud, Panot). Compare les sorties produites par le pipeline avec les analyses humaines validées. Documente les écarts.

— *Génération M01-P automatique* — appel LLM léger (Sonnet 4.6 ou Haiku) qui prend un M01-M validé en entrée et produit la sortie publique 150-300 mots avec validation par schéma (longueur, présence des cinq éléments, absence de termes évaluatifs non marqués).

*Critères d'acceptation Phase 1.*

— Le pipeline produit des M01-M qui valident contre `schemas.py` sur 100% des essais.
— Les écarts entre M01 humaines et M01 pipeline sont documentés et expliqués (sans nécessairement être nuls — les analyses humaines bénéficient d'inférences contextuelles que le pipeline ne reproduit pas nécessairement).
— Le temps de production d'une M01 par le pipeline est inférieur à 5 minutes (avec API Opus 4.7) ou 2 minutes (Sonnet 4.6).
— Le coût API par M01 produite est documenté et estimé inférieur à 0,50 € par analyse en Sonnet 4.6 / 2 € par analyse en Opus 4.7.

### Phase 2 — Architecture multi-agents anonymisés (4-6 semaines)

*Objectif* — implémenter les quatre agents anonymisés mentionnés dans la couche d'exécution v2 (à formaliser en v2.1.1) avec orchestration explicite. Le pipeline monolithique de Phase 1 est décomposé en agents spécialisés.

*Architecture indicative à valider en Phase 0.*

— *Agent 1 — Charité* — produit la reconstruction charitable de l'argument principal (gabarit v2.1 section 6.1-6.2). Modèle léger (Sonnet 4.6) avec prompt spécialisé.

— *Agent 2 — Vulnérabilités et omissions* — identifie les vulnérabilités argumentatives et omissions par unité (gabarit v2.1 sections 5.4-5.5). Modèle plus capable (Opus 4.7) parce que la tâche demande analyse logique fine.

— *Agent 3 — Chaînes causales et bloc V* — produit les chaînes amont et aval, identifie les engagements vérifiables, recherche les effets observables (web_search activé). Opus 4.7.

— *Agent 4 — Synthèse épistémique et Red Team* — produit la synthèse en trois statuts épistémiques, formule les hypothèses concurrentes, applique le red teaming. Opus 4.7 avec instructions explicites de défense de l'hypothèse non intentionnelle dominante (gabarit v2.1.1 — intentionality_bias_audit).

*Orchestrateur* — coordonne les agents, gère les dépendances (l'agent 2 dépend de l'agent 1, etc.), agrège les résultats en M01-M conforme au schéma. Implémenté en langgraph (recommandation Phase 0).

*Anonymisation des agents.* Chaque agent ne connaît que son rôle et les éléments du texte source nécessaires à sa tâche. Pas de partage d'identité des autres agents. Conforme à la doctrine d'autonomie épistémique du projet (charte v2.1 — éviter la dépendance à une instance LLM unique).

*Livrables Phase 2.*

— Quatre prompts d'agents spécialisés, validés par tests sur cas réels.
— Orchestrateur langgraph avec graphe d'exécution documenté.
— Tests d'intégration multi-agents sur les cinq cas réels existants.
— Métriques de qualité — concordance avec analyses humaines, temps de production, coût.

*Critère d'acceptation Phase 2 critique.* La M01-M produite par le pipeline multi-agents est *au moins aussi bonne* que celle du pipeline monolithique de Phase 1, mesurée par concordance avec les analyses humaines validées. Si elle est moins bonne, retour à Phase 1 avec optimisation du prompt monolithique avant orchestration multi-agents.

### Phase 3 — Persistance avancée — graphe cognitif et journal versionné (4-6 semaines)

*Objectif* — passer de la persistance fichier (YAML + Markdown) à la persistance structurée (graphe + journal indexé) pour permettre les requêtes complexes inter-analyses et l'audit.

*Livrables.*

— *Sérialiseur YAML → graphe cognitif* — convertit les analyses M01-M et M03-M en nœuds et arêtes Cypher/AGE. Nœuds — Acteur, Proposition, ObjetThématique, ObjetVisé, UnitéArgumentative, Cadre, Effet. Arêtes — typées selon `ArenaRelationType` et autres relations du gabarit.

— *Indexeur du journal méthodologique* — parse les entrées du journal en JSON structuré, les indexe pour requêtes (par méthode, par catégorie d'entrée, par date, par référence à un cas).

— *Module de requêtes inter-analyses* — interface qui permet de requêter le graphe pour audits transversaux. Exemple — "lister tous les cas où le pattern `broken_explicitly` a été identifié et leur taux d'observation des prédictions".

— *Migrations doctrinales* — système de migration des analyses persistées quand la doctrine évolue (v2.1.1 → v2.2 → v3). Important pour ne pas perdre l'historique.

— *Implémentation des audits automatiques* — `intentionality_bias_audit` et `hypothesis_gap_audit` du gabarit v2.1.1 deviennent des requêtes sur le graphe + journal indexé.

### Phase 4 — Interfaces et déploiement (durée variable selon ambition)

*Objectif* — exposer le système aux utilisateurs cibles selon les trois modes opérationnels.

*Livrables minimaux pour Mode 1 (analystes).*

— API REST authentifiée pour soumission de texte source et récupération d'analyse.
— Interface analyste — soit terminal CLI étendu, soit interface web minimaliste (FastAPI + frontend léger).
— Système de stockage des analyses pour consultation ultérieure.
— Système d'audit des décisions humaines (mode d'exécution validé par l'humain).

*Livrables additionnels pour Mode 2 (distribution restreinte).*

— Contrôle d'accès contractuel.
— Logging et audit renforcés pour conformité réglementaire éventuelle.
— Modes d'analyse étendus (M02 lecture indiciaire si retenue prioritaire).

*Livrables additionnels pour Mode 3 (chat public).*

— Interface conversationnelle avec gestion de session.
— Module Elenchus renforcé pour examen des requêtes utilisateur final.
— Garde-fous de sécurité (gestion de la charge éthique, refus de cas inappropriés).
— Modération et journal des refus.

*Décision en Phase 0* — quel mode déployer en priorité ? Recommandation préliminaire — Mode 1 d'abord (analystes professionnels), Mode 2 ensuite (selon partenariats), Mode 3 plus tard (demande modération substantielle).

### Phase 5 — Refonte v3 (après accumulation)

*Objectif* — refonte majeure qui invalide la rétrocompatibilité v2.1.1. À engager après accumulation de 15-25 analyses supplémentaires et retour d'expérience opérationnel des Phases 1-4.

Pas planifiée à ce stade. Inscrite comme objectif lointain.

---

## 5. Disciplines transversales (à toutes les phases)

### 5.1 Architecture

*Pattern recommandé* — architecture hexagonale (ports et adaptateurs). Le cœur métier (méthodes M01, M03, etc.) est isolé des détails techniques (API LLM, persistance, interfaces). Permet de remplacer une implémentation technique (par exemple Anthropic API par un autre fournisseur) sans toucher au cœur métier.

*Couches.*

— *Domaine* — modèles Pydantic des sorties (existants), logique de validation, doctrine encodée.
— *Application* — services qui orchestrent les méthodes (M01Service, M03Service, ElenchusService).
— *Infrastructure* — adaptateurs vers API LLM, persistance, interfaces utilisateur.

### 5.2 Tests

*Tests unitaires* sur le cœur métier — schemas, validators, logique de classification. Couverture cible 80% minimum.

*Tests d'intégration* sur le pipeline complet — sur les cas réels existants. Couverture comparative — chaque analyse produite par le pipeline est comparée à l'analyse humaine validée correspondante.

*Tests de régression* à chaque release. Le pipeline doit produire des analyses au moins aussi bonnes que la version précédente sur les cas références.

*Tests négatifs* étendus — chaque contrainte mordante du gabarit doit avoir un test négatif validant son rejet.

### 5.3 Versionning Git

*Convention de commit* — Conventional Commits (feat, fix, docs, refactor, test, chore). Permet le changelog automatique.

*Branches* — `main` (production stable), `develop` (intégration), `feature/*` (développements isolés), `release/*` (préparation de release).

*Tags* — semver strict. Compatible avec les versions de la doctrine (v0.1.0 → v0.2.0 quand Phase 1 livrée, v1.0.0 quand Phase 4 livrée et Mode 1 opérationnel).

### 5.4 Documentation au fil du codage

*Docstrings* obligatoires sur tout module exposé (fonctions, classes, méthodes). Format Google ou NumPy.

*README technique* maintenu à jour à chaque phase. Distinct du README du projet (qui couvre la doctrine et les analyses). Le README technique couvre installation, configuration, usage technique.

*Journal de développement* — entries au fil du codage qui documentent les décisions techniques significatives, les frictions résolues, les choix architecturaux. Distinct du journal méthodologique général (qui couvre la doctrine). Inscrit dans `dev_journal.md` à la racine du repo technique.

### 5.5 CI/CD minimaliste

*CI au minimum* — sur chaque pull request, lance tests unitaires + linter + type checking.

*CD reporté* — déploiement manuel jusqu'à Phase 4 minimum. Pas de déploiement automatique tant que le système n'est pas opérationnel pour utilisateurs réels.

### 5.6 Sécurité et audit des outputs

*Audit du contenu produit par les agents* — tous les outputs LLM passent par un validator avant sortie utilisateur. Détection de — fuites de prompt, hallucinations factuelles évidentes, contenu éthiquement problématique non signalé.

*Anonymisation des données* — les analyses sur cas réels peuvent contenir des références identifiables. Le système doit permettre soit conservation (Mode 1 analystes professionnels) soit anonymisation partielle (Mode 3 chat public).

*Audit des coûts API* — surveillance du coût par analyse, alertes si dépassement.

### 5.7 Conformité doctrinale maintenue

*À chaque release.*

— Tous les YAML d'analyses produites par le pipeline validés contre les schemas Pydantic à jour.
— Cohérence avec le gabarit v2.1 ou version courante (révisions intermédiaires v2.1.1, v2.1.2 prises en compte sans refonte structurelle).
— Tests sur les six cas-jouets canoniques v2.1.

*Audit doctrinal périodique* — tous les six mois, vérification que le code reste conforme à la doctrine courante (qui peut avoir évolué entre temps).

---

## 6. Disciplines spécifiques au projet L'Entité

Disciplines documentées dans la doctrine v2.1 et le journal méthodologique qui s'appliquent au code en plus des disciplines générales.

*Anonymisation stricte des agents.* Aucun agent IA ne connaît l'identité ou le rôle complet des autres agents. Cohérent avec l'autonomie épistémique du projet.

*Validation Pydantic obligatoire de toutes les sorties M01-M et M03-M.* Aucune sortie ne quitte le système sans avoir validé contre le schéma. Garantie de conformité doctrinale.

*Discipline séparation sortie humaine / journal méthodologique.* Le code génère M01-H (lisible non-analyste), M01-M (machine), M01-P (publique) comme outputs distincts. Pas de mélange.

*Discipline anti-cumul.* Pas d'accumulation de versions successives de documents de coordination. Le journal versionne, mais le document de coordination courant est unique.

*Audit périodique des typologies (typology_audit).* Implémenté en Phase 3 sur le graphe. Détection automatique des nouveaux types d'effets observables, vulnérabilités, patterns dans les analyses entrantes. Examen périodique selon la charte v2.1 section 6.6.

*Audits inscrits au gabarit v2.1.1.* `intentionality_bias_audit` et `hypothesis_gap_audit` implémentés en Phase 3 sur la base accumulée d'analyses.

*Journal méthodologique au fil de l'eau.* Le code émet des entries au journal méthodologique général à chaque décision technique significative. Append-only.

---

## 7. Outillage recommandé

| Outil | Usage | Justification |
|---|---|---|
| Python 3.11+ | Langage principal | Cohérent avec pipeline existant, écosystème mature, performance correcte |
| Pydantic 2.13+ | Validation schémas | Cohérent avec pipeline existant, performance excellente, écosystème mature |
| Anthropic SDK | Appels LLM | Modèle principal des analyses (Opus 4.7 pour analyse, Sonnet 4.6 pour M01-P) |
| langgraph | Orchestration multi-agents | Lisibilité du graphe, écosystème mûr ; à valider en Phase 0 |
| PostgreSQL 15+ + Apache AGE | Graphe cognitif | Cohérent avec licence open source du projet, SQL + Cypher hybride |
| FastAPI | API REST | Performance, écosystème, intégration native Pydantic |
| Pytest | Tests | Standard de fait Python |
| Black + Ruff + mypy | Qualité code | Formatage et typage statique |
| Git + GitHub/GitLab | Versioning | Standard de fait |
| Claude Code (CLI) | Développement assisté | Cohérent avec pratique du porteur (Seb) |
| Cowork | Accès workspace local | Cohérent avec pratique du porteur |
| Docker (optionnel) | Conteneurisation | Pour déploiement à partir de Phase 4 |

---

## 8. Décisions à prendre avant la Phase 0

Cinq décisions structurantes à prendre par le porteur principal avant de commencer le codage substantiel. Chacune est documentée dans la section 4 (Phase 0) avec options examinées et recommandation préliminaire.

1. *Orchestration multi-agents* — langgraph (recommandation), custom, langchain.
2. *Persistance graphe* — PostgreSQL + AGE (recommandation), Neo4j Community.
3. *Persistance journal* — Git + JSON structuré indexé (recommandation), base événementielle, hybride.
4. *Licence* — Apache 2.0 (recommandation), MIT, AGPL.
5. *Modèle de distribution* — distribution duale (recommandation), open source intégral dès le départ, closed pendant phase opérationnelle.

Ces décisions sont *réversibles avec coût significatif*. Mieux vaut les prendre méthodiquement en Phase 0 que les reporter en Phase 1 où elles auront un impact sur le code déjà produit.

---

## 9. Estimation de durée totale

Durée approximative pour atteindre Mode 1 opérationnel (système utilisable par analystes professionnels) — *4 à 6 mois* en développement à temps partiel (un développeur principal + assistance LLM), *2 à 3 mois* en développement à temps plein.

Décomposition.

— Phase 0 — Préparation et décisions (1-2 semaines).
— Phase 1 — Pipeline monolithique (3-5 semaines).
— Phase 2 — Architecture multi-agents (4-6 semaines).
— Phase 3 — Persistance avancée (4-6 semaines).
— Phase 4 — Interfaces et déploiement Mode 1 (4-8 semaines).

Estimation marges. *Optimiste* — 12 semaines (3 mois). *Réaliste* — 20 semaines (5 mois). *Pessimiste* — 28 semaines (7 mois). Cohérent avec un projet d'infrastructure logicielle de cette complexité (multi-agents IA + graphe + interface).

Estimation coûts API. *Phase 1 développement* — ~50-200 € d'API Anthropic. *Phase 2 développement* — ~200-500 €. *Phase 4 production initiale* — ~2-5 € par analyse Mode 1 selon volume et complexité. À budgétiser selon trajectoire commerciale.

---

## 10. Premier livrable concret recommandé

*Document "Plan de codage v0.1"* qui formalise les décisions de la Phase 0. Une fois ce document validé par le porteur, la Phase 0 prototype peut commencer.

*Contenu attendu du Plan de codage v0.1.*

1. État des cinq décisions structurantes — choix arrêté avec motif.
2. Couche d'exécution v2.1.1 mise à jour à partir de la v2 obsolète.
3. Spécification précise du prototype technique de Phase 0 (un fichier `prototype_m01.py` qui produit une analyse M01-M à partir d'un texte source avec un appel LLM unique).
4. Critères de succès du prototype.
5. Plan détaillé Phase 1 avec milestones hebdomadaires.

*Format* — document markdown court (1500-2500 mots), pas de pavé. Adressé au porteur principal pour validation.

*Production possible.* Le Plan de codage v0.1 peut être produit par Claude (cette instance ou ultérieure) une fois que le porteur a pris position sur les cinq décisions structurantes. Volume estimé ~2500 mots.

---

## 11. Risques identifiés et stratégies de mitigation

*Risque 1 — surinvestissement en architecture multi-agents avant validation de la faisabilité.* Mitigation — Phase 1 monolithique avant Phase 2 multi-agents. Si Phase 1 ne fonctionne pas, Phase 2 ne fonctionnera pas non plus.

*Risque 2 — divergence entre analyses humaines et analyses pipeline.* Mitigation — tests de concordance systématiques. Si la divergence est trop grande, retour sur les prompts d'agents avant déploiement.

*Risque 3 — coûts API supérieurs aux estimations.* Mitigation — surveillance par analyse, alertes, basculement vers modèles moins coûteux (Haiku 4.5) pour les sous-tâches qui le supportent.

*Risque 4 — évolution doctrinale en cours de codage.* Mitigation — gel doctrinal pendant Phase 1-2 (pas de nouvelle révision majeure jusqu'à Mode 1 opérationnel), sauf découverte critique. Les révisions mineures (v2.1.1, v2.1.2) sont compatibles.

*Risque 5 — dette technique accumulée par développement rapide.* Mitigation — refactoring inclus dans chaque phase, tests automatisés, pre-commit hooks. Pas de bypass des disciplines transversales.

*Risque 6 — biais d'optimisme sur la durée.* Mitigation — milestones hebdomadaires, ajustement réaliste de la trajectoire après chaque phase.

*Risque 7 — silos de connaissance entre développeur et porteur doctrinal.* Mitigation — si Seb développe seul, pas de risque ; sinon, documentation au fil de l'eau et synchronisations régulières.

---

## 12. Réponse synthétique aux deux questions

**Question 1 — quand commencer à coder ?** *Maintenant pour la Phase 0 préparation* (1-2 semaines). Les conditions sont satisfaites pour cette phase. *Après Phase 0 pour les Phases substantielles* — Phase 1 pipeline monolithique, puis Phase 2 multi-agents, puis Phase 3 persistance avancée, puis Phase 4 interfaces et Mode 1 opérationnel.

**Question 2 — méthodologie de travail ?** *Cinq phases* avec critères d'acceptation explicites. *Disciplines transversales* — architecture hexagonale, tests à chaque niveau, versionning Git rigoureux, documentation au fil de l'eau, CI minimaliste, sécurité et audit des outputs. *Disciplines spécifiques* — anonymisation des agents, validation Pydantic obligatoire, séparation sortie humaine / journal, anti-cumul, audits inscrits au gabarit v2.1.1. *Cinq décisions structurantes* à prendre avant Phase 0. *Premier livrable concret* — Plan de codage v0.1 qui formalise les décisions.

**Le code commence par les décisions, pas par le clavier.** La discipline rigoureuse du projet appliquée au code — la doctrine est éprouvée avant d'être instrumentée. Le pipeline existant est la *fondation*, pas le système.

---

*Méthodologie de codage v1.0 — édité le 17 mai 2026. À réviser après Phase 0 selon les décisions prises et le retour d'expérience du prototype. Inscrit dans la couche méthodologique de développement du projet, distinct des couches doctrinale (charte, gabarit, méthodes) et opérationnelle (analyses, pipeline minimal).*
