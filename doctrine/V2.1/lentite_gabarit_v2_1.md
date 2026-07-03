# L'Entité — Gabarit des méthodes v2.1

*Document normatif qui contraint toute méthode du catalogue. Couche B. Intègre les corrections de la révision v2 → v2.1 — stratification de l'efficience par objets, chaînes causales amont et aval comme objets d'enquête, séparation sortie humaine / journal méthodologique, doctrine sur les patterns observés. Remplace le gabarit v2.*

---

## 0. Préambule — nature, portée, articulation

Le gabarit fixe les contraintes formelles que toute méthode du catalogue (M01 actuelle, M02 à M08 à venir) doit respecter. Il n'est pas une méthode. Il est la grammaire des méthodes. Une méthode qui ne satisfait pas une exigence du gabarit n'est pas dans le catalogue.

Le gabarit a seize sections normatives. Elles décrivent successivement comment une méthode déclare son identité (section 1), comment elle qualifie son type d'objet et ses objets multiples (section 2), comment elle déclare sa finalité (section 3), comment elle décide de son applicabilité à un objet donné (section 4), comment elle structure ses définitions opératoires (section 5), comment elle se déroule en procédure (section 6), comment elle s'audite (sections 7 et 8), comment elle produit ses sorties (sections 9, 10 et 11), comment elle s'articule au graphe (section 12), comment elle s'évalue (section 13), comment elle se calibre par cas-jouets (section 14), ce qu'elle reconnaît comme limites (section 15), comment elle tient son journal (section 16).

Le gabarit v2.1 hérite de la charte v2.1 sans la répéter. Il opérationnalise les engagements et les disciplines de la charte par des contraintes vérifiables. La doctrine de la charte 6.6 sur les patterns (observés vs fabriqués, ancrage empirique requis) est appliquée dans le gabarit aux typologies opératoires des méthodes — patterns temporels, patterns d'effets, sous-types rhétoriques. Toute friction identifiée dans une méthode qui résiste à une résolution interne remonte au gabarit pour examen, et le cas échéant à la charte.

---

## 1. Métadonnées de la méthode

Toute méthode déclare en tête sept métadonnées obligatoires.

*method_id* — identifiant stable au format `MXX` (M01, M02, etc.). Une fois attribué, l'identifiant n'est jamais réaffecté à une autre méthode même après obsolescence.

*method_name* — nom français de la méthode, court (cinq à dix mots), descriptif de l'objet et de l'opération principale.

*method_version* — version au format `X.Y` selon la convention semver simplifiée. La majeure incrémente lors d'une refonte qui invalide la rétrocompatibilité des sorties. La mineure incrémente lors d'évolutions internes compatibles.

*charter_version_required* — version de la charte avec laquelle la méthode est compatible.

*gabarit_version_required* — version du gabarit avec laquelle la méthode est compatible.

*authors* — liste des auteurs de la version courante de la méthode.

*last_revision_date* — date de la dernière révision substantielle.

---

## 2. Type d'objet et identification des objets analysés

Toute méthode déclare les types d'objets sur lesquels elle peut s'appliquer et la procédure d'identification des objets multiples présents dans chaque discours analysé.

### 2.1 Genre d'objet (typologie inchangée v2)

Le type d'objet est une catégorie de production textuelle ou documentaire, caractérisée par son genre, son cadre énonciatif, ses conventions. Les types d'objet canoniques recensés : discours politique (déclaration officielle, intervention parlementaire, allocution télévisée, conférence de presse), communiqué institutionnel structuré, éditorial signé, interview substantielle préparée, plaidoyer judiciaire public, communication d'entreprise stratégique sur décision majeure, document doctrinal d'organisation, déclaration de doctrine d'autorité indépendante, allocution cérémonielle institutionnelle.

Une méthode peut couvrir un, plusieurs ou tous ces types. Elle déclare la liste explicite. Tout objet relevant d'un type non listé ne tombe pas dans le périmètre d'applicabilité de la méthode.

Le type d'objet est distinct du contenu thématique. Une méthode d'analyse rhétorique peut couvrir un discours politique portant sur n'importe quel sujet ; elle ne couvre pas un poème publié, qui n'est pas un genre d'objet listé.

### 2.2 Identification des objets du discours (v2.1)

Pour chaque discours analysé, l'analyste identifie deux catégories d'objets selon la charte v2.1 section 5.

— *L'objet thématique* : ce sur quoi le discours porte explicitement (la réforme des retraites, la critique du gouvernement, la doctrine constitutionnelle, le bilan présidentiel, etc.). Un discours peut avoir plusieurs objets thématiques articulés. L'identification de l'objet thématique procède de la lecture du discours et de ses thèmes traités.

— *Les objets visés* : ce que le discours cherche à produire comme conséquence sur le réel. Typologie ouverte ancrée empiriquement dans la pratique politique et médiatique — positionnement politique d'un acteur, consolidation ou recomposition d'alliance, mobilisation d'un électorat, contestation d'une coalition adverse, ouverture ou fermeture d'une fenêtre d'opportunité, transfert d'autorité institutionnelle, préemption symbolique de critiques attendues, modification d'une jurisprudence à venir, légitimation d'une trajectoire personnelle, etc. L'identification des objets visés procède de l'inférence à partir du discours et du contexte, avec degré de confiance et conditions de révision documentés.

### 2.3 Qualification d'efficience par objet (v2.1)

Pour chaque objet identifié (thématique et visés), le locuteur est qualifié comme *efficient* ou *non-efficient* sur cet objet spécifique. Un même locuteur est typiquement efficient sur certains objets et non-efficient sur d'autres. La qualification est documentée par objet selon la définition opératoire de la section 5.9.

### 2.4 Conséquence sur le déroulement de la méthode

L'identification des objets thématiques et visés, ainsi que la qualification d'efficience par objet, conditionnent la configuration de la procédure d'analyse, notamment du bloc V de la sortie humaine (cf section 9.5). Une méthode qui ne réalise pas cette identification fonctionne en mode dégradé et le déclare.

---

## 3. Finalité analytique

Toute méthode déclare sa finalité analytique en deux paragraphes. *Qu'est-ce que la méthode cherche à éclairer ?* (objet de connaissance) et *quels usages elle sert et quels usages elle ne sert pas* (périmètre d'utilité).

Cette section interdit l'utilisation détournée de la méthode. Une méthode d'analyse rhétorique de discours publics n'est pas utilisable pour produire un jugement sur la personne du locuteur. Une méthode d'analyse historiographique n'est pas utilisable pour arbitrer entre historiographies sur le fond.

La finalité analytique doit être compatible avec la doctrine de la charte v2.1. Elle ne peut pas contredire les quatre engagements de l'ADN ni la discipline épistémique. Notamment, elle doit reconnaître que l'enquête porte sur les chaînes causales amont et aval comme objets d'enquête, conformément à la charte v2.1 section 1 note v2.1 et section 5.

---

## 4. Décision d'applicabilité

Toute méthode définit explicitement la procédure de décision d'applicabilité à un objet donné. La décision produit l'un de quatre verdicts.

*applicable_complete* — l'objet remplit toutes les conditions, la méthode s'exécute en mode standard. Les degrés de confiance peuvent atteindre 1,0.

*applicable_degraded* — l'objet remplit les conditions minimales mais une ou plusieurs conditions ne sont pas pleinement satisfaites (verbatim partiel, contexte difficilement reconstructible, identification du locuteur incertaine, accès aux sources de comparaison limité). La méthode s'exécute en mode dégradé. Les degrés de confiance des annotations sont plafonnés à 0,85. Le mode dégradé est déclaré dans la fiche d'énonciation et justifié par les conditions qui le motivent.

*applicable_vigilance_adversariale* — l'objet est techniquement applicable mais présente des caractéristiques de discours adversarial (charge affective high, polyphonie de registres, attaques personnelles cumulées, glissements sémantiques marqués, emprunts lexicaux à des cadres disqualifiés). La méthode s'exécute avec plafonnement de confidence à 0,85 sur les inférences globales et activation systématique des sous-blocs résultats nuls et éthique. La vigilance adversariale est déclarée dans la fiche d'énonciation et justifiée.

*not_applicable* — l'objet ne remplit pas les conditions minimales. La méthode ne s'exécute pas. Le motif du rejet est inscrit au journal et l'analyste se voit suggérer la méthode appropriée si une autre méthode du catalogue couvre l'objet.

Le détecteur de surcharge contextuelle est un sous-dispositif de la décision d'applicabilité. Il bascule en mode dégradé quand le texte ou le contexte sature les capacités d'analyse — texte excessivement long (au-delà de quinze mille mots), contexte politique impliquant trop d'acteurs simultanés (au-delà de dix acteurs principaux dans une séquence courte), accès aux sources secondaires substantiellement réduit.

En l'état du projet (v2.1), la décision d'applicabilité reste *semi-manuelle* — un analyste humain prend la décision sur la base de critères opérationnels documentés dans la méthode. L'automatisation par un classifieur dédié est inscrite comme objectif v3.

---

## 5. Définitions opératoires

Toute méthode fournit les définitions opératoires des concepts qu'elle mobilise. La définition opératoire d'un concept est sa traduction en critère vérifiable à l'application. Une définition académique ne suffit pas — il faut "ce qui compte comme X dans l'analyse".

Le gabarit v2.1 impose les champs de définition obligatoires suivants pour toute méthode.

*5.1 Unité d'analyse de la méthode.* Une unité argumentative dans M01, un indice dans M02 si elle est instanciée, etc. Définition opératoire : critères qui permettent de découper un texte en unités sans ambiguïté excessive.

*5.2 Statuts épistémiques.* Trois statuts canoniques de la charte (fait établi, inférence, hypothèse), avec les critères opératoires de classification.

*5.3 Régime épistémique des attributions mentales.* Quatre opérateurs distincts de la discipline des passages — K (savoir établi factif), B (croyance), Affirme (assertion sans hypothèse sur la croyance), Prétend_savoir (présentation comme certain sans validation indépendante). Critères opératoires pour basculer d'un opérateur à l'autre.

*5.4 Gradation des sophismes ou vulnérabilités argumentatives.* Trois niveaux — certain, probable, possible. Définition opératoire du sophisme certain par les trois critères cumulatifs (structure logique formellement défaillante, absence de lecture charitable alternative, démontrabilité sans information externe). Un seul critère manquant rétrograde le défaut en vulnérabilité probable ou possible.

*5.5 Gradation des omissions.* Trois niveaux — structurelle, stratégique probable, intentionnelle non prouvée.

*5.6 Charge affective du discours.* Trois niveaux — faible, moyenne, élevée. Conditionne la vigilance sur les vulnérabilités d'analyse liées (sympathie projetée, mimétisme rhétorique).

*5.7 Charge éthique du discours.* Trois niveaux — faible, moyenne, élevée. Conditionne le régime de la reconstruction charitable et l'activation du sous-bloc éthique non neutralisé.

*5.8 Pondération des historiographies concurrentes.* Quatre niveaux — disqualifiée, marginale, contestée, consensus fort. Toute mention d'historiographie concurrente déclare son niveau. La typologie est ancrée empiriquement dans la pratique académique des sciences sociales — c'est un pattern observé conformément à la doctrine de la charte v2.1 section 6.6.

### 5.9 Efficience d'un acteur sur un objet (v2.1)

Définition opératoire : un acteur est *efficient* sur un objet donné si, dans la fenêtre temporelle pertinente, il peut directement ou via une chaîne courte documentable produire des actes qui modifient le réel correspondant à cet objet. *Indicateurs* : compétence institutionnelle reconnue, pouvoir de décision unilatéral ou de blocage, capacité d'exécution opérationnelle, signature d'engagement à valeur juridique ou institutionnelle. *L'absence des indicateurs* qualifie comme *non-efficient* sur cet objet.

La qualification est strictement relative à l'objet. Un même acteur peut être efficient sur l'objet O1 et non-efficient sur l'objet O2. Exemples ancrés empiriquement : un président de groupe parlementaire d'opposition est non-efficient sur l'objet "composition du gouvernement" mais efficient sur l'objet "consolidation publique de son alliance électorale" ; un Premier ministre est efficient sur l'objet "annonce d'une réforme" et "engagement procédural sur le 49.3" mais non-efficient sur l'objet "perception publique de sa méthode" ; un président du Conseil constitutionnel est efficient sur l'objet "annonce d'une décision à venir" et "réaffirmation de la doctrine institutionnelle".

Trois valeurs possibles : `efficient`, `efficient_partiel` (le locuteur a une influence directe partielle, le succès dépend aussi d'autres acteurs), `non_efficient`. La valeur `efficient_partiel` permet de qualifier les cas où le locuteur produit un acte de parole performatif mais où la conséquence dépend également de la réception ou du vote d'autres acteurs.

### 5.10 Objet thématique et objets visés du discours (v2.1)

*L'objet thématique* est ce sur quoi le discours porte explicitement, identifiable par les thèmes traités dans le discours et par leur structure argumentative.

*Les objets visés* sont ce que le discours cherche à produire comme conséquences sur le réel, identifiables par inférence à partir du discours et du contexte. *Critère opérationnel d'identification* : pour chaque grande figure rhétorique mobilisée (hyperbole, prophétie, disqualification d'un acteur, appel à l'alliance, transfert d'autorité, préemption symbolique, etc.), quelle conséquence sur le réel cette figure cherche-t-elle plausiblement à produire ? Les conséquences identifiées sont consolidées en typologie d'objets visés propre à l'analyse.

L'inférence est non définitive — chaque objet visé porte son degré de confiance (entre 0 et 1) et ses conditions de révision. La confidence sur l'identification d'un objet visé porte sur l'inférence d'identification, pas sur la vérité de l'objet (qui est lui-même un acte de discours observé).

Les objets visés sont distincts des effets observables. Un objet visé est *l'intention plausible de production* attribuée au discours ; un effet observable est *le résultat constatable* dans la fenêtre temporelle. L'écart entre objet visé et effet observable est précisément ce que documente le sous-bloc V.4 de la sortie humaine.

### 5.11 Chaîne causale amont et chaîne causale aval (v2.1)

*Chaîne causale amont* : ce qui, dans le contexte politique, médiatique, biographique du locuteur ou de la séquence, a nourri ou rendu probable le discours dans sa forme actuelle. Identification d'éléments documentables — positions antérieures du locuteur, conjoncture politique, événements déclencheurs, attentes électorales documentables, négociations préalables, contraintes institutionnelles. Chaque élément documenté par source et avec confidence.

*Chaîne causale aval* : ce que le discours cherche à produire comme conséquences sur les objets visés, et ce qui peut être observé ou prédit comme effet plausible. Identification d'éléments observables ou inférables — réactions documentables d'autres acteurs, modifications des coalitions, effets de mobilisation mesurables, ouvertures ou fermetures d'options politiques.

Les deux chaînes sont des *objets d'enquête*, pas des présupposés. L'enquête sur les chaînes mobilise les sources externes au discours, applique la défaisabilité (au moins deux defeaters par lien causal inféré, cf section 6.5), et produit des hypothèses argumentées avec degré de confiance. L'engagement 4 de l'ADN (refus de présupposer la chaîne causale) s'applique pleinement.

Toute méthode peut ajouter des définitions opératoires propres à sa spécificité, dans le respect de la doctrine de la charte v2.1 section 6.6 — toute typologie additionnelle doit être ancrée empiriquement par au moins deux ou trois cas externes au projet documentables, faute de quoi elle est requalifiée en inférence.

---

## 6. Procédure générique en étapes typées

Toute méthode déclare sa procédure en étapes ordonnées et typées. Chaque étape porte un identifiant, une entrée typée, une opération, une sortie typée, et un critère de succès / échec.

Le gabarit v2.1 ne fixe pas la liste des étapes (chaque méthode a sa procédure propre), mais il fixe huit *contraintes transversales* qui s'appliquent à toutes les méthodes du catalogue.

### 6.1 Charité interprétative non négociable comme étape précoce

Toute méthode portant sur un discours, un argumentaire ou une production textuelle structurée intègre une étape de reconstruction charitable de l'argument du locuteur dans sa meilleure version, *avant* toute étape de détection de défauts. Cette étape n'est pas optionnelle.

### 6.2 Règle opérationnelle pour la charité

La reconstruction charitable obéit à une règle opérationnelle stricte. Tout terme évaluatif emprunté au discours analysé est traité selon l'une de trois modalités. *Marqué entre guillemets*, *attribué explicitement au locuteur*, ou *reformulé en lexique descriptif neutre*. La règle interdit l'emploi non marqué des termes évaluatifs du locuteur. La violation de la règle est un défaut d'analyse signalé au journal méthodologique.

### 6.3 Articulation charité et charge éthique

Quand la charge éthique du discours est qualifiée *élevée*, la reconstruction charitable s'applique à la structure argumentative du discours mais *ne neutralise pas la qualification éthique de son objet*. Le sous-bloc éthique non neutralisé de la sortie humaine signale explicitement le contenu éthiquement disqualifiable qui demeure dans la reformulation charitable. La charité reformule l'argument ; elle ne lave pas son objet.

### 6.4 Régime épistémique des attributions mentales

Toute attribution d'état mental ou cognitif à un locuteur dans le cours de l'analyse déclare son régime parmi les quatre opérateurs de la section 5.3 (K, B, Affirme, Prétend_savoir). L'usage de K (savoir établi factif) requiert que la proposition attribuée soit indépendamment vérifiable par les sources. Si la proposition n'est pas indépendamment établie, K n'est pas disponible — on doit utiliser B, Affirme ou Prétend_savoir selon le cas.

### 6.5 Défaisabilité des règles causales et comportementales

Toute inférence causale ou comportementale invoquée dans une analyse déclare au moins *deux conditions de défaite* (defeaters). Une condition de défaite est une situation documentable où la règle ne tiendrait pas. Les defeaters sont énumérés dans la sortie machine M01-M et discutés brièvement dans la sortie humaine lorsqu'ils éclairent significativement l'analyse.

L'exigence de défaisabilité s'applique en particulier aux liens inférés dans les chaînes causales amont et aval de la section 5.11. Tout `PlausibleConsequence` du schéma porte au moins deux defeaters.

### 6.6 Patterns temporels pour les écarts discours / actes (v2.1)

Toute documentation d'un écart entre un discours qui annonce un acte et la réalité observée typage l'écart par l'un de sept patterns canoniques. La liste des patterns est conforme à la doctrine de la charte v2.1 section 6.6 — chaque pattern est ancré empiriquement par au moins deux ou trois cas externes au projet documentables. Les patterns relèvent de motifs observés dans la pratique politique et institutionnelle, pas de catégories fabriquées a priori.

*not_yet_observed* — l'acte annoncé n'est pas encore observable parce que la fenêtre temporelle prévue n'est pas close. Ancrage empirique : engagements à long terme typiques des programmes électoraux ou des plans de mandat.

*never_observed* — l'acte annoncé devait être réalisé dans une fenêtre temporelle close, et il ne l'a pas été. Ancrage empirique : promesses non tenues sans justification publique invoquée (multiples cas documentés dans les bilans de mandat).

*observed_later* — l'acte annoncé a été réalisé après la fenêtre temporelle initialement prévue, avec ou sans modification de modalités. Ancrage empirique : engagements reportés (réforme des institutions, simplification administrative, etc.).

*observed_otherwise* — l'acte annoncé a été réalisé sous une forme modifiée par rapport à l'annonce. Ancrage empirique : engagements réinterprétés dans leur mise en œuvre (notamment dans les négociations parlementaires ou syndicales).

*observed_by_other_actor* — l'acte annoncé a été produit par un acteur différent du locuteur, dans un cadre institutionnel modifié. Ancrage empirique : changements de gouvernement ou de législature qui déplacent l'agent de l'engagement.

*prevented_by_constraint* — l'acte annoncé n'a pas été réalisé en raison d'une contrainte institutionnelle, juridique ou politique documentable qui rendait sa réalisation impossible. La contrainte est nommée. Ancrage empirique : censure constitutionnelle d'une mesure annoncée, blocage parlementaire structurel sans alternative, opposition d'une autre institution avec pouvoir de blocage.

*broken_explicitly* (v2.1) — l'acte annoncé a été *publiquement révisé ou abandonné* par le locuteur lui-même, avec motivation publique invoquée (changement de circonstances, impasse parlementaire, calcul stratégique révisé). Distinct de `never_observed` (sans justification publique) et de `prevented_by_constraint` (contrainte externe non levable). Le pattern reconnaît la pratique politique de la révision publique d'engagement comme dispositif de gestion. Ancrage empirique : Hollande sur la déchéance de nationalité janvier-mars 2016 (annoncée après les attentats, retirée après l'impossibilité d'obtenir l'accord parlementaire, avec motivation publique invoquant l'impasse) ; Lecornu sur le 49.3 en janvier 2026 (annoncé dans la DPG du 14 octobre 2025 comme rupture méthodologique, renié le 19 janvier 2026 face à l'impossibilité de faire voter le budget par majorité, avec motivation publique invoquant 350 heures de débat sans issue) ; Hollande sur les retraites en 2014 (engagement réinterprété face aux contraintes budgétaires européennes).

Le typage est obligatoire ; il distingue sept situations que le langage courant amalgame. La typologie est révisable selon le critère d'ancrage empirique — un pattern qui perdrait son ancrage par révision de cas serait requalifié en inférence.

### 6.7 Hypothèses concurrentes et zone d'indétermination

Toute synthèse en hypothèses concurrentes inclut au moins trois hypothèses, dont au moins deux non intentionnelles. L'écart de confiance entre l'hypothèse dominante et la deuxième hypothèse est calculé.

Si l'écart est *inférieur ou égal à 0,2*, la synthèse déclare une *zone d'indétermination* — aucune hypothèse n'est qualifiée univoquement de dominante, les hypothèses sont présentées comme co-explicatives.

Si l'écart est *compris entre 0,2 (exclu) et 0,4 (inclu)*, la dominance est qualifiée *incertaine* ; la synthèse formule explicitement les conditions d'arbitrage qui permettraient de trancher.

Si l'écart est *supérieur à 0,4*, la dominance est claire et la synthèse en énonce les conditions de révision.

### 6.8 Séparation des chaînes causales et des hypothèses concurrentes (v2.1)

L'analyse des chaînes causales amont et aval (section 5.11) est *distincte* de la synthèse en hypothèses concurrentes (section 6.7). Les chaînes causales documentent les éléments contextuels qui éclairent la genèse et les conséquences plausibles du discours. Les hypothèses concurrentes formulent des lectures explicatives globales du discours qui restent en compétition épistémique.

Une chaîne causale amont peut nourrir une hypothèse concurrente sans s'y substituer. Une hypothèse concurrente peut prédire des effets observables qui figurent dans la chaîne causale aval sans la résumer. Les deux dispositifs travaillent ensemble mais ne sont pas équivalents.

---

## 7. Contrôles internes

Toute méthode déclare ses contrôles internes — dispositifs vérifiables qui auditent l'exécution de la méthode.

*Anonymisation des agents.* Les instances LLM mobilisées dans l'exécution de la méthode (analyste, contradicteur, auditeur) n'ont pas de persona, pas de nom, pas d'historique. Le system prompt de chaque agent contient les instructions opérationnelles tirées de la spec de méthode et rien d'autre.

*Journalisation systématique.* Chaque appel LLM produit dans le cadre de la méthode est journalisé intégralement — prompt complet, réponse complète, modèle utilisé avec version, paramètres, latence, coût en tokens. La journalisation est append-only et liée à l'identifiant d'analyse.

*Audit des sources par poste d'observation.* La méthode produit, en sortie machine, la liste des sources convoquées. Un module d'audit régulier vérifie la distribution des sources et signale les asymétries fortes.

*Vérification de la conformité au gabarit.* Une analyse produite n'est validée comme conforme au gabarit que si elle satisfait tous les champs obligatoires définis dans les sections 5, 6, 9, 10, 11. La vérification est automatisable par schéma Pydantic.

*Audit des typologies opératoires (v2.1).* Conformément à la doctrine de la charte v2.1 section 6.6, les typologies opératoires de la méthode (patterns temporels, patterns d'effets sur l'arène, sous-types de présuppositions, niveaux de consensus historiographique, etc.) sont auditées périodiquement selon le critère d'ancrage empirique. Une typologie qui perd son ancrage par révision de cas est requalifiée en inférence. L'audit est documenté au journal de la méthode (section 16).

---

## 8. Dégradation gracieuse

Toute méthode déclare comment elle se comporte face à des conditions sous-optimales. La dégradation gracieuse a quatre paliers.

*Palier 1 — verbatim partiel.* Le texte source n'est accessible que partiellement. Mode dégradé déclaré, plafonnement de confiance à 0,85, signalement systématique des conditions de révision liées à l'accès au texte intégral.

*Palier 2 — contexte difficile à reconstruire.* Le contexte politique, institutionnel ou social du discours n'est pas pleinement documentable depuis le poste d'observation. Mode dégradé déclaré.

*Palier 3 — saturation cognitive du LLM.* Le texte excède les capacités de traitement d'un appel LLM unique. Découpage du texte en segments avec analyse séquentielle. Synthèse explicite des segments. Risque de dérive de la discipline méthodologique signalé.

*Palier 4 — rentabilité épistémique insuffisante.* L'analyse ne produit ni fait nouveau, ni inférence solide, ni hypothèse discriminante. La méthode s'arrête, déclare l'insuffisance, et l'inscrit au journal.

---

## 9. Sortie humaine

Toute méthode produit une sortie humaine structurée. Format : Markdown structuré.

### 9.0 Discipline de séparation (v2.1)

La sortie humaine est conçue pour être lisible par un lecteur humain non-analyste. Elle présente l'analyse rhétorique du discours, ses inférences, ses hypothèses concurrentes, ses résultats nuls et ses conditions de révision selon les blocs structurés ci-dessous. Elle *n'inclut pas* les notes méthodologiques sur les choix d'interprétation, les recommandations pour révision du gabarit, les méta-commentaires sur la calibration de la version courante, les auto-évaluations de conformité — qui appartiennent au journal méthodologique séparé.

*Test de qualité opérationnel* : la sortie humaine doit être lisible par un lecteur intéressé par le contenu du discours analysé sans pré-requis sur le gabarit. Cette discipline s'applique à toutes les méthodes du catalogue.

### 9.1 Bloc I — Fiche d'énonciation

Locuteur (avec rôle à la date), date, lieu, auditoires (primaire et secondaires), canal, séquence politique ou institutionnelle, genre, contrat de communication implicite, *charge affective codée*, *charge éthique codée*, *identification des objets thématiques* (selon section 2.2 et 5.10), *identification des objets visés* avec confidence (selon section 2.2 et 5.10), *qualification d'efficience par objet* (selon section 2.3 et 5.9), décision d'applicabilité avec mode.

### 9.2 Bloc II — Reconstruction charitable

Reformulation de l'argument du discours dans sa meilleure version, dans le respect de la règle opérationnelle (section 6.2). Cette reconstruction est la base de l'analyse en aval — tout défaut identifié est défaut de cette meilleure version.

### 9.3 Bloc III — Analyse par unités

Pour chaque unité argumentative identifiée : citation ou paraphrase du segment, types d'actes de langage, présuppositions (avec leur type doxique, idéologique, pragmatique), vulnérabilités argumentatives (avec leur gradation et la lecture charitable alternative quand elle existe), omissions (avec leur gradation), fonction politique inférée (avec son niveau de confiance et l'opérateur épistémique applicable).

### 9.4 Bloc IV — Lexique, registres et figures

Termes-clés mobilisés avec glissements sémantiques éventuels, registres empruntés, ethos construit par le locuteur, pathos mobilisé, logos structurant, doxa mobilisée.

### 9.5 Bloc V — Chaînes causales et écarts (v2.1)

Le bloc V documente l'inscription du discours dans les chaînes causales amont et aval, et les écarts identifiables entre ce que le discours dit ou annonce et ce qui est ou peut être observé. Le bloc V est structuré en quatre sous-blocs.

*Sous-bloc V.1 — Chaîne causale amont.* Identification des éléments documentables qui ont nourri le discours dans sa forme actuelle, selon la définition de la section 5.11. Chaque élément documenté par source. La chaîne amont éclaire la genèse du discours sans la réduire à elle. Defeaters globaux à la chaîne mentionnés.

*Sous-bloc V.2 — Objets visés et chaîne causale aval.* Identification des objets visés par le discours (selon section 5.10). Pour chaque objet visé, hypothèse sur les conséquences plausibles que le discours cherche à produire, avec degré de confiance et au moins deux defeaters par conséquence (selon section 6.5). Effets déjà observables documentés s'ils sont disponibles à la date de l'analyse.

*Sous-bloc V.3 — Écarts sur l'objet thématique (si locuteur efficient sur cet objet).* Pour chaque engagement, prédiction ou annonce du discours portant sur l'objet thématique, identification de l'acte attendu et comparaison à la réalité observée. Typage par les sept patterns temporels de la section 6.6.

Le sous-bloc V.3 est *vide* si le locuteur est non-efficient sur l'objet thématique (cas typique des discours d'opposition sans pouvoir d'agir direct). Il est *plein et minimal* si le locuteur est efficient sans engagements vérifiables substantiels (cas typique des discours doctrinaux d'autorité indépendante). Il est *plein et substantiel* si le locuteur est efficient avec engagements multiples (cas typique des DPG ou des annonces gouvernementales).

*Sous-bloc V.4 — Effets observables sur les objets visés.* Pour tout locuteur, efficient ou non sur l'objet thématique. Documentation des effets observables ou plausibles du discours sur les objets visés : réception par d'autres acteurs, reprises et contestations, modifications de coalitions, ouvertures ou fermetures d'options. Typologie ancrée empiriquement dans la pratique médiatico-politique — amplification, contestation, ignorement, reprise par alliance, appropriation tactique, amplification non anticipable (effets dus à des événements postérieurs au discours et non liés directement à la stratégie du locuteur, ancrage empirique : amplification du discours Fabius par décès Badinter ; amplification rétrospective de discours politiques par succession institutionnelle imprévue).

Les sous-blocs sont activés selon la configuration de l'analyse. Sur un locuteur efficient sur l'objet thématique, V.1 + V.2 + V.3 + V.4 sont typiquement substantiels. Sur un locuteur non-efficient sur l'objet thématique mais efficient sur des objets visés, V.1 + V.2 + V.4 sont substantiels et V.3 est vide ou minimal. Le bloc V dans son ensemble documente *toujours* l'inscription du discours dans des chaînes causales — c'est ce qui distingue la finalité d'enquête de L'Entité d'une simple analyse rhétorique.

### 9.6 Bloc VI — Historiographies mobilisées

Chaque historiographie mobilisée par le discours est nommée. Pour chaque historiographie, son ou ses historiographies concurrentes sont nommées avec leur niveau de consensus académique selon la typologie de la section 5.8. Pas de fausse symétrie. La distinction entre *mobilisation thématique-explicite* et *mobilisation lexicale-marginale* d'une historiographie est documentée — un terme emprunté à un cadre disqualifié sans thématisation explicite est mobilisé lexicalement-marginalement, ce qui est distinct d'une adhésion thématique au cadre.

### 9.7 Bloc VII — Synthèse en trois statuts épistémiques

Faits établis, inférences (avec leur niveau de confiance et leur prémisse), hypothèses concurrentes (au moins trois dont au moins deux non intentionnelles). Calcul de l'écart de confiance entre hypothèse dominante et deuxième hypothèse. Application de la convention 6.7 — zone d'indétermination, dominance incertaine, ou dominance claire selon l'écart. Red team objections à l'hypothèse dominante ou à l'hypothèse co-dominante.

### 9.8 Bloc VIII — Blocs de neutralisation et conditions de révision

Quatre sous-blocs obligatoires.

*Résultats nuls* — ce que la méthode a cherché et n'a pas trouvé (sophismes certains, omissions intentionnelles prouvées, écarts documentés au-delà du raisonnable, incohérences factuelles, etc.). Discipline contre le biais de soupçon.

*Ce que le discours dit correctement* — éléments du discours qui sont exemplairement précis, fondés, ou méthodologiquement irréprochables. Cette discipline empêche la lecture systématiquement défavorable.

*Indices non convergents* — éléments d'analyse qui ne pointent pas nettement dans une direction et qui demandent à être suspendus ou arbitrés par des informations externes.

*Conditions de révision* — circonstances documentables qui modifieraient l'analyse.

Pour les discours à *charge éthique élevée ou medium avec emprunts identifiés*, le bloc VIII inclut un cinquième sous-bloc : *Contenu éthiquement non neutralisé par la charité* — signalement explicite du contenu disqualifiable qui demeure dans la reformulation charitable, en application de la section 6.3.

---

## 10. Sortie publique M01-P

Toute méthode produit une sortie publique structurée en cinq éléments imposés. La sortie publique est destinée au Mode 3 (chat public) et aux usages de lecture rapide. Format : prose continue, *cent cinquante à trois cents mots*.

*Élément 1 — Énonciation.* Une phrase qui dit qui parle, à qui, dans quel cadre, à quelle date.

*Élément 2 — Fait dominant ou inférence principale.* Deux à trois phrases qui énoncent le constat le plus solide produit par l'analyse, avec son régime épistémique explicite (fait établi ou inférence).

*Élément 3 — Hypothèse dominante avec confiance et alternative non intentionnelle principale.* L'hypothèse dominante avec sa confiance, et l'hypothèse alternative non intentionnelle principale avec sa confiance. Si la zone d'indétermination est déclarée en bloc VII, la formule "deux hypothèses sont proches en confiance et coexistent comme co-explicatives" est employée plutôt qu'une qualification de dominance.

*Élément 4 — Renvois.* Un lien vers l'analyse complète et un lien vers la source primaire pour l'auditeur qui veut juger lui-même.

*Élément 5 — Bloc de clôture logique.* Une formule typée qui qualifie la solidité de l'inférence principale (solide / plausible / fragile), énonce la prémisse implicite principale sur laquelle elle repose, et liste deux ou trois conditions de révision documentables.

La règle opérationnelle pour la charité (section 6.2) s'applique également à la sortie publique. Les termes évaluatifs du locuteur sont mis entre guillemets.

La sortie publique est *générée automatiquement* à partir d'une sortie machine validée, par un appel LLM dédié (modèle plus léger admis). La génération est validée par schéma — longueur dans la plage, présence des cinq éléments dans l'ordre, absence de termes évaluatifs du locuteur non marqués.

---

## 11. Sortie machine

Toute méthode produit une sortie machine structurée en YAML. La sortie machine est destinée à l'ingestion dans le graphe cognitif et à la validation par schéma. Format : YAML conforme au schéma Pydantic de la méthode.

Le gabarit v2.1 impose les blocs canoniques suivants pour toute sortie machine. Schéma Pydantic enrichi par rapport à v2.

```yaml
method_id: string
method_version: string
analysis_id: string
execution_date: date
execution_mode:
  - applicable_complete
  - applicable_degraded
  - applicable_vigilance_adversariale
  - not_applicable
execution_mode_reason: string

source:
  text_id: string
  provenance: string
  integrity_status:
    - certified
    - partial
    - uncertain
  text_span_total: string
  retrieval_date: datetime
  content_hash: string

enonciation:
  speaker:
    id: string
    name: string
    role_at_date: string
  date: date
  place: string
  primary_audience: string
  secondary_audiences: list[string]
  channel: string
  political_sequence: string | null
  genre: string
  communication_contract: string
  affective_charge:
    - low
    - medium
    - high
  ethical_charge:
    - low
    - medium
    - high
  # nouveau v2.1 : identification des objets
  thematic_objects: list[ThematicObject]
  targeted_objects: list[TargetedObject]

charity_reconstruction:
  content: string
  borrowed_terms_handled:
    - term: string
      handling:
        - quoted
        - attributed
        - reformulated_neutral

units: list[Unit]

# nouveau v2.1 : chaînes causales
upstream_causal_chain: UpstreamCausalChain
downstream_causal_chains: list[DownstreamCausalChain]

# nouveau v2.1 : écarts sur objet thématique (V.3)
discourse_action_gaps_on_thematic_objects: list[DiscourseActGap]
observable_effects_on_targeted_objects: list[ObservableEffect]

historiographies: list[Historiography]

epistemic_synthesis:
  established_facts: list[string]
  inferences: list[Inference]
  competing_hypotheses: list[Hypothesis]
  hypothesis_gap: float
  hypothesis_status:
    - zone_of_indetermination
    - uncertain_dominance
    - clear_dominance
  red_team_objections: list[string]

null_results:
  searched_not_found:
    fallacies: string
    omissions: string
    discourse_act_gaps: string
  rhetorically_ordinary_elements: list[string]
  non_convergent_indices: list[string]
  what_the_discourse_states_correctly: list[string]
  ethical_content_not_neutralized: string | null

invisible_and_revision:
  invisible_from_this_post: list[string]
  revision_conditions: list[string]
  next_methods_recommended: list[string]
```

Schémas spécifiques v2.1 :

```yaml
ThematicObject:
  object_id: string
  label: string
  efficiency_status:
    - efficient
    - efficient_partiel
    - non_efficient
    - ambiguous
  efficiency_justification: string

TargetedObject:
  object_id: string
  label: string
  inference_confidence: float
  inference_confidence_applies_to: inference   # contrainte : toujours "inference"
  grounded_in: list[string]                    # min 1 — éléments du discours qui supportent l'inférence
  efficiency_status:
    - efficient
    - efficient_partiel
    - non_efficient
    - ambiguous
  efficiency_justification: string

UpstreamCausalChain:
  elements: list[UpstreamElement]

UpstreamElement:
  element_label: string
  type:
    - prior_position
    - context
    - trigger_event
    - electoral_expectation
    - prior_negotiation
    - institutional_constraint
  source_reference: string
  confidence: float
  confidence_applies_to: inference

DownstreamCausalChain:
  targeted_object_id: string
  plausible_consequences: list[PlausibleConsequence]

PlausibleConsequence:
  consequence_label: string
  confidence: float
  confidence_applies_to: inference
  defeaters: list[string]                      # min 2 — contrainte section 6.5
  observable_to_date: string | null

DiscourseActGap:
  thematic_object_id: string
  declared: string                             # ce qui a été annoncé
  pattern_type:                                # contrainte section 6.6 — sept patterns v2.1
    - not_yet_observed
    - never_observed
    - observed_later
    - observed_otherwise
    - observed_by_other_actor
    - prevented_by_constraint
    - broken_explicitly
  observation_window: string
  observation: string                          # ce qui est observé à la date d'analyse
  constraint_named: string | null              # si pattern == prevented_by_constraint
  public_motivation_invoked: string | null     # si pattern == broken_explicitly
  source_reference: string

ObservableEffect:
  targeted_object_id: string
  effect_type:                                 # typologie v2.1 ancrée empiriquement
    - amplification
    - contestation
    - ignorement
    - reprise_par_alliance
    - appropriation_tactique
    - amplification_non_anticipable
    - confirmation_institutionnelle
  description: string
  source_reference: string

Vulnerability:
  type: string
  level:
    - certain
    - probable
    - possible
  evidence_span: string
  confidence: float
  confidence_applies_to:
    - inference
    - hypothesis
    - source_reliability
  charitable_alternative: string | null
  hidden_premises: list[string]
  defeaters: list[string]                      # min 2 pour règles causales

Omission:
  missing_element: string
  level:
    - structural
    - strategic_probable
    - intentional_proven
  why_expected: string
  evidence_of_expected_knowledge: string
  confidence: float
  confidence_applies_to: inference

InferredFunction:
  label: string
  confidence: float
  confidence_applies_to: inference
  epistemic_regime:                            # contrainte section 6.4
    - knows
    - believes
    - asserts
    - claims_to_know
  alternative_functions: list[InferredFunction]

Historiography:
  reference_in_text: string
  mobilized: string
  mobilization_type:                           # nouveau v2.1
    - thematic_explicit
    - lexical_marginal
  consensus_level_mobilized:
    - disqualified
    - marginal
    - contested
    - strong_consensus
  competing: string | null
  consensus_level_competing: string | null
  what_competing_would_say: string | null
```

Validation supplémentaire v2.1 : tout `TargetedObject` doit avoir `grounded_in` non vide. Toute `PlausibleConsequence` doit porter au moins deux defeaters. Tout `DiscourseActGap` avec `pattern_type == broken_explicitly` doit avoir `public_motivation_invoked` non null.

Le YAML est validé par schéma Pydantic à chaque ingestion. Toute analyse non valide est rejetée et renvoyée à l'agent analyste pour correction.

---

## 12. Articulation au graphe cognitif

Toute méthode déclare ses *exports graphe* — nœuds et arêtes à ingérer dans le graphe à partir de la sortie machine. Le gabarit v2.1 fixe les types canoniques de nœuds et arêtes accessibles, sans imposer qu'une méthode les mobilise tous.

*Types de nœuds canoniques.* Speaker, SpeechEvent, SpeechAct, Presupposition, Sophism (ou ArgumentativeVulnerability), Omission, HistoriographyReference, Method, Source, Hypothesis, DiscourseActGap. *Nouveaux nœuds v2.1* : ThematicObject, TargetedObject, UpstreamElement, PlausibleConsequence, ObservableEffect.

*Types d'arêtes canoniques.* utters, contains_act, presupposes, produces_vulnerability, omits, mobilizes_historiography, mobilizes_historiography_lexically (nouveau v2.1), competes_with, produced_by_method, cites, explains, reveals_gap. *Nouvelles arêtes v2.1* : targets_object (SpeechEvent → TargetedObject), nourished_by (SpeechEvent → UpstreamElement), aims_at_consequence (TargetedObject → PlausibleConsequence), produces_observable_effect (SpeechEvent → ObservableEffect).

Chaque arête porte au minimum les attributs suivants : `causality_type` (efficient_strong, efficient_weak, correlational, structural), `weight` (0.0 à 1.0), `evidence` (référence textuelle), `confidence` (0.0 à 1.0), `confidence_applies_to` (inference, hypothesis, source_reliability), `method_id`.

Le graphe est versionné. L'ontologie évolue selon les besoins, et les évolutions sont tracées dans le journal méthodologique. Toute méthode déclare la version de l'ontologie graphe qu'elle utilise.

---

## 13. Critères d'évaluation

Toute méthode déclare comment elle s'évalue. Le gabarit v2.1 fixe sept critères transversaux applicables à toute méthode du catalogue.

*Conformité de format.* La sortie machine valide le schéma. La sortie humaine respecte la structure en huit blocs avec les sous-blocs obligatoires, y compris le bloc V en quatre sous-blocs v2.1. La sortie publique respecte les cinq éléments imposés.

*Discipline de la gradation.* Sophismes certains rares et justifiés par les trois critères cumulatifs. Omissions intentionnelles non prouvées rares et signalées comme telles. Pas de niveau "certain" sans démonstration soutenable.

*Présence d'un bloc résultats nuls substantiel.* Au moins quatre points distincts dans le bloc résultats nuls.

*Présence d'hypothèses non intentionnelles concurrentes.* Au moins deux hypothèses non intentionnelles dans la synthèse, formulées comme alternatives sérieuses.

*Cohérence avec la pondération des historiographies.* Toute historiographie concurrente déclarée est qualifiée selon la typologie en quatre niveaux. Pas de fausse symétrie.

*Conformité à la règle opérationnelle de la charité.* La reconstruction charitable ne contient pas de termes évaluatifs du locuteur non marqués.

*Cohérence du bloc V avec la qualification d'efficience (v2.1).* Le sous-bloc V.3 est vide si et seulement si le locuteur est non-efficient sur l'objet thématique. Le sous-bloc V.2 est toujours plein si des objets visés sont identifiés. Le sous-bloc V.1 est toujours plein. Le sous-bloc V.4 est plein si des effets sont observables dans la fenêtre temporelle d'analyse.

*Critère décisif pour les cas-jouets sans cible.* La méthode appliquée à un discours sobre produit zéro sophisme certain et un bloc résultats nuls substantiel.

*Critère décisif pour les cas-jouets adversariaux.* La méthode appliquée à un discours conçu pour piéger l'analyse bascule en mode `applicable_vigilance_adversariale` plutôt que produire un résultat trompeur présenté comme complet.

---

## 14. Cas-jouets normés (v2.1)

Toute méthode dispose d'un jeu de cas-jouets normés pour la calibration. Le gabarit v2.1 fixe six types de cas-jouets canoniques que toute méthode doit avoir. Les cas-jouets v2.1 incorporent la stratification des objets et l'analyse des chaînes causales.

*Cas 1 — simple.* Discours d'acteur efficient sur l'objet thématique, avec sophisme certain et omission structurelle évidents. Critère décisif : la méthode identifie les deux sans hésitation.

*Cas 2 — sans cible (régime sobre).* Discours d'acteur efficient sur l'objet thématique, sobre, sans sophisme majeur, sans omission stratégique probable. Critère décisif : la méthode produit zéro sophisme certain et un bloc résultats nuls substantiel. Cas-jouet canonique : *Fabius v2.1* (vœux Conseil constitutionnel 8 janvier 2024).

*Cas 3 — ambigu.* Discours d'acteur efficient avec zone d'indétermination des hypothèses. Critère décisif : la méthode classifie l'omission au bon niveau et applique la convention 6.7. Cas-jouet canonique : *Lecornu v2.1* (DPG 14 octobre 2025) — pour la zone d'indétermination et les engagements multiples sur l'objet thématique.

*Cas 4 — adversarial (régime de vigilance).* Discours non-efficient sur l'objet thématique mais efficient sur objets visés, avec surcharge contextuelle, cadrage affectif fort, polyphonie. Critère décisif : la méthode bascule en mode `applicable_vigilance_adversariale`, identifie correctement les objets visés et la chaîne causale aval, produit un sous-bloc V.3 vide motivé et un sous-bloc V.4 substantiel. Cas-jouet canonique : *Ciotti v2.1* (réponse à la DPG Lecornu, 14 octobre 2025).

*Cas 5 — écart réel documenté.* Discours d'acteur efficient sur l'objet thématique avec écart réellement documenté (acte annoncé non réalisé, fenêtre close). Critère décisif : la méthode identifie l'écart selon le pattern temporel approprié des sept patterns v2.1. Cas-jouet à instancier dans le rejeu de la séquence retraites avec engagement non tenu documenté.

*Cas 6 — écart apparent expliqué par contrainte.* Discours d'acteur efficient avec écart apparent qui peut être expliqué par une contrainte institutionnelle documentable. Critère décisif : la méthode identifie le pattern `prevented_by_constraint` et nomme la contrainte. Cas-jouet à instancier.

Les cas-jouets sont inscrits dans le repo de la méthode comme fixtures de test. Toute modification substantielle de la méthode (passage de version) déclenche un rejeu des six cas-jouets, dont le résultat est inscrit au journal.

---

## 15. Limites du gabarit

Le gabarit v2.1 ne traite pas explicitement plusieurs questions que les méthodes futures pourraient soulever.

*Méthodes non textuelles.* Le gabarit est conçu pour les méthodes qui analysent des productions textuelles. Une méthode qui analyserait des images, des vidéos, des données quantitatives demanderait des contraintes adaptées.

*Méthodes de synthèse multi-textuelle.* Le gabarit traite l'analyse d'un texte à la fois. M03 (analyse comparative multi-acteurs) demande une extension du gabarit pour la cohérence inter-textuelle et l'agrégation des objets visés multi-acteurs. Extension partielle réalisée en v2.1 par la matrice des objets visés ; extension complète à finaliser.

*Méthodes prédictives.* Le gabarit traite l'analyse rétrospective ou contemporaine. Une méthode prédictive devrait formaliser ses incertitudes et ses conditions de révision différemment.

*Articulation au mode 2.* Les contraintes spécifiques aux méthodes du mode 2 (conseiller du prince) ne sont pas explicitées dans le gabarit v2.1. Elles relèvent du distribution restreinte (charte v2.1 section 8.2) et seront fixées dans une extension dédiée du gabarit.

---

## 16. Journal méthodologique de la méthode

Toute méthode tient un journal méthodologique propre, distinct du journal général du projet. Le journal de la méthode trace les évolutions de la méthode (passages de version, frictions identifiées, corrections intégrées), les exécutions notables (cas-jouets rejoués, rejeux comparatifs), les audits des typologies opératoires.

Le journal de la méthode est versionné en Git, append-only en pratique, accessible aux analystes en lecture seule et à l'auteur de la méthode en écriture.

Une catégorie d'entrée canonique du journal est *failure_pattern* — recensement des erreurs de raisonnement identifiées au fil des analyses. Patterns documentés à la date du gabarit v2.1 : valid_form_with_false_premise, hidden_premise_not_marked, confidence_treated_as_truth, temporal_sequence_treated_as_causality, omission_treated_as_intention, speaker_belief_treated_as_knowledge.

*Statut spécifique des failure_patterns selon la charte v2.1 section 6.6.* Les failure_patterns sont des patterns de gouvernance du projet (motifs récurrents d'erreur dans la conduite de l'analyse) — distincts des patterns analytiques portant sur les métiers observés (patterns temporels, patterns d'effets sur l'arène, etc.). Ils sont conservés au journal mais clairement séparés des typologies analytiques de la méthode. Leur fonction est interne au projet et n'impacte pas directement les sorties d'analyse.

Une seconde catégorie d'entrée canonique v2.1 est *typology_audit* — examen périodique des typologies opératoires de la méthode selon le critère d'ancrage empirique de la charte 6.6. Chaque audit documente les typologies maintenues (avec cas externes documentés), requalifiées en inférences (avec motivation), ou supprimées (avec motivation).

---

*Gabarit v2.1 — entrée en vigueur immédiate. Remplace le gabarit v2. Toute méthode du catalogue (M01 actuelle, M03 actuelle, M02 et autres à venir) doit être révisée pour conformité au présent gabarit avant exécution sur de nouvelles analyses. Les analyses déjà produites sous gabarit v2 demeurent valables mais ne bénéficient pas des disciplines v2.1 sauf rejeu explicite.*
