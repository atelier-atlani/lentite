# Décision 001 — Orchestration multi-agents

*Décision structurante Phase 0 du codage. Prise en délibération avec sparring partner (Claude.ai, Mode Architecte/sparring). Référence : `plan_action_001.md` §4.1. Append-only — toute révision fera l'objet d'une nouvelle décision référençant celle-ci.*

*Méta-information.*
- Date de décision : 3 juillet 2026.
- Décideur : Seb (Dirigeant).
- Statut : validée.
- Décisions liées : contrainte par 002 (les agents produisent des YAML candidats soumis au validateur, jamais d'écriture directe dans le graphe) et 003 (aucune écriture agentique au journal) ; compatible 004 (SDK Anthropic et NetworkX sans conflit de licence ; langgraph MIT compatible en cas de bascule).

---

## 1. Contexte

La couche d'exécution prévoit quatre agents spécialisés conformes à la doctrine v2.1.1 — Charité, Vulnérabilités, Chaînes causales, Synthèse — pour produire automatiquement des analyses M01-M à partir de textes sources. À juillet 2026, ces agents existent comme rôles de prompt (matériau réutilisable dans `lentite_observatrice_complet/` : prompts contradicteur et analystes spécialisés), non comme processus orchestrés. Par ailleurs, le projet opère déjà une orchestration de fait à l'échelle humaine : le workflow `.claude/` (Architecte → Implementer → Reviewer, bus de messages par fichiers), éprouvé sur le présent cycle de décisions.

## 2. Problème

Quel dispositif d'orchestration pour la chaîne texte source → quatre agents → YAML candidat → validation, sachant que : (a) les décisions 002 et 003 ont réduit la surface de l'orchestration (les agents ne touchent ni graphe ni journal — ils produisent des fichiers candidats) ; (b) la chaîne cible de la Phase 1 est linéaire (séquence de quatre rôles avec boucle de retry sur échec de validation), sans parallélisation ni branchements complexes ; (c) le critère doctrinal prioritaire est l'auditabilité des décisions d'agents, chaque étape devant être traçable par un tiers.

## 3. Options examinées

**Option A — langgraph** (recommandation préliminaire du plan).
Framework dédié aux graphes d'agents, écosystème mûr, support natif Anthropic. Mais pour une séquence linéaire de quatre appels, la couche d'abstraction (state, checkpointers, compilation du graphe) s'interpose entre l'auditeur et ce qui s'est réellement passé : elle réduit la transparence au lieu de l'augmenter à cette échelle. L'argument de lisibilité du graphe vaut pour des topologies complexes, inexistantes en Phase 0-1. Adopter le framework avant d'avoir fait tourner les quatre rôles sur un texte réel, c'est choisir la tuyauterie avant de connaître le débit.

**Option B-séquencée — Custom Python minimal avec critère de bascule** (retenue).
SDK Anthropic direct, pipeline linéaire (~150 lignes), architecture hexagonale légère, traçabilité par artefacts de log JSON. Bascule vers langgraph sur critères documentés (§7). Détail au §5.

**Option C — LangChain agents (legacy).**
Écartée — le plan a raison : architecture moins explicite que langgraph, considérée legacy par l'éditeur lui-même. Aucun cas où elle domine A ou B.

## 4. Critères de décision

- Auditabilité des décisions d'agents (critère doctrinal n°1) : un tiers doit pouvoir reconstituer chaque étape — entrée, sortie, modèle, horodatage — sans connaître le framework.
- Proportionnalité : pas de dépendance ni d'abstraction avant le besoin topologique (anti-tâche du plan d'action 001 §5).
- Réversibilité : la migration vers un framework ne doit toucher que la couche orchestration (architecture hexagonale).
- Réutilisation de l'existant : prompts d'agents d'`observatrice_complet/` cannibalisables ; workflow `.claude/` comme modèle d'orchestration par fichiers déjà éprouvé.
- Cohérence avec 002/003 : l'orchestration écrit des fichiers candidats, exclusivement.

## 5. Décision retenue

**Option B-séquencée** :

**Volet 1 — Implémentation Phase 0-1 : custom Python minimal.**
- Appels directs au SDK Anthropic (pas de framework d'orchestration).
- Pipeline linéaire : texte source → agent Charité → agent Vulnérabilités → agent Chaînes causales → agent Synthèse → assemblage YAML candidat → `validate.py` ; boucle de retry bornée (max 2 itérations) sur échec de validation, avec le rapport d'erreurs du validateur réinjecté à l'agent Synthèse.
- Architecture hexagonale légère : le cœur métier (schémas Pydantic, validation, `graph_builder.py`) ignore tout de l'orchestration ; les agents sont des adaptateurs. Garantit que la bascule éventuelle (§7) ne touche que la couche orchestration.
- Les prompts d'agents sont des fichiers versionnés (cannibalisation du matériau d'`observatrice_complet/` comme base, adaptation à la doctrine v2.1.1), jamais des chaînes en dur dans le code.

**Volet 2 — Traçabilité par artefacts** (pendant orchestration du principe fichiers-source-de-vérité). Chaque appel d'agent produit un artefact de log JSON archivé à côté du YAML produit : prompt complet envoyé, réponse brute reçue, modèle et version, horodatage, tokens, numéro d'itération. Le dossier d'une analyse contient ainsi son YAML validé et la trace intégrale de sa production — auditable par un tiers sans exécuter quoi que ce soit.

## 6. Motif principal

À topologie linéaire, quatre appels API loggés en JSON brut sont plus auditables qu'un graphe compilé : le framework ajouterait une abstraction là où la doctrine exige de la transparence nue. L'objection « réinventer la roue » tombe à cette échelle — quatre appels séquentiels ne sont pas une roue, c'est un axe ; le risque réel serait de maintenir du custom quand la complexité aura grandi, et il est traité par un critère de bascule explicite plutôt que par un choix définitif prématuré. La décision reproduit au niveau logiciel le modèle qui fonctionne déjà au niveau humain : une orchestration par fichiers, lisible, append-only.

## 7. Conditions de révision

Bascule vers langgraph (cible confirmée, licence MIT compatible décision 004) lorsque l'orchestration cesse d'être linéaire, c'est-à-dire dès que l'un de ces besoins est avéré et documenté au journal :

- Parallélisation des agents (exécution concurrente de rôles indépendants).
- Branchements conditionnels multiples (routage dynamique selon le contenu).
- Reprise sur erreur avec état persistant entre sessions d'exécution.
- Boucles contradicteur/analyste dépassant deux tours (dialectique itérative du Mode 3 ou des audits adverses).

En cas de bascule : le volet 2 (artefacts de log JSON) est conservé tel quel — il est indépendant du dispositif d'orchestration et reste l'exigence doctrinale. Réexamen également si Anthropic publie un SDK d'orchestration d'agents natif rendant langgraph redondant — alternative à évaluer alors à critères constants.

## 8. Conséquences immédiates

- `plan_action_002.md` devra spécifier : le module d'orchestration minimal (structure, interfaces hexagonales), le format de l'artefact de log JSON, la boucle de retry bornée, et l'emplacement des prompts versionnés (proposition : `pipeline/agents/`).
- La cannibalisation d'`observatrice_complet/` est activée : extraction des prompts réutilisables vers `pipeline/agents/`, archivage du reste en strate génétique datée, entrée au journal — à exécuter en phase d'hygiène (jalon 1 de la décision 005) ou en première tâche du prototype.
- Dépendances Phase 0-1 : SDK Anthropic Python + `networkx` + Pydantic v2 (déjà présent). Aucun framework d'orchestration.
- Le Mode Implementer (Claude Code) dispose avec cette décision d'un périmètre non ambigu : pas de choix de framework à faire en cours d'implémentation.
- Inscription au journal méthodologique général comme entrée 8.6 (numérotation du plan d'action 001 §6).

---

*Décision 001 v1.0 — 3 juillet 2026. Append-only.*
