# L'Entité — Méthode 01 v2.1 : Analyse rhétorique d'un discours public

*Couche C — instance de méthode dans le catalogue. Implémente le gabarit v2.1 pour le type d'objet "discours politique et institutionnel". Refonte ciblée par rapport à M01 v2 — section 3 (Finalité), étape 1 (validation + identification des objets), étape 11 (chaînes causales et écarts en quatre sous-étapes), avec intégration des contraintes v2.1 sur la stratification de l'efficience par objet, les chaînes causales amont et aval, la doctrine des patterns observés. Remplace M01 v2.*

---

## 1. Métadonnées

```yaml
method_id: M01_ANALYSE_RHETORIQUE
method_name: "Analyse rhétorique d'un discours public"
method_version: 2.1
charter_version_required: 2.1
gabarit_version_required: 2.1
authors: [équipe projet L'Entité]
last_revision_date: 2026-05-17
```

---

## 2. Type d'objet et identification des objets analysés

M01 couvre les types d'objet suivants définis par le gabarit v2.1 section 2.1 : *discours politique* (déclaration officielle, intervention parlementaire, allocution télévisée, conférence de presse), *communiqué institutionnel structuré*, *éditorial signé*, *interview substantielle préparée*, *allocution cérémonielle institutionnelle*, *déclaration de doctrine d'autorité indépendante*.

M01 ne couvre pas le *plaidoyer judiciaire public* (méthode dédiée à instancier sous M07) ni la *communication d'entreprise stratégique sur décision majeure* (méthode dédiée à instancier sous M08).

Le type d'objet est distinct du sujet thématique. M01 peut s'appliquer à un discours politique sur n'importe quel sujet (retraites, immigration, écologie, défense, doctrine constitutionnelle, etc.). Le sujet thématique conditionne les sources de comparaison mobilisables et les historiographies pertinentes, mais ne modifie pas le périmètre d'applicabilité.

*Identification obligatoire des objets du discours (v2.1).* Pour chaque discours analysé, M01 identifie l'*objet thématique* (ce sur quoi le discours porte explicitement) et les *objets visés* (ce que le discours cherche à produire comme conséquences sur le réel), selon le gabarit v2.1 sections 2.2 et 5.10. Pour chaque objet, qualification d'efficience du locuteur selon le gabarit v2.1 sections 2.3 et 5.9.

---

## 3. Finalité analytique (v2.1)

M01 éclaire la structure rhétorique d'un discours public et son inscription dans les chaînes causales — amont (ce qui a nourri le discours) et aval (les objets visés et les conséquences plausibles).

Pour chaque discours analysé, M01 identifie l'objet thématique sur lequel le discours porte explicitement et les objets visés que le discours cherche à produire comme conséquences. Sur l'objet thématique, si le locuteur est efficient, M01 documente les écarts éventuels entre discours et actes selon les sept patterns temporels du gabarit v2.1 section 6.6. Sur les objets visés, M01 documente la chaîne causale aval — les conséquences plausibles avec defeaters, et les effets observables dans la fenêtre temporelle d'analyse.

M01 produit une analyse à plusieurs niveaux qui rend visible la fabrique rhétorique du texte et son inscription dans une trajectoire causale, sans les confondre avec un jugement sur la personne du locuteur ou sur la légitimité de ses positions politiques. La méthode reste silencieuse sur la valeur des positions défendues.

M01 sert : à l'analyse critique du débat public, à l'auto-formation des analystes, à l'objectivation de séquences politiques contestées, à la mise en évidence d'écarts entre engagement déclaré et réalisation effective sur les objets thématiques, à la cartographie des objets visés par les discours et de leurs chaînes causales documentables. M01 ne sert pas : à produire un jugement moral sur le locuteur, à prédire le succès politique de son discours, à arbitrer entre positions politiques en compétition.

---

## 4. Décision d'applicabilité

M01 applique la procédure de décision d'applicabilité du gabarit v2.1 section 4 avec quatre conditions opérationnelles spécifiques.

*Condition d'identification du locuteur.* Le locuteur doit être identifiable (nom, fonction, date d'occupation de la fonction). Un texte publié anonymement n'est pas analysable par M01 sans identification préalable de l'auteur.

*Condition d'intégrité du texte.* Le texte doit être accessible dans sa version officielle ou dans une transcription certifiée. Si seul un extrait substantiel mais non exhaustif est accessible, la méthode bascule en mode dégradé.

*Condition de contexte reconstructible.* Le contexte politique, institutionnel ou social du discours doit pouvoir être documenté depuis les sources publiques accessibles. Si le contexte est opaque, la méthode bascule en mode dégradé.

*Condition de finalité analytique.* La demande qui motive l'analyse doit être compatible avec la finalité de M01 (section 3). Une demande qui sollicite implicitement un jugement moral sur le locuteur ou un arbitrage sur la légitimité de ses positions est traitée par le module Elenchus avant l'exécution.

Le détecteur de surcharge contextuelle (gabarit section 4) bascule M01 en mode dégradé quand le texte excède quinze mille mots, ou quand la séquence politique impliquée mobilise plus de dix acteurs principaux dans une courte fenêtre temporelle.

Le verdict `applicable_vigilance_adversariale` (nouveau v2.1) est activé pour les discours présentant des caractéristiques adversariales — charge affective high, polyphonie de registres, attaques personnelles cumulées, glissements sémantiques marqués, emprunts lexicaux à des cadres idéologiques disqualifiés. Plafonnement de confidence à 0,85 sur les inférences globales, activation systématique des sous-blocs résultats nuls et éthique. Cas-jouet canonique de ce régime : Ciotti v2.1.

---

## 5. Définitions opératoires propres à M01

M01 hérite des définitions opératoires du gabarit v2.1 section 5 (unité d'analyse, statuts épistémiques, régime épistémique des attributions mentales, gradation des sophismes, gradation des omissions, charge affective, charge éthique, pondération des historiographies) et des trois définitions v2.1 sur efficience par objet (5.9), objets thématiques et visés (5.10), chaînes causales amont et aval (5.11). Elle y ajoute quatre définitions propres à l'analyse rhétorique.

### 5.1 Unité argumentative

*Unité argumentative* — segment du discours qui forme une opération rhétorique identifiable, paraphrasable en une phrase contenant un verbe principal et un complément. Une unité peut contenir plusieurs phrases si elles produisent ensemble une seule opération. Une phrase peut contenir plusieurs unités si elle produit plusieurs opérations distinctes.

Critère de découpage : on découpe au plus petit niveau qui préserve la cohérence de l'opération rhétorique. Si en hésitation, on découpe au niveau qui produit l'analyse la plus claire. La granularité du découpage est documentée comme point sensible — un autre analyste pourrait raisonnablement produire un nombre différent d'unités sur le même texte.

### 5.2 Typologie des actes de langage

Onze types canoniques ancrés dans la pratique discursive politique et institutionnelle : *assertion*, *justification*, *concession*, *réfutation*, *promesse*, *annonce performative*, *évaluation*, *définition*, *attribution causale*, *appel*, *récit*. Un même segment peut combiner plusieurs actes. La typologie est ancrée empiriquement dans la tradition de l'analyse pragmatique des discours (Austin, Searle, Grice) — pattern observé conformément à la charte v2.1 section 6.6.

### 5.3 Typologie des présuppositions

Trois types canoniques. *Présupposition doxique* — proposition implicite partagée comme évidence par l'auditoire visé. *Présupposition idéologique* — proposition implicite portée par un cadre idéologique identifiable, non universellement partagée. *Présupposition pragmatique* — proposition implicite nécessaire à la cohérence du discours.

Sous-type `modal_shift` (présupposition idéologique) — glissement entre modalités (nécessité empirique transformée en obligation morale, possibilité transformée en probabilité, conditionnel transformé en certain, situation politique transformée en acte volontaire de destruction). Pattern observé dans la rhétorique politique mobilisant la dramatisation. Ancrage empirique : Ciotti U5 "bûcher érigé" et U9 "submersion migratoire" ; multiples discours politiques mobilisant la transformation de descriptions empiriques en jugements axiologiques implicites.

### 5.4 Typologie des vulnérabilités argumentatives

Les vulnérabilités argumentatives canoniques de M01 sont regroupées en six familles avec leur définition opérationnelle, leur forme logique le cas échéant, et la lecture charitable alternative typique. Typologie ancrée dans la tradition logique et rhétorique (Aristote, Hamblin, Walton) — patterns observés conformément à la charte v2.1 section 6.6.

*Famille 1 — appels rhétoriques à l'évidence.* Sous-types : ad populum, ad verecundiam, ad antiquitatem.

*Famille 2 — défauts du raisonnement formel.* Sous-types : affirmation du conséquent, négation de l'antécédent, pétition de principe.

*Famille 3 — faux dilemmes et fausses oppositions.*

*Famille 4 — disqualifications de l'opposition.* Sous-types : disqualification morale, disqualification par la passion.

*Famille 5 — confusions de modalités.* Sous-types : nécessité empirique transformée en obligation morale, possibilité transformée en probabilité, conditionnel transformé en certain.

*Famille 6 — défauts de l'attribution mentale.* Sous-types : usage non factif de K (le locuteur affirme savoir ce que les sources n'établissent pas), attribution de croyance non justifiée.

La typologie n'est pas exhaustive. Une vulnérabilité non listée est rapportée à la famille la plus proche et le cas est inscrit au journal pour examen d'extension de la typologie selon le critère d'ancrage empirique de la charte 6.6.

---

## 6. Procédure en quatorze étapes (refonte v2.1 ciblée)

M01 v2.1 conserve l'architecture en quatorze étapes, avec refonte ciblée des étapes 1 et 11 et adaptation de l'étape 12 pour la mobilisation thématique/lexicale des historiographies.

### Étape 1 — Validation du matériau, qualification du locuteur, identification des objets (v2.1)

Vérification des quatre conditions de la section 4. Application du détecteur de surcharge contextuelle.

*Sous-étape 1.1 — Identification de l'objet thématique.* Lecture du discours et identification des thèmes traités. Un discours peut avoir plusieurs objets thématiques articulés. Documentation par référence aux passages du discours qui établissent l'objet thématique.

*Sous-étape 1.2 — Identification des objets visés.* Inférence à partir du discours et du contexte selon le critère opérationnel du gabarit v2.1 section 5.10. Pour chaque grande figure rhétorique mobilisée par le discours (hyperbole, prophétie, disqualification, transfert d'autorité, préemption symbolique, etc.), quelle conséquence sur le réel cette figure cherche-t-elle plausiblement à produire ? Les conséquences identifiées sont consolidées en typologie d'objets visés propre à l'analyse, avec degré de confiance (entre 0 et 1) documenté par `grounded_in` (passages du discours qui supportent l'inférence).

*Sous-étape 1.3 — Qualification d'efficience par objet.* Pour chaque objet identifié (thématique et visés), application de la définition opératoire du gabarit v2.1 section 5.9. Trois valeurs possibles — `efficient`, `efficient_partiel`, `non_efficient`. Justification documentée.

*Sous-étape 1.4 — Verdict d'applicabilité.* `applicable_complete`, `applicable_degraded` (avec justification), `applicable_vigilance_adversariale` (avec justification), ou `not_applicable` (avec motif et redirection éventuelle).

Les identifications d'objets et qualifications d'efficience conditionnent la configuration du bloc V à l'étape 11 et la rédaction du bloc I de la sortie humaine.

### Étape 2 — Fiche d'énonciation enrichie

Production des champs de la fiche d'énonciation selon le gabarit v2.1 section 9.1 bloc I. Inclut obligatoirement le rôle du locuteur à la date, la séquence politique ou institutionnelle, le contrat de communication implicite, *la charge affective codée*, *la charge éthique codée*, les *objets thématiques identifiés à l'étape 1*, les *objets visés identifiés à l'étape 1*, la *qualification d'efficience par objet*.

### Étape 3 — Genre et contrat de communication

Identification du genre rhétorique précis (DPG, allocution télévisée, vœux institutionnels, réponse à DPG par président de groupe, etc.) et de ses conventions propres. Cette étape conditionne l'identification ultérieure des éléments rhétoriquement ordinaires (relevant du genre) par opposition aux choix stratégiques individuels.

### Étape 4 — Découpage en unités argumentatives

Application de la définition opératoire de l'unité argumentative (section 5.1). Production d'une liste numérotée d'unités (U1, U2, etc.) avec leur citation ou paraphrase.

### Étape 5 — Reconstruction charitable de l'argument principal (NON-NÉGOCIABLE)

Cette étape précède toute détection de défauts. Reformulation de l'argument du discours dans sa meilleure version — telle qu'un défenseur compétent du locuteur la formulerait.

Application obligatoire de la *règle opérationnelle pour la charité* (gabarit v2.1 section 6.2). Tout terme évaluatif emprunté au discours est traité selon l'une de trois modalités — *guillemets*, *attribution explicite*, *reformulation en lexique descriptif neutre*. La sortie de cette étape déclare pour chaque terme évaluatif identifié quelle modalité a été appliquée.

Si la charge éthique a été codée *élevée* en étape 2, ou *moyenne avec emprunts lexicaux à des cadres disqualifiés* (cas Ciotti U9 "submersion migratoire"), l'étape 5 produit en parallèle un *signalement* du contenu éthiquement disqualifiable qui demeure dans la reformulation. Ce signalement alimente le cinquième sous-bloc du bloc VIII en sortie humaine.

### Étape 6 — Actes de langage par unité

Pour chaque unité, identification des actes de langage selon la typologie de la section 5.2 et de leur niveau de confiance. Un même segment peut combiner plusieurs actes.

Pour les actes qui attribuent un état mental au locuteur ou à un tiers, application du *régime épistémique des attributions mentales* (gabarit v2.1 section 6.4) — déclaration du régime parmi K, B, Affirme, Prétend_savoir.

### Étape 7 — Lexique, registres, ethos, pathos, logos, doxa

Identification des termes-clés mobilisés avec leurs glissements sémantiques éventuels. Identification des registres empruntés. Caractérisation de l'ethos construit par le locuteur. Caractérisation du pathos mobilisé en cohérence avec la charge affective déclarée. Structure logique principale (logos). Doxa mobilisée.

### Étape 8 — Présuppositions et cadrages

Identification des présuppositions selon la typologie de la section 5.3. Chaque présupposition déclare son type, sa formulation, son `evidence_span`. Le sous-type `modal_shift` (glissement modal) est identifié explicitement quand il est présent.

### Étape 9 — Vulnérabilités argumentatives et sophismes

Pour chaque unité, identification des vulnérabilités argumentatives selon la typologie de la section 5.4. Application stricte des *trois critères cumulatifs du sophisme certain* (gabarit v2.1 section 5.4) : structure logique formellement défaillante, absence de lecture charitable alternative, démontrabilité sans information externe.

Pour les vulnérabilités relevant de la famille 2 ou de la famille 5, identification des *prémisses cachées* qui rendent l'argument apparemment valide, avec leur statut épistémique et leur niveau de confiance. Identification des *defeaters* (gabarit v2.1 section 6.5) — conditions qui défont l'inférence si elles sont vérifiées. Au moins deux defeaters par règle causale inférée.

Le verdict par défaut est *vulnérabilité possible* ou *vulnérabilité probable*. Le verdict *sophisme certain* est rare et systématiquement justifié par les trois critères. Si un seul critère manque, le verdict rétrograde.

### Étape 10 — Omissions qualifiées

Identification des omissions selon les trois niveaux du gabarit v2.1 section 5.5 — *structurelle*, *stratégique probable*, *intentionnelle non prouvée*.

Pour chaque omission, déclaration de l'élément manquant, du niveau, de la raison pour laquelle on attend sa présence, et de la preuve que le locuteur avait accès à l'information manquante.

### Étape 11 — Chaînes causales amont et aval, écarts sur l'objet thématique (refonte v2.1)

L'étape 11 est refondue en quatre sous-étapes selon la doctrine v2.1.

*Sous-étape 11.1 — Chaîne causale amont.* Pour chaque élément documentable du contexte qui a nourri le discours dans sa forme actuelle, identification et documentation par source. Six types canoniques (gabarit v2.1 schéma `UpstreamElement`) — *position antérieure* du locuteur, *contexte* politique ou conjoncturel, *événement déclencheur*, *attente électorale* documentable, *négociation préalable* avec d'autres acteurs, *contrainte institutionnelle*. Au moins deux defeaters pour chaque lien causal inféré entre élément amont et discours observé. Confidence documentée.

La chaîne amont éclaire la genèse du discours sans la réduire à elle. Les defeaters globaux à la chaîne amont sont énoncés — la convention du genre rhétorique impose certains traits indépendamment du contexte ; l'expression sincère de conviction reste possible parallèlement aux calculs stratégiques inférables.

*Sous-étape 11.2 — Objets visés et chaîne causale aval.* Pour chaque objet visé identifié à l'étape 1, formulation des conséquences plausibles que le discours cherche à produire sur le réel. Pour chaque conséquence plausible, déclaration de la confidence (entre 0 et 1, inférence) et d'au moins deux defeaters (gabarit v2.1 section 6.5).

La chaîne aval distingue les conséquences *inférées comme intentions plausibles* (ce que le discours cherche à produire) des conséquences *observables effectives* (ce qui s'est produit dans la fenêtre temporelle, traité au sous-bloc V.4). Les deux sont liées mais distinctes.

*Sous-étape 11.3 — Écarts sur l'objet thématique (si locuteur efficient sur cet objet).* Pour chaque engagement, prédiction ou annonce du discours portant sur l'objet thématique, identification de l'acte attendu et comparaison à la réalité observée dans la fenêtre temporelle pertinente. Application obligatoire du *typage par les sept patterns temporels* du gabarit v2.1 section 6.6 — *not_yet_observed*, *never_observed*, *observed_later*, *observed_otherwise*, *observed_by_other_actor*, *prevented_by_constraint*, *broken_explicitly*.

Pour les écarts en mode `not_yet_observed`, déclaration de la fenêtre de vérification.

Pour les écarts en mode `prevented_by_constraint`, nomination explicite de la contrainte.

Pour les écarts en mode `observed_otherwise`, comparaison entre la forme annoncée et la forme effective.

Pour les écarts en mode `broken_explicitly` (nouveau v2.1), identification de la motivation publique invoquée par le locuteur pour la révision ou l'abandon de l'engagement (par exemple, l'invocation d'une impasse parlementaire après une période de débat documentée).

Le sous-bloc V.3 est *vide* si le locuteur est non-efficient sur l'objet thématique (cas Ciotti v2.1). *Plein et minimal* si efficient sans engagements vérifiables substantiels — engagements tenus sans écarts (cas Fabius v2.1). *Plein et substantiel* si efficient avec engagements multiples — engagements multiples, certains tenus, d'autres rompus ou modifiés (cas Lecornu v2.1).

Cette sous-étape dépend de l'accès à des sources externes au discours. En mode dégradé, elle peut être partielle — chaque écart non documentable est signalé comme tel.

*Sous-étape 11.4 — Effets observables sur les objets visés.* Pour chaque objet visé identifié à l'étape 1, documentation des effets observables ou plausibles du discours dans la fenêtre temporelle d'analyse — réception par d'autres acteurs, reprises et contestations, modifications de coalitions, ouvertures ou fermetures d'options. Typologie ancrée empiriquement dans la pratique médiatico-politique (gabarit v2.1 schéma `ObservableEffect`) — *amplification*, *contestation*, *ignorement*, *reprise_par_alliance*, *appropriation_tactique*, *amplification_non_anticipable* (effets dus à des événements postérieurs au discours, ancrage empirique : décès Badinter un mois après le discours Fabius), *confirmation_institutionnelle*.

Le sous-bloc V.4 est plein pour tout locuteur (efficient ou non sur l'objet thématique) dès lors que des effets sont observables dans la fenêtre temporelle d'analyse.

### Étape 12 — Historiographies mobilisées (v2.1)

Identification des historiographies mobilisées par le discours. Pour chaque historiographie, identification de son ou ses historiographies concurrentes. Application obligatoire de la *pondération par niveau de consensus académique* (gabarit v2.1 sections 5.8 et 9.6) — disqualifiée, marginale, contestée, consensus fort. Toute historiographie concurrente déclare son niveau.

*Distinction v2.1.* Pour chaque historiographie mobilisée, déclaration du *type de mobilisation* (gabarit v2.1 schéma `Historiography`) — *thematic_explicit* (mobilisation thématique avec adhésion ou critique explicite au cadre) ou *lexical_marginal* (mobilisation par emprunt lexical sans thématisation explicite). La distinction est importante quand l'historiographie sous-jacente est disqualifiée — par exemple, "submersion migratoire" emprunté lexicalement et marginalement au cadre "grand remplacement" (disqualifié) dans le discours Ciotti, sans adhésion thématique explicite au cadre. La distinction permet de signaler l'élément à transparence éthique sans surcharger l'analyse globale du discours en classification disqualifiée.

Pour chaque historiographie concurrente non disqualifiée, formulation succincte de ce qu'elle dirait que l'historiographie mobilisée tait.

### Étape 13 — Hypothèses concurrentes et red team

Production d'au moins trois hypothèses explicatives concurrentes des décisions ou positions du locuteur dans le discours analysé, dont au moins deux *hypothèses non intentionnelles*. Pour chaque hypothèse, déclaration de son type (intentionnelle / non intentionnelle), de sa confiance (entre 0,0 et 1,0), et des éléments factuels et inférentiels qui la fondent.

Calcul de l'*écart de confiance* entre l'hypothèse dominante et la deuxième hypothèse. Application de la convention 6.7 du gabarit v2.1.

*Distinction v2.1 (gabarit v2.1 section 6.8) — séparation des chaînes causales et des hypothèses concurrentes.* Les chaînes causales documentent les éléments contextuels qui éclairent la genèse et les conséquences plausibles du discours (étape 11). Les hypothèses concurrentes formulent des lectures explicatives globales du discours qui restent en compétition épistémique (étape 13). Les deux dispositifs travaillent ensemble mais ne sont pas équivalents. Une chaîne causale amont peut nourrir une hypothèse concurrente sans s'y substituer ; une hypothèse concurrente peut prédire des effets observables qui figurent dans la chaîne causale aval sans la résumer.

Production d'objections de type *red team* à l'hypothèse dominante ou aux hypothèses co-dominantes. Une red team objection efficace soulève un défaut substantiel de l'hypothèse, pas un détail.

### Étape 14 — Synthèse en trois statuts et exports

Production de la sortie humaine M01-H (gabarit v2.1 sections 9.0 à 9.8, huit blocs avec discipline de séparation), de la sortie machine M01-M (gabarit v2.1 section 11), et de la sortie publique M01-P (gabarit v2.1 section 10, cinq éléments).

*Discipline de séparation M01-H / journal méthodologique (v2.1).* La sortie humaine M01-H est allégée du méta-discours méthodologique — notes sur les choix d'interprétation, recommandations pour révision du gabarit, calibration de version, frictions identifiées dans le rejeu. Ces éléments appartiennent au journal méthodologique de la méthode (section 16), pas à la M01-H. Test de qualité opérationnel — la M01-H doit être lisible par un lecteur non-analyste sans pré-requis sur le gabarit.

La sortie publique M01-P est générée *à partir* du M01-M validé par un appel LLM dédié. Le générateur respecte le format en cinq éléments imposé par le gabarit. La règle opérationnelle pour la charité s'applique à la M01-P.

---

## 7. Contrôles internes propres à M01

M01 hérite des contrôles internes du gabarit v2.1 section 7 et y ajoute trois contrôles propres.

*Contrôle de granularité du découpage.* La méthode signale au journal méthodologique le nombre d'unités identifiées à l'étape 4. Si le nombre s'écarte significativement de la fourchette typique pour le genre, un signal est levé pour examen.

*Contrôle de la conformité de la charité.* La méthode vérifie automatiquement la sortie de l'étape 5 contre la règle opérationnelle. Tout terme évaluatif détecté comme appartenant au discours analysé et utilisé non marqué dans la reconstruction charitable est signalé comme défaut de conformité.

*Contrôle de la cohérence efficience/bloc V (nouveau v2.1).* La méthode vérifie que la configuration des sous-blocs V.1 à V.4 est cohérente avec la qualification d'efficience par objet de l'étape 1. Si le locuteur est qualifié non-efficient sur l'objet thématique et que le sous-bloc V.3 contient des écarts substantiels, signal de défaut. Si le locuteur est qualifié efficient sur l'objet thématique et que le sous-bloc V.3 est vide sans justification, signal de défaut.

---

## 8. Dégradation gracieuse

M01 applique les quatre paliers de dégradation du gabarit v2.1 section 8 avec les adaptations suivantes pour le type d'objet "discours public".

*Palier 1 — verbatim partiel.* M01 peut produire une analyse substantielle à partir d'extraits convergents représentant au moins soixante pour cent du discours. En deçà, la méthode bascule en `not_applicable`.

*Palier 2 — contexte difficile à reconstruire.* L'étape 11 (chaînes causales et écarts) est la plus affectée — la chaîne amont et la chaîne aval demandent un accès au contexte. M01 documente chaque chaîne ou écart non documentable, et l'analyse demeure substantielle sur les autres étapes.

*Palier 3 — saturation cognitive du LLM.* Pour les discours longs, découpage en segments avec analyse séquentielle. M01 produit une synthèse de segments explicite.

*Palier 4 — rentabilité épistémique insuffisante.* Si l'analyse ne produit ni fait nouveau, ni inférence solide, ni hypothèse discriminante, M01 produit une sortie minimale qui déclare l'insuffisance et l'inscrit au journal.

---

## 9. Sortie humaine M01-H

M01 produit les huit blocs canoniques du gabarit v2.1 section 9, avec discipline de séparation sortie humaine / journal méthodologique (gabarit v2.1 section 9.0).

Le *bloc III* (Analyse par unités) est en général le bloc le plus volumineux pour M01.

Le *bloc V* (Chaînes causales et écarts) est refondé en quatre sous-blocs v2.1 (V.1 chaîne amont, V.2 objets visés et chaîne aval, V.3 écarts sur objet thématique, V.4 effets observables). Sa configuration dépend de l'efficience du locuteur par objet.

Le *cinquième sous-bloc du bloc VIII* — *Contenu éthiquement non neutralisé par la charité* — est obligatoire si la charge éthique a été codée *élevée*, et activable en charge *moyenne* avec emprunts lexicaux à des cadres disqualifiés identifiés.

---

## 10. Sortie publique M01-P

M01 produit la sortie publique selon le gabarit v2.1 section 10 — cinq éléments dans l'ordre, cent cinquante à trois cents mots.

*Élément 3 — hypothèses concurrentes avec écart de confiance.* Sur un cas en zone d'indétermination (écart ≤ 0,2), la formulation type recommandée est : "Deux hypothèses sont proches en confiance et coexistent comme co-explicatives — [hypothèse A] (confiance X) et [hypothèse B] (confiance Y). Les deux peuvent être simultanément vraies à des degrés variables."

*Élément 5 — bloc de clôture logique.* Qualification de l'inférence principale (solide / plausible / fragile). *Solide* — inférence fondée sur des faits établis et une chaîne de raisonnement explicite, sans prémisse implicite contestable, avec engagements vérifiés tenus le cas échéant. *Plausible* — inférence reposant sur une prémisse implicite identifiable et soutenable mais non démontrée. *Fragile* — inférence reposant sur plusieurs prémisses implicites contestables.

La sortie publique est validée par schéma — longueur dans la plage 150-300 mots, présence des cinq éléments dans l'ordre, absence de termes évaluatifs du locuteur non marqués, cohérence entre qualification du bloc de clôture et contenu de l'élément 2.

---

## 11. Sortie machine M01-M

M01 produit le YAML conforme au schéma du gabarit v2.1 section 11. Le schéma Pydantic spécifique à M01 inclut tous les champs canoniques du gabarit (y compris les nouveaux blocs v2.1 — `thematic_objects`, `targeted_objects`, `upstream_causal_chain`, `downstream_causal_chains`, `discourse_action_gaps_on_thematic_objects`, `observable_effects_on_targeted_objects`) et ajoute deux blocs propres à M01.

*Bloc `lexicon_analysis`* — termes-clés, glissements sémantiques, registres empruntés, ethos, pathos, logos, doxa. Structuré selon le bloc IV de la sortie humaine.

*Bloc `historiographies`* enrichi v2.1 — chaque historiographie mobilisée avec son `mobilization_type` (thematic_explicit ou lexical_marginal), son `consensus_level_mobilized`, son ou ses historiographies concurrentes avec leur pondération.

Le bloc `units` est typé par le schéma `Unit` du gabarit. Chaque unité porte ses speech_acts, ses presuppositions (incluant le sous-type `modal_shift` si applicable), ses argumentative_vulnerabilities (avec defeaters min 2 pour règles causales), ses omissions, et son inferred_function (avec `epistemic_regime` obligatoire pour les attributions d'état mental).

Validation supplémentaire v2.1 — tout `TargetedObject` doit avoir `grounded_in` non vide, toute `PlausibleConsequence` doit porter au moins deux defeaters, tout `DiscourseActGap` avec `pattern_type == broken_explicitly` doit avoir `public_motivation_invoked` non null.

---

## 12. Articulation au graphe cognitif

M01 produit les exports graphe selon le gabarit v2.1 section 12. Les nouveaux nœuds et arêtes v2.1 — `ThematicObject`, `TargetedObject`, `UpstreamElement`, `PlausibleConsequence`, `ObservableEffect`, et les arêtes `targets_object`, `nourished_by`, `aims_at_consequence`, `produces_observable_effect`, `mobilizes_historiography_lexically` — sont exportés pour ingestion dans le graphe cognitif.

Chaque arête porte les attributs canoniques du gabarit — `causality_type`, `weight`, `evidence`, `confidence`, `confidence_applies_to`, `method_id`.

---

## 13. Critères d'évaluation propres à M01

M01 hérite des sept critères transversaux du gabarit v2.1 section 13 et y ajoute deux critères propres.

*Critère de richesse du bloc III.* Le bloc III contient en général entre cinq et quinze unités argumentatives selon la longueur du discours. Un bloc III contenant moins de cinq unités signale soit un discours très court, soit un découpage insuffisamment granulaire — examen au journal.

*Critère de cohérence du bloc V avec l'efficience (v2.1).* Le sous-bloc V.3 est vide si et seulement si le locuteur est non-efficient sur l'objet thématique. Le sous-bloc V.2 est toujours plein si des objets visés sont identifiés. Le sous-bloc V.1 est toujours plein. Le sous-bloc V.4 est plein si des effets sont observables.

---

## 14. Cas-jouets de calibration

M01 dispose des six cas-jouets canoniques du gabarit v2.1 section 14 instanciés sous la version v2.1.

*Cas 1 — simple.* Discours d'acteur efficient sur l'objet thématique avec sophisme certain et omission structurelle évidents. Cas-jouet à instancier — un discours politique simple à charge éthique low avec une attribution causale formellement défaillante (par exemple, "le taux de chômage a baissé pendant mon mandat, donc ma politique en est la cause").

*Cas 2 — sans cible (régime sobre).* Cas-jouet canonique *Fabius v2.1* (vœux Conseil constitutionnel 8 janvier 2024). Locuteur efficient sur les deux objets thématiques (réaffirmation doctrine, annonce décision 25 janvier), V.3 plein et minimal (engagements tenus sans écarts), zone d'indétermination écart 0,20, charge éthique low. Critère décisif validé — zéro sophisme certain, bloc résultats nuls substantiel.

*Cas 3 — ambigu et substantiel.* Cas-jouet canonique *Lecornu v2.1* (DPG 14 octobre 2025). Locuteur efficient sur trois objets thématiques (suspension retraites, renoncement 49.3, programme de méthode), V.3 plein et substantiel — engagement 1 tenu (`observed_as_announced`), engagement 2 rompu explicitement (`broken_explicitly` avec motivation publique invoquant 350 heures de débat), engagement 3 à la limite supérieure (`partially_observed`). Critère décisif validé — pattern `broken_explicitly` correctement identifié et documenté.

*Cas 4 — adversarial (régime de vigilance).* Cas-jouet canonique *Ciotti v2.1* (réponse à la DPG Lecornu 14 octobre 2025). Locuteur non-efficient sur l'objet thématique (critique du gouvernement) mais efficient sur trois des cinq objets visés (positionnement électoral, consolidation alliance UDR-RN, légitimation trajectoire). V.3 vide motivé, V.2 et V.4 substantiels. Critère décisif validé — basculement en `applicable_vigilance_adversariale`, identification correcte des objets visés, chaîne causale aval avec defeaters, motion de censure rejetée et Bardella non nommé à mai 2026 documentés au V.4.

*Cas 5 — écart réel documenté.* À instancier dans rejeux ultérieurs sur la séquence des bilans de mandat.

*Cas 6 — écart apparent expliqué par contrainte.* À instancier dans rejeux ultérieurs.

Les cas-jouets sont inscrits dans le repo de la méthode comme fixtures de test. Toute modification substantielle de M01 déclenche un rejeu des six cas-jouets, dont le résultat est inscrit au journal.

---

## 15. Limites de M01

*Discours courts conventionnels.* M01 est calibrée pour des discours d'au moins quelques centaines de mots avec un enjeu interprétatif. Un communiqué bref purement procédural relève plutôt d'une lecture courante que d'une analyse rhétorique substantielle. M01 peut le traiter mais avec rentabilité épistémique faible.

*Discours multi-locuteurs (débats, échanges parlementaires courts).* M01 traite un discours à la fois. Les échanges parlementaires (questions au gouvernement, motions de censure avec multiples interventions) demandent M03 (analyse comparative multi-acteurs) après application séparée de M01 à chaque intervention substantielle.

*Discours politiques étrangers.* M01 v2.1 est calibrée sur le contexte politique français. Son application à des discours politiques étrangers (US, UK, Allemagne, etc.) demande adaptation des typologies d'historiographies, des registres mobilisés, et des conventions de genre. À traiter quand le besoin se présentera.

---

## 16. Journal méthodologique de M01

M01 tient un journal méthodologique propre selon le gabarit v2.1 section 16.

*Entrées canoniques.*

*method_evolution* — passages de version, frictions identifiées, corrections intégrées. Le passage v2 → v2.1 documente la refonte des étapes 1 et 11 selon les trois frictions identifiées dans le rejeu Ciotti v2 (lisibilité, efficience stratifiée par objet, chaînes causales).

*case_execution* — exécutions notables (cas-jouets rejoués, rejeux comparatifs). Les rejeux v2.1 produits — Ciotti, Fabius, Lecornu — sont inscrits comme validations des trois régimes principaux de M01 v2.1.

*failure_pattern* — recensement des erreurs de raisonnement identifiées au fil des analyses. Patterns documentés à la date de M01 v2.1 : valid_form_with_false_premise, hidden_premise_not_marked, confidence_treated_as_truth, temporal_sequence_treated_as_causality, omission_treated_as_intention, speaker_belief_treated_as_knowledge.

*typology_audit (nouveau v2.1)* — examen périodique des typologies opératoires de M01 selon le critère d'ancrage empirique de la charte v2.1 section 6.6. Chaque audit documente les typologies maintenues, requalifiées, supprimées. Premier audit v2.1 — typologie des actes de langage maintenue (ancrage Austin/Searle/Grice), typologie des présuppositions maintenue (ancrage philosophique du langage), typologie des vulnérabilités argumentatives maintenue (ancrage Aristote/Hamblin/Walton), patterns temporels maintenus avec ancrage empirique documenté (gabarit v2.1 section 6.6), typologie des effets observables maintenue avec ancrage empirique politique-médiatique.

*Statut des failure_patterns selon la charte v2.1.* Les failure_patterns sont des patterns de gouvernance de la méthode, distincts des typologies analytiques applicables aux discours. Ils sont conservés au journal mais clairement séparés des typologies opératoires. Leur fonction est interne au projet et n'impacte pas directement les sorties d'analyse.

Le journal de M01 est versionné en Git, append-only en pratique, accessible aux analystes en lecture seule et à l'auteur de la méthode en écriture.

---

*M01 v2.1 — entrée en vigueur immédiate. Remplace M01 v2. Les analyses déjà produites sous M01 v2 demeurent valables mais ne bénéficient pas des disciplines v2.1 sauf rejeu explicite. Les trois rejeux validants (Ciotti, Fabius, Lecornu) sont inscrits comme cas-jouets canoniques de la version v2.1.*
