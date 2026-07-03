# L'Entité — Méthode 01 v2 : Analyse rhétorique d'un discours public

*Couche C — instance de méthode dans le catalogue. Implémente le gabarit v2 pour le type d'objet "discours politique et institutionnel". Remplace M01 v1.*

---

## 1. Métadonnées

```yaml
method_id: M01_ANALYSE_RHETORIQUE
method_name: "Analyse rhétorique d'un discours public"
method_version: 2.0
charter_version_required: 2.0
gabarit_version_required: 2.0
authors: [équipe projet L'Entité]
last_revision_date: 2026-05-16
```

---

## 2. Type d'objet

M01 couvre les types d'objet suivants définis par le gabarit section 2 : *discours politique* (déclaration officielle, intervention parlementaire, allocution télévisée, conférence de presse), *communiqué institutionnel structuré*, *éditorial signé*, *interview substantielle préparée*, *allocution cérémonielle institutionnelle*, *déclaration de doctrine d'autorité indépendante*.

M01 ne couvre pas le *plaidoyer judiciaire public* (méthode dédiée à instancier sous M07 — analyse des plaidoiries) ni la *communication d'entreprise stratégique sur décision majeure* (méthode dédiée à instancier sous M08 — analyse de communication corporate).

Le type d'objet est distinct du sujet thématique. M01 peut s'appliquer à un discours politique sur n'importe quel sujet (retraites, immigration, écologie, défense, etc.). Le sujet thématique conditionne les sources de comparaison mobilisables et les historiographies pertinentes, mais ne modifie pas le périmètre d'applicabilité.

---

## 3. Finalité analytique

M01 cherche à éclairer la structure rhétorique d'un discours public en distinguant rigoureusement ce que le discours *dit*, ce que le discours *présuppose*, ce que le discours *omet*, ce qui dans le discours *fait écart* avec les actes du locuteur, et ce que le discours *mobilise* comme cadres historiographiques. La méthode produit une analyse à plusieurs niveaux qui rend visible la fabrique rhétorique du texte sans la confondre avec un jugement sur la personne du locuteur ou sur la légitimité de ses positions politiques.

M01 sert : à l'analyse critique du débat public, à l'auto-formation des analystes, à l'objectivation de séquences politiques contestées, à la mise en évidence d'écarts entre engagement déclaré et réalisation effective. M01 ne sert pas : à produire un jugement moral sur le locuteur, à prédire le succès politique de son discours, à arbitrer entre positions politiques en compétition. La méthode est rigoureuse sur la structure rhétorique ; elle est silencieuse sur la valeur des positions défendues.

---

## 4. Décision d'applicabilité

M01 applique la procédure de décision d'applicabilité du gabarit section 4 avec quatre conditions opérationnelles spécifiques.

*Condition d'identification du locuteur.* Le locuteur doit être identifiable (nom, fonction, date d'occupation de la fonction). Un texte publié anonymement n'est pas analysable par M01 sans identification préalable de l'auteur.

*Condition d'intégrité du texte.* Le texte doit être accessible dans sa version officielle ou dans une transcription certifiée. Si seul un extrait substantiel mais non exhaustif est accessible, la méthode bascule en mode dégradé.

*Condition de contexte reconstructible.* Le contexte politique, institutionnel ou social du discours doit pouvoir être documenté depuis les sources publiques accessibles. Si le contexte est opaque (par exemple un discours interne à une organisation dont les enjeux sont confidentiels), la méthode bascule en mode dégradé.

*Condition de finalité analytique.* La demande qui motive l'analyse doit être compatible avec la finalité de M01 (section 3). Une demande qui sollicite implicitement un jugement moral sur le locuteur ou un arbitrage sur la légitimité de ses positions est traitée par le module Elenchus (couche d'exécution v2) qui reformule la demande en termes compatibles avec M01 avant l'exécution.

Le détecteur de surcharge contextuelle (gabarit section 4) bascule M01 en mode dégradé quand le texte excède quinze mille mots, ou quand la séquence politique impliquée mobilise plus de dix acteurs principaux dans une courte fenêtre temporelle.

---

## 5. Définitions opératoires propres à M01

M01 hérite des huit définitions opératoires du gabarit section 5 (unité d'analyse, statuts épistémiques, régime épistémique des attributions mentales, gradation des sophismes, gradation des omissions, charge affective, charge éthique, pondération des historiographies). Elle y ajoute quatre définitions propres à l'analyse rhétorique.

### 5.1 Unité argumentative

Définition opératoire : une *unité argumentative* est un segment du discours qui forme une opération rhétorique identifiable, paraphrasable en une phrase contenant un verbe principal et un complément. Une unité peut contenir plusieurs phrases si elles produisent ensemble une seule opération (par exemple, énoncer une thèse puis la justifier par un exemple immédiat). Une phrase peut contenir plusieurs unités si elle produit plusieurs opérations distinctes (assertion + concession + retour à la thèse, par exemple).

Critère de découpage : on découpe au plus petit niveau qui préserve la cohérence de l'opération rhétorique. Si en hésitation, on découpe au niveau qui produit l'analyse la plus claire — pas le plus fin, pas le plus large.

La granularité du découpage est un point sensible documenté. Un autre analyste pourrait raisonnablement produire un nombre différent d'unités sur le même texte. Le journal méthodologique trace les frictions de granularité identifiées au fil des analyses.

### 5.2 Typologie des actes de langage

M01 mobilise une typologie d'actes de langage adaptée aux discours politiques et institutionnels. Onze types canoniques : *assertion* (le locuteur énonce une proposition comme vraie), *justification* (le locuteur fonde une proposition antérieure), *concession* (le locuteur reconnaît un argument adverse partiellement), *réfutation* (le locuteur écarte un argument adverse), *promesse* (le locuteur s'engage sur une action future), *annonce performative* (le locuteur produit l'effet qu'il énonce — "je proclame", "j'annonce"), *évaluation* (le locuteur juge une situation ou un acteur), *définition* (le locuteur fixe le sens d'un terme), *attribution causale* (le locuteur établit un lien causal entre deux faits), *appel* (le locuteur sollicite une action ou un soutien), *récit* (le locuteur narre une séquence d'événements).

Un même segment peut combiner plusieurs actes. La typologie n'est pas exhaustive ; un acte non listé est rapporté à la catégorie la plus proche et le cas est inscrit au journal pour examen d'une extension de la typologie.

### 5.3 Typologie des présuppositions

Trois types canoniques. *Présupposition doxique* — proposition implicite partagée comme évidence par l'auditoire visé (par exemple, "le système de retraite par répartition est la base du contrat social français"). *Présupposition idéologique* — proposition implicite portée par un cadre idéologique identifiable, non universellement partagée (par exemple, "la stabilité politique est un bien suprême et indivisible"). *Présupposition pragmatique* — proposition implicite nécessaire à la cohérence du discours, sans laquelle l'énoncé serait incohérent ou non interprétable (par exemple, dans "même pendant la suspension", la présupposition pragmatique est qu'il y aura effectivement suspension).

Chaque présupposition identifiée déclare son type, sa formulation explicite, et son `evidence_span` (passage du discours qui la fait surgir).

### 5.4 Typologie des vulnérabilités argumentatives

Les vulnérabilités argumentatives canoniques de M01 sont regroupées en six familles avec leur définition opérationnelle, leur forme logique le cas échéant, et la lecture charitable alternative typique.

*Famille 1 — appels rhétoriques à l'évidence.* Sous-types : ad populum ("plus personne ne peut le nier"), ad verecundiam (appel à l'autorité non pertinente), ad antiquitatem (appel à la tradition). Forme typique : "X est vrai parce que tous reconnaissent X" — où la reconnaissance ne prouve pas la vérité. Lecture charitable alternative : la formule est conventionnelle et n'engage pas l'interdiction de la contestation.

*Famille 2 — défauts du raisonnement formel.* Sous-types : affirmation du conséquent ((P→Q) ∧ Q ⇒ P), négation de l'antécédent ((P→Q) ∧ ¬P ⇒ ¬Q), pétition de principe (la conclusion est dans une des prémisses). Forme logique vérifiable. Le sophisme certain dans cette famille exige les trois critères cumulatifs du gabarit (structure formellement défaillante, absence de lecture charitable, démontrabilité sans information externe).

*Famille 3 — faux dilemmes et fausses oppositions.* Sous-types : présentation de deux options comme les seules disponibles alors qu'une troisième existe, opposition de positions qui ne sont pas réellement incompatibles. Lecture charitable alternative : le locuteur peut faire un raccourci rhétorique sans nier l'existence d'autres options.

*Famille 4 — disqualifications de l'opposition.* Sous-types : disqualification morale (les opposants sont irresponsables, lâches, malhonnêtes), disqualification par la passion (les opposants ne raisonnent pas, ils ressentent). Forme typique : "[opposants à P] sont [terme disqualifiant]". Vulnérabilité fréquente mais rarement sophisme certain — la lecture charitable alternative est presque toujours disponible (le locuteur peut viser une fraction spécifique des opposants).

*Famille 5 — confusions de modalités.* Sous-types : nécessité empirique transformée en obligation morale, possibilité transformée en probabilité, conditionnel transformé en certain. Forme typique : "X est nécessaire, donc s'opposer à X est mal". Vulnérabilité importante pour les discours qui mobilisent de la nécessité (économique, politique, technique).

*Famille 6 — défauts de l'attribution mentale.* Sous-types : usage non factif de K (le locuteur affirme savoir ce que les sources n'établissent pas), attribution de croyance non justifiée (le locuteur attribue à un tiers une croyance non documentée). Cette famille est nouvelle en M01 v2 — elle découle directement de la discipline des passages de la charte v2 section 6.5.

La typologie n'est pas exhaustive. Une vulnérabilité non listée est rapportée à la famille la plus proche et le cas est inscrit au journal.

---

## 6. Procédure en quatorze étapes

M01 v2 conserve l'architecture en quatorze étapes de la v1, avec des corrections internes à plusieurs étapes pour intégrer les contraintes du gabarit v2.

### Étape 1 — Validation du matériau et décision d'applicabilité

Vérification des quatre conditions de la section 4. Application du détecteur de surcharge contextuelle. Verdict : `applicable_complete`, `applicable_degraded` (avec justification explicite) ou `not_applicable` (avec motif et redirection éventuelle).

### Étape 2 — Fiche d'énonciation enrichie

Production des champs de la fiche d'énonciation selon le gabarit section 9 bloc I. Inclut obligatoirement le pouvoir d'agir effectif du locuteur à la date, la séquence politique ou institutionnelle, le contrat de communication implicite, *la charge affective codée* et *la charge éthique codée* (les deux selon le gabarit section 5).

### Étape 3 — Genre et contrat de communication

Identification du genre rhétorique précis (DPG, allocution télévisée, vœux institutionnels, etc.) et de ses conventions propres. Cette étape conditionne l'identification ultérieure des éléments rhétoriquement ordinaires (relevant du genre) par opposition aux choix stratégiques individuels.

### Étape 4 — Découpage en unités argumentatives

Application de la définition opératoire de l'unité argumentative (section 5.1). Production d'une liste numérotée d'unités (U1, U2, etc.) avec leur citation ou paraphrase.

### Étape 5 — Reconstruction charitable de l'argument principal (NON-NÉGOCIABLE)

Cette étape précède toute détection de défauts. Reformulation de l'argument du discours dans sa meilleure version — telle qu'un défenseur compétent du locuteur la formulerait.

Application obligatoire de la *règle opérationnelle pour la charité* (gabarit section 6.2). Tout terme évaluatif emprunté au discours est traité selon l'une de trois modalités — *guillemets*, *attribution explicite*, *reformulation en lexique descriptif neutre*. La sortie de cette étape déclare pour chaque terme évaluatif identifié quelle modalité a été appliquée.

Si la charge éthique a été codée *élevée* en étape 2, l'étape 5 produit en parallèle un *signalement* du contenu éthiquement disqualifiable qui demeure dans la reformulation. Ce signalement alimentera le cinquième sous-bloc du bloc VIII en sortie humaine (gabarit section 6.3).

### Étape 6 — Actes de langage par unité

Pour chaque unité, identification des actes de langage selon la typologie de la section 5.2 et de leur niveau de confiance. Un même segment peut combiner plusieurs actes.

Pour les actes qui attribuent un état mental au locuteur ou à un tiers, application du *régime épistémique des attributions mentales* (gabarit section 6.4) — déclaration du régime parmi K (savoir factif), B (croyance), Affirme (assertion sans hypothèse de croyance), Prétend_savoir (présenté comme certain sans validation indépendante).

### Étape 7 — Lexique, registres, ethos, pathos, logos, doxa

Identification des termes-clés mobilisés avec leurs glissements sémantiques éventuels. Identification des registres empruntés (juridique-institutionnel, industrialiste-souverainiste, social-démocrate, gaullien, etc.). Caractérisation de l'ethos construit par le locuteur. Caractérisation du pathos mobilisé en cohérence avec la charge affective déclarée en étape 2. Structure logique principale (logos). Doxa mobilisée.

### Étape 8 — Présuppositions et cadrages

Identification des présuppositions selon la typologie de la section 5.3 (doxique, idéologique, pragmatique). Chaque présupposition déclare son type, sa formulation, son `evidence_span`.

### Étape 9 — Vulnérabilités argumentatives et sophismes

Pour chaque unité, identification des vulnérabilités argumentatives selon la typologie de la section 5.4. Application stricte des *trois critères cumulatifs du sophisme certain* (gabarit section 5) : structure logique formellement défaillante, absence de lecture charitable alternative, démontrabilité sans information externe.

Pour les vulnérabilités relevant de la famille 2 (défauts du raisonnement formel) ou de la famille 5 (confusions de modalités), identification des *prémisses cachées* qui rendent l'argument apparemment valide, avec leur statut épistémique (établi / contesté / non justifié) et leur niveau de confiance. Identification des *defeaters* (gabarit section 6.5) — conditions qui défont l'inférence si elles sont vérifiées.

Le verdict par défaut est *vulnérabilité possible* ou *vulnérabilité probable*. Le verdict *sophisme certain* est rare et systématiquement justifié par les trois critères. Si un seul critère manque, le verdict rétrograde.

### Étape 10 — Omissions qualifiées

Identification des omissions selon les trois niveaux du gabarit section 5 — *structurelle* (élément nécessaire à la compréhension, dont la présence est attendue), *stratégique probable* (élément qui aurait servi l'argumentation mais que l'orateur avait vraisemblablement intérêt à écarter), *intentionnelle non prouvée* (élément probable mais intention de dissimulation non démontrée).

Pour chaque omission, déclaration de l'élément manquant, du niveau, de la raison pour laquelle on attend sa présence, et de la preuve que le locuteur avait accès à l'information manquante (sources publiques disponibles à la date du discours, par exemple).

### Étape 11 — Croisement discours / actes

Pour chaque engagement ou prédiction contenu dans le discours, identification de l'acte attendu et comparaison à la réalité observée dans la fenêtre temporelle pertinente. Application obligatoire du *typage par les six patterns temporels* (gabarit section 6.6) : non encore observé, jamais observé, observé plus tard, observé autrement, observé par un autre acteur, empêché par une contrainte.

Pour les écarts en mode *non encore observé*, déclaration de la fenêtre de vérification. Pour les écarts en mode *empêché par une contrainte*, nomination explicite de la contrainte. Pour les écarts en mode *observé autrement*, comparaison entre la forme annoncée et la forme effective.

Cette étape dépend systématiquement de l'accès à des sources externes au discours. En mode dégradé, l'étape peut être partielle — chaque écart non documentable est signalé comme tel.

### Étape 12 — Historiographies mobilisées

Identification des historiographies mobilisées par le discours. Pour chaque historiographie mobilisée, identification de son ou ses historiographies concurrentes. Application obligatoire de la *pondération par niveau de consensus académique* (gabarit section 5 et charte v2 section 6.4) — disqualifiée, marginale, contestée, consensus fort. Toute historiographie concurrente déclare son niveau.

Pour chaque historiographie concurrente non disqualifiée, formulation succincte de ce qu'elle dirait que l'historiographie mobilisée tait.

### Étape 13 — Hypothèses concurrentes et red team

Production d'au moins trois hypothèses explicatives concurrentes des décisions ou positions du locuteur dans le discours analysé, dont au moins deux *hypothèses non intentionnelles*. Pour chaque hypothèse, déclaration de son type (intentionnelle / non intentionnelle), de sa confiance (entre 0,0 et 1,0), et des éléments factuels et inférentiels qui la fondent.

Calcul de l'*écart de confiance* entre l'hypothèse dominante et la deuxième hypothèse. Application de la convention 6.7 du gabarit :
- *écart ≤ 0,2* — zone d'indétermination, aucune hypothèse n'est qualifiée univoquement de dominante ;
- *écart entre 0,2 et 0,4* — dominance incertaine, conditions d'arbitrage formulées explicitement ;
- *écart > 0,4* — dominance claire, conditions de révision énoncées.

Production d'objections de type *red team* à l'hypothèse dominante ou aux hypothèses co-dominantes. Une red team objection efficace soulève un défaut substantiel de l'hypothèse, pas un détail.

### Étape 14 — Synthèse en trois statuts et exports

Production de la sortie humaine M01-H (gabarit section 9, huit blocs), de la sortie machine M01-M (gabarit section 11), et de la sortie publique M01-P (gabarit section 10, cinq éléments).

La sortie publique M01-P est générée *à partir* du M01-M validé par un appel LLM dédié. Le générateur respecte le format en cinq éléments imposé par le gabarit — énonciation, fait dominant ou inférence principale, hypothèses concurrentes avec écart de confiance, renvois, bloc de clôture logique. La règle opérationnelle pour la charité s'applique à la M01-P.

---

## 7. Contrôles internes propres à M01

M01 hérite des contrôles internes du gabarit section 7 (anonymisation des agents, journalisation systématique, audit des sources, vérification de conformité au gabarit) et y ajoute deux contrôles propres.

*Contrôle de granularité du découpage.* La méthode signale au journal méthodologique le nombre d'unités identifiées à l'étape 4. Si le nombre s'écarte significativement de la fourchette typique pour le genre (par exemple, plus de vingt unités pour un discours de mille mots), un signal est levé pour examen.

*Contrôle de la conformité de la charité.* La méthode vérifie automatiquement la sortie de l'étape 5 contre la règle opérationnelle (section 6.2 du gabarit). Tout terme évaluatif détecté comme appartenant au discours analysé et utilisé non marqué dans la reconstruction charitable est signalé comme défaut de conformité. La détection automatique est imparfaite — elle complète mais ne remplace pas la vigilance de l'analyste.

---

## 8. Dégradation gracieuse

M01 applique les quatre paliers de dégradation du gabarit section 8 avec les adaptations suivantes pour le type d'objet "discours public".

*Palier 1 — verbatim partiel.* M01 peut produire une analyse substantielle à partir d'extraits convergents représentant au moins soixante pour cent du discours. En deçà, la méthode bascule en *not_applicable* avec recommandation d'attendre l'accès au verbatim complet. Le cas-jouet Fabius valide cet usage du palier 1.

*Palier 2 — contexte difficile à reconstruire.* L'étape 11 (croisement discours / actes) est la plus affectée. M01 documente chaque écart non documentable, et l'analyse demeure substantielle sur les autres étapes.

*Palier 3 — saturation cognitive du LLM.* Pour les discours longs, découpage en segments avec analyse séquentielle. M01 produit alors une *synthèse de segments* explicite, et signale les risques de dérive de la discipline entre segments (par exemple, la reconstruction charitable d'un segment peut influencer indûment l'analyse d'un autre).

*Palier 4 — rentabilité épistémique insuffisante.* Si l'analyse ne produit ni fait nouveau, ni inférence solide, ni hypothèse discriminante (par exemple sur un discours purement conventionnel sans enjeu interprétatif), M01 produit une sortie minimale qui déclare l'insuffisance et l'inscrit au journal.

---

## 9. Sortie humaine M01-H

M01 produit les huit blocs canoniques du gabarit section 9, sans modification de structure. Les particularités de M01 sont les suivantes.

Le *bloc III* (Analyse par unités) est en général le bloc le plus volumineux pour M01 — c'est le cœur de l'analyse rhétorique. La profondeur de l'analyse de chaque unité est *variable selon la richesse rhétorique* de l'unité — une unité qui mobilise plusieurs présuppositions et plusieurs vulnérabilités demande plus de développement qu'une unité conventionnelle.

Le *bloc V* (Écarts discours/actes) est souvent le plus dépendant de l'accès aux sources externes. En mode dégradé, ce bloc peut être substantiellement réduit ; le bloc VIII (résultats nuls et conditions de révision) prend alors plus d'importance.

Le *cinquième sous-bloc du bloc VIII* — *Contenu éthiquement non neutralisé par la charité* — est obligatoire si la charge éthique a été codée *élevée* en étape 2. Sur un discours politique mainstream, ce sous-bloc est rarement déclenché. Sur un discours xénophobe, négationniste ou appelant à la violence, il est obligatoire et substantiel.

---

## 10. Sortie publique M01-P

M01 produit la sortie publique selon le gabarit section 10 — cinq éléments dans l'ordre, cent cinquante à trois cents mots. Les recommandations propres à M01 pour la rédaction de la M01-P :

*Élément 3 — hypothèses concurrentes avec écart de confiance.* Sur un cas en zone d'indétermination (écart ≤ 0,2), la formulation type recommandée est : "Deux hypothèses sont proches en confiance et coexistent comme co-explicatives — [hypothèse A] (confiance X) et [hypothèse B] (confiance Y). L'analyse ne tranche pas entre elles ; les deux peuvent être simultanément vraies à des degrés variables." Cette formulation préserve la nuance épistémique tout en restant lisible.

*Élément 5 — bloc de clôture logique.* Pour M01, le bloc de clôture qualifie l'inférence principale (solide / plausible / fragile) selon les critères opérationnels suivants. *Solide* — l'inférence est fondée sur des faits établis et une chaîne de raisonnement explicite, sans prémisse implicite contestable. *Plausible* — l'inférence repose sur une prémisse implicite identifiable et soutenable mais non démontrée. *Fragile* — l'inférence repose sur plusieurs prémisses implicites contestables ou sur une chaîne dont un maillon est explicitement incertain.

La sortie publique est validée par un schéma qui vérifie : la longueur (plage 150-300 mots), la présence des cinq éléments dans l'ordre, l'absence de termes évaluatifs du locuteur non marqués, la cohérence entre la qualification du bloc de clôture et le contenu de l'élément 2 (un fait dominant ne peut pas être déclaré dans l'élément 2 si l'inférence principale est qualifiée *fragile* dans l'élément 5).

---

## 11. Sortie machine M01-M

M01 produit le YAML conforme au schéma du gabarit section 11. Le schéma Pydantic spécifique à M01 inclut tous les champs canoniques et ajoute deux blocs propres à M01.

*Bloc `lexicon_analysis`* — termes-clés, glissements sémantiques, registres empruntés, ethos, pathos, logos, doxa. Structuré selon le bloc IV de la sortie humaine.

*Bloc `historiographies`* — chaque historiographie mobilisée avec son ou ses historiographies concurrentes et la pondération par niveau de consensus.

Le bloc `units` est typé par le schéma `Unit` du gabarit section 11. Chaque unité porte ses speech_acts (selon la typologie 5.2), ses presuppositions (selon la typologie 5.3), ses argumentative_vulnerabilities (selon la typologie 5.4), ses omissions, et son inferred_function. Le champ `epistemic_regime` est obligatoire pour les inferred_functions qui attribuent un état mental.

Le bloc `discourse_action_gaps` est typé par le schéma `DiscourseActGap` du gabarit. Chaque écart porte son `pattern_type` parmi les six patterns canoniques.

---

## 12. Articulation au graphe cognitif

M01 produit dans le graphe les types de nœuds canoniques suivants : Speaker, SpeechEvent, SpeechAct, Presupposition, ArgumentativeVulnerability, Omission, HistoriographyReference, Method, Source, Hypothesis, DiscourseActGap.

Les arêtes typiques que M01 produit : utters, contains_act, presupposes, produces_vulnerability, omits, mobilizes_historiography, competes_with, produced_by_method, cites, explains, reveals_gap.

Chaque arête porte les attributs obligatoires du gabarit section 12 (causality_type, weight, evidence, confidence, confidence_applies_to, method_id).

L'ingestion graphe est conditionnée à la validation du M01-M par le schéma Pydantic. Une analyse non valide n'est pas ingérée — elle est renvoyée à l'agent analyste pour correction.

---

## 13. Critères d'évaluation propres à M01

M01 hérite des six critères transversaux du gabarit section 13 (conformité de format, discipline de la gradation, bloc résultats nuls substantiel, hypothèses non intentionnelles concurrentes, cohérence pondération historiographies, conformité règle charité). Elle y ajoute trois critères propres.

*Cohérence inter-blocs.* Les blocs III, IV, VI, VII de la sortie humaine doivent être mutuellement cohérents. Une historiographie identifiée comme contestée dans le bloc VI doit produire des présuppositions identifiées dans le bloc III. Une hypothèse dominante du bloc VII doit être documentée par les actes de langage et les omissions des blocs III et IV.

*Calibration de la profondeur.* L'analyse d'une unité argumentative doit être proportionnée à sa richesse rhétorique. Une unité conventionnelle ne reçoit qu'une analyse minimale ; une unité dense reçoit une analyse développée. La répartition uniforme de l'attention sur toutes les unités est un signal de défaut — soit l'analyste a sur-analysé des unités conventionnelles, soit il a sous-analysé des unités denses.

*Calibration de la M01-P.* La sortie publique préserve la nuance épistémique du M01-H sans la trahir. Si le M01-H déclare une zone d'indétermination, le M01-P ne peut pas désigner une hypothèse dominante. Si le M01-H qualifie l'inférence principale fragile, le M01-P ne peut pas la qualifier solide.

---

## 14. Cas-jouets de M01

M01 dispose des six cas-jouets canoniques du gabarit section 14. À la date du gabarit v2, trois cas ont été instanciés sur des sources réelles ; trois cas restent à instancier.

*Cas 1 — simple, à instancier.* Discours avec sophisme certain et omission structurelle évidents. Candidat à examiner : un communiqué de campagne électorale comportant un faux dilemme manifeste. À produire dans la suite v2.

*Cas 2 — sans cible, instancié.* Discours de Laurent Fabius, vœux du Conseil constitutionnel au Président de la République, 8 janvier 2024. *Verdict : passé.* La méthode produit zéro sophisme certain et un bloc résultats nuls substantiel (sept points). Le mode dégradé est correctement appliqué (verbatim partiel, plafonnement de confiance à 0,85). Référence : `lentite_cas_jouet_2_fabius.md` (v1) et `lentite_rejeu_v2_lecornu_fabius.md` (v2).

*Cas 3 — ambigu, partiellement instancié.* Le rejeu Lecornu v2 sert de cas 3 — l'écart de confiance entre hypothèses A et B est à 0,2, exactement à la limite de la zone d'indétermination. La méthode déclare correctement l'indétermination. Référence : `lentite_rejeu_v2_lecornu_fabius.md`.

*Cas 4 — adversarial, à instancier.* Discours conçu pour piéger l'analyse (surcharge contextuelle, cadrage affectif fort, ironie, polyphonie). Candidat à examiner : un discours de polémiste mobilisant plusieurs registres simultanément. C'est le test décisif restant pour la dégradation gracieuse de M01 v2.

*Cas 5 — écart réel, à instancier.* Discours qui annonce un acte effectivement non réalisé dans la fenêtre de vérification close. Candidat : un engagement de campagne précis non tenu deux ans après.

*Cas 6 — écart apparent, à instancier.* Discours qui annonce un acte non réalisé, mais avec une contrainte institutionnelle documentable. Candidat : un engagement présidentiel empêché par une décision du Conseil constitutionnel.

Toute modification majeure de M01 (passage de version) déclenche un rejeu des six cas-jouets, dont le résultat est inscrit au journal.

---

## 15. Limites de M01

M01 ne traite pas l'analyse de cohérence entre plusieurs discours d'un même locuteur sur une période. Cette analyse demande une méthode dédiée (M02 candidate — analyse longitudinale de trajectoire discursive).

M01 ne traite pas l'analyse comparative de plusieurs locuteurs sur un même événement. Cette analyse demande une méthode dédiée (M03 candidate — analyse comparative de discours concurrents).

M01 ne traite pas l'analyse de réception du discours par ses auditoires. La réception est un objet distinct (réactions médiatiques, sondages, comportements politiques observables). Une méthode dédiée serait M04 — analyse de réception.

M01 ne produit pas d'analyse historiographique du débat de fond convoqué par le discours. Elle identifie les historiographies mobilisées et leurs concurrentes pondérées, mais elle ne tranche pas le débat lui-même. Une méthode dédiée serait M05 — triangulation historiographique.

M01 ne produit pas d'analyse contrefactuelle (qu'aurait-il pu se passer si le locuteur avait dit autre chose, fait autre chose, été dans une autre position). Une méthode dédiée serait M06 — analyse contrefactuelle.

Ces limites ne sont pas des défauts. Elles sont la condition de la rigueur de M01 sur son périmètre.

---

## 16. Journal méthodologique de M01

Le journal méthodologique de M01 trace l'évolution de la méthode depuis sa première version, et l'inscrit dans la mémoire d'échecs.

*Évolution v0 → v1.* Restructuration en quatorze étapes avec la charité interprétative comme étape 5 non négociable. Introduction de la gradation des sophismes (certain / probable / possible) et des omissions (structurelle / stratégique probable / intentionnelle non prouvée). Introduction des blocs de neutralisation obligatoires (résultats nuls, ce que le discours dit correctement, indices non convergents). Introduction de la sortie machine M01-M YAML. Test sur le rejeu Lecornu — vérification que la discipline v1 tient.

*Évolution v1 → v2.* Intégration des sept corrections de la restructuration v2 (charge éthique en plus de la charge affective, règle opérationnelle pour la charité, sortie M01-P publique, zone d'indétermination ≤ 0,2, pondération des historiographies en quatre niveaux, clarification du sophisme certain par trois critères cumulatifs, articulation charité et seuil de toxicité). Intégration des corrections logiques retenues dans le rapport sur la logique (régime épistémique K/B/Affirme/Prétend_savoir dans les attributions mentales, défaisabilité des règles avec au moins deux defeaters, distinction confidence/truth jamais sur truth_itself, patterns temporels pour les écarts discours/actes, bloc de clôture logique en M01-P). Test sur le rejeu v2 Lecornu + cas-jouet 2 Fabius — vérification que la discipline v2 tient.

*Frictions identifiées à surveiller.*

— Granularité du découpage en unités argumentatives. Définition opératoire améliorée en v1 par la formule "paraphrasable en une phrase avec verbe principal et complément" mais le seuil de granularité reste un point d'appréciation de l'analyste. Test inter-analyste à conduire.

— Frontière entre *contesté* et *marginal* pour la pondération des historiographies. L'indicateur opérationnel "moins de 20% de la communauté académique pertinente identifiable" est posé en gabarit v2 mais reste à éprouver sur d'autres cas.

— Convention "inférieur ou égal à 0,2" pour la zone d'indétermination. Sur Lecornu et Fabius, l'écart est exactement à 0,2 — déclenchement systématique. À éprouver sur un cas où l'écart serait à 0,25 (déclenchement attendu de "dominance incertaine") et sur un cas à 0,15 (déclenchement clair d'indétermination).

— Tension M01-P sur les discours rhétoriquement chargés. La sortie publique fonctionne naturellement sur discours sobre (Fabius) ; elle exige plus de discipline pour préserver la nuance épistémique sur discours chargé (Lecornu). À surveiller sur cas 4 adversarial.

*Patterns d'échec documentés (failure_pattern selon gabarit section 16).* Six patterns inscrits comme mémoire d'échecs de raisonnement : valid_form_with_false_premise, hidden_premise_not_marked, confidence_treated_as_truth, temporal_sequence_treated_as_causality, omission_treated_as_intention, speaker_belief_treated_as_knowledge. Ce dernier pattern est particulièrement pertinent pour M01 — il correspond à l'usage non factif de K dans les attributions mentales, que la discipline des passages cherche à empêcher.

---

*M01 v2 — entrée en vigueur immédiate. Toute nouvelle analyse rhétorique produite par le projet applique M01 v2. Les analyses produites sous M01 v1 demeurent valables comme références historiques mais ne bénéficient pas des disciplines v2 sauf rejeu explicite. Le rejeu v2 sur Lecornu et Fabius est inscrit au journal comme validation préalable.*
