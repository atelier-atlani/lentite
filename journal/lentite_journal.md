# L'Entité — Journal méthodologique général

*Mémoire institutionnelle du projet. Trace les évolutions doctrinales, les découvertes méthodologiques transversales, les frictions identifiées, les critiques externes examinées, les décisions structurantes. Document factuel et daté. Distinct des journaux méthodologiques propres à chaque méthode (M01, M03) qui tracent les évolutions internes de ces méthodes.*

---

## 1. Préambule

Ce journal général sert quatre fonctions.

— *Mémoire institutionnelle.* Conserver la trace des décisions doctrinales et architecturales qui ne sont pas explicites dans les documents canoniques. Permettre à toute reprise ultérieure (par Seb, par un collaborateur, par une instance future de Claude) de comprendre pourquoi le projet est dans son état courant.

— *Transparence méthodologique.* Documenter les choix qui auraient pu être différents, les pistes explorées et abandonnées, les frictions résolues. Permettre l'audit externe et la critique informée.

— *Surveillance des patterns du projet lui-même.* Tracer les patterns d'échec de gouvernance du projet (distincts des failure_patterns analytiques inscrits aux journaux de chaque méthode) — chronological_cumulation_of_amendments, self_cumulation_of_coordination_documents, etc.

— *Préparation à l'évolution.* Identifier les zones de friction non encore résolues, les questions ouvertes, les hypothèses de v3 à examiner.

Le journal est append-only en pratique. Les entrées sont datées et ordonnées. Une entrée n'est jamais supprimée — si une décision est révisée, une nouvelle entrée est ajoutée pour documenter la révision.

---

## 2. Évolutions doctrinales majeures

### 2.1 Phase initiale → v2 (période précédant le journal courant)

Phase de constitution du projet. Définition de la phrase-cœur ("la vérité est dans la qualité du chemin"), de la figure (enquêteur forensique), des quatre engagements de l'ADN, des trois modes opérationnels (1 éclairage médiatique, 2 conseiller du prince, 3 chat public).

Architecture en trois couches établie — couche A (charte), couche B (gabarit), couche C (méthodes).

Première méthode produite — M01 (analyse rhétorique d'un discours public). Premier cas-jouet substantiel testé — Ciotti v2 sur réponse à DPG Lecornu du 14 octobre 2025.

### 2.2 v2 → v2.1 — refonte par stratification

Date approximative — début mai 2026.

**Motif de la transition.** Trois frictions identifiées dans le rejeu du cas Ciotti v2 et dans l'examen rétrospectif des analyses précédentes.

*Friction 1 — lisibilité M01-H.* La sortie humaine devenait surchargée de méta-discours méthodologique (notes sur les choix d'interprétation, recommandations pour révision du gabarit, calibration de version). Le lecteur informé non-analyste perdait le fil. *Résolution v2.1* — discipline de séparation M01-H / journal méthodologique de la méthode (gabarit v2.1 section 9.0). La M01-H présente l'analyse rhétorique structurée ; le méta-discours va au journal séparé.

*Friction 2 — efficience binaire trop grossière.* La qualification "efficient" / "non-efficient" appliquée globalement à un acteur sur un discours masquait des configurations stratégiques saillantes. Le cas Ciotti — non-efficient sur la chute du gouvernement (objet thématique principal) mais efficient sur la consolidation publique de l'alliance UDR-RN et le positionnement électoral (objets visés) — révélait que la binarité était fausse. *Résolution v2.1* — stratification de l'efficience par objet (gabarit v2.1 sections 2.2, 2.3, 5.9, 5.10). Identification obligatoire d'objets thématiques et d'objets visés, qualification d'efficience par objet (trois valeurs — efficient, efficient_partiel, non_efficient).

*Friction 3 — chaînes causales non explicitement tracées.* L'engagement 4 de l'ADN (refus de présupposer la chaîne causale) était inscrit doctrinalement mais pas opérationnellement. Les analyses sautaient directement à l'inférence sans documenter explicitement la chaîne causale amont (ce qui a nourri le discours) et la chaîne causale aval (les conséquences plausibles). *Résolution v2.1* — chaînes causales amont et aval comme objets d'enquête formels (gabarit v2.1 section 5.11). Bloc V de la sortie humaine refondé en quatre sous-blocs (V.1 chaîne amont, V.2 objets visés et chaîne aval, V.3 écarts sur objet thématique, V.4 effets observables).

**Conséquences architecturales.** Refonte de la charte (couche A, section 5 sur les deux dimensions de l'objet, section 6.6 sur les patterns observés vs fabriqués). Refonte du gabarit (couche B — 16 sections normatives, sept patterns temporels avec ancrage empirique, schéma Pydantic enrichi). Refonte ciblée de M01 (étapes 1 et 11 refondues, étape 12 enrichie). Extension de M03 (matrice des objets visés, chaînes causales aval comparées, cas saillants v2.1).

**Doctrine sur les patterns établie à l'occasion de la transition.** Patterns observés empiriquement (motifs récurrents observables dans la pratique d'un métier, attestés par au moins 2-3 cas externes documentables) — légitimes et nécessaires à l'analyse compétente. Patterns fabriqués a priori (catégories typologiques construites par l'analyse sans ancrage empirique) — à requalifier en inférences. L'inférence reste première — préserve la singularité du cas. Les patterns observés nourrissent l'inférence sans s'y substituer. Statut spécifique des failure_patterns du journal — patterns de gouvernance du projet, distincts des typologies analytiques des métiers observés (charte v2.1 section 6.6).

### 2.3 v2.1 → v2.1.1 — révision mineure

Date — mai 2026.

**Motif.** Critique externe par LLM tiers formalisée et examinée systématiquement (voir section 6 du présent journal). Deux observations méritaient surveillance statistique périodique sans modification des contraintes normatives existantes.

**Contenu de la révision.** Ajout de deux catégories d'entrée canoniques au journal méthodologique (gabarit section 16) — `intentionality_bias_audit` (surveillance de la fréquence des hypothèses intentionnelles dominantes, seuil d'alerte 80%) et `hypothesis_gap_audit` (surveillance de la distribution des écarts hypothèses, seuils d'alerte multiples). Aucune contrainte normative existante modifiée. Toute analyse v2.1 demeure conforme v2.1.1 sans rejeu nécessaire.

**Décision documentée.** Pas de modification des seuils 0,2 / 0,4 de la convention 6.7. Pas d'ajout de coefficient correctif sur les hypothèses non intentionnelles. La doctrine v2.1 tient — le dispositif d'audit permet de détecter dans la durée d'éventuelles dérives sans préempter le diagnostic.

---

## 3. Découvertes méthodologiques transversales

### 3.1 Clivage stabilité / rupture transversal aux clivages thématiques classiques

*Découverte révélée par* — croisement des matrices positions épistémiques + objets visés dans l'application M03 v2.1 sur séquence retraites octobre 2025.

*Énoncé.* Les acteurs qui visent la stabilité institutionnelle (Lecornu PM macroniste, Vallaud direction PS) convergent tactiquement *par-delà leur opposition politique*. Les acteurs qui visent la rupture institutionnelle (Ciotti UDR-RN, Panot LFI, frondeurs PS) convergent tactiquement *par-delà leurs divergences doctrinales totales*. Le clivage stabilité/rupture est *transversal* aux clivages gauche/droite et aux propositions thématiques structurantes.

*Implication méthodologique.* La doctrine v2.1 (matrice des objets visés + matrice des positions épistémiques croisées) rend visibles des structures invisibles à la lecture thématique seule. Sans la stratification de l'efficience par objet, le clivage n'apparaîtrait pas.

*Hypothèse pour généralisation.* Ce pattern de clivage stratégique pourrait être généralisable à d'autres controverses politiques contemporaines. À éprouver sur d'autres applications M03 v2.1 — séquence loi immigration décembre 2023, séquences présidentielles, autres séquences budgétaires.

### 3.2 La CFDT comme pivot transversal de légitimation

*Découverte révélée par* — convergence non explicitée Lecornu-Vallaud sur l'objet visé OV_E (alliance CFDT) dans l'application M03 v2.1.

*Énoncé.* La CFDT fonctionne dans la séquence comme acteur tiers de légitimation qui rend possible le compromis Lecornu-Vallaud. Lecornu reprend textuellement la formule CFDT ("aucun relèvement de l'âge n'interviendra") dans sa DPG. Vallaud revendique la suspension comme "reconnaissance du combat mené par les organisations syndicales". Le compromis CFDT-PS-gouvernement est rendu présentable politiquement pour les deux camps par la médiation syndicale.

*Implication structurelle.* La doctrine paritariste française tient transversalement aux clivages politiques classiques. Cette doctrine, inscrite dans la tradition du Conseil national de la résistance et le préambule constitutionnel de 1946, fournit aux acteurs politiques contemporains un cadre de légitimation transversal sur les réformes sociales.

*Hypothèse pour généralisation.* Pattern attestable empiriquement sur d'autres séquences sociales françaises depuis 1981 (Mauroy / blocage des prix, Jospin / 35 heures, Sarkozy / autonomie des universités, Hollande / ANI 2013, Macron / SNCF 2018). Le rôle pivot des centrales syndicales modérées (CFDT principalement) dans la légitimation transversale des réformes négociées est un pattern observé empiriquement, à documenter dans la couche analytique future.

### 3.3 Engagements parlementaires à seuil structurellement sous-déterminés

*Découverte révélée par* — analyse Vallaud v2.1, engagement 3 sur la "sanction du gouvernement tout au long du débat budgétaire si engagements non tenus".

*Énoncé.* Les engagements parlementaires qui prennent la forme de "sanction conditionnelle" ou "vigilance" sont *par construction sous-déterminés dans leur seuil de déclenchement*. La formulation initiale ne spécifie pas ce qui compte précisément comme rupture suffisamment grave pour déclencher la sanction. Le seuil effectif révèle la fonction réelle de l'engagement — signal politique (engagement performatif pour positionnement) plutôt que contrainte stricte (engagement substantif avec mécanique de déclenchement).

*Confirmation empirique.* Le PS n'a pas exercé la "sanction" par censure quand Lecornu a rompu l'engagement 49.3 en janvier 2026 (pattern `broken_explicitly` + public_motivation_invoked sur la DPG, observé in situ). La sanction promise s'est traduite par votes critiques et amendements, pas par censure. Pattern temporel retenu — `observed_otherwise` (l'engagement a été réalisé sous une forme modifiée par rapport à la formulation initiale).

*Implication méthodologique.* Pour les analyses futures, distinguer dans le bloc V.3 les engagements *substantifs* (acte précis dans une fenêtre claire) des engagements *à seuil* (sanction conditionnelle, vigilance, exigence diffuse). Les seconds demandent attention spéciale — leur réalisation effective révèle leur fonction politique réelle.

### 3.4 Asymétries de bénéfice révélant la structure profonde

*Découverte révélée par* — étape 12 de M03 v2.1 application (chaînes causales aval comparées).

*Énoncé.* Les bénéfices observables d'un effet ne suivent pas mécaniquement la structure des coalitions politiques apparentes. Cas saillant — l'effet "rupture explicite de l'engagement 49.3 par Lecornu en janvier 2026" bénéficie *rétrospectivement* à Ciotti et à LFI (validation de leur critique du gouvernement) alors qu'aucun des deux n'avait directement provoqué la rupture. À l'inverse, cet effet *affaiblit* Vallaud (sanction promise non exercée).

*Implication méthodologique.* L'analyse comparative doit documenter explicitement les asymétries de bénéfice (étape 12.2 de M03 v2.1) parce qu'elles révèlent ce que les coalitions de circonstance ne disent pas — la structure profonde des intérêts stratégiques. Sans cette documentation, l'analyse rate la dimension la plus signifiante de la séquence.

*Conséquence pour le schéma Pydantic.* Modèle `BenefitAsymmetry` ajouté au schéma M03 v2.1 avec contrainte `actors_benefiting` non vide. Implémenté dans `pipeline/schemas_m03.py`.

### 3.5 Distinction mobilisation thématique / mobilisation lexicale-marginale d'une historiographie

*Découverte révélée par* — analyse Ciotti v2 sur l'usage de "submersion migratoire" (U9), terme emprunté lexicalement au cadre du "grand remplacement" (historiographie disqualifiée selon le consensus académique).

*Énoncé.* Le gabarit v2 traitait les historiographies par leur niveau de consensus académique (disqualifiée, marginale, contestée, consensus fort) sans distinguer le *type de mobilisation*. Une historiographie peut être mobilisée *thematiquement-explicitement* (adhésion ou critique explicite au cadre, intégration des thèses) ou *lexicalement-marginalement* (emprunt lexical ponctuel sans thématisation explicite). La distinction est analytiquement importante quand l'historiographie sous-jacente est disqualifiée — l'emprunt lexical signale une porosité ou une stratégie d'évitement de la classification disqualifiée, sans adhésion thématique complète.

*Résolution v2.1.* Champ `mobilization_type` ajouté au schéma `Historiography` (gabarit v2.1 section 9.6, schéma Pydantic section 11). Deux valeurs — `thematic_explicit` ou `lexical_marginal`.

*Conséquence pour les analyses.* Le cas Ciotti U9 "submersion migratoire" est classé en `lexical_marginal` du cadre grand_remplacement (disqualified), ce qui permet de signaler le contenu éthiquement non neutralisé (bloc VIII sous-bloc cinq) sans surcharger l'analyse globale en classification disqualifiée.

### 3.6 Sept patterns temporels avec ancrage empirique

*Découverte révélée par* — passage du gabarit v2 (six patterns) à v2.1 (sept patterns).

*Énoncé.* La typologie des patterns temporels d'écart entre discours et actes doit être ancrée empiriquement par cas externes au projet documentables. Six patterns initiaux — `not_yet_observed`, `never_observed`, `observed_later`, `observed_otherwise`, `observed_by_other_actor`, `prevented_by_constraint`. Sept patterns v2.1 — ajout de `broken_explicitly` (engagement publiquement révisé ou abandonné par le locuteur lui-même, avec motivation publique invoquée).

*Ancrage empirique de `broken_explicitly`.* Hollande sur la déchéance de nationalité janvier-mars 2016 (annoncée après les attentats, retirée après l'impossibilité d'obtenir l'accord parlementaire, avec motivation publique invoquant l'impasse). Lecornu sur le 49.3 en janvier 2026 (annoncé dans la DPG du 14 octobre 2025 comme rupture méthodologique, renié le 19 janvier 2026 face à l'impossibilité de faire voter le budget par majorité, avec motivation publique invoquant 350 heures de débat sans issue). Hollande sur les retraites en 2014 (engagement réinterprété face aux contraintes budgétaires européennes).

*Contrainte mordante implémentée.* Le pattern `broken_explicitly` exige le champ `public_motivation_invoked` non null. Sans cette motivation, le pattern est requalifié en `never_observed` (silence inexpliqué). Validation automatique par le validator custom `validate_pattern_constraints` du schéma Pydantic.

### 3.7 Discipline anti-cumul des documents de coordination

*Découverte révélée par* — observation de l'auto-cumul potentiel des documents de coordination lors de la transition v2 → v2.1.

*Énoncé.* Lors d'une transition de version, un document de coordination est produit pour articuler les changements. Si chaque nouvelle transition produit un nouveau document de coordination sans archiver les précédents, on accumule des documents de coordination contradictoires ou redondants. Le pattern est self_cumulation_of_coordination_documents — auto-cumul.

*Discipline appliquée.* Un seul document de coordination canonique courant. Lors d'une nouvelle transition, le précédent est archivé au journal et le nouveau remplace. Pas de version successive empilée.

*Inscription au journal comme failure_pattern de gouvernance.* Distinct des failure_patterns analytiques (patterns d'erreur de raisonnement dans les analyses) — c'est un pattern de discipline du projet lui-même.

### 3.8 Test décisif du pipeline opérationnel

*Découverte révélée par* — passage de la doctrine documentaire au pipeline Python opérationnel.

*Énoncé.* La traduction de la doctrine v2.1 en schéma Pydantic + validateur CLI a révélé que certaines parties de la doctrine étaient implicitement formulées et nécessitaient explicitation. Notamment — la typologie `ObservableEffectType` a dû être étendue pour intégrer les catégories effectivement utilisées dans les analyses (`amplification_memorielle_non_anticipable` pour Fabius-Badinter, `amplification_doctrinale_partielle_contestation_politique_sans_rupture_institutionnelle`, etc.). Chaque ajout est ancré empiriquement par le cas concret qui le motive.

*Implication méthodologique.* La friction productive entre doctrine documentaire et implémentation technique est utile — elle révèle les zones d'imprécision de la doctrine et force l'explicitation. Conforme à la doctrine de la charte v2.1 section 6.6 sur les patterns observés, mais signale la nécessité d'un audit périodique de la typologie pour éviter sa prolifération non contrôlée. Catégorie d'entrée `typology_audit` inscrite au journal méthodologique des méthodes.

*Validations transversales réalisées.* Huit analyses M01 v2.1 validées (4 cas réels + 4 cas-jouets). Une application M03 v2.1 validée. Trois tests négatifs confirment que les contraintes mordent.

---

## 4. Failure patterns de gouvernance du projet

*Patterns d'échec récurrents dans la conduite du projet lui-même, distincts des failure_patterns analytiques inscrits au journal de chaque méthode (qui tracent les erreurs de raisonnement dans les analyses).*

### 4.1 `chronological_cumulation_of_amendments`

*Pattern.* Lors d'une révision doctrinale, accumuler les amendements par ordre chronologique sans les repositionner par niveau d'architecture (charte / gabarit / méthode). Produit un patchwork où la trace historique l'emporte sur la cohérence logique.

*Discipline appliquée.* Repositionnement méthodique par niveau d'architecture lors de chaque révision. Le document de coordination de la transition v2 → v2.1 a été refait deux fois précisément pour éviter ce pattern — la deuxième version intégrait les trois frictions par niveau d'architecture cohérent (lisibilité → couche C M01, efficience stratifiée → couche B gabarit puis couche A charte, chaînes causales → couche B gabarit puis couche A charte).

### 4.2 `self_cumulation_of_coordination_documents`

*Pattern.* Voir section 3.7. Cumul des documents de coordination eux-mêmes lors de transitions successives. Pattern annexe — un document de coordination produit pour résoudre les frictions internes peut lui-même devenir source de cumul.

*Discipline appliquée.* Un seul document de coordination canonique par transition. Archivage au journal du précédent. Pas d'empilement.

### 4.3 (Patterns potentiels à surveiller)

— *`premature_v3_engagement`* — engager une refonte majeure (v3) avant d'avoir accumulé suffisamment de données empiriques pour la motiver. Surveillance maintenue. Doctrine actuelle — ne pas engager v3 avant d'avoir au moins dix à vingt nouvelles analyses produites permettant d'alimenter les audits inscrits au gabarit v2.1.1.

— *`deference_to_external_LLM_authority`* — accepter une critique externe par LLM tiers sans examen systématique, par déférence à l'autorité supposée du système concurrent. Surveillance maintenue. Doctrine actuelle — examiner systématiquement avec position prise sur chaque point (intégration, rejet motivé, ou requalification). La critique externe Gemini de mai 2026 a été traitée selon cette discipline (voir section 6).

— *`typology_proliferation`* — multiplier les catégories typologiques (effets observables, vulnérabilités, patterns) sans ancrage empirique systématique. Surveillance maintenue. Doctrine actuelle — `typology_audit` périodique selon le critère d'ancrage empirique de la charte v2.1 section 6.6.

---

## 5. Failure patterns analytiques (synthèse inter-méthodes)

*Patterns d'erreur de raisonnement identifiés au fil des analyses, à surveiller dans toute exécution de méthode. Liste inscrite aux journaux méthodologiques des méthodes (M01, M03) — répétée ici pour visibilité transversale.*

— `valid_form_with_false_premise` — argument de forme valide mais avec prémisse fausse. Erreur fréquente sur les attributions causales politiques.

— `hidden_premise_not_marked` — prémisse implicite non identifiée et donc non examinée. Erreur fréquente sur les argumentations à structure complexe.

— `confidence_treated_as_truth` — confidence sur une inférence prise comme certitude sur la vérité de la proposition inférée. Confusion entre `confidence_applies_to: inference` et `confidence_applies_to: hypothesis`.

— `temporal_sequence_treated_as_causality` — post hoc ergo propter hoc. Erreur fréquente sur les bilans politiques (cas-jouet 1 — fixture canonique pour calibration).

— `omission_treated_as_intention` — omission systématiquement interprétée comme intentionnelle alors que des explications structurelles ou stratégiques probables existent. Discipline — trois niveaux d'omission (structurelle / stratégique probable / intentionnelle non prouvée) du gabarit v2.1 section 5.5.

— `speaker_belief_treated_as_knowledge` — usage non factif de K dans les attributions mentales. Discipline — quatre opérateurs distincts (K / B / Affirme / Prétend_savoir) du gabarit v2.1 section 5.3 et 6.4.

---

## 6. Critiques externes examinées

### 6.1 Critique LLM tiers — mai 2026

*Origine.* Critique externe par LLM tiers (Gemini) sur la doctrine v2.1, formalisée en quatre points (matrice d'évaluation incluse).

*Examen méthodique du projet.* Chaque point examiné avec position prise (intégration, rejet motivé, ou requalification).

**Point 2.A — Concentration des écarts hypothèses sur la zone d'indétermination.** Observation factuelle juste — sept cas testés au moment de la critique, six en zone d'indétermination ou à la limite supérieure du `uncertain_dominance`. Lecture en "neutralité molle systématique" rejetée comme excessive. Correction proposée (modificateur de densité documentaire) rejetée comme patch sans fondement doctrinal. *Intégration v2.1.1* — catégorie d'audit `hypothesis_gap_audit` ajoutée pour surveillance statistique périodique. Pas de modification des seuils 0,2 / 0,4. La doctrine v2.1 tient.

**Point 2.B — Biais machiavélique inhérent au parsing.** Observation juste empiriquement — sur les analyses produites, l'hypothèse intentionnelle dominante apparaît systématiquement (confidence > 0,80) avec hypothèse non intentionnelle plafonnée (≤ 0,55). Lecture en "paranoïa algorithmique systémique" rejetée comme excessive. Correction proposée (coefficient bonus +0,15 sur hypothèses non intentionnelles) rejetée comme correctif statistique sans fondement épistémique. *Intégration v2.1.1* — catégorie d'audit `intentionality_bias_audit` ajoutée. Pas de coefficient correctif.

**Point 2.C — Biais documentaire de la trace écrite.** Observation juste — L'Entité parse des productions textuelles publiques certifiées et ignore les sources off-the-record, fuites, briefings. Correction proposée par Gemini réinvente la méthode M02 (lecture indiciaire Ginzburg) déjà inscrite au catalogue du projet. *Intégration partielle* — la suggestion d'une modalité épistémique spécifique `sourced_leak` (fiabilité faible mais poids structurel lourd dans l'arène) est retenue comme suggestion d'implémentation pour M02 quand cette méthode sera instanciée.

**Matrice d'évaluation et verdict architectural Gemini.** Synthèse sans valeur ajoutée substantielle. Imprécisions techniques (référence à Neo4j alors que l'architecture est documentée PostgreSQL+AGE dans la couche d'exécution). Verdict architectural flatteur ("intellectuellement blindé") rejeté comme excessif — un système éprouvé sur sept cas-jouets et quatre analyses réelles n'est pas blindé, il est *préliminairement validé sur les régimes testés*. Distinction maintenue.

*Question de la critique sur l'automatisation du classifieur d'applicabilité (étape 1).* Reformulée — la dépendance à l'arbitrage humain n'est pas une fragilité, c'est une discipline. Recommandation alternative — vérifications mécaniques automatisées au niveau 1 (déterministe) + arbitrage avec aide LLM au niveau 2 avec validation humaine obligatoire. Pas de classifieur entraîné avant accumulation de 100+ décisions humaines documentées.

*Bilan.* La critique a contribué à étendre le dispositif de surveillance (deux catégories d'audit ajoutées) sans déstabiliser la doctrine. Le projet maintient son autonomie épistémique face aux LLM tiers — examen systématique sans déférence à l'autorité supposée.

---

## 7. Inventaire des audits

| Audit | Inscrit à | Statut | Fenêtre roulante | Données accumulées |
|---|---|---|---|---|
| `typology_audit` | gabarit v2.1 section 16 | premier audit fait à v2.1 | par méthode | typologies M01 maintenues avec ancrage empirique documenté ; typologie ObservableEffectType étendue par le rejeu pipeline |
| `intentionality_bias_audit` | gabarit v2.1.1 section 16 | en accumulation | 10 analyses, seuil alerte 80% | 5 analyses M01 sur cas réels — premier audit possible après 5 analyses supplémentaires |
| `hypothesis_gap_audit` | gabarit v2.1.1 section 16 | en accumulation | 20-30 analyses, seuils multiples | 8 analyses (5 cas réels + 3 cas-jouets) — premier audit possible après 12-22 analyses supplémentaires |

*Audits futurs envisagés.*

— *Audit de couverture des cadres interprétatifs* (M03 v2.1) — vérifier que les cadres identifiés dans les applications M03 sont ancrés empiriquement par au moins 2-3 cas externes documentables. À déclencher après accumulation de 3-5 applications M03.

— *Audit de cohérence inter-méthodes* — vérifier que les analyses M01 individuelles utilisées par M03 produisent des résultats cohérents avec la matrice M03 issue de leur agrégation. À déclencher périodiquement quand applications M03 substantielles produites.

---

## 8. Décisions méthodologiques significatives

### 8.1 Choix de la stratification ternaire de l'efficience (mai 2026)

*Décision.* Trois valeurs d'efficience — `efficient`, `efficient_partiel`, `non_efficient`. Pas de binarité, pas de continuum.

*Alternatives examinées.* (a) Binarité simple (efficient / non-efficient) — rejetée, masque les configurations partielles. (b) Continuum 0-1 — rejeté, fausse précision et difficulté de calibration. (c) Trois valeurs avec définitions opérationnelles claires — retenu.

*Conséquence.* Schéma `EfficiencyStatus` Pydantic enum avec trois valeurs. Validators custom de cohérence dans M01Analysis. Implémenté et testé.

### 8.2 Choix de la séparation sortie humaine / journal méthodologique (mai 2026)

*Décision.* Trois sorties séparées par analyse — M01-H (sortie humaine, lisible non-analyste), M01-M (sortie machine YAML pour pipeline), M01-P (sortie publique 150-300 mots). Plus journal méthodologique de l'analyse séparé.

*Alternative examinée.* Sortie unique avec annotations méthodologiques. Rejeté — surcharge la lisibilité pour le lecteur informé non-analyste.

*Conséquence.* Discipline 9.0 du gabarit v2.1. Test opérationnel — la M01-H doit être lisible par un lecteur intéressé par le contenu sans pré-requis sur le gabarit.

### 8.3 Choix de la doctrine sur les patterns observés vs fabriqués (mai 2026)

*Décision.* Patterns observés empiriquement (ancrés par au moins 2-3 cas externes documentables) légitimes et nécessaires à l'analyse compétente du métier observé. Patterns fabriqués a priori (catégories typologiques construites par l'analyse sans ancrage empirique) à requalifier en inférences. Statut spécifique des failure_patterns du journal — patterns de gouvernance, distincts des typologies analytiques.

*Alternative examinée.* Refus de toute typologie (analyse strictement par inférence cas par cas). Rejeté — empêche la mobilisation de la technicité métier de l'observateur. La typologie des actes de langage Austin/Searle/Grice, la typologie des sophismes Aristote/Hamblin/Walton, la typologie des présuppositions philosophique du langage sont *ancrées empiriquement* dans la tradition académique et utiles à l'analyse.

*Conséquence.* Charte v2.1 section 6.6. Implémenté dans `typology_audit` (gabarit section 16). Conduit l'extension contrôlée de la typologie ObservableEffectType par le rejeu pipeline.

### 8.4 Choix de ne pas automatiser la décision d'applicabilité (étape 1, v2.1)

*Décision.* La décision d'applicabilité reste semi-manuelle. Un analyste humain prend la décision sur la base de critères opérationnels documentés. L'automatisation par classifieur dédié est inscrite comme objectif v3 sous condition d'accumulation de données.

*Motif.* La décision concerne précisément les points sensibles — vigilance adversariale, mode dégradé, basculement en `not_applicable`. Le coût d'erreur est élevé. La discipline du jugement humain à ce niveau est cohérente avec l'engagement 3 de l'ADN (ligne fine naïveté/paranoïa).

*Alternative examinée.* Classifieur LLM ou ML entraîné sur décisions humaines documentées. Rejeté pour v2.1 — pas assez de données documentées pour entraîner sans biais initial. Réexaminable en v3 après accumulation de 100+ décisions documentées.

### 8.7 Choix de la persistance du graphe cognitif — fichiers-source-de-vérité (3 juillet 2026)

*Décision.* Principe fichiers-source-de-vérité retenu pour le graphe cognitif. Les YAML validés et versionnés dans git sont la source de vérité unique du graphe cognitif ; le graphe est une vue dérivée, jetable et reconstructible par rejeu intégral du corpus. Aucune écriture directe dans le graphe n'est autorisée, par aucun acteur humain ou logiciel. Implémentation Phase 0-1 — module `graph_builder.py` ingérant les YAML validés vers NetworkX (Python pur, licence BSD, zéro serveur), avec exports GraphML/JSON pour visualisation et audits. Bascule vers PostgreSQL + Apache AGE prévue sur seuils documentés.

*Alternatives examinées.* (a) PostgreSQL + Apache AGE immédiat (recommandation préliminaire du plan d'action 001) — rejeté pour la Phase 0, infrastructure prématurée pour un volume de quelques centaines de nœuds/arêtes, et ne répond pas à la question de la source de vérité. (b) Principe fichiers-source-de-vérité + graphe dérivé (NetworkX) — retenu, satisfait l'auditabilité (doctrine P7), la discipline anti-corruption (validateur en unique porte d'entrée) et la proportionnalité (pas d'infrastructure avant le besoin). (c) Neo4j Community — écarté, GPLv3 gérable en composant serveur non modifié mais pricing Enterprise hostile à terme et aucun apport à l'échelle actuelle que l'option retenue ne fournisse déjà.

*Conséquence.* La décision 003 (persistance journal) hérite du même principe — git append-only comme source de vérité, index dérivé. La décision 001 (orchestration) est contrainte — les agents produisent des YAML candidats soumis au validateur, jamais d'écriture directe ; le graphe reste en lecture seule pour l'orchestration. `plan_action_002.md` devra spécifier `graph_builder.py` (ingestion YAML → NetworkX, exports, premiers audits comme parcours de graphe). Dépendance à ajouter au prototype — `networkx` (BSD), aucune infrastructure serveur en Phase 0-1. `git init` sur `lentité/` est un prérequis bloquant du prototype. Seuils de bascule vers PostgreSQL + AGE — corpus dépassant ~50 analyses validées ou rejeu complet excédant 60 secondes, besoin de requêtes concurrentes multi-utilisateurs (Mode 1 en service), besoin de requêtes croisées SQL + graphe non couvrables raisonnablement en NetworkX/pandas. Voir `.claude/decisions/decision_002_persistance_graphe.md`.

### 8.9 Choix de la licence — tri-partition par classe d'artefacts (3 juillet 2026)

*Décision.* Licence unique rejetée au profit d'une tri-partition par classe d'artefacts. Spécification/gabarit (couche B — schémas Pydantic, validateurs, documentation du format) en Apache 2.0 (code) + CC BY 4.0 (spec). Moteur (pipeline d'ingestion, orchestration multi-agents, graphe cognitif, synthèse) en AGPL-3.0, copyright détenu intégralement par le porteur, préservant le droit de double licence commerciale pour le Mode 2. Productions analytiques (dossiers M01/M03 publiés en Mode 1) en CC BY-SA 4.0.

*Alternatives examinées.* (a) Apache 2.0 unique — rejeté, aucune protection du moteur contre la capture propriétaire d'un tiers opérant un service Mode 2 concurrent sans obligation de contribution. (b) AGPL-3.0 unique — rejeté, contamination copyleft incompatible avec la diffusion du gabarit comme standard ouvert. (c) Tri-partition par classe d'artefacts — retenue, seule option satisfaisant simultanément la diffusion du gabarit comme standard et la protection du moteur ; précédent documenté dans l'écosystème — Neo4j, Grafana, MongoDB (pré-SSPL), où l'AGPL ne bloque pas le business mais crée la raison de contracter.

*Conséquence.* Matérialisation prévue dans le repo — fichier `LICENSE` racine (AGPL-3.0 par défaut), dossier `LICENSES/` avec les trois textes, en-tête SPDX par fichier, section « Licences » du README. Mise en place reportée à `plan_action_002.md`. Conditions de révision documentées — CLA/DCO obligatoire avant toute première PR externe sur le périmètre AGPL (bloquant, y compris pour le co-dirigeant AXON-1) ; réexamen de la licence moteur si trois prospects Mode 1/Mode 2 qualifiés refusent explicitement pour motif AGPL sur douze mois ; migration de gouvernance de la spécification envisageable si le gabarit devient un standard adopté par des tiers. Décision 005 (distribution) peut retenir le modèle dual en cohérence. Voir `.claude/decisions/decision_004_licence.md`.

---

## 9. Questions ouvertes et hypothèses pour v3

*Questions doctrinales non encore tranchées.*

— *Méthodes du catalogue à instancier.* M02 (lecture indiciaire Ginzburg) prioritaire selon la critique externe ; M04 (triangulation historiographique) attendue ; M05-M08 à spécifier. L'ordre d'instanciation dépendra des besoins analytiques rencontrés.

— *Articulation avec mode 2 (conseiller du prince).* Les contraintes spécifiques aux méthodes du mode 2 ne sont pas explicitées dans le gabarit v2.1. Relèvent du distribution restreinte (charte v2.1 section 8.2). Extension du gabarit à produire quand le mode 2 sera engagé opérationnellement.

— *Méthodes prédictives.* Le gabarit v2.1 traite l'analyse rétrospective ou contemporaine. Une méthode prédictive demanderait une formalisation différente des incertitudes et conditions de révision.

— *Méthodes non textuelles.* Image, vidéo, données quantitatives. Demanderait adaptation substantielle du gabarit.

— *Méthodes de synthèse multi-textuelle.* M03 traite la comparaison ponctuelle. Une méthode longitudinale d'un seul acteur sur plusieurs discours, ou une méthode d'analyse de séquences politiques étalées sur plusieurs mois, demanderait extension.

*Décisions politiques pendantes.* Licence open source, modèle d'accès Mode 2 distribution restreinte, premier groupe Mode 1, trajectoire financement Mode 3. Relèvent du choix du porteur principal (Seb).

*Hypothèses pour v3.* (a) Génération M01-P automatique par appel LLM léger validé par schéma. (b) Pipeline d'audit des typologies automatique sur analyses entrantes. (c) Export vers graphe cognitif (Neo4j ou PostgreSQL+AGE selon décision technique). (d) Classifieur d'applicabilité supervisé après accumulation de 100+ décisions documentées. (e) Couverture de mode 2 par extension dédiée du gabarit.

---

## 10. Métadonnées et navigation du journal

*Conventions de datation.* Entrées datées au mois et année (granularité actuellement suffisante). Datation au jour pour événements précis (décisions, productions de documents canoniques).

*Conventions de référence.* Renvois à la doctrine par section précise (par exemple — "charte v2.1 section 6.6", "gabarit v2.1 section 5.11"). Renvois aux analyses par identifiant complet (par exemple — "M01_LECORNU_DPG_20251014_v2_1").

*Discipline append-only.* Les entrées ne sont pas modifiées ni supprimées une fois inscrites. Une décision révisée fait l'objet d'une nouvelle entrée qui documente la révision et référence l'entrée précédente.

*Statut du journal.* Document de référence pour la mémoire institutionnelle. Pas de version canonique courante au sens où la doctrine évolue par versions. Le journal s'enrichit au fil des productions et des décisions.

*Prochaines entrées attendues.* Production de l'extension M03 v2.1 à quatre acteurs (avec Panot). Premier audit `intentionality_bias_audit` après accumulation de 5 analyses supplémentaires. Premier audit `hypothesis_gap_audit` après accumulation de 12-22 analyses supplémentaires. Première instanciation de M02 si retenue comme méthode prioritaire suivante. Décisions politiques quand elles seront prises.

---

---

```yaml
date: 2026-07-03
type: friction
refs: [decision_002, decision_003]
```

### Friction — entrée 8.7 insérée hors régime append-only physique

*Constat.* L'entrée 8.7 (décision 002, persistance du graphe cognitif) a été ajoutée par insertion dans le corps de la section 8, entre 8.4 et 8.9, et non par append physique en fin de fichier. Ceci contrevient au régime établi par la décision 003 (§5) — « les entrées s'ajoutent exclusivement en fin de fichier [...] aucune insertion ni réordonnancement ». La décision 003 étant postérieure à cette insertion, l'entrée 8.7 n'est pas corrigée rétroactivement (append-only : pas de réécriture du corps existant). Ce constat documente la friction pour mémoire et vaut confirmation du régime applicable à toute entrée future — y compris celle qui suit immédiatement.

---

```yaml
date: 2026-07-03
type: décision
refs: [decision_003, plan_action_001]
```

### 8.8 Choix de la persistance du journal méthodologique — markdown append-only + front matter (3 juillet 2026)

*Décision.* Le journal méthodologique général et les journaux de méthodes restent des fichiers markdown versionnés dans git, en régime append-only physique — les entrées s'ajoutent exclusivement en fin de fichier, dans l'ordre chronologique d'écriture ; la numérotation logique (ex. 8.6-8.10) n'autorise aucune insertion ni réordonnancement dans le corps existant, un numéro logique pouvant être écrit hors ordre. Chaque nouvelle entrée porte un front matter YAML minimal (`date`, `type` — décision | révision doctrinale | friction | audit | reprise —, `refs`). Toute structure de requête (index, extraction, tableau de bord) reste dérivée et jetable, jamais source de vérité. Seul le Dirigeant, ou un processus explicitement validé par lui, écrit au journal — les agents de l'orchestration n'y ont pas accès en écriture.

*Alternatives examinées.* (a) Git + JSON structuré indexé (recommandation préliminaire du plan d'action 001) — rejeté, impose une migration du journal existant et sacrifie la lisibilité humaine directe pour un gain de requêtabilité que ne réclame aucun besoin identifié (les audits du gabarit portent sur le graphe cognitif, couvert par la décision 002). (b) Git + markdown append-only + front matter YAML léger — retenu, continuité avec la pratique réelle (deux mois de journal markdown), zéro migration, indexation future ouverte à coût nul. (c) Base de données avec event sourcing — écartée, contredit le principe fichiers-source-de-vérité (décision 002) et couple le journal à l'infrastructure du graphe. (d) Hybride Git + DB d'index — écartée comme choix initial, reste une voie d'évolution ouverte par le front matter.

*Conséquence.* Aucune migration du journal existant ; seules les entrées futures adoptent le front matter et le régime d'append physique strict. `plan_action_002.md` devra prévoir la convention de front matter dans `conventions.md` et le squelette du script d'indexation en anti-tâche explicite (ne pas le coder avant besoin avéré). `git init` sur `lentité/` reste un prérequis bloquant. Vérification effectuée — l'entrée 8.7 (décision 002) a été insérée dans le corps existant plutôt qu'appendue physiquement ; consignée ci-dessus comme friction, sans réécriture (append-only). Voir `.claude/decisions/decision_003_persistance_journal.md`.

---

```yaml
date: 2026-07-03
type: décision
refs: [decision_005, decision_004, plan_action_001]
```

### 8.10 Choix du modèle de distribution — dualité à trois jalons conditionnels (3 juillet 2026)

*Décision.* Distribution duale séquencée en trois jalons vérifiables. Jalon 1 — dépôt `atelier-atlani/lentite` privé structuré (immédiat, phase d'hygiène), accès Dirigeant + co-dirigeant sous CLA préalable sur le périmètre AGPL. Jalon 2 — passage public du cœur, conditionné à (a) dossier zéro rétrospectif livré, validé au pipeline et relu par deux lecteurs externes, et (b) relecture juridique de la responsabilité éditoriale effectuée et intégrée à la charte ; le périmètre spec/gabarit peut passer public dès ce jalon ou avant, par décision légère non structurante. Jalon 3 — ouverture commerciale Mode 2 (licence commerciale séparée), postérieure au jalon 2. Mode 3 (chat public) hors scope, report doctrinal maintenu.

*Alternatives examinées.* (a) Open source complet immédiat — écarté, publierait le moteur avant traitement du risque juridique (responsabilité éditoriale) et avant preuve méthodologique (dossier zéro non livré). (b) Distribution duale à publication « Phase 2+ » non datée (formulation du plan d'action 001) — écartée, aucun critère vérifiable de passage public. (c) Distribution duale à trois jalons conditionnels — retenue, transforme une intention en engagement pilotable, ordonne auditabilité avant monétisation. (d) Closed transitoire — rejet confirmé, incompatible avec la philosophie du projet (rejet déjà acté au plan d'action 001).

*Conséquence.* La phase d'hygiène (git init, purge des doublons, README resynchronisé) devient formellement le jalon 1, prérequis commun aux décisions 002, 003 et 005. Le CLA co-dirigeant doit être rédigé avant sa première PR — à inscrire à `plan_action_002.md` ou en tâche parallèle légère. Les critères du jalon 2 activent deux chantiers déjà identifiés — dossier zéro rétrospectif, consultation juridique responsabilité éditoriale. `plan_action_002.md` — le prototype se développe en privé (jalon 1), aucune contrainte de publication ne pèse sur la Phase 0-1. Voir `.claude/decisions/decision_005_modele_distribution.md`.

Séquence des cinq décisions structurantes de la Phase 0 (plan d'action 001) close avec cette entrée — 8.6 (orchestration multi-agents, décision 001) reste la seule entrée non encore inscrite.

---

```yaml
date: 2026-07-03
type: décision
refs: [decision_001, decision_002, decision_003, decision_004, plan_action_001]
```

### 8.6 Choix de l'orchestration multi-agents — custom Python séquentiel avec critère de bascule (3 juillet 2026)

*Décision.* Orchestration Phase 0-1 en custom Python minimal, sans framework — appels directs au SDK Anthropic, pipeline linéaire à quatre agents (Charité, Vulnérabilités, Chaînes causales, Synthèse) → assemblage YAML candidat → `validate.py`, boucle de retry bornée (max 2 itérations) avec rapport d'erreurs réinjecté à l'agent Synthèse. Architecture hexagonale légère — le cœur métier (schémas Pydantic, validation, `graph_builder.py`) ignore l'orchestration, les agents sont des adaptateurs. Prompts versionnés en fichiers (jamais en dur dans le code). Traçabilité par artefacts de log JSON par appel d'agent (prompt complet, réponse brute, modèle/version, horodatage, tokens, itération), archivés à côté du YAML produit.

*Alternatives examinées.* (a) langgraph (recommandation préliminaire du plan d'action 001) — rejeté pour la Phase 0-1, l'abstraction du framework (state, checkpointers, graphe compilé) réduit la transparence auditée sur une topologie strictement linéaire à quatre appels ; bascule prévue sur critères explicites (§7 de la décision) plutôt que choix définitif prématuré. (b) Custom Python minimal avec critère de bascule — retenu, cohérent avec 002/003 (l'orchestration ne produit que des fichiers candidats), réutilise les prompts d'`observatrice_complet/` et le modèle d'orchestration par fichiers déjà éprouvé du workflow `.claude/`. (c) LangChain agents (legacy) — écartée, moins explicite que langgraph et déjà considérée legacy par l'éditeur, dominée dans tous les cas par (a) ou (b).

*Conséquence.* `plan_action_002.md` devra spécifier le module d'orchestration minimal, le format de l'artefact de log JSON, la boucle de retry bornée, et l'emplacement des prompts versionnés (`pipeline/agents/` proposé). Cannibalisation d'`observatrice_complet/` activée — extraction des prompts réutilisables, archivage du reste en strate génétique datée, à exécuter en phase d'hygiène (jalon 1, décision 005) ou en première tâche du prototype. Dépendances Phase 0-1 — SDK Anthropic Python, `networkx`, Pydantic v2 ; aucun framework d'orchestration. Bascule vers langgraph si parallélisation, branchements conditionnels multiples, reprise sur erreur avec état persistant, ou boucles contradicteur/analyste dépassant deux tours deviennent nécessaires — le volet artefacts de log JSON est conservé indépendamment du dispositif d'orchestration en cas de bascule. Voir `.claude/decisions/decision_001_orchestration_multi_agents.md`.

Séquence des cinq décisions structurantes de la Phase 0 (plan d'action 001 §4, entrées 8.6-8.10) close avec cette entrée.

---

```yaml
date: 2026-07-03
type: reprise
refs: [plan_action_001, plan_action_002, decision_001, decision_002, decision_003, decision_004, decision_005]
```

### Classement du plan d'action 002 — prototype technique Phase 0

*Constat.* `plan_action_001.md` est clos — les cinq décisions structurantes (entrées 8.6-8.10) sont prises et classées. `plan_action_002.md`, produit en Mode Architecte le 3 juillet 2026, est classé dans `.claude/plans/`. Il spécifie le prototype technique de la Phase 0 en trois séquences — 0 (hygiène et fondation, jalon 1 de la décision 005 : git init, purge, cannibalisation d'`observatrice_complet/`, licences, README, CLA, conventions), 1 (durcissement du gabarit couche B : bloc omission, bitemporalité, politique de corpus, calibration), 2 (prototype pipeline : `validate.py` M01, `graph_builder.py`, audits, orchestrateur, étalonnage sur texte réel).

*Conséquence.* Exécution attendue par l'Implementer (Claude Code, Sonnet 4.6), avec vérification préalable (tâche 0.0) de non-contradiction avec `conventions.md`/`etat_projet.md`. Discipline — une séquence à la fois, un lot = une session = des commits propres, toute friction consignée au journal avec front matter conforme (décision 003), aucune décision structurante prise par l'Implementer. Plan suivant attendu — `plan_action_003.md` (dossier zéro rétrospectif) après revue du prototype par Mode Reviewer. Voir `.claude/plans/plan_action_002.md`.

---

```yaml
date: 2026-07-03
type: reprise
refs: [plan_action_002, decision_001, decision_004]
```

### Cannibalisation d'`observatrice_complet/` — statut cannibalisé + archivé

*Constat.* Exécution de la tâche 0.3 de `plan_action_002.md` (lot {0.3-0.7}). Sur les vingt fichiers du prototype `lentite_observatrice_complet/` (13-14 mai 2026), cinq prompts réutilisables ont été extraits vers `pipeline/agents/` — contradicteur (v1.1) et quatre analystes spécialisés (discours v1.1, économiste v1.1, juriste v1.0, sociologue v1.0), chacun conforme à la décision 001 (prompts versionnés en fichiers, jamais en dur dans le code) et à la décision 004 (SPDX `AGPL-3.0-only`, périmètre moteur/orchestration). Les quinze fichiers restants (définition du projet, protocoles d'observation/interaction/consultation, prompt système v1.2, architecture technique, MVP, schémas de données, mémoire, briefing, test loi immigration 2024) ont été déplacés vers `archives/observatrice_complet_2026-05/` — strate génétique datée, non cannibalisée. Le répertoire `lentite_observatrice_complet/` est vidé et retiré.

*Conséquence.* Statut du prototype — cannibalisé (prompts) + archivé (reste). Les cinq prompts extraits ne sont pas encore adaptés à la doctrine v2.1.1 ni aux schémas durcis de la séquence 1 — adaptation prévue tâche 2.5 de `plan_action_002.md`, hors périmètre du présent lot. Voir `pipeline/agents/` et `archives/observatrice_complet_2026-05/`.

---

```yaml
date: 2026-07-03
type: friction
refs: [plan_action_002]
```

### Friction — suppression du journal obsolète à la racine, avec récupération de contenu non dupliqué

*Constat.* `lentite_journal.md` à la racine (17 mai 2026, 20,9 Ko) était une version figée du journal, non nommée « copie » et donc hors du périmètre littéral de la tâche 0.2 (purge des copies), mais manifestement dépassée par `journal/lentite_journal.md` — seul journal canonique actif, tenu à jour depuis. Signalé par l'Implementer à l'issue du lot {0.1-0.2} sans suppression unilatérale ; arbitrage rendu par l'Architecte (adressé comme addendum (a) à l'exécution du lot {0.3-0.7}) — suppression du fichier racine.

*Vérification avant suppression.* Comparaison section par section entre le fichier racine et `journal/lentite_journal.md` avant destruction. Les deux fichiers divergent au-delà d'un simple décalage temporel — le fichier racine contient trois entrées absentes du journal canonique — section 3.9 (« Division durable de la gauche post-rupture NUPES »), section 3.10 (« Régime adversarial — pattern d'effets observables asymétriques »), toutes deux révélées par l'application M03 v2.1 à quatre acteurs, et section 8.5 (« Choix de la méthodologie de codage en phases »). Ce contenu est récupéré ci-dessous avant suppression du fichier — voir les trois entrées de récupération qui suivent immédiatement.

*Conséquence.* `lentite_journal.md` supprimé de la racine après récupération du contenu non dupliqué. Journal canonique unique confirmé — `journal/lentite_journal.md`.

---

```yaml
date: 2026-07-03
type: révision doctrinale
refs: [plan_action_002]
```

### 3.9 (récupéré) Division durable de la gauche post-rupture NUPES

*Note de récupération.* Entrée retrouvée dans `lentite_journal.md` (racine, 17 mai 2026) lors de sa suppression, absente de `journal/lentite_journal.md`. Appendue ici en régime append-only, numérotation logique d'origine conservée (3.9) sans réordonnancement du corps existant.

*Révélée par* — application M03 v2.1 à 4 acteurs (mai 2026), spécifiquement par la divergence Vallaud-Panot sur la proposition P1 (suspension comme victoire vs comme leurre).

*Énoncé.* La gauche post-rupture NUPES est structurellement divisée entre stratégie réformiste (Vallaud-PS-CFDT — conquête sociale par négociation, paritarisme) et stratégie rupturiste (Panot-LFI-base militante — rupture institutionnelle, 6ème République, refus du paritarisme). La rupture NUPES de 2024 est rentabilisée politiquement par chaque camp — le PS reconstruit sa lisibilité « conquête sociale par négociation », LFI reconstruit sa lisibilité « rupture institutionnelle exclusive ». La division est durable jusqu'à 2027 selon la trajectoire observable à mai 2026.

*Implication méthodologique.* Pattern à éprouver sur d'autres séquences politiques 2026-2027. La division pourrait soit s'approfondir (deux candidatures présidentielles distinctes en 2027) soit se résorber (union tactique de second tour). Les effets observables à venir départageront.

*Inférence formalisée.* Confidence 0,70 dans la synthèse épistémique de M03 v2.1 à 4 acteurs. Promue de simple observation à hypothèse concurrente formelle parce qu'elle prédit des effets observables vérifiables.

---

```yaml
date: 2026-07-03
type: révision doctrinale
refs: [plan_action_002]
```

### 3.10 (récupéré) Régime adversarial — pattern d'effets observables asymétriques

*Note de récupération.* Entrée retrouvée dans `lentite_journal.md` (racine, 17 mai 2026) lors de sa suppression, absente de `journal/lentite_journal.md`. Appendue ici en régime append-only, numérotation logique d'origine conservée (3.10) sans réordonnancement du corps existant.

*Révélée par* — confirmation transversale du pattern sur deux cas (Ciotti et Panot) dans M03 v2.1 à 4 acteurs.

*Énoncé.* Le régime adversarial (`applicable_vigilance_adversariale`) produit des effets observables systématiquement asymétriques — visibilité médiatique et positionnement politique obtenus (effet `amplification` sur OV_B chez Ciotti et Panot), objets thématiques principaux non atteints (motion rejetée, Bardella non nommé, destitution non aboutie). La rhétorique adversariale fonctionne sur le positionnement, pas sur l'efficacité parlementaire.

*Inférence formalisée.* Confidence 0,65 dans la synthèse épistémique de M03 v2.1 à 4 acteurs. À éprouver sur d'autres applications M03 (autres séquences politiques, autres acteurs adversariaux).

---

```yaml
date: 2026-07-03
type: décision
refs: [plan_action_002]
```

### 8.5 (récupéré) Choix de la méthodologie de codage en phases

*Note de récupération.* Entrée retrouvée dans `lentite_journal.md` (racine, 17 mai 2026) lors de sa suppression, absente de `journal/lentite_journal.md`. Appendue ici en régime append-only, numérotation logique d'origine conservée (8.5) sans réordonnancement du corps existant.

*Décision.* Codage en cinq phases avec critères d'acceptation explicites (mai 2026). Phase 0 préparation avec cinq décisions structurantes à prendre avant codage substantiel. *Motif* — le pipeline existant valide les YAML, le système opérationnel complet (production automatique d'analyses à partir de textes sources) demande architecture multi-agents et persistance avancée non encore codées. La méthodologie de codage formalise la séquence rigoureuse.

*Alternatives examinées.* (a) Codage direct d'un MVP complet — rejeté, risque de réécriture si décisions architecturales mauvaises. (b) Phase de R&D ouverte sans méthodologie — rejeté, risque de dette technique et de divergence doctrinale. (c) Méthodologie en phases avec décisions structurantes en amont — retenu. Cohérent avec la discipline rigoureuse du projet.

*Conséquence.* Document de méthodologie de codage produit comme nouveau volet de l'architecture du projet (couche méthodologique de développement, distincte des couches doctrinale et opérationnelle) — `lentite_methodologie_codage_v1.md`, déplacé vers `dev/` en tâche 0.3-0.7 (addendum c) du présent plan.

---

```yaml
date: 2026-07-03
type: friction
refs: [plan_action_002]
```

### Friction — échec du test d'onboarding à froid sur l'environnement Python

*Constat.* Test d'onboarding à froid exécuté (clone propre de `atelier-atlani/lentite`, lecture du seul README, tentative de validation d'une analyse YAML en suivant uniquement ses instructions — critère de sortie de la séquence 0, `plan_action_002.md` §3). Résultat — **échec**. Deux blocages distincts. (1) La commande d'installation documentée (`pip install --break-system-packages pydantic pyyaml`) échoue — `pip` n'existe pas comme commande sur macOS (seul `pip3`), et l'option `--break-system-packages` n'est pas reconnue par la version de pip installée. (2) Une fois l'installation improvisée, la commande de validation documentée échoue avec une traceback opaque (`TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'`) — cause réelle : le `python3` par défaut sur macOS (Xcode Command Line Tools) est 3.9.6, incompatible avec la syntaxe d'union `X | None` (PEP 604) utilisée par `schemas.py`, alors que le README annonce « Python 3.11+ » sans indiquer de vérification préalable ni de conduite à tenir si `python3` résout vers une version insuffisante.

*Conséquence.* Correctif immédiat — lot 0-bis. `requirements.txt` ajouté à la racine (versions épinglées, confirmées fonctionnelles — `pydantic==2.13.4`, `PyYAML==6.0.3`). Section README réécrite (§6.1 Environnement) — vérification préalable `python3 --version`, branche explicite si < 3.10 (interpréteur nommé ou venv), installation via `python -m pip install -r requirements.txt` (élimine l'ambiguïté pip/pip3 et le flag non portable), commande de vérification rapide, et triage d'erreur explicite pour la traceback `TypeError ... 'type' and 'NoneType'`. `conventions.md` §6.7 amendé pour admettre `requirements.txt` à la racine minimale.

---

```yaml
date: 2026-07-03
type: audit
refs: [plan_action_002]
```

### Revalidation du test d'onboarding à froid — succès

*Constat.* Après le correctif ci-dessus poussé sur `origin/main`, le test d'onboarding à froid a été rejoué intégralement — nouveau clone de `https://github.com/atelier-atlani/lentite.git` (répertoire de travail distinct, pas de réutilisation du clone précédent), suivi exact de la séquence documentée en README §6.1 (a) `python3 --version` → 3.9.6 constaté, (b) branche « < 3.10 » suivie, interpréteur `python3.11` nommé explicitement, (c) `python3.11 -m pip install -r requirements.txt`, (d) commande de vérification rapide. Les quatre étapes réussissent sans improvisation. Validation finale — `python3.11 pipeline/validate_m03.py pipeline/analyses/m03_retraites_octobre_2025_4acteurs_v2_1.yaml` → succès.

*Conséquence.* Le critère de sortie de la séquence 0 relatif à l'onboarding (`plan_action_002.md` §3) est satisfait pour la première fois sur cette revalidation. Statut nuancé — la revalidation a été exécutée par la même instance ayant produit le correctif, pas par un tiers réellement indépendant ; elle confirme la reproductibilité technique des commandes, pas l'absence de biais de connaissance préalable du rédacteur. Une revalidation par un tiers humain ou une instance véritablement vierge reste recommandée avant de considérer le critère d'onboarding définitivement clos.

---

```yaml
date: 2026-07-03
type: reprise
refs: [plan_action_002]
```

### Lot {1.1–1.2} de la séquence 1 — bloc omission durci et bitemporalité minimale

*Constat.* Exécution des tâches 1.1 et 1.2 de `plan_action_002.md` séquence 1 (durcissement du gabarit couche B). 1.1 — le modèle `Omission` de `pipeline/schemas.py` exige désormais quatre champs obligatoires : `pouvoir_agir` (référence documentée à la compétence/capacité d'agir), `opportunite` (datée), `cloture_corpus` (déclaration du corpus + date de clôture), `explications_innocentes` (au moins une alternative examinée, statut examinée/écartée/retenue). 1.2 — champs `date_fait`/`date_connaissance` (défaut explicite `non_renseigne`) ajoutés sur quatre modèles d'assertion (`Vulnerability`, `Omission`, `DiscourseActGap`, `ObservableEffect`) ; nouveau champ `gabarit_version` sur `M01Analysis` rendant ces deux champs obligatoires quand sa valeur est `2.1-durci-seq1`. Un test négatif par tâche ajouté à `pipeline/tests/`, les deux rejetés avec erreur ciblée. Les 12 YAML existants et les 3 tests négatifs préexistants revalident sans modification ni régression (vérification manuelle — la revalidation formelle du corpus reste celle de la tâche 1.5).

*Frictions signalées, non arbitrées silencieusement* (détail dans `.claude/logs/log_session_002_lot_1.1-1.2.md`) — le plan ne liste pas explicitement les modèles couverts par « toute assertion » en 1.2 (périmètre retenu — les quatre modèles ci-dessus, cohérent avec le qualificatif « minimale ») ; `schemas_m03.py` non modifié faute d'équivalent `Omission` dans M03 et d'instruction explicite du plan pour 1.2 sur ce fichier ; le nom `gabarit_version=2.1-durci-seq1` a été choisi distinct des numéros de version mineure réels de la doctrine (`2.1`, `2.1.1`) pour ne pas laisser croire à une révision de doctrine — moratoire respecté.

*Conséquence.* Séquence 1 non close — restent 1.3 (politique de corpus), 1.4 (grille de calibration), 1.5 (revalidation intégrale du corpus + entrée journal de synthèse de clôture de séquence, seule entrée qui portera le critère de sortie §4 du plan). Commits `cafaff8` (schéma) et `4efa2c4` (note de lot) poussés sur `origin/main`.

---

```yaml
date: 2026-07-03
type: friction
refs: [plan_action_002]
```

### Écart au §9 du plan — séquence 1 ouverte par anticipation, séquence 0 non formellement close

*Constat.* La séquence 0 de `plan_action_002.md` n'est pas formellement close au sens strict de son critère de sortie (§3 — « test d'onboarding à froid réussi, un tiers — instance Claude vierge — clone, lit le seul README, et parvient à valider une analyse existante sans autre aide »). L'entrée « Revalidation du test d'onboarding à froid — succès » ci-dessus le signalait déjà en nuance — la revalidation a été exécutée par la même instance ayant produit le correctif 0-bis, pas par un tiers réellement indépendant. Un re-test d'onboarding à froid, mené par un tiers ou une instance véritablement vierge, reste dû après le correctif 0-bis pour clore formellement la séquence 0.

Malgré cela, le lot {1.1–1.2} de la séquence 1 a été exécuté et commité (voir entrée « reprise » précédente) avant cette clôture formelle. C'est un écart explicite à la discipline d'exécution du plan (§9 — « Une séquence à la fois, dans l'ordre. La séquence 1 ne commence pas avant le critère de sortie de la 0 »).

*Conséquence.* Écart assumé et tracé sur instruction du Dirigeant, plutôt que dissimulé — conforme à la discipline « toute friction au journal » (§9 du plan). Séquence 0 reste ouverte jusqu'à un test d'onboarding à froid mené par un tiers véritablement indépendant de l'instance ayant produit le correctif. Séquence 1 se poursuit par anticipation ; sa propre clôture (tâche 1.5) est de toute façon postérieure à ce point. Aucune décision structurante n'est affectée par cet écart — le travail déjà produit et validé sur la séquence 1 (12/12 YAML + tests négatifs 1.1/1.2) reste en l'état ; seule la séquentialité stricte du plan n'a pas été respectée.

---

```yaml
date: 2026-07-03
type: reprise
refs: [plan_action_002]
```

### Lot {1.3–1.4} de la séquence 1 — politique de corpus et grille de calibration

*Constat.* Exécution des tâches 1.3 et 1.4 de `plan_action_002.md` séquence 1. 1.3 — nouveau document `doctrine/V2.1/lentite_politique_corpus_v1.md` (CC BY 4.0) : typologie à cinq types de sources (officielle, journalistique, statistique, militante, académique) avec fiabilité déclarée par type, règle d'extension tracée, articulation explicite avec `cloture_corpus` du bloc omission durci (tâche 1.1). 1.4 — nouveau document `doctrine/V2.1/lentite_calibration_confiance_v1.md` (CC BY 4.0) : grille à quatre degrés (faible/modéré/fort/établi) sur le score `confidence` existant, cas-jouets 1/5/6 promus cas-étalons avec leurs valeurs réelles vérifiées contre `lentite_cas_jouets_1_5_6_v2_1.md`, protocole inter-annotateurs spécifié (non exécuté, conformément au plan). Aucune modification aux documents doctrinaux existants ni au code — moratoire respecté, ce sont deux documents nouveaux.

*Frictions signalées, non arbitrées silencieusement* (détail dans `.claude/logs/log_session_002_lot_1.3-1.4.md`) — risque de confusion entre le degré qualitatif « établi » de la grille 1.4 et le statut épistémique « fait établi » de la charte, prévenu par un avertissement terminologique explicite dans le nouveau document ; aucun type de front matter existant (`conventions.md` §6.9) ne nomme le cas « source ajoutée en cours d'enquête » de la règle d'extension 1.3 — `audit` retenu par défaut, point signalé comme ouvert ; les trois cas-étalons 1/5/6 ne couvrent pas la bande « faible » de la grille (aucune valeur < 0,40) ; le « journal méthodologique de M01 » référencé par le gabarit section 16 n'existe pas comme fichier séparé dans le dépôt, seul `journal/lentite_journal.md` est instancié.

*Conséquence.* Séquence 1 non close — reste 1.5 (revalidation intégrale du corpus, entrée de synthèse de clôture portant le critère de sortie §4 du plan, et arbitrage des points ouverts ci-dessus). L'écart au §9 signalé au lot précédent (séquence 1 ouverte par anticipation, séquence 0 non formellement close faute de re-test d'onboarding par un tiers indépendant) reste en l'état, ni aggravé ni résolu par ce lot.

---

```yaml
date: 2026-07-04
type: audit
refs: [plan_action_002]
```

### Clôture de la séquence 1 (durcissement du gabarit) — critère de sortie satisfait

*Constat.* Le critère de sortie de la séquence 1 (`plan_action_002.md` §4 — « suite de tests complète verte, positifs et négatifs, corpus intégralement revalidé ») est satisfait. Bilan de la séquence — 1.1 bloc omission durci (quatre champs obligatoires sur `Omission`, `pipeline/schemas.py`) ; 1.2 bitemporalité minimale (`date_fait`/`date_connaissance` sur `Vulnerability`, `Omission`, `DiscourseActGap`, `ObservableEffect`, validation conditionnelle sur `gabarit_version`) ; 1.3 politique de corpus v1 (`doctrine/V2.1/lentite_politique_corpus_v1.md`) ; 1.4 grille de calibration v1 (`doctrine/V2.1/lentite_calibration_confiance_v1.md`) ; 1.5 revalidation intégrale — les 12 YAML du corpus (10 M01 amendés individuellement + 2 M03 inchangés) valident sous `gabarit_version=2.1-durci-seq1`, et les 5 tests négatifs (3 préexistants + 2 nouveaux tâches 1.1/1.2) sont rejetés comme attendu. Deux arbitrages Architecte intégrés en 1.5 — (a) type `extension_corpus` ajouté à `conventions.md` §6.9 ; (b) `journal/lentite_journal_m01.md` créé, résolvant le vide signalé en 1.3/1.4 sur le journal méthodologique de M01 (gabarit v2.1 §16).

*Frictions ouvertes* (aucune ne bloque la clôture — consignées pour suite, aucune ne relève d'une révision doctrinale à chaud, moratoire respecté) :

— *Bande faible de la grille de calibration (1.4) non couverte.* Les trois cas-étalons 1/5/6 ne produisent aucune hypothèse dominante sous 0,40 — candidate v2.2 post-moratoire, extension par cas-jouet supplémentaire calibré pour une dominance faible.

— *Terminologie « établi » (degré de confidence) vs « fait établi » (statut épistémique).* Risque de confusion prévenu par un avertissement explicite dans `lentite_calibration_confiance_v1.md` §1, mais reste une ambiguïté de surface entre deux documents — candidate v2.2 post-moratoire pour clarification dans le gabarit lui-même si le besoin se confirme à l'usage.

— *M03 non durci.* `schemas_m03.py` ne porte ni `gabarit_version` ni champs bitemporels — les deux YAML M03 du corpus valident sans amendement parce qu'aucune contrainte nouvelle ne s'y applique, pas parce qu'ils ont été vérifiés sous un gabarit durci équivalent. Question ouverte non tranchée depuis le lot {1.1–1.2}, non résolue ici.

— *Asymétrie de datation.* Sur 57 champs `date_fait` amendés en 1.5, 21 portent une date réelle et 36 `non_documente` — les faits ponctuels médiatisés (votes, décisions de justice) sont systématiquement datés, les faits diffus (perceptions, cohésions, narrations) presque jamais. Donnée nouvelle documentée dans `journal/lentite_journal_m01.md`, candidate à un futur `typology_audit`.

— *Écart au §9 du plan (rappel, non résolu par cette clôture).* La séquence 0 reste non formellement close (re-test d'onboarding par un tiers indépendant toujours dû, cf. entrée de friction précédente). La clôture de la séquence 1 ne referme pas cet écart, qui est indépendant et reste ouvert.

*Conséquence.* Séquence 1 close. Séquence 2 (prototype pipeline — `validate.py` M01, `graph_builder.py`, audits, orchestrateur, étalonnage) peut commencer, sous réserve de la même discipline de lots qu'en séquence 1. Le point séquence 0 / écart §9 reste distinct et non résolu — à traiter indépendamment de l'avancement de la séquence 2.

---

```yaml
date: 2026-07-04
type: étape
refs: [plan_action_002]
```

### Création de la couche communication — documents dérivés de pilotage

*Constat.* Micro-lot hors séquence, classement uniquement (pas d'exécution de tâche numérotée de `plan_action_002.md`). Répertoire `communication/` créé à la racine (admis par la discipline de racine minimale, `conventions.md` §6.7, qui autorise tout répertoire). Trois documents dérivés y sont classés, licence CC BY 4.0 (même régime que la doctrine, décision 004) — `00_document_maitre.md` (v1.1, identité à deux étages noyau/instance, ADN, architecture, état réel, trajectoire), `01_positionnement_usages.md` (v1.0, positionnement, anti-positionnement, objections, messages par interlocuteur), `04_exploitation_actifs.md` (v1.0, inventaire des actifs et canaux d'exploitation par horizon de jalon). Les trois portent déjà, tels que fournis, un en-tête déclarant leur statut de document dérivé et la préséance de la doctrine et des décisions structurantes en cas de divergence — vérifié avant classement, aucune modification de contenu apportée.

*Règle de resynchronisation actée.* Toute révision doctrinale (couche A/B/C, `.claude/decisions/`) déclenche la mise à jour des documents de `communication/` ; jamais l'inverse — ces documents ne sont pas une source de vérité et n'ont aucune autorité normative sur la doctrine ou les décisions. Cette règle, déjà inscrite dans l'en-tête de chacun des trois documents, est actée ici au niveau du projet et reflétée dans le README racine (§3, ligne « Vues dérivées de pilotage et communication — jamais source de vérité »).

*Observation, non corrigée (classement uniquement).* `00_document_maitre.md` porte une incohérence de version interne — l'en-tête annonce « Version 1.1 » quand le colophon final indique « Document maître v1.0 ». Signalé ici plutôt que corrigé silencieusement ; correction relevant du producteur du document, pas du classement.

*Nouveau type de front matter.* `étape` ajouté à `conventions.md` §6.9 (instruction Dirigeant) — jalon de classement ou de structuration hors séquence d'un plan d'action, distinct de `reprise` (réservée à l'avancement d'une tâche déjà numérotée).

*Conséquence.* Aucun impact sur la séquence 2 en cours (lot {2.0–2.2}, distinct et non touché par ce micro-lot). Documents `communication/` disponibles pour usage interne immédiat (pilotage, onboarding co-dirigeant, préparation pédagogique) — toute diffusion externe reste soumise aux mêmes jalons de la décision 005 que le reste du projet.

---

```yaml
date: 2026-07-05
type: décision
refs: [decision_004, plan_action_002]
```

### Validation du Dirigeant — CLA v0.2.1

*Constat.* Le Dirigeant (Seb) a validé `gouvernance/CLA.md` dans sa version v0.2.1 le 5 juillet 2026, conformément à la note de méta-information de `plan_action_002.md` §5 tâche 0.6 et à la décision 004 (licence, §7). La version validée porte le mécanisme de cession exclusive irrévocable avec licence de retour non concurrente (v0.2, modèle CLA fort type Harmony CA — remplace la licence non exclusive de v0.1), les clauses de cessibilité du bénéfice du CLA à toute structure contrôlée par le Porteur, de droits moraux, et de garantie d'absence de droits d'employeur/donneur d'ordre, ainsi que le correctif ciblé du §5 (v0.2.1) référençant le formalisme de l'article L.131-3 CPI.

*Conséquence.* La validation du Dirigeant porte sur l'adéquation du mécanisme aux besoins de gouvernance du projet — elle ne se substitue pas à la relecture juridique, toujours non effectuée et toujours requise avant toute signature effective par un contributeur externe (§5 du CLA, inchangé sur ce point). Le CLA reste donc un projet de document, validé pour usage interne et pour orienter une éventuelle relecture juridique, non prêt pour signature par un tiers.

---

*Journal v1.0 — édité le 17 mai 2026. Prochaine révision attendue après extension M03 à 4 acteurs et nouvelles analyses substantielles. Document de mémoire institutionnelle, pas de récit. Pour la doctrine, lire charte et gabarit. Pour les analyses, lire les fichiers correspondants.*
