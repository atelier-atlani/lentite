# L'Entité — Restructuration v2

*Document de refonte intégrant les critiques externes reçues sur la v1. Livrable autonome, structuré par couches. Définit les corrections de doctrine, de méthode et d'architecture, tranche les décisions bloquantes, fixe le plan de travail v2. Ce document remplace toute version antérieure pour les points qu'il traite explicitement ; les v1 demeurent référence pour le reste.*

---

## 0. Nature et portée du document

Ce document n'est pas une version v2 complète des artefacts du projet. Il est l'instrument de transition entre la v1 stabilisée (charte, gabarit, méthode 01, couche d'exécution) et les versions v2 qui en découleront. Il fixe la doctrine des corrections à apporter, dans une forme qui permet aux fichiers v2 d'être réécrits ensuite sans dérive. Il a valeur normative immédiate : toute analyse produite après cette date intègre les corrections définies ici, même avant la réécriture formelle des fichiers v2.

Les corrections relèvent de quatre catégories : doctrine (couche A), méthode (couche B et instances C), architecture (couche d'exécution), décisions politiques bloquantes. Chaque catégorie est traitée en section dédiée. La dernière section fixe le plan de travail.

---

## 1. Corrections de doctrine — Couche A

### 1.1 Statut du déplacement de la fragilité humaine

La doctrine v2 énonce explicitement ce que la v1 laissait implicite : le projet ne supprime pas la fragilité humaine, il la déplace dans des artefacts qui la rendent versionnable, auditable, discutable. Le journal méthodologique, le catalogue de méthodes, les schémas de validation, les cas-jouets sont les lieux où la fragilité humaine est inscrite pour pouvoir être travaillée. Cette caractéristique est constitutive et assumée. Elle distingue le projet des systèmes qui prétendent à une rigueur autonome.

Conséquence dans la charte v2 : ajouter une cinquième section après "ADN — quatre engagements non-négociables" intitulée "Statut de l'humain dans le projet" qui rend ce point explicite. La formulation est en cours d'arbitrage ; elle doit éviter à la fois l'illusion d'autonomie machine et la dépendance déclarative à un expert humain.

### 1.2 Historiographies disqualifiées

Le refus d'arbitrer entre historiographies concurrentes — pilier de la doctrine v1 — s'applique aux concurrences légitimes. Il ne s'applique pas aux historiographies scientifiquement disqualifiées : négationnismes documentés, fraudes établies, méthodologies démontrées défaillantes par la communauté concernée. Ces historiographies ne sont pas mises en regard d'historiographies validées comme des alternatives symétriques ; elles sont identifiées comme disqualifiées avec leur statut.

Conséquence dans la charte v2 : ajouter à la section "Discipline épistémique" un point intitulé "Refus de la fausse symétrie". Trois critères opérationnels caractérisent une historiographie disqualifiée : (a) consensus négatif documenté de la communauté académique pertinente, (b) impossibilité méthodologique reproductible (sources falsifiées, raisonnements circulaires démontrés), (c) statut juridique le cas échéant (interdiction légale de certains négationnismes). Au moins deux critères sur trois sont nécessaires pour disqualifier.

### 1.3 Pondération des historiographies concurrentes légitimes

Pour les historiographies concurrentes qui ne sont pas disqualifiées, le projet introduit une typologie en trois niveaux de consensus académique : *consensus fort* (hypothèse majoritaire dans la littérature spécialisée récente, sans contestation substantielle), *contesté* (deux écoles ou plus s'affrontent sur des bases méthodologiques distinctes), *marginal* (position défendue par une minorité identifiable, légitime mais minoritaire). Toute mention d'historiographie concurrente déclare son niveau de consensus.

Conséquence : sur le cas Lecornu, la lecture hétérodoxe des retraites (Sterdyniak, Zemmour) est qualifiée *marginale* — minoritaire dans la littérature économique mainstream, légitime, défendue par un courant identifiable. Sur le cas Fabius, la lecture du Conseil constitutionnel comme "chien de garde de l'exécutif" est qualifiée *contestée* — défendue par une partie de la doctrine, contestée par une autre, sans verdict mainstream univoque. Cette typologie ne tranche pas le débat ; elle situe l'auditeur.

### 1.4 Modes 1, 2, 3 — séparation infrastructurelle

La doctrine v1 énonce trois modes (éclairage médiatique, conseiller du prince, chat public). La v2 sépare leur infrastructure technique et leur régime de publication. La charte v2 énonce que les trois modes partagent la même doctrine et le même catalogue de méthodes, mais qu'ils ne partagent pas la même infrastructure, ni la même surface d'accès, ni les mêmes sorties.

Conséquence : la doctrine en charte v2 inscrit explicitement que les trois modes ne sont pas simultanément déployables. Le déploiement procède par mode, avec des conditions de passage entre modes définies. Voir section 4 du présent document pour les décisions de déploiement.

---

## 2. Corrections de méthode — Couche B (gabarit) et instance C (M01)

### 2.1 Charge éthique du discours

Le gabarit v2 ajoute à la fiche d'énonciation un champ obligatoire : *charge éthique du discours*, codée en trois niveaux. *Faible* : discours dont la mise en circulation ne sollicite ni la haine, ni la violence, ni la disqualification d'identités. *Moyenne* : discours qui mobilise des oppositions de groupes ou de positions sans appel explicite à la disqualification. *Élevée* : discours qui sollicite la haine de groupes identifiés, appelle à la violence, ou nie des faits historiques constitutifs (génocides, crimes de masse documentés).

Effet sur la méthode : quand la charge éthique est élevée, l'étape 5 (reconstruction charitable) reformule l'argumentation interne dans sa meilleure version, mais le bloc résultats nuls signale explicitement le contenu éthiquement disqualifié qui demeure dans cette meilleure version. La charité reformule l'argument ; elle ne neutralise pas son objet. Un discours xénophobe argumenté reste un discours xénophobe une fois la charité appliquée, et l'analyse le déclare.

### 2.2 Règle opérationnelle pour la charité interprétative

Le gabarit v2 ajoute à l'étape 5 une règle opérationnelle qui formalise la friction identifiée dans le rejeu Lecornu (la charité empruntait le lexique valorisant du locuteur). La règle : la reconstruction charitable interdit l'emploi non marqué des termes évaluatifs du locuteur. Tout terme évaluatif emprunté au discours analysé (par exemple "rupture", "ouverture", "responsabilité", "fermeté") doit être (a) mis entre guillemets, (b) attribué explicitement au locuteur ("ce que le locuteur appelle 'rupture'"), ou (c) reformulé dans un lexique descriptif neutre ("la décision de suspendre la réforme jusqu'à l'élection présidentielle").

Sur Lecornu, la formulation v1 "ouverture méthodologique" est non conforme à la règle v2. Reformulation conforme : "ce que le Premier ministre présente comme une 'ouverture méthodologique', c'est-à-dire le passage d'une méthode de réforme par décret à une méthode de réforme par négociation parlementaire". Cette reformulation conserve la charité (reconnaît la cohérence de l'argument) sans en avaliser le lexique évaluatif.

### 2.3 Sortie publique M01-P

Le gabarit v2 ajoute aux deux sorties existantes (M01-H markdown détaillée, M01-M YAML machine) une troisième sortie : M01-P, publique, générée automatiquement à partir de M01-M validé. Format imposé : entre cent cinquante et trois cents mots, structuré en quatre éléments dans l'ordre. *Énonciation* — qui parle, à qui, dans quel cadre, en une phrase. *Fait dominant ou inférence principale* — le constat le plus solide produit par l'analyse, en deux à trois phrases. *Hypothèse explicative dominante avec sa confiance et son alternative non intentionnelle principale* — pour ne pas fermer le débat. *Renvois* — un lien vers l'analyse complète M01-H pour l'auditeur exigeant, et un lien vers la source pour l'auditeur qui veut juger lui-même.

La sortie M01-P n'est pas une simplification de la pensée ; elle est une projection brève de la synthèse en trois statuts épistémiques, conçue pour le mode 3 (chat public) et pour les usages où la lecture rapide est la condition. La règle opérationnelle de la charité s'applique également à M01-P.

### 2.4 Zone d'indétermination entre hypothèses concurrentes

Le gabarit v2 ajoute à la synthèse en trois statuts une convention sur la zone d'indétermination. Quand l'écart de confiance entre l'hypothèse dominante et la deuxième hypothèse est inférieur ou égal à 0,2 (par exemple 0,7 et 0,5), aucune hypothèse n'est qualifiée de dominante ; la synthèse déclare une zone d'indétermination. Quand l'écart est compris entre 0,2 et 0,4, la dominance est qualifiée d'incertaine, et la synthèse formule explicitement les conditions d'arbitrage possible. Quand l'écart dépasse 0,4, la dominance est claire.

Sur Fabius, l'écart entre hypothèse A (0,7) et hypothèse B (0,5) est de 0,2 — limite haute de la zone d'indétermination. La synthèse v1 affirmait une hypothèse dominante ; la synthèse v2 déclarera l'indétermination ou la dominance incertaine, avec ses conditions d'arbitrage. Cette convention n'est pas un relativisme ; elle est une discipline de signalement quand l'analyse interne ne suffit pas à trancher.

### 2.5 Pondération des historiographies dans la sortie

Conséquence dans le gabarit v2 de la doctrine (section 1.3 du présent document) : la section VI du M01-H (Historiographies mobilisées) doit, pour chaque historiographie concurrente identifiée, déclarer son niveau de consensus académique (*consensus fort* / *contesté* / *marginal*) ou la qualifier comme *disqualifiée* le cas échéant. Le YAML M01-M ajoute ce champ aux entrées d'historiographie.

### 2.6 Sophismes versus vulnérabilités argumentatives — clarification

La gradation v1 distingue *sophisme certain*, *vulnérabilité probable*, *vulnérabilité possible*. Les deux critiques externes ont noté l'absence pratique de sophisme certain sur les deux cas analysés. Le gabarit v2 précise les conditions du sophisme certain : (a) la structure logique formelle est défaillante (pétition de principe formellement vérifiable, contradiction logique stricte, faux dilemme avec troisième option démontrable), (b) la lecture charitable alternative est non disponible (toute lecture qui sauve la structure altère le sens du discours), (c) le défaut est démontrable à un destinataire compétent sans information externe. Quand un seul critère manque, le défaut est qualifié *vulnérabilité probable* ou *vulnérabilité possible*. Cette précision rend opérationnelle la rareté du sophisme certain.

### 2.7 Charité et seuil de toxicité

Articulation entre les sections 2.1, 2.2 et 2.6 : sur un discours à charge éthique élevée, la charité s'applique à la *structure argumentative* du discours mais le bloc résultats nuls porte explicitement la qualification du *contenu éthique* qui demeure. Le projet ne produit pas de neutralisation rhétorique d'un contenu disqualifiable. Cette articulation est inscrite dans le gabarit v2 comme contrainte normative.

---

## 3. Corrections d'architecture — Couche d'exécution

### 3.1 Module M01-P de génération publique

La couche d'exécution v2 ajoute un composant `lentite.outputs.public` qui prend en entrée un M01-M validé et produit le M01-P selon le format spécifié en section 2.3. Le composant utilise un appel LLM dédié (modèle plus léger possible — Sonnet 4.6) avec un prompt strict qui contraint le format à quatre éléments dans l'ordre. La sortie M01-P est validée par schéma (longueur, présence des quatre sections, absence de termes évaluatifs non marqués du locuteur — règle 2.2). Le composant journalise l'appel et le résultat comme tout autre composant du pipeline.

### 3.2 Module d'audit consensus académique

La couche d'exécution v2 ajoute un quatrième module d'audit (après distribution sources, distribution hypothèses, distribution sophismes) : *audit du consensus académique sur historiographies mobilisées*. Le module agrège, sur le corpus d'analyses produites, la distribution des qualifications de consensus (*fort* / *contesté* / *marginal* / *disqualifié*). Signal d'alerte si une catégorie est sur-représentée par rapport à l'attente raisonnable du corpus (par exemple, si toutes les historiographies concurrentes mentionnées sur les discours politiques contemporains sont qualifiées *marginales*, le module signale un biais possible de sélection).

### 3.3 Distinction version publique et version restreinte du code

Décision prise sur la base de la critique 4.3 et de l'analyse du dilemme open source vs gouvernance du Mode 2 : le code du projet est scindé en deux distributions.

*Distribution publique.* Charte, gabarit, méthode 01 et méthodes futures (M02-M08) à mesure de leur stabilisation, schémas de validation, couche d'exécution Mode 1 (analyste interne), CLI minimal, modules d'audit. Licence ouverte permissive (probablement Apache 2.0 ou similaire — à arbitrer). Cette distribution permet à n'importe qui de reproduire les analyses, d'auditer le code, de proposer des contributions.

*Distribution restreinte.* Les composants spécifiques au Mode 2 (conseiller du prince) ne sont pas publiés. Ils incluent : les méthodes spécialisées du Mode 2, les prompts d'agents adaptés au Mode 2, les modules d'inférence sur les rapports de force, l'orchestration spécifique. Licence à définir, accès par authentification, traçabilité obligatoire. Cette distribution est accessible à un nombre restreint de partenaires identifiés sous contrat.

Cette distinction matérialise la résolution du dilemme : la doctrine est publique (transparence épistémique respectée) ; l'instrument spécifique du Mode 2 ne l'est pas (asymétrie du conseil stratégique protégée). La critique 4.3 de la première critique ("S'il est inclus, alors l'ethos de 'machine qui n'a pas de carrière à défendre' est incompatible avec le fait de réserver l'outil à quelques happy few") est partiellement reconnue mais retournée : ce qui est réservé n'est pas la rigueur méthodologique, c'est l'application spécifique au conseil aux acteurs de pouvoir. La rigueur reste accessible à tous via le Mode 1.

### 3.4 Décision d'applicabilité — clarification du compromis

La couche d'exécution v1 spécifie que l'étape 3 (décision d'applicabilité en mode complet / dégradé / non applicable) demeure semi-manuelle en v1. La critique externe note que cela contredit l'argument que la machine soutient une discipline que l'humain tient mal. La couche d'exécution v2 clarifie le compromis sans le résoudre.

Position assumée : la décision d'applicabilité repose sur une lecture rapide du texte source et du contexte, qui suppose un jugement de genre, de saturation, de reconstructibilité du contexte. Aucun classifieur LLM actuellement disponible ne tient cette décision de façon fiable sans supervision. La v1 et la v2 accepteront cette dépendance, en l'inscrivant dans le journal et en planifiant son automatisation comme objectif v3 (instanciation d'une méthode M-applicabilité dans le gabarit, entraînement d'un classifieur dédié sur un corpus annoté). Le compromis est honnête : la machine ne tient pas tout, l'humain reste en boucle aux endroits où le LLM ne tient pas la discipline.

### 3.5 Exposition du journal méthodologique

La couche d'exécution v1 spécifie un journal append-only en PostgreSQL avec accès par CLI. La critique externe note que le journal reste une boîte noire pour les utilisateurs externes. La couche d'exécution v2 ajoute deux modes d'exposition.

*Journal opérationnel* — CLI et requêtes SQL, pour les analystes et développeurs. Sans changement par rapport à v1.

*Journal public* — interface web minimale (Streamlit v1, frontend dédié v2) qui expose : les méthodes versionnées (avec leurs diffs), les frictions identifiées dans les analyses récentes, les corrections de doctrine intégrées au fil de l'eau, les audits agrégés. Ce journal public est l'instrument de la transparence épistémique du projet. Il rend lisible l'auto-critique du système.

### 3.6 Coût LLM et financement Mode 3

La critique 4.3 pose la question : qui paie les coûts LLM pour le Mode 3 ? La couche d'exécution v2 reconnaît que cette question n'a pas de solution technique. Trois trajectoires de financement sont identifiées sans arbitrage : mécénat (fondations, programmes de recherche), abonnement institutionnel (rédactions, universités), modèle freemium (Mode 1 gratuit, Mode 3 limité en volume gratuit puis tarifé). La décision relève d'arbitrages politiques et stratégiques hors du périmètre technique du projet. Position assumée : le Mode 3 ne sera pas déployé sans modèle de financement identifié et engagé. Le déploiement initial reste Mode 1 sur un petit groupe d'utilisateurs jusqu'à résolution.

---

## 4. Décisions politiques tranchées

Les trois décisions bloquantes identifiées par les critiques externes sont tranchées comme suit.

### 4.1 Open source ou non

Décision : *distribution duale*. La charte, le gabarit, les méthodes (à mesure de leur stabilisation), les schémas de validation, le pipeline Mode 1, les cas-jouets sont open source sous licence permissive. Les composants spécifiques au Mode 2 ne le sont pas — version restreinte sous contrat avec partenaires identifiés. Voir section 3.3 ci-dessus pour la matérialisation technique.

### 4.2 Financement du Mode 3

Décision : *report conditionné*. Le Mode 3 n'est pas déployé en v1. Il sera examiné lorsque (a) un modèle de financement pérenne aura été identifié et engagé, (b) la sortie M01-P sera implémentée et validée sur au moins vingt cas représentatifs, (c) un système de modération a priori des requêtes entrantes aura été conçu (pour éviter que le Mode 3 ne soit utilisé pour produire des analyses ad hominem ou sur des objets hors périmètre).

### 4.3 Premier déploiement réel

Décision : *Mode 1 limité, premier groupe d'utilisateurs identifié*. Le premier déploiement est limité à un groupe restreint d'analystes, chercheurs et journalistes identifiés, en Mode 1, avec interface CLI et export Markdown. Pas de Mode 2 dans ce premier déploiement (les composants spécifiques ne sont pas encore stabilisés). Pas de Mode 3 (cf 4.2). La condition d'entrée pour les utilisateurs : signer un engagement de respect des règles d'usage (notamment l'interdiction d'utiliser les analyses pour produire des attaques personnelles ou pour fonder des accusations sans procédure de validation).

Cas d'usage cible du premier déploiement : décryptage d'une séquence politique de moyenne ampleur — par exemple une campagne électorale régionale, le suivi d'une politique publique sur six mois, l'analyse comparée de deux discours d'investiture présidentielle. Pas d'enjeu de très court terme (news cycles, breaking news) qui exigerait des temps de production que la v1 ne tient pas.

---

## 5. Plan de travail v2

Les corrections définies aux sections 1 à 4 produisent une séquence de tâches. Ordre prioritaire.

### 5.1 Refonte des artefacts de doctrine et de méthode

*Tâche 1.* Réécriture de la charte v2 intégrant les points 1.1 (statut humain), 1.2 (historiographies disqualifiées), 1.3 (pondération concurrentes), 1.4 (séparation infrastructurelle des modes).

*Tâche 2.* Réécriture du gabarit v2 intégrant les points 2.1 (charge éthique), 2.2 (règle charité opérationnelle), 2.3 (sortie M01-P), 2.4 (zone d'indétermination), 2.5 (pondération historiographies en sortie), 2.6 (clarification sophismes), 2.7 (charité et seuil toxicité).

*Tâche 3.* Réécriture de la méthode 01 v2 selon les contraintes du gabarit v2.

*Tâche 4.* Rejeu des deux applications réelles (Lecornu, Fabius) en v2, pour vérifier que la nouvelle discipline tient. Sur Lecornu, vérifier que la reconstruction charitable conforme à 2.2 ne perd pas la qualité d'analyse. Sur Fabius, vérifier que la zone d'indétermination de 2.4 produit un signalement honnête. Sur les deux, produire la sortie M01-P et la valider.

### 5.2 Refonte de l'architecture technique

*Tâche 5.* Réécriture de la couche d'exécution v2 intégrant les points 3.1 (module M01-P), 3.2 (module audit consensus académique), 3.3 (distribution duale), 3.4 (clarification décision applicabilité), 3.5 (exposition journal).

*Tâche 6.* Implémentation effective du pipeline minimal défini en couche d'exécution v1 (schémas Pydantic, agent analyste anonymisé, persistance PostgreSQL/AGE, CLI). Premier test : exécuter la méthode sur le cas Fabius via l'agent anonymisé (pas via Claude conversationnel orchestré) et comparer avec la sortie produite manuellement en v1. C'est le test décisif que les deux critiques externes exigent.

### 5.3 Décisions à prendre durant l'implémentation

*Choix de licence* pour la distribution publique (Apache 2.0, MIT, AGPLv3, autre — à arbitrer selon objectifs juridiques et stratégiques).

*Modèle d'accès* à la distribution restreinte (contrat individuel, partenariat institutionnel, club fermé — à arbitrer).

*Premier groupe d'utilisateurs* du Mode 1 limité (identifier, contacter, négocier les conditions — relève de l'arbitrage politique).

*Trajectoire de financement* pour préparer un éventuel Mode 3 (sondage des fondations, programmes de recherche, partenaires institutionnels).

### 5.4 Cas-jouets restants pour la calibration

Après production des artefacts v2, les cas-jouets restants du gabarit (cas 4 adversarial, cas 6 écart apparent, cas 1 simple, cas 3 ambigu, cas 5 écart réel) sont exécutés selon la nouvelle discipline. L'ordre prioritaire reste : cas 4 (test décisif sur la dégradation gracieuse face à un discours adversarial), puis cas 6 (écarts apparents explicables par contrainte institutionnelle), puis les trois autres.

### 5.5 Instanciation des méthodes M02 à M08

Hors périmètre v2 immédiat. À engager après stabilisation effective de M01 v2 sur un corpus d'au moins une dizaine d'analyses produites par le pipeline réel (pas par Claude conversationnel orchestré). M02 (lecture indiciaire selon Ginzburg) reste la prochaine méthode à instancier, suivie de M03 (analyse contrefactuelle) et M04 (triangulation historiographique).

---

## 6. Conventions transversales pour la v2

### 6.1 Conventions de versionnement

Les artefacts v2 portent le suffixe `_v2.md` et coexistent avec les v1 jusqu'à validation. Le journal méthodologique enregistre la transition v1 → v2 avec ses motifs (critiques externes intégrées, corrections de doctrine). Les analyses produites à partir de cette date appliquent les conventions v2 même si les fichiers de gabarit v2 ne sont pas encore réécrits formellement — les corrections de doctrine sont normatives immédiatement.

### 6.2 Conventions de transparence

Le projet rend publics : la charte, le gabarit, les méthodes, les schémas, les cas-jouets, les analyses produites en Mode 1 (sauf opposition documentée du sujet pour les analyses portant sur des acteurs privés), le journal public (cf 3.5).

Le projet ne rend pas publics : les composants Mode 2, les analyses Mode 2 (sauf consentement des parties), les négociations contractuelles avec partenaires, les coûts opérationnels détaillés.

### 6.3 Conventions d'auto-critique

Toute critique externe substantielle du projet est consignée au journal public et fait l'objet d'une réponse motivée (acceptation, rejet, mise en discussion) publiée dans un délai raisonnable. Les corrections intégrées en v2 selon le présent document sont la première application de cette convention.

---

*Fin de la restructuration v2. Document de transition à utiliser en tant que référence pour la réécriture des artefacts v2 dans l'ordre des tâches définies en section 5.*
