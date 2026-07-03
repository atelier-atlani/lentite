# L'Entité — Journal méthodologique général

*Mémoire institutionnelle du projet. Trace les évolutions doctrinales, les découvertes méthodologiques transversales, les frictions identifiées, les critiques externes examinées, les décisions structurantes. Document factuel et daté. Distinct des journaux méthodologiques propres à chaque méthode (M01, M03) qui tracent les évolutions internes de ces méthodes.*

---

## 1. Préambule

Ce journal général sert quatre fonctions.

— *Mémoire institutionnelle.* Conserver la trace des décisions doctrinales et architecturales qui ne sont pas explicites dans les documents canoniques.

— *Transparence méthodologique.* Documenter les choix, les pistes explorées et abandonnées, les frictions résolues. Permettre l'audit externe.

— *Surveillance des patterns du projet lui-même.* Tracer les patterns d'échec de gouvernance du projet (distincts des failure_patterns analytiques inscrits aux journaux de chaque méthode).

— *Préparation à l'évolution.* Identifier les zones de friction non résolues, les questions ouvertes, les hypothèses de v3.

Le journal est append-only en pratique. Les entrées sont datées et ordonnées. Une entrée n'est jamais supprimée — si une décision est révisée, une nouvelle entrée est ajoutée pour documenter la révision.

---

## 2. Évolutions doctrinales majeures

### 2.1 Phase initiale → v2

Phase de constitution du projet. Phrase-cœur, figure, quatre engagements de l'ADN, trois modes opérationnels. Architecture en trois couches établie. Première méthode produite — M01. Premier cas-jouet substantiel testé — Ciotti v2.

### 2.2 v2 → v2.1 — refonte par stratification

Début mai 2026. *Trois frictions identifiées* dans le rejeu et l'examen rétrospectif.

*Friction 1 — lisibilité M01-H.* Surchargée par le méta-discours. *Résolution* — discipline de séparation M01-H / journal méthodologique de la méthode.

*Friction 2 — efficience binaire trop grossière.* La binarité masquait les configurations stratégiques. *Résolution* — stratification de l'efficience par objet (objets thématiques + objets visés, trois valeurs efficient/efficient_partiel/non_efficient).

*Friction 3 — chaînes causales non explicitement tracées.* Engagement 4 inscrit doctrinalement mais pas opérationnellement. *Résolution* — chaînes causales amont et aval comme objets d'enquête formels, bloc V refondé en quatre sous-blocs.

*Conséquences architecturales.* Refonte de la charte, du gabarit, de M01 et M03.

*Doctrine sur les patterns établie.* Patterns observés empiriquement (ancrés par 2-3 cas externes documentables) légitimes. Patterns fabriqués a priori à requalifier en inférences. Inférence reste première. Failure_patterns du journal — patterns de gouvernance, distincts des typologies analytiques.

### 2.3 v2.1 → v2.1.1 — révision mineure

Mai 2026. *Motif* — critique externe par LLM tiers formalisée. Deux observations à surveiller statistiquement sans modification des contraintes normatives.

*Contenu.* Ajout de deux catégories d'entrée au journal méthodologique (gabarit section 16) — `intentionality_bias_audit` (seuil 80%, fenêtre 10 analyses) et `hypothesis_gap_audit` (seuils multiples, fenêtre 20-30 analyses). Aucune contrainte normative existante modifiée.

*Décision documentée.* Pas de modification des seuils 0,2 / 0,4 de la convention 6.7. Pas d'ajout de coefficient correctif. La doctrine v2.1 tient.

---

## 3. Découvertes méthodologiques transversales

### 3.1 Clivage stabilité/rupture transversal aux clivages thématiques

*Révélée par* — croisement des matrices dans M03 v2.1 application séquence retraites octobre 2025.

*Énoncé.* Les acteurs qui visent la stabilité institutionnelle (Lecornu, direction PS Vallaud) convergent tactiquement par-delà leur opposition politique. Les acteurs qui visent la rupture (Ciotti UDR-RN, Panot LFI, frondeurs PS) convergent tactiquement par-delà leurs divergences doctrinales totales. Clivage transversal aux clivages thématiques.

*Confirmation à 4 acteurs (mai 2026).* L'inclusion de Panot renforce empiriquement le clivage. La motion LFI à 271 voix réunit précisément les familles politiques radicalement opposées sur l'objet visé "faire chuter le gouvernement". Hypothèse promue d'inférence à hypothèse concurrente formelle dans la synthèse épistémique de M03 (confidence 0,75).

### 3.2 La CFDT comme pivot transversal de légitimation

*Révélée par* — convergence non explicitée Lecornu-Vallaud sur l'objet visé OV_E.

*Énoncé.* La CFDT fonctionne comme acteur tiers de légitimation qui rend possible le compromis Lecornu-Vallaud. Doctrine paritariste transversale aux clivages politiques classiques.

*Confirmation à 4 acteurs (mai 2026).* L'inclusion de Panot confirme transversalement par contraste. Panot silent sur P5 (légitimité syndicale) et not_aimed sur OV_E (alliance CFDT). La doctrine paritariste française est *mobilisée par les modérés gauche-droite, rejetée par les radicaux des deux bords*. Pattern confirmé empiriquement à 4 acteurs.

*Hypothèse pour généralisation.* Pattern attestable sur d'autres séquences sociales françaises depuis 1981. Document de référence — M04 (triangulation historiographique) à instancier sur ce sujet.

### 3.3 Engagements parlementaires à seuil structurellement sous-déterminés

*Révélée par* — analyse Vallaud v2.1.

*Énoncé.* Les engagements de type "sanction conditionnelle" ou "vigilance" sont par construction sous-déterminés dans leur seuil. La fonction réelle (signal politique vs contrainte stricte) se révèle par le seuil effectif.

*Confirmation à 4 acteurs (mai 2026).* L'engagement Panot "compte à rebours du départ de Macron" est lui aussi à seuil sous-déterminé. La destitution est attendue dans une fenêtre non close. Le seuil effectif (procédure aboutie ou non) révèle la fonction politique réelle (signal positionnement vs contrainte stricte). Pattern confirmé empiriquement sur un deuxième cas.

### 3.4 Asymétries de bénéfice révélant la structure profonde

*Révélée par* — étape 12 de M03 v2.1 application.

*Énoncé.* Les bénéfices observables ne suivent pas la structure des coalitions politiques apparentes. Les asymétries révèlent la structure profonde des intérêts stratégiques.

*Extension à 4 acteurs (mai 2026).* Cinq asymétries documentées au lieu de quatre. La rupture explicite du 49.3 par Lecornu en janvier 2026 (`broken_explicitly`) bénéficie *à Panot autant qu'à Ciotti* — validation rétrospective des deux critiques adversariales. Nouvelle asymétrie identifiée — *les sept frondeurs PS au vote du 16 octobre* bénéficient à Panot (validation partielle de la préemption symbolique) au détriment de Vallaud (cohésion fissurée).

### 3.5 Distinction mobilisation thématique / lexicale-marginale d'une historiographie

*Révélée par* — analyse Ciotti v2 sur "submersion migratoire".

*Énoncé.* Le `mobilization_type` distingue mobilisation thématique explicite et emprunt lexical marginal. Permet de signaler la porosité aux cadres disqualifiés sans surcharger la classification globale.

*Pas de modification à 4 acteurs.* Le concept reste stable et opérationnel. Aucun emprunt lexical à cadre disqualifié identifié dans les analyses Vallaud et Panot — les charges éthiques étaient low pour les deux.

### 3.6 Sept patterns temporels avec ancrage empirique

*Révélée par* — passage v2 (six patterns) à v2.1 (sept patterns).

*Énoncé.* Typologie ancrée par cas externes documentables. Pattern `broken_explicitly` ajouté v2.1.

*Confirmation à 4 acteurs (mai 2026).* L'analyse Panot v2.1 mobilise deux patterns nouveaux dans le corpus — `never_observed` (chute du gouvernement) et `not_yet_observed` (destitution Macron). Distinction systématique entre `never_observed` (silence inexpliqué, fenêtre close) et `not_yet_observed` (fenêtre non close) maintenue.

### 3.7 Discipline anti-cumul des documents de coordination

*Révélée par* — observation de l'auto-cumul potentiel lors de la transition v2 → v2.1.

*Énoncé.* Un seul document de coordination canonique courant. Pas d'empilement.

*Application à 4 acteurs (mai 2026).* L'application M03 à 4 acteurs remplace la version à 3 acteurs comme référence canonique courante. La version à 3 acteurs est archivée dans le journal du projet par discipline du journal, pas perdue. Application stricte du pattern.

### 3.8 Test décisif du pipeline opérationnel

*Révélée par* — passage de la doctrine documentaire au pipeline Python.

*Énoncé.* La friction productive entre doctrine et implémentation technique révèle les zones d'imprécision. Typologie `ObservableEffectType` étendue avec ancrage empirique cas par cas.

*Extension à 4 acteurs (mai 2026).* Le schéma `schemas_m03.py` a validé sans modification l'application à 4 acteurs malgré l'ajout d'une proposition (P6) et d'un objet visé (OV_H). Le schéma tient à l'échelle. Aucune extension de typologie nécessaire pour l'extension à 4 acteurs.

### 3.9 Division durable de la gauche post-rupture NUPES (nouveau v2.1 à 4 acteurs)

*Révélée par* — application M03 v2.1 à 4 acteurs (mai 2026), spécifiquement par la divergence Vallaud-Panot sur la proposition P1 (suspension comme victoire vs comme leurre).

*Énoncé.* La gauche post-rupture NUPES est *structurellement divisée* entre stratégie réformiste (Vallaud-PS-CFDT — conquête sociale par négociation, paritarisme) et stratégie rupturiste (Panot-LFI-base militante — rupture institutionnelle, 6ème République, refus du paritarisme). La rupture NUPES de 2024 est rentabilisée politiquement par chaque camp — le PS reconstruit sa lisibilité "conquête sociale par négociation", LFI reconstruit sa lisibilité "rupture institutionnelle exclusive". La division est durable jusqu'à 2027 selon la trajectoire observable à mai 2026.

*Implication méthodologique.* Pattern à éprouver sur d'autres séquences politiques 2026-2027. La division pourrait soit s'approfondir (deux candidatures présidentielles distinctes en 2027) soit se résorber (union tactique de second tour). Les effets observables à venir départageront.

*Inférence formalisée.* Confidence 0,70 dans la synthèse épistémique de M03 v2.1 à 4 acteurs. Promue de simple observation à hypothèse concurrente formelle parce qu'elle prédit des effets observables vérifiables.

### 3.10 Régime adversarial — pattern d'effets observables asymétriques (nouveau v2.1 à 4 acteurs)

*Révélée par* — confirmation transversale du pattern sur deux cas (Ciotti et Panot) dans M03 v2.1 à 4 acteurs.

*Énoncé.* Le régime adversarial (`applicable_vigilance_adversariale`) produit des effets observables systématiquement asymétriques — visibilité médiatique et positionnement politique obtenus (effet `amplification` sur OV_B chez Ciotti et Panot), objets thématiques principaux non atteints (motion rejetée, Bardella non nommé, destitution non aboutie). La rhétorique adversariale fonctionne sur le positionnement, pas sur l'efficacité parlementaire.

*Inférence formalisée.* Confidence 0,65 dans la synthèse épistémique de M03 v2.1 à 4 acteurs. À éprouver sur d'autres applications M03 (autres séquences politiques, autres acteurs adversariaux).

---

## 4. Failure patterns de gouvernance du projet

### 4.1 `chronological_cumulation_of_amendments`

*Pattern.* Accumuler les amendements par ordre chronologique sans les repositionner par niveau d'architecture. *Discipline appliquée* — repositionnement méthodique par niveau d'architecture lors de chaque révision.

### 4.2 `self_cumulation_of_coordination_documents`

*Pattern.* Cumul des documents de coordination eux-mêmes. *Discipline appliquée* — un seul document de coordination canonique par transition.

### 4.3 Patterns potentiels à surveiller

— `premature_v3_engagement` — surveillance maintenue.

— `deference_to_external_LLM_authority` — surveillance maintenue. La critique Gemini de mai 2026 a été traitée selon la discipline.

— `typology_proliferation` — surveillance maintenue. Le test à 4 acteurs n'a pas demandé d'extension de typologie — bon signe.

— `chronological_cumulation_of_analyses` (nouveau v2.1 à 4 acteurs) — risque d'accumuler les analyses M01 sans audit périodique. *Discipline à mettre en place* — déclencher `intentionality_bias_audit` après chaque tranche de 10 analyses, `hypothesis_gap_audit` après chaque tranche de 20-30.

---

## 5. Failure patterns analytiques (synthèse inter-méthodes)

Liste maintenue. Six patterns d'erreur de raisonnement identifiés et inscrits aux journaux méthodologiques des méthodes M01 et M03.

— `valid_form_with_false_premise`
— `hidden_premise_not_marked`
— `confidence_treated_as_truth`
— `temporal_sequence_treated_as_causality`
— `omission_treated_as_intention`
— `speaker_belief_treated_as_knowledge`

---

## 6. Critiques externes examinées

### 6.1 Critique LLM tiers — mai 2026

*Origine.* Critique externe par LLM tiers (Gemini) formalisée en quatre points.

*Examen méthodique du projet.* Chaque point examiné avec position prise.

**Point 2.A — Concentration des écarts hypothèses sur la zone d'indétermination.** Observation factuelle juste. Lecture en "neutralité molle systématique" rejetée. *Intégration v2.1.1* — catégorie d'audit `hypothesis_gap_audit`. *Confirmation à 4 acteurs (mai 2026)* — l'extension à 4 acteurs *resserre* l'écart à 0,05 (vs 0,10 à 3 acteurs). Pattern de concentration en zone d'indétermination confirmé empiriquement. Cohérent avec la discipline anti-paranoïa du projet.

**Point 2.B — Biais machiavélique inhérent au parsing.** Observation juste. *Intégration v2.1.1* — catégorie d'audit `intentionality_bias_audit`. *Confirmation à 4 acteurs (mai 2026)* — l'analyse Panot confirme le pattern (hypothèse intentionnelle dominante à 0,85, non intentionnelle plafonnée à 0,55).

**Point 2.C — Biais documentaire de la trace écrite.** Observation juste. *Intégration partielle* — suggestion modalité `sourced_leak` retenue pour M02.

**Verdict architectural Gemini.** Synthèse sans valeur ajoutée substantielle. Imprécisions techniques. Rejet de la lecture flatteuse ("intellectuellement blindé").

*Bilan.* Le projet maintient son autonomie épistémique face aux LLM tiers. Le dispositif d'audit étend la surveillance sans déstabiliser la doctrine.

---

## 7. Inventaire des audits

| Audit | Inscrit à | Statut | Fenêtre roulante | Données accumulées à mai 2026 |
|---|---|---|---|---|
| `typology_audit` | gabarit v2.1 section 16 | premier audit fait à v2.1 | par méthode | typologies maintenues avec ancrage empirique. Aucune extension typologie pour passage 3→4 acteurs M03 |
| `intentionality_bias_audit` | gabarit v2.1.1 section 16 | en accumulation | 10 analyses, seuil alerte 80% | **5 analyses M01 sur cas réels** — premier audit possible après 5 analyses supplémentaires |
| `hypothesis_gap_audit` | gabarit v2.1.1 section 16 | en accumulation | 20-30 analyses, seuils multiples | **8 analyses M01** (5 cas réels + 3 cas-jouets) **+ 1 application M03 à 4 acteurs** — premier audit possible après 12-22 analyses supplémentaires |

*Audits futurs envisagés.*

— *Audit de couverture des cadres interprétatifs M03* — vérifier ancrage empirique. À déclencher après 3-5 applications M03.

— *Audit de cohérence inter-méthodes* — vérifier que les M01 individuelles agrégées dans une M03 produisent des résultats cohérents.

— *Audit de divergence pipeline / analyses humaines* (nouveau, à activer en Phase 1 du codage) — comparer les analyses produites par le pipeline opérationnel aux analyses humaines validées.

---

## 8. Décisions méthodologiques significatives

### 8.1 Choix de la stratification ternaire de l'efficience

Décision mai 2026. Trois valeurs — efficient, efficient_partiel, non_efficient.

### 8.2 Choix de la séparation sortie humaine / journal méthodologique

Décision mai 2026. Trois sorties séparées — M01-H, M01-M, M01-P. Plus journal séparé.

### 8.3 Choix de la doctrine sur les patterns observés vs fabriqués

Décision mai 2026. Patterns observés légitimes si ancrés empiriquement. Patterns fabriqués à requalifier en inférences.

### 8.4 Choix de ne pas automatiser la décision d'applicabilité

Décision mai 2026. Décision semi-manuelle pour v2.1. Réexaminable après accumulation de 100+ décisions documentées.

### 8.5 Choix de la méthodologie de codage en phases (nouveau v2.1.1)

Décision mai 2026. Codage en cinq phases avec critères d'acceptation explicites. Phase 0 préparation avec cinq décisions structurantes à prendre avant codage substantiel. *Motif* — le pipeline existant valide les YAML, le système opérationnel complet (production automatique d'analyses à partir de textes sources) demande architecture multi-agents et persistance avancée non encore codées. La méthodologie de codage formalise la séquence rigoureuse.

*Alternatives examinées.* (a) Codage direct d'un MVP complet — rejeté, risque de réécriture si décisions architecturales mauvaises. (b) Phase de R&D ouverte sans méthodologie — rejeté, risque de dette technique et de divergence doctrinale. (c) Méthodologie en phases avec décisions structurantes en amont — *retenu*. Cohérent avec la discipline rigoureuse du projet.

*Conséquence.* Document `dev/methodologie_codage_v1.md` produit comme nouveau volet de l'architecture du projet (couche méthodologique de développement, distinct des couches doctrinale et opérationnelle).

---

## 9. Questions ouvertes et hypothèses pour v3

*Questions doctrinales non encore tranchées.*

— Méthodes du catalogue à instancier — M02 (lecture indiciaire Ginzburg) prioritaire selon critique externe.

— Articulation avec mode 2 (conseiller du prince) — contraintes spécifiques non explicitées.

— Méthodes prédictives.

— Méthodes non textuelles.

— Méthodes de synthèse longitudinale.

*Décisions politiques pendantes.* Licence open source, modèle d'accès Mode 2, premier groupe Mode 1, trajectoire financement Mode 3. Relèvent du choix du porteur principal. Documentées dans `dev/methodologie_codage_v1.md` section 8.

*Hypothèses pour v3.* (a) Génération M01-P automatique. (b) Pipeline d'audit des typologies automatique. (c) Export graphe cognitif. (d) Classifieur d'applicabilité supervisé. (e) Couverture mode 2 par extension dédiée du gabarit.

*Nouvelle question ouverte (mai 2026)* — *quand passer en Phase 1 du codage ?* Conditionné aux décisions Phase 0 (cinq décisions structurantes). Une fois prises, Phase 1 peut commencer immédiatement.

---

## 10. Métadonnées et navigation du journal

*Conventions de datation.* Entrées datées au mois et année. Datation au jour pour événements précis.

*Conventions de référence.* Renvois à la doctrine par section précise. Renvois aux analyses par identifiant complet.

*Discipline append-only.* Pas de modification ni suppression. Révisions documentées par nouvelle entrée.

*Statut du journal.* Document de référence pour la mémoire institutionnelle. S'enrichit au fil des productions et décisions.

*Prochaines entrées attendues.*

— Décisions Phase 0 codage (cinq décisions structurantes).

— Démarrage Phase 1 codage et premier prototype technique.

— Premier audit `intentionality_bias_audit` après accumulation de 5 analyses supplémentaires.

— Premier audit `hypothesis_gap_audit` après accumulation de 12-22 analyses supplémentaires.

— Première instanciation de M02 si retenue comme méthode prioritaire suivante.

— Extension M03 à 5 acteurs si retenue.

— Décisions politiques quand elles seront prises.

---

## Métadonnées du journal

- *Version du journal* : 1.1
- *Date d'édition* : 17 mai 2026
- *Modification depuis 1.0* — intégration de la validation transversale à 4 acteurs des découvertes 3.1, 3.2, 3.3, 3.4, 3.6, 3.7, 3.8 ; ajout de la découverte 3.9 (division durable post-NUPES) ; ajout de la découverte 3.10 (régime adversarial produit effets observables asymétriques) ; ajout de la décision méthodologique 8.5 (méthodologie de codage en phases) ; ajout du failure_pattern de gouvernance 4.3 `chronological_cumulation_of_analyses` ; mise à jour de l'inventaire des audits avec compteurs actualisés et nouvel audit prévu (divergence pipeline / analyses humaines).

---

*Journal v1.1 — édité le 17 mai 2026. Prochaine révision attendue après décisions Phase 0 codage et démarrage Phase 1. Document de mémoire institutionnelle, pas de récit.*
