# L'Entité — Méthode 03 v2.1 : Analyse comparative multi-acteurs sur même controverse

*Couche C — deuxième instance de méthode dans le catalogue après M01. Implémente le gabarit v2.1 pour le type d'objet "controverse politique avec multiplicité de discours d'acteurs sur une même séquence". Refonte ciblée par rapport à M03 v2 — intégration de la matrice des objets visés multi-acteurs en complément de la matrice des positions épistémiques, et comparaison des chaînes causales aval entre acteurs. Produit caractéristique enrichi : matrice K/B/Affirme/Prétend_savoir + matrice des objets visés croisée avec efficience par objet. Remplace M03 v2.*

---

## 1. Métadonnées

```yaml
method_id: M03_ANALYSE_COMPARATIVE_MULTI_ACTEURS
method_name: "Analyse comparative multi-acteurs sur même controverse"
method_version: 2.1
charter_version_required: 2.1
gabarit_version_required: 2.1
authors: [équipe projet L'Entité]
last_revision_date: 2026-05-17
```

---

## 2. Type d'objet

M03 couvre le type d'objet *controverse politique avec multiplicité de discours d'acteurs sur une même séquence* — séquence temporelle pendant laquelle plusieurs acteurs publics produisent des discours substantiels sur un objet politique commun (loi, décision, événement, principe).

Exemples canoniques : la séquence retraites octobre 2025 (Lecornu, Ciotti, Wauquiez, Chatelain, Bayrou, etc.) ; la séquence loi immigration décembre 2023 - janvier 2024 (gouvernement, parlement, Conseil constitutionnel, organisations professionnelles) ; les séquences présidentielles avec multiplicité de candidats produisant des discours sur les mêmes thématiques.

M03 ne couvre pas l'analyse d'un discours unique (M01) ni l'analyse longitudinale d'un seul acteur sur plusieurs discours (méthode dédiée à instancier).

---

## 3. Finalité analytique (v2.1)

M03 éclaire la structure d'une controverse politique multi-acteurs en distinguant rigoureusement, pour chaque acteur, ses positions épistémiques sur les propositions structurantes de la controverse *et* les objets visés par son intervention dans la controverse. La méthode produit une cartographie comparative qui rend visibles simultanément les désaccords de fond sur les propositions et les divergences stratégiques sur les objets visés.

Pour chaque controverse analysée, M03 documente : la matrice des positions épistémiques (acteurs × propositions, croisée avec K/B/Affirme/Prétend_savoir), la matrice des objets visés (acteurs × objets visés inférés, croisée avec efficience par objet), les cadres interprétatifs concurrents mobilisés, la structure de l'arène (relations entre acteurs), les chaînes causales aval comparées (objets visés effectivement atteints ou non, par acteur, dans la fenêtre temporelle).

M03 sert : à l'analyse rigoureuse de séquences politiques contestées, à la mise en évidence des structures de désaccord factuel et normatif, à la cartographie des stratégies divergentes derrière des positions thématiques apparemment voisines, à l'identification des prétentions abusives de savoir, à l'objectivation de la dynamique d'arène. M03 ne sert pas : à arbitrer la controverse, à produire un jugement moral sur les acteurs, à prédire l'issue politique de la controverse.

---

## 4. Décision d'applicabilité

M03 applique la procédure de décision d'applicabilité du gabarit v2.1 section 4 avec quatre conditions opérationnelles spécifiques.

*Condition de pluralité documentable d'acteurs.* Au moins trois acteurs avec discours substantiels accessibles sur la même controverse. En deçà, l'analyse comparative perd sa rentabilité épistémique.

*Condition de séquence temporelle resserrée.* Les discours doivent être produits dans une fenêtre temporelle suffisamment courte pour que la comparaison soit pertinente (typiquement de quelques jours à quelques semaines). Sur des séquences trop étalées, les positions des acteurs évoluent et l'analyse multi-acteurs doit alors être déclinée en plusieurs analyses ponctuelles.

*Condition de M01 préalable.* M01 v2.1 doit avoir été exécutée individuellement sur chaque discours du corpus avant le démarrage de M03. M03 agrège des sorties M01-M validées ; elle ne se substitue pas à M01.

*Condition de structuration documentaire.* Les positions des acteurs doivent être documentables par sources publiques accessibles (verbatim de discours, transcriptions, communiqués officiels). Les positions purement off-the-record ou rumorales sont exclues.

Le verdict `applicable_vigilance_adversariale` est activé pour les controverses incluant un ou plusieurs acteurs au régime adversarial (sur la séquence retraites octobre 2025, Ciotti). La vigilance s'applique aux acteurs concernés sans contaminer l'analyse globale.

---

## 5. Définitions opératoires propres à M03

M03 hérite des définitions du gabarit v2.1 section 5 (y compris les définitions v2.1 sur efficience par objet, objets thématiques et visés, chaînes causales) et des définitions de M01 v2.1 section 5. Elle y ajoute six définitions propres.

### 5.1 Controverse

Une *controverse* est un ensemble structuré de positions publiques contestées sur un objet politique commun. Une controverse est composée de : (a) un objet structurant (loi, décision, événement, principe), (b) un noyau de propositions sur lesquelles les acteurs prennent position, (c) une séquence temporelle dans laquelle les positions sont produites, (d) un ensemble d'acteurs publiquement identifiables.

Le *noyau de propositions* est explicité par M03 — typiquement entre trois et sept propositions identifiables sur lesquelles les acteurs s'accordent ou se divisent.

### 5.2 Efficience par acteur et par dimension de la controverse

M03 applique la définition d'efficience du gabarit v2.1 section 5.9 à la controverse multi-acteurs. *Un acteur est efficient sur une dimension de la controverse* s'il peut produire des actes effectifs sur cette dimension dans la fenêtre temporelle pertinente.

L'efficience est documentée par dimension de la controverse, pas globalement. Un même acteur peut être efficient sur certaines dimensions et non-efficient sur d'autres. Exemple sur la séquence retraites octobre 2025 — le Parti socialiste est efficient sur la dimension "votera-t-il la motion de censure ?" (son vote est décisif) et non-efficient sur la dimension "que doit contenir la réforme ?" (il ne dirige pas le gouvernement) ; Ciotti est efficient sur la dimension "consolidation publique de l'alliance UDR-RN" et non-efficient sur la dimension "composition du gouvernement Lecornu II".

Trois valeurs canoniques — `efficient`, `efficient_partiel`, `non_efficient` — selon le gabarit v2.1 section 5.9.

### 5.3 Matrice des positions épistémiques

La *matrice des positions épistémiques* est l'une des deux productions caractéristiques de M03 v2.1. Elle croise les acteurs (en lignes) et les propositions du noyau (en colonnes). Chaque cellule porte le régime épistémique de l'acteur sur la proposition, parmi quatre valeurs : K (savoir factif), B (croyance), Affirme (assertion sans hypothèse), Prétend_savoir (présentation comme certain sans validation).

La matrice est complétée par : (a) une cellule supplémentaire indiquant l'efficience de l'acteur par dimension pertinente de la controverse, (b) des annotations pour les positions silencieuses (acteur n'a pas pris position sur la proposition), (c) des annotations pour les positions ambiguës (ne tranche pas entre B et Affirme), (d) la citation précise du texte source qui justifie chaque attribution.

Lecture de la matrice : *désaccords factuels* (deux acteurs ont K(p) et K(¬p)), *désaccords normatifs* (les acteurs ont K(p) ou B(p) sur le diagnostic mais divergent sur la prescription), *asymétries d'expertise* (certains acteurs ont K et d'autres B sur une même proposition factuelle), *prétentions abusives de savoir* (un acteur a Prétend_savoir(p) alors que K(p) ne peut pas être établi indépendamment).

### 5.4 Matrice des objets visés multi-acteurs (nouveau v2.1)

La *matrice des objets visés* est la seconde production caractéristique de M03 v2.1. Elle croise les acteurs (en lignes) et les objets visés (en colonnes) — chaque acteur identifie ses propres objets visés par son intervention dans la controverse, selon le gabarit v2.1 sections 2.2 et 5.10.

Chaque cellule porte : (a) un statut — l'objet visé est `visé`, `non_visé`, ou `ambigu` pour cet acteur, (b) la `inference_confidence` sur l'identification de l'objet visé (entre 0 et 1), (c) la qualification d'efficience de l'acteur sur l'objet visé (`efficient`, `efficient_partiel`, `non_efficient`), (d) la citation précise du texte source qui supporte l'inférence.

*Construction de la matrice.* Les objets visés sont extraits de l'union des objets visés identifiés par les analyses M01 v2.1 individuelles des acteurs. Si un objet visé est identifié pour un acteur, M03 examine si cet objet est aussi visé par les autres acteurs (même implicitement) — soit comme objet partagé, soit comme objet en compétition. La matrice fait donc apparaître les *convergences stratégiques* (plusieurs acteurs visent le même objet) et les *divergences stratégiques* (les objets visés sont disjoints malgré des positions thématiques voisines).

*Lecture de la matrice.* Cas saillants. *Convergence sur objet visé avec divergence sur proposition* — plusieurs acteurs visent l'objet "consolidation d'une coalition de gauche" tout en divergeant sur la proposition (P3) "la suspension est une solution adéquate". *Convergence sur proposition avec divergence sur objet visé* — deux acteurs s'accordent sur (P4) "le 49.3 est à éviter" mais l'un vise la stabilité institutionnelle quand l'autre vise l'affaiblissement du gouvernement. Ces cas sont précisément ce que la matrice rend visible.

*Articulation avec la matrice des positions épistémiques.* Les deux matrices travaillent ensemble. La matrice des positions épistémiques documente *ce que les acteurs disent ou prétendent savoir* sur les propositions structurantes. La matrice des objets visés documente *ce que les acteurs cherchent à produire* par leur intervention dans la controverse. Une analyse comparative complète mobilise les deux dimensions — sans les confondre.

### 5.5 Cadres interprétatifs concurrents

Un *cadre interprétatif* est un système de présuppositions, de catégorisations et de cadrages qui structure la lecture de la controverse par un acteur. Sur une même controverse, plusieurs cadres concurrents peuvent coexister. M03 les identifie, les nomme, et les pondère par leur audience dans le débat public et leur consensus dans la communauté académique pertinente.

*Ancrage empirique des cadres (v2.1).* Conformément à la charte v2.1 section 6.6, chaque cadre interprétatif identifié par M03 doit pouvoir être documenté empiriquement par au moins deux ou trois cas externes au projet — discours politiques antérieurs, productions académiques, prises de position éditoriales — qui mobilisent le même cadre de façon attestée. Les cadres sont des patterns observés dans la pratique politique et médiatique, pas des catégories fabriquées par l'analyse.

Sur la séquence retraites octobre 2025, les cadres concurrents identifiables avec ancrage empirique documentable : *technocratique-actuariel* (ancrage : doctrine du Commissariat général au Plan, productions de Bruno Le Maire, IFRAP), *social-démocrate* (ancrage : doctrine CFDT depuis Maire Berger, productions de Terra Nova, Vallaud), *libéral-individualiste* (ancrage : doctrine Institut Montaigne, Renaissance, productions d'Attal sur la capitalisation), *souverainiste-protectionniste* (ancrage : doctrine RN et UDR, productions de Bardella et Ciotti), *écologiste-décroissant* (ancrage : doctrine EELV et insoumise sur le travail, productions de Tondelier et Panot).

Ces cinq cadres ne sont pas exhaustifs ; M03 les identifie en fonction des discours analysés et de leur ancrage empirique.

### 5.6 Structure de l'arène et chaînes causales aval comparées

L'*arène* est la configuration relationnelle des acteurs sur la controverse — qui parle à qui, qui répond à qui, qui ignore qui, qui forme alliance avec qui. M03 cartographie l'arène par un graphe orienté où les nœuds sont les acteurs et les arêtes sont les relations identifiables (réponse à, alliance avec, opposition à, ignore, cite).

*Chaînes causales aval comparées (nouveau v2.1).* Pour chaque acteur, à partir de la sortie M01-M individuelle (sous-bloc V.4 de l'analyse M01 v2.1), documentation des effets observables sur ses objets visés dans la fenêtre temporelle de la controverse. La mise en parallèle multi-acteurs révèle quels acteurs ont vu leurs objets visés atteints, quels acteurs ont vu leurs objets non atteints, et quels effets observables ont profité à un acteur plutôt qu'à un autre.

Exemple sur la séquence retraites octobre 2025 — Lecornu efficient sur la survie du gouvernement (motion de censure rejetée) et sur la suspension de la réforme (votée 12 novembre 2025), non efficient sur le renoncement au 49.3 (renié 19 janvier 2026, pattern `broken_explicitly`) ; Ciotti efficient sur la consolidation publique de l'alliance UDR-RN (vote conjoint motion de censure 16 octobre 2025) et sur la visibilité médiatique, non efficient sur la prédiction "remplacement Bardella imminent" (non observée à mai 2026) ; PS efficient sur l'obtention de la suspension des retraites comme contrepartie au non-vote de censure ; Wauquiez efficient sur le maintien de la ligne LR (aucun député LR n'a basculé vers UDR-RN).

L'arène n'est pas la structure politique formelle — elle est la structure relationnelle effective révélée par les discours et confirmée ou modifiée par les effets observables.

---

## 6. Procédure en quatorze étapes (refonte v2.1)

M03 v2.1 procède en quatorze étapes ordonnées. Les étapes 1-4 sont préparatoires, les étapes 5-11 sont analytiques, les étapes 12-14 sont synthétiques. La refonte v2.1 ajoute une étape (matrice des objets visés) et enrichit deux étapes (efficience stratifiée, comparaison des chaînes causales).

### Étape 1 — Identification de la controverse

Délimitation de l'objet, de la séquence temporelle, et identification préliminaire des acteurs. Verdict d'applicabilité selon section 4.

### Étape 2 — Sélection des acteurs

Application des critères de sélection (pouvoir d'agir, audience, originalité, représentativité). Production de la liste des acteurs retenus avec justification de leur inclusion. Liste des acteurs exclus avec justification.

### Étape 3 — Constitution du corpus

Pour chaque acteur retenu, identification du ou des textes substantiels accessibles. Vérification de l'intégrité du verbatim. Décision sur le mode d'exécution (complet, dégradé, vigilance adversariale) pour chaque acteur.

### Étape 4 — Analyse M01 v2.1 préalable pour chaque acteur

M01 v2.1 est exécutée individuellement sur chaque texte du corpus. Les sorties M01-M validées sont la matière première de M03. M01 v2.1 inclut l'identification des objets thématiques et visés, la qualification d'efficience par objet, les chaînes causales amont et aval, le bloc V en quatre sous-blocs — ces éléments sont exploités directement par M03 v2.1.

Sur une controverse à six acteurs, M01 v2.1 doit être conduite six fois avant que M03 ne commence. C'est un coût d'entrée important mais nécessaire — il garantit que l'analyse comparative n'agrège pas des lectures bâclées.

### Étape 5 — Qualification efficience par acteur et par dimension (v2.1)

Pour chaque acteur, application de la définition de la section 5.2 — qualification d'efficience par dimension pertinente de la controverse. Les cas ambigus sont documentés. Cette qualification utilise les qualifications d'efficience par objet déjà produites en étape 4 (M01 v2.1) et les recompose à la maille de la controverse multi-acteurs.

### Étape 6 — Identification du noyau de propositions

Extraction du noyau de propositions structurantes de la controverse (typiquement trois à sept). Les propositions sont formulées dans des termes neutres qui permettent l'attribution sans ambiguïté des positions des acteurs. Le noyau est validé par retour aux textes — chaque acteur doit pouvoir être positionné sur chaque proposition.

### Étape 7 — Attribution des régimes épistémiques par acteur et par proposition

Pour chaque cellule de la matrice (acteur × proposition), application du gabarit v2.1 section 6.4 sur le régime épistémique. K, B, Affirme, ou Prétend_savoir selon les critères. L'attribution doit être documentée par citation précise.

Les cas où l'analyse hésite entre deux régimes sont signalés comme indices non convergents.

### Étape 8 — Identification des objets visés par acteur (nouveau v2.1)

Pour chaque acteur, extraction des objets visés identifiés en étape 4 (sortie M01 v2.1). Compilation de l'*union des objets visés* à travers tous les acteurs de la controverse. Cette compilation produit la liste des colonnes de la matrice des objets visés.

Pour chaque acteur, examen si chaque objet visé compilé est aussi visé par cet acteur (statut `visé`, `non_visé`, ou `ambigu`). Documentation de la `inference_confidence` et de l'efficience de l'acteur sur chaque objet visé selon le gabarit v2.1 sections 5.9 et 5.10.

### Étape 9 — Identification des désaccords et asymétries

Croisement systématique de la matrice des positions épistémiques. *Désaccords factuels* (K(p) vs K(¬p)). *Désaccords normatifs* (K(p) ou B(p) partagés mais divergence sur la prescription). *Asymétries d'expertise* (K vs B sur une proposition factuelle). *Prétentions abusives* (Prétend_savoir non validable indépendamment).

Pour chaque catégorie identifiée, documentation des acteurs concernés et de la citation précise.

### Étape 10 — Croisement matrices positions épistémiques et objets visés (nouveau v2.1)

Examen croisé des deux matrices pour identifier les cas saillants v2.1.

*Convergence sur objet visé avec divergence sur proposition* — plusieurs acteurs visent le même objet mais divergent sur les propositions structurantes. Lecture analytique : leurs intérêts stratégiques convergent malgré leurs désaccords de fond.

*Convergence sur proposition avec divergence sur objet visé* — plusieurs acteurs s'accordent sur une proposition mais visent des objets différents. Lecture analytique : leur accord apparent masque des intérêts stratégiques divergents.

*Coalitions tactiques* — convergence sur objet visé entre acteurs habituellement opposés. Ancrage empirique : Ciotti-RN sur la motion de censure du 16 octobre 2025 (convergence sur l'objet "chute du gouvernement Lecornu II") malgré divergences historiques.

*Convergences non anticipées* — convergence sur objet visé qui n'est explicitée par aucun des acteurs concernés. Lecture analytique : effet structural de la configuration de l'arène plus que stratégie consciente.

### Étape 11 — Identification des cadres interprétatifs concurrents

À partir des sorties M01-M de chaque acteur (notamment les blocs `lexicon_analysis` et `historiographies` v2.1), identification des cadres interprétatifs concurrents avec ancrage empirique documenté (section 5.5). Pondération par audience et consensus académique selon le gabarit v2.1 section 5.8.

Identification des cadres qui structurent le discours de chaque acteur (un acteur peut mobiliser plusieurs cadres). Distinction entre mobilisation `thematic_explicit` et mobilisation `lexical_marginal` héritée de M01 v2.1 étape 12.

### Étape 12 — Cartographie de la structure de l'arène et chaînes causales aval comparées (enrichi v2.1)

À partir des sorties M01-M (notamment les blocs sur l'audience visée, les références aux autres acteurs, les alliances déclarées), construction du graphe relationnel de l'arène (section 5.6).

*Chaînes causales aval comparées (v2.1).* À partir du sous-bloc V.4 de chaque sortie M01 v2.1, compilation des effets observables sur les objets visés pour chaque acteur. Mise en parallèle multi-acteurs pour identifier qui a atteint ses objets visés, qui ne les a pas atteints, et quels effets ont profité à quel acteur. Cette compilation fait apparaître les *asymétries de bénéfice* (un effet observable bénéficie plus à un acteur qu'à un autre) et les *prédictions invalidées* (objets visés prédits par certains acteurs non observés dans la fenêtre temporelle).

### Étape 13 — Synthèse comparative et hypothèses concurrentes

Production de la synthèse en trois niveaux. *Faits établis* sur la controverse — propositions sur lesquelles convergent K de plusieurs acteurs avec sources indépendantes établies. *Inférences* sur la structure de la controverse — caractérisation des désaccords (factuels, normatifs, asymétries, prétentions), des convergences et divergences stratégiques révélées par les deux matrices, des cadres interprétatifs concurrents, de la structure de l'arène, des asymétries de bénéfice dans les chaînes causales aval. *Hypothèses concurrentes* sur la dynamique de la controverse — au moins trois hypothèses, dont au moins deux portant sur les acteurs non-efficients ou efficients_partiels et leur effet sur l'arène.

Application de la convention 6.7 du gabarit v2.1 sur l'écart de confidence des hypothèses. Distinction maintenue entre chaînes causales (étapes 8 et 12) et hypothèses concurrentes (étape 13) selon le gabarit v2.1 section 6.8.

### Étape 14 — Production des sorties M03

Production de la sortie humaine M03-H, de la sortie machine M03-M (YAML avec schéma propre intégrant les deux matrices et les chaînes causales comparées), et de la sortie publique M03-P. Discipline de séparation sortie humaine / journal méthodologique selon le gabarit v2.1 section 9.0.

---

## 7. Contrôles internes propres à M03

M03 hérite des contrôles internes du gabarit v2.1 section 7 et y ajoute quatre contrôles propres.

*Contrôle de couverture du noyau.* Chaque acteur doit pouvoir être positionné sur chaque proposition du noyau. Les positions silencieuses sont documentées sans être traitées comme défaut analytique.

*Contrôle de cohérence matrice positions épistémiques / texte source.* Pour chaque attribution dans la matrice, citation précise du texte source qui la justifie. Échantillonnage par l'auditeur.

*Contrôle de cohérence matrice des objets visés / sortie M01 (nouveau v2.1).* Pour chaque cellule de la matrice des objets visés, vérification de la cohérence avec la sortie M01-M individuelle de l'acteur. Si un objet visé est identifié pour un acteur dans M03 sans être présent dans la sortie M01-M de cet acteur, signal de défaut.

*Contrôle de la distinction efficient / non-efficient par objet et par dimension.* La qualification doit être documentable et tracée. L'auditeur vérifie que la qualification reflète la situation effective de l'acteur sur la dimension ou l'objet spécifique, pas une qualification générique.

---

## 8. Dégradation gracieuse

M03 applique les quatre paliers du gabarit v2.1 section 8 avec adaptations spécifiques.

*Palier 1 — verbatim partiel pour certains acteurs.* Si un sous-ensemble des acteurs du corpus est en mode dégradé sur leur sortie M01 individuelle, M03 documente la dégradation par acteur et la prend en compte dans le plafonnement de confidence des cellules concernées.

*Palier 2 — contexte difficile sur certaines dimensions.* Si une dimension de la controverse est mal documentable, M03 peut signaler son traitement partiel sans abandonner la méthode globalement.

*Palier 3 — saturation cognitive.* Avec plus de dix acteurs, M03 produit la matrice par lots avec synthèse.

*Palier 4 — rentabilité épistémique insuffisante.* Si l'analyse ne fait pas apparaître de désaccords structurants ni de divergences stratégiques substantielles, M03 produit une sortie minimale qui le déclare.

---

## 9. Sortie humaine M03-H

M03 produit une sortie humaine structurée différemment de M01-H pour refléter la dimension comparative. Discipline de séparation sortie humaine / journal méthodologique (gabarit v2.1 section 9.0).

Structure en neuf blocs.

*Bloc I — Présentation de la controverse.* Objet structurant, séquence temporelle, acteurs retenus avec justification de leur inclusion, contexte général.

*Bloc II — Fiches d'énonciation des acteurs.* Pour chaque acteur, fiche d'énonciation héritée de la sortie M01-H individuelle, avec mention de l'efficience par dimension de la controverse.

*Bloc III — Noyau de propositions structurantes.* Énoncé des propositions du noyau (trois à sept).

*Bloc IV — Matrice des positions épistémiques.* Présentation lisible de la matrice K/B/Affirme/Prétend_savoir avec annotations et citations précises.

*Bloc V — Matrice des objets visés (v2.1).* Présentation lisible de la matrice des objets visés multi-acteurs avec confidences, efficiences et citations précises.

*Bloc VI — Croisement des matrices et cas saillants (v2.1).* Convergences sur objet visé avec divergence sur proposition, convergences sur proposition avec divergence sur objet visé, coalitions tactiques, convergences non anticipées. Pour chaque cas saillant, lecture analytique.

*Bloc VII — Cadres interprétatifs et structure de l'arène.* Cadres concurrents identifiés avec ancrage empirique et pondération. Graphe relationnel de l'arène avec relations identifiées.

*Bloc VIII — Chaînes causales aval comparées (v2.1).* Pour chaque acteur, effets observables sur ses objets visés dans la fenêtre temporelle. Asymétries de bénéfice identifiées. Prédictions invalidées documentées.

*Bloc IX — Synthèse et blocs de neutralisation.* Synthèse en trois statuts épistémiques. Hypothèses concurrentes avec convention 6.7. Résultats nuls. Ce que la controverse dit correctement sur la situation. Indices non convergents. Conditions de révision.

---

## 10. Sortie publique M03-P

M03 produit la sortie publique selon le gabarit v2.1 section 10 — cinq éléments dans l'ordre, cent cinquante à trois cents mots. Adaptation à la dimension comparative.

*Élément 1.* Une phrase qui dit qu'est-ce que la controverse, quels acteurs, dans quel cadre, à quelle date.

*Élément 2.* Deux à trois phrases qui énoncent le ou les constats les plus solides — désaccord factuel établi, divergence stratégique saillante, asymétrie de bénéfice documentée — avec leur régime épistémique.

*Élément 3.* Hypothèses concurrentes sur la dynamique de la controverse avec écart de confiance. Application de la convention 6.7.

*Élément 4.* Renvois — vers la sortie M03-H complète et vers les sources primaires des acteurs.

*Élément 5.* Bloc de clôture logique — solide / plausible / fragile.

---

## 11. Sortie machine M03-M

M03 produit le YAML conforme au schéma du gabarit v2.1 section 11 avec adaptations pour la dimension comparative.

Schéma Pydantic spécifique à M03 v2.1 :

```yaml
method_id: M03_ANALYSE_COMPARATIVE_MULTI_ACTEURS
method_version: 2.1
analysis_id: string
execution_date: date
execution_mode:
  - applicable_complete
  - applicable_degraded
  - applicable_vigilance_adversariale
  - not_applicable

controversy:
  object: string
  temporal_sequence: string
  date_range: [start, end]

actors: list[Actor]

Actor:
  actor_id: string
  name: string
  role_at_date: string
  m01_analysis_id: string             # référence à l'analyse M01 v2.1 individuelle
  efficiency_by_dimension: list[EfficiencyByDimension]
  execution_mode_on_m01: string

EfficiencyByDimension:
  dimension_label: string
  efficiency_status:
    - efficient
    - efficient_partiel
    - non_efficient
  justification: string

structuring_propositions: list[StructuringProposition]

StructuringProposition:
  proposition_id: string               # P1, P2, etc.
  label: string                        # énoncé en termes neutres
  source_documentability: string

epistemic_position_matrix: list[EpistemicCell]

EpistemicCell:
  actor_id: string
  proposition_id: string
  regime:
    - K
    - B
    - Asserts
    - ClaimsToKnow
    - silent
    - ambiguous_B_Asserts
    - ambiguous_K_ClaimsToKnow
  source_citation: string
  confidence: float
  confidence_applies_to: inference

targeted_objects_matrix: list[TargetedObjectCell]   # nouveau v2.1

TargetedObjectCell:
  actor_id: string
  targeted_object_id: string
  targeted_object_label: string
  status:
    - aimed
    - not_aimed
    - ambiguous
  inference_confidence: float
  inference_confidence_applies_to: inference
  grounded_in: list[string]
  efficiency_status:
    - efficient
    - efficient_partiel
    - non_efficient

cross_matrix_salient_cases: list[CrossMatrixCase]   # nouveau v2.1

CrossMatrixCase:
  type:
    - convergence_aim_divergence_proposition
    - convergence_proposition_divergence_aim
    - tactical_coalition
    - unanticipated_convergence
  actors_involved: list[string]
  description: string
  analytical_reading: string

interpretive_frames: list[InterpretiveFrame]

InterpretiveFrame:
  frame_label: string
  empirical_grounding: list[string]    # cas externes au projet documentant ce cadre
  consensus_level:
    - disqualified
    - marginal
    - contested
    - strong_consensus
  mobilizing_actors: list[string]

arena_structure:
  nodes: list[string]                  # acteurs
  edges: list[ArenaEdge]

ArenaEdge:
  source_actor: string
  target_actor: string
  relation_type:
    - responds_to
    - allies_with
    - opposes
    - ignores
    - cites
  source_citation: string

comparative_downstream_chains: list[ActorDownstreamChain]   # nouveau v2.1

ActorDownstreamChain:
  actor_id: string
  observable_effects: list[ObservableEffect]   # hérité de M01 v2.1 sous-bloc V.4

asymmetries_of_benefit: list[BenefitAsymmetry]   # nouveau v2.1

BenefitAsymmetry:
  effect_label: string
  actors_benefiting: list[string]
  actors_not_benefiting: list[string]
  documentation: string

invalidated_predictions: list[InvalidatedPrediction]   # nouveau v2.1

InvalidatedPrediction:
  actor_id: string
  predicted: string
  observation_to_date: string
  source_citation: string

epistemic_synthesis:
  established_facts: list[string]
  inferences: list[Inference]
  competing_hypotheses: list[Hypothesis]
  hypothesis_gap: float
  hypothesis_status:
    - zone_of_indetermination
    - uncertain_dominance
    - clear_dominance

null_results:
  searched_not_found: SearchedNotFound
  rhetorically_ordinary_elements: list[string]
  non_convergent_indices: list[string]
  what_the_controversy_states_correctly: list[string]

invisible_and_revision:
  invisible_from_this_post: list[string]
  revision_conditions: list[string]
  next_methods_recommended: list[string]
```

Validation supplémentaire v2.1 — chaque `TargetedObjectCell` avec status `aimed` doit avoir `grounded_in` non vide, chaque `InterpretiveFrame` doit avoir `empirical_grounding` avec au moins deux cas externes documentés.

---

## 12. Articulation au graphe cognitif

M03 produit les exports graphe selon le gabarit v2.1 section 12. Nouveaux nœuds et arêtes propres à M03 v2.1 — `Controversy`, `StructuringProposition`, `InterpretiveFrame`, `BenefitAsymmetry`. Arêtes — `takes_position_on` (Actor → StructuringProposition avec regime), `aims_at_in_controversy` (Actor → TargetedObject), `mobilizes_frame` (Actor → InterpretiveFrame), `benefits_from` (Actor → ObservableEffect).

---

## 13. Critères d'évaluation propres à M03

M03 hérite des sept critères transversaux du gabarit v2.1 section 13 et y ajoute trois critères propres.

*Critère de couverture du noyau.* Chaque acteur positionné sur chaque proposition du noyau, ou position silencieuse documentée.

*Critère de cohérence inter-matrices (v2.1).* Les deux matrices (positions épistémiques et objets visés) sont cohérentes entre elles et avec les sorties M01-M individuelles. Pas de désaccord interne.

*Critère de cas saillants identifiés (v2.1).* Au moins un cas saillant identifié dans le croisement des deux matrices — convergence stratégique malgré divergence thématique, ou inverse. Si aucun cas saillant n'est identifié, soit la controverse est purement thématique sans dimension stratégique (cas rare), soit l'analyse est incomplète.

---

## 14. Cas-jouets de calibration

M03 v2.1 dispose d'un jeu de cas-jouets à instancier.

*Cas-jouet principal v2.1.* Séquence retraites octobre 2025 — Lecornu, Ciotti, et au moins un acteur supplémentaire parmi Wauquiez, Chatelain, Bardella, Vallaud, Bayrou. Test de la matrice des positions épistémiques + matrice des objets visés sur la controverse. Validation attendue — convergence sur objet visé "chute du gouvernement" entre LFI et UDR-RN malgré divergences thématiques, divergence sur objet visé entre PS et LFI malgré convergence partielle sur certaines propositions.

*Cas-jouet à instancier.* Séquence loi immigration décembre 2023 - janvier 2024 — gouvernement, opposition parlementaire, Conseil constitutionnel, partenaires sociaux. Test de la matrice sur controverse multi-institutions.

---

## 15. Limites de M03

*Controverses à très nombreux acteurs.* Au-delà d'une dizaine d'acteurs, M03 perd en lisibilité. Une décomposition en sous-controverses ou en groupes d'acteurs est nécessaire.

*Controverses sans verbatim accessible pour certains acteurs.* Si plusieurs acteurs centraux sont en mode dégradé sur leur sortie M01, la rentabilité épistémique de M03 baisse. Seuil à éprouver — probablement dégradation acceptable jusqu'à un tiers des acteurs en mode dégradé.

*Controverses internationales.* M03 v2.1 est calibrée sur le contexte politique français. Application à des controverses européennes ou internationales demande adaptation des cadres interprétatifs et des conventions de genre.

---

## 16. Journal méthodologique de M03

M03 tient un journal méthodologique propre selon le gabarit v2.1 section 16.

*method_evolution.* Le passage v2 → v2.1 documente l'ajout de la matrice des objets visés et de la comparaison des chaînes causales aval, selon le document de coordination v2.1.

*case_execution.* À renseigner avec les premières applications M03 v2.1 (priorité — séquence retraites octobre 2025).

*failure_pattern.* À enrichir au fil des applications. Patterns hérités du gabarit v2.1 section 16. Pattern propre à M03 à surveiller — agrégation de positions épistémiques d'acteurs sans vérification de cohérence avec les sorties M01-M individuelles.

*typology_audit (v2.1).* Premier audit — cadres interprétatifs ancrés empiriquement avec cas externes documentés (technocratique-actuariel, social-démocrate, libéral-individualiste, souverainiste-protectionniste, écologiste-décroissant — tous ancrés). Régimes K/B/Affirme/Prétend_savoir ancrés philosophiquement (Williamson, Hintikka, Stalnaker). Typologie des relations d'arène ancrée empiriquement dans la pratique de l'analyse politique (Bourdieu sur le champ politique, Lagroye sur la sociologie politique).

---

*M03 v2.1 — entrée en vigueur immédiate. Remplace M03 v2. Première application prioritaire — séquence retraites octobre 2025 avec Lecornu, Ciotti, et acteurs complémentaires, en exploitant les sorties M01 v2.1 déjà produites (Lecornu v2.1, Ciotti v2.1) et en conduisant les M01 v2.1 manquantes.*
