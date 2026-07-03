# L'Entité — Gabarit des méthodes v2

*Document normatif qui contraint toute méthode du catalogue. Couche B. Intègre les corrections de la restructuration v2 et les corrections logiques retenues dans le rapport sur l'intégration de la logique. Remplace le gabarit v1.*

---

## 0. Préambule — nature, portée, articulation

Le gabarit fixe les contraintes formelles que toute méthode du catalogue (M01 actuelle, M02 à M08 à venir) doit respecter. Il n'est pas une méthode. Il est la grammaire des méthodes. Une méthode qui ne satisfait pas une exigence du gabarit n'est pas dans le catalogue.

Le gabarit a quinze sections normatives. Elles décrivent successivement comment une méthode déclare son identité (sections 1 à 3), comment elle décide de son applicabilité à un objet donné (section 4), comment elle structure ses définitions opératoires (section 5), comment elle se déroule en procédure (section 6), comment elle s'audite (sections 7 et 8), comment elle produit ses sorties (sections 9, 10 et 11), comment elle s'articule au graphe (section 12), comment elle s'évalue (section 13), comment elle se calibre par cas-jouets (section 14), ce qu'elle reconnaît comme limites (section 15). Une seizième section traite du journal méthodologique propre à la méthode.

Le gabarit hérite de la charte v2 sans la répéter. Il opérationnalise les engagements et les disciplines de la charte par des contraintes vérifiables. Toute friction identifiée dans une méthode qui résiste à une résolution interne remonte au gabarit pour examen, et le cas échéant à la charte.

---

## 1. Métadonnées de la méthode

Toute méthode déclare en tête sept métadonnées obligatoires.

*method_id* — identifiant stable au format `MXX` (M01, M02, etc.). Une fois attribué, l'identifiant n'est jamais réaffecté à une autre méthode même après obsolescence.

*method_name* — nom français de la méthode, court (cinq à dix mots), descriptif de l'objet et de l'opération principale. Exemple : "Analyse rhétorique d'un discours public".

*method_version* — version au format `X.Y` selon la convention semver simplifiée. La majeure incrémente lors d'une refonte qui invalide la rétrocompatibilité des sorties. La mineure incrémente lors d'évolutions internes compatibles.

*charter_version_required* — version de la charte avec laquelle la méthode est compatible. Une méthode dont la `charter_version_required` est obsolète face à la charte courante doit être revue.

*gabarit_version_required* — version du gabarit avec laquelle la méthode est compatible. Idem.

*authors* — liste des auteurs de la version courante de la méthode.

*last_revision_date* — date de la dernière révision substantielle.

---

## 2. Type d'objet et applicabilité par genre

Toute méthode déclare les types d'objets sur lesquels elle peut s'appliquer. Le type d'objet est une catégorie de production textuelle ou documentaire, caractérisée par son genre, son cadre énonciatif, ses conventions.

Les types d'objet canoniques recensés à la date du gabarit v2 : discours politique (déclaration officielle, intervention parlementaire, allocution télévisée, conférence de presse), communiqué institutionnel structuré, éditorial signé, interview substantielle préparée, plaidoyer judiciaire public, communication d'entreprise stratégique sur décision majeure, document doctrinal d'organisation, déclaration de doctrine d'autorité indépendante, allocution cérémonielle institutionnelle.

Une méthode peut couvrir un, plusieurs ou tous ces types. Elle déclare la liste explicite. Tout objet relevant d'un type non listé ne tombe pas dans le périmètre d'applicabilité de la méthode.

Le type d'objet est distinct du contenu thématique. Une méthode d'analyse rhétorique peut couvrir un discours politique portant sur n'importe quel sujet ; elle ne couvre pas un poème publié, qui n'est pas un genre d'objet listé.

---

## 3. Finalité analytique

Toute méthode déclare sa finalité analytique en deux paragraphes. *Qu'est-ce que la méthode cherche à éclairer ?* (objet de connaissance) et *quels usages elle sert et quels usages elle ne sert pas* (périmètre d'utilité).

Cette section interdit l'utilisation détournée de la méthode. Une méthode d'analyse rhétorique de discours publics n'est pas utilisable pour produire un jugement sur la personne du locuteur. Une méthode d'analyse historiographique n'est pas utilisable pour arbitrer entre historiographies sur le fond.

La finalité analytique doit être compatible avec la doctrine de la charte. Elle ne peut pas contredire les quatre engagements de l'ADN ni la discipline épistémique.

---

## 4. Décision d'applicabilité

Toute méthode définit explicitement la procédure de décision d'applicabilité à un objet donné. La décision produit l'un de trois verdicts.

*applicable_complete* — l'objet remplit toutes les conditions, la méthode s'exécute en mode standard. Les degrés de confiance peuvent atteindre 1,0.

*applicable_degraded* — l'objet remplit les conditions minimales mais une ou plusieurs conditions ne sont pas pleinement satisfaites (verbatim partiel, contexte difficilement reconstructible, identification du locuteur incertaine, accès aux sources de comparaison limité). La méthode s'exécute en mode dégradé. Les degrés de confiance des annotations sont plafonnés à 0,85. Le mode dégradé est déclaré dans la fiche d'énonciation et justifié par les conditions qui le motivent.

*not_applicable* — l'objet ne remplit pas les conditions minimales. La méthode ne s'exécute pas. Le motif du rejet est inscrit au journal et l'analyste se voit suggérer la méthode appropriée si une autre méthode du catalogue couvre l'objet.

Le détecteur de surcharge contextuelle est un sous-dispositif de la décision d'applicabilité. Il bascule en mode dégradé quand le texte ou le contexte sature les capacités d'analyse — texte excessivement long (au-delà de quinze mille mots par exemple), contexte politique impliquant trop d'acteurs simultanés (au-delà de dix acteurs principaux dans une séquence courte), accès aux sources secondaires substantiellement réduit.

En l'état du projet (v2), la décision d'applicabilité reste *semi-manuelle* — un analyste humain prend la décision sur la base de critères opérationnels documentés dans la méthode. L'automatisation par un classifieur dédié est inscrite comme objectif v3.

---

## 5. Définitions opératoires

Toute méthode fournit les définitions opératoires des concepts qu'elle mobilise. La définition opératoire d'un concept est sa traduction en critère vérifiable à l'application. Une définition académique ne suffit pas — il faut "ce qui compte comme X dans l'analyse".

Le gabarit v2 impose huit champs de définition obligatoires pour toute méthode.

*Unité d'analyse de la méthode.* Une unité argumentative dans M01, un indice dans M02 si elle est instanciée, etc. Définition opératoire : critères qui permettent de découper un texte en unités sans ambiguïté excessive.

*Statuts épistémiques.* Trois statuts canoniques de la charte (fait établi, inférence, hypothèse), avec les critères opératoires de classification.

*Régime épistémique des attributions mentales.* Quatre opérateurs distincts de la discipline des passages — K (savoir établi factif), B (croyance), Affirme (assertion sans hypothèse sur la croyance), Prétend_savoir (présentation comme certain sans validation indépendante). Critères opératoires pour basculer d'un opérateur à l'autre.

*Gradation des sophismes ou vulnérabilités argumentatives.* Trois niveaux — certain, probable, possible. Définition opératoire du sophisme certain par les trois critères cumulatifs (structure logique formellement défaillante, absence de lecture charitable alternative, démontrabilité sans information externe). Un seul critère manquant rétrograde le défaut en vulnérabilité probable ou possible.

*Gradation des omissions.* Trois niveaux — structurelle (l'élément manquant est nécessaire à la compréhension du dossier ; sa présence est attendue), stratégique probable (l'élément manquant aurait servi l'argumentation mais l'orateur avait vraisemblablement intérêt à l'écarter), intentionnelle non prouvée (l'élément manquant est probable mais l'intention de dissimulation n'est pas démontrée).

*Charge affective du discours.* Trois niveaux — faible (registre principalement informatif ou institutionnel), moyenne (pathos ciblé sur des séquences identifiables), élevée (pathos dominant qui structure l'argumentation). La charge affective est déclarée dans la fiche d'énonciation et conditionne la vigilance sur les vulnérabilités d'analyse liées (sympathie projetée, mimétisme rhétorique).

*Charge éthique du discours.* Trois niveaux — faible (le discours n'engage pas une qualification éthique au-delà du débat politique légitime), moyenne (le discours mobilise des oppositions identitaires ou des positions contestées éthiquement, sans appel à la disqualification ou à la violence), élevée (le discours sollicite la haine de groupes identifiés, appelle à la violence, ou nie des faits historiques constitutifs comme un génocide documenté). La charge éthique est déclarée dans la fiche d'énonciation et conditionne le régime de la reconstruction charitable (cf section 6, étape 5).

*Pondération des historiographies concurrentes.* Quatre niveaux — disqualifiée (au moins deux critères sur trois de la charte 6.3), marginale (position défendue par une minorité identifiable, indicateur opérationnel ≤ 20% de la communauté académique pertinente), contestée (deux écoles ou plus s'affrontent sans dominance claire), consensus fort (hypothèse majoritaire sans contestation substantielle). Toute mention d'historiographie concurrente déclare son niveau.

Toute méthode peut ajouter des définitions opératoires propres à sa spécificité.

---

## 6. Procédure générique en étapes typées

Toute méthode déclare sa procédure en étapes ordonnées et typées. Chaque étape porte un identifiant, une entrée typée, une opération, une sortie typée, et un critère de succès / échec.

Le gabarit v2 ne fixe pas la liste des étapes (chaque méthode a sa procédure propre), mais il fixe sept *contraintes transversales* qui s'appliquent à toutes les méthodes du catalogue.

### 6.1 Charité interprétative non négociable comme étape précoce

Toute méthode portant sur un discours, un argumentaire ou une production textuelle structurée intègre une étape de reconstruction charitable de l'argument du locuteur dans sa meilleure version, *avant* toute étape de détection de défauts. Cette étape n'est pas optionnelle.

### 6.2 Règle opérationnelle pour la charité

La reconstruction charitable obéit à une règle opérationnelle stricte. Tout terme évaluatif emprunté au discours analysé est traité selon l'une de trois modalités. *Marqué entre guillemets* — la reconstruction conserve le terme avec ses guillemets, indiquant qu'il appartient au lexique du locuteur. *Attribué explicitement au locuteur* — "ce que le Premier ministre appelle X" ou équivalent. *Reformulé en lexique descriptif neutre* — substitution du terme évaluatif par une formulation descriptive qui décrit l'opération sans l'évaluer.

La règle interdit l'emploi non marqué des termes évaluatifs du locuteur. La violation de la règle est un défaut d'analyse signalé au journal méthodologique.

### 6.3 Articulation charité et charge éthique

Quand la charge éthique du discours est qualifiée *élevée*, la reconstruction charitable s'applique à la structure argumentative du discours mais *ne neutralise pas la qualification éthique de son objet*. Le bloc résultats nuls de la sortie humaine signale explicitement le contenu éthiquement disqualifiable qui demeure dans la reformulation charitable. La charité reformule l'argument ; elle ne lave pas son objet.

### 6.4 Régime épistémique des attributions mentales

Toute attribution d'état mental ou cognitif à un locuteur dans le cours de l'analyse déclare son régime parmi les quatre opérateurs de la section 5 (K, B, Affirme, Prétend_savoir). L'usage de K (savoir établi factif) requiert que la proposition attribuée soit indépendamment vérifiable par les sources. Si la proposition n'est pas indépendamment établie, K n'est pas disponible — on doit utiliser B, Affirme ou Prétend_savoir selon le cas.

### 6.5 Défaisabilité des règles causales et comportementales

Toute inférence causale ou comportementale invoquée dans une analyse déclare au moins deux conditions de défaite (defeaters). Une condition de défaite est une situation documentable où la règle ne tiendrait pas. Les defeaters sont énumérés dans la sortie machine M01-M et discutés brièvement dans la sortie humaine M01-H lorsqu'ils éclairent significativement l'analyse.

### 6.6 Patterns temporels pour les écarts discours / actes

Toute documentation d'un écart entre un discours qui annonce un acte et la réalité observée typage l'écart par l'un de six patterns canoniques : *non encore observé*, *jamais observé*, *observé plus tard*, *observé autrement*, *observé par un autre acteur*, *empêché par une contrainte*. Le typage est obligatoire ; il distingue six situations que le langage courant amalgame.

### 6.7 Hypothèses concurrentes et zone d'indétermination

Toute synthèse en hypothèses concurrentes inclut au moins trois hypothèses, dont au moins deux non intentionnelles. L'écart de confiance entre l'hypothèse dominante et la deuxième hypothèse est calculé.

Si l'écart est *inférieur ou égal à 0,2*, la synthèse déclare une *zone d'indétermination* — aucune hypothèse n'est qualifiée univoquement de dominante, les hypothèses sont présentées comme co-explicatives.

Si l'écart est *compris entre 0,2 (exclu) et 0,4 (inclu)*, la dominance est qualifiée *incertaine* ; la synthèse formule explicitement les conditions d'arbitrage qui permettraient de trancher.

Si l'écart est *supérieur à 0,4*, la dominance est claire et la synthèse en énonce les conditions de révision.

---

## 7. Contrôles internes

Toute méthode déclare ses contrôles internes — dispositifs vérifiables qui auditent l'exécution de la méthode.

*Anonymisation des agents.* Les instances LLM mobilisées dans l'exécution de la méthode (analyste, contradicteur, auditeur) n'ont pas de persona, pas de nom, pas d'historique. Le system prompt de chaque agent contient les instructions opérationnelles tirées de la spec de méthode et rien d'autre. Pas de "tu es un analyste rigoureux et perspicace" — la consigne est interdite.

*Journalisation systématique.* Chaque appel LLM produit dans le cadre de la méthode est journalisé intégralement — prompt complet, réponse complète, modèle utilisé avec version, paramètres (temperature, max_tokens), latence, coût en tokens. La journalisation est append-only et liée à l'identifiant d'analyse.

*Audit des sources par poste d'observation.* La méthode produit, en sortie machine, la liste des sources convoquées. Un module d'audit régulier (couche d'exécution) vérifie la distribution des sources et signale les asymétries fortes.

*Vérification de la conformité au gabarit.* Une analyse produite n'est validée comme conforme au gabarit que si elle satisfait tous les champs obligatoires définis dans les sections 5 (définitions opératoires), 6 (procédure), 9 (sortie humaine), 10 (sortie publique), 11 (sortie machine). La vérification est automatisable par schéma Pydantic.

---

## 8. Dégradation gracieuse

Toute méthode déclare comment elle se comporte face à des conditions sous-optimales. La dégradation gracieuse a quatre paliers.

*Palier 1 — verbatim partiel.* Le texte source n'est accessible que partiellement (extraits, transcription incomplète). Mode dégradé déclaré, plafonnement de confiance à 0,85, signalement systématique des conditions de révision liées à l'accès au texte intégral.

*Palier 2 — contexte difficile à reconstruire.* Le contexte politique, institutionnel ou social du discours n'est pas pleinement documentable depuis le poste d'observation. Mode dégradé déclaré. L'analyse signale les inférences contextuelles qui auraient pu être plus précises avec un accès élargi.

*Palier 3 — saturation cognitive du LLM.* Le texte excède les capacités de traitement d'un appel LLM unique. Découpage du texte en segments avec analyse séquentielle. Synthèse explicite des segments. Risque de dérive de la discipline méthodologique signalé.

*Palier 4 — rentabilité épistémique insuffisante.* L'analyse ne produit ni fait nouveau, ni inférence solide, ni hypothèse discriminante. La méthode s'arrête, déclare l'insuffisance, et l'inscrit au journal. Une analyse creuse n'est pas livrée comme analyse — c'est une discipline de l'écart.

---

## 9. Sortie humaine M01-H

Toute méthode produit une sortie humaine structurée en huit blocs canoniques. La sortie humaine est destinée à un lecteur informé qui investit le temps d'une analyse complète. Format : Markdown structuré.

*Bloc I — Fiche d'énonciation et décision d'applicabilité.* Locuteur (avec identification du pouvoir d'agir effectif à la date), date, lieu, auditoires (primaire et secondaires), canal, séquence politique ou institutionnelle, genre, contrat de communication implicite, *charge affective codée* (faible / moyenne / élevée), *charge éthique codée* (faible / moyenne / élevée), décision d'applicabilité avec mode (complet / dégradé / non applicable).

*Bloc II — Reconstruction charitable de l'argument principal.* Reformulation de l'argument du discours dans sa meilleure version, dans le respect de la règle opérationnelle (section 6.2). Cette reconstruction est la base de l'analyse en aval — tout défaut identifié est défaut de cette meilleure version.

*Bloc III — Analyse par unités.* Pour chaque unité argumentative identifiée : citation ou paraphrase du segment, types d'actes de langage, présuppositions (avec leur type doxique, idéologique, pragmatique), vulnérabilités argumentatives (avec leur gradation et la lecture charitable alternative quand elle existe), omissions (avec leur gradation), fonction politique inférée (avec son niveau de confiance et l'opérateur épistémique applicable — Affirme, B, K, Prétend_savoir).

*Bloc IV — Lexique, registres et figures.* Termes-clés mobilisés avec glissements sémantiques éventuels, registres empruntés, ethos construit par le locuteur, pathos mobilisé (en cohérence avec la charge affective déclarée), logos structurant, doxa mobilisée.

*Bloc V — Écarts discours / actes documentés.* Chaque écart documenté est typé selon les six patterns temporels de la section 6.6. Pour les écarts en mode "non encore observé", la fenêtre de vérification est explicitée. Pour les écarts en mode "empêché par une contrainte", la contrainte est nommée.

*Bloc VI — Historiographies mobilisées.* Chaque historiographie mobilisée par le discours est nommée. Pour chaque historiographie, son ou ses historiographies concurrentes sont nommées avec leur *niveau de consensus académique* (disqualifiée, marginale, contestée, consensus fort) selon la typologie de la section 5. Pas de fausse symétrie.

*Bloc VII — Synthèse en trois statuts épistémiques.* Faits établis, inférences (avec leur niveau de confiance et leur prémisse), hypothèses concurrentes (au moins trois dont au moins deux non intentionnelles). Calcul de l'écart de confiance entre hypothèse dominante et deuxième hypothèse. Application de la convention 6.7 — zone d'indétermination, dominance incertaine, ou dominance claire selon l'écart. Red team objections à l'hypothèse dominante ou à l'hypothèse co-dominante.

*Bloc VIII — Blocs de neutralisation et conditions de révision.* Quatre sous-blocs obligatoires.

*Résultats nuls* — ce que la méthode a cherché et n'a pas trouvé (sophismes certains, omissions intentionnelles prouvées, écarts documentés au-delà du raisonnable, incohérences factuelles, etc.). Ce sous-bloc est la discipline contre le biais de soupçon.

*Ce que le discours dit correctement* — éléments du discours qui sont exemplairement précis, fondés, ou méthodologiquement irréprochables. Cette discipline empêche la lecture systématiquement défavorable.

*Indices non convergents* — éléments d'analyse qui ne pointent pas nettement dans une direction et qui demandent à être suspendus ou arbitrés par des informations externes.

*Conditions de révision* — circonstances documentables qui modifieraient l'analyse. Les conditions sont énumérées pour rendre l'analyse explicitement révisable.

Pour les discours à *charge éthique élevée*, le bloc VIII inclut un cinquième sous-bloc : *Contenu éthiquement non neutralisé par la charité* — signalement explicite du contenu disqualifiable qui demeure dans la reformulation charitable, en application de la section 6.3.

---

## 10. Sortie publique M01-P

Toute méthode produit une sortie publique structurée en cinq éléments imposés. La sortie publique est destinée au Mode 3 (chat public) et aux usages de lecture rapide. Format : prose continue, *cent cinquante à trois cents mots*.

*Élément 1 — Énonciation.* Une phrase qui dit qui parle, à qui, dans quel cadre, à quelle date.

*Élément 2 — Fait dominant ou inférence principale.* Deux à trois phrases qui énoncent le constat le plus solide produit par l'analyse, avec son régime épistémique explicite (fait établi ou inférence).

*Élément 3 — Hypothèse dominante avec confiance et alternative non intentionnelle principale.* L'hypothèse dominante avec sa confiance, et l'hypothèse alternative non intentionnelle principale avec sa confiance. Si la zone d'indétermination est déclarée en bloc VII (écart ≤ 0,2), la formule "deux hypothèses sont proches en confiance et coexistent comme co-explicatives" est employée plutôt qu'une qualification de dominance.

*Élément 4 — Renvois.* Un lien vers l'analyse complète M01-H et un lien vers la source primaire pour l'auditeur qui veut juger lui-même.

*Élément 5 — Bloc de clôture logique.* Une formule typée qui qualifie la solidité de l'inférence principale (solide / plausible / fragile), énonce la prémisse implicite principale sur laquelle elle repose, et liste deux ou trois conditions de révision documentables.

La règle opérationnelle pour la charité (section 6.2) s'applique également à la sortie publique. Les termes évaluatifs du locuteur sont mis entre guillemets.

La sortie publique est *générée automatiquement* à partir d'une sortie machine M01-M validée, par un appel LLM dédié (modèle plus léger admis, par exemple Sonnet 4.6). La génération est validée par schéma — longueur dans la plage, présence des cinq éléments dans l'ordre, absence de termes évaluatifs du locuteur non marqués.

---

## 11. Sortie machine M01-M

Toute méthode produit une sortie machine structurée en YAML. La sortie machine est destinée à l'ingestion dans le graphe cognitif et à la validation par schéma. Format : YAML conforme au schéma Pydantic de la méthode.

Le gabarit v2 impose les blocs canoniques suivants pour toute sortie machine.

```yaml
method_id: string                    # ex: M01_ANALYSE_RHETORIQUE
method_version: string               # ex: 2.0
analysis_id: string                  # identifiant unique de cette analyse
execution_date: date                 # date d'exécution
execution_mode:                      # selon section 4
  - applicable_complete
  - applicable_degraded
  - not_applicable
execution_mode_reason: string        # si dégradé ou non applicable

source:
  text_id: string
  provenance: string
  integrity_status:                  # selon section 8
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
    effective_agency: string
  date: date
  place: string
  primary_audience: string
  secondary_audiences: list[string]
  channel: string
  political_sequence: string | null
  genre: string
  communication_contract: string
  affective_charge:                  # selon section 5
    - low
    - medium
    - high
  ethical_charge:                    # selon section 5
    - low
    - medium
    - high

charity_reconstruction:
  content: string                    # min 100 caractères, anti-évitement
  borrowed_terms_handled:            # règle 6.2
    - term: string
      handling:
        - quoted
        - attributed
        - reformulated_neutral

units: list[Unit]                    # cf schéma Unit ci-dessous

# (autres blocs spécifiques à la méthode)

epistemic_synthesis:
  established_facts: list[string]
  inferences: list[Inference]
  competing_hypotheses: list[Hypothesis]   # min 3, dont 2 non intentionnelles
  hypothesis_gap: float              # écart confiance dominante - 2e
  hypothesis_status:                 # selon section 6.7
    - zone_of_indetermination
    - uncertain_dominance
    - clear_dominance
  red_team_objections: list[string]

null_results:                        # bloc obligatoire — section 9 bloc VIII
  searched_not_found:
    fallacies: string                # ce qui a été cherché en sophismes et non trouvé
    omissions: string
    discourse_act_gaps: string
  rhetorically_ordinary_elements: list[string]
  non_convergent_indices: list[string]
  what_the_discourse_states_correctly: list[string]
  ethical_content_not_neutralized: string | null   # obligatoire si ethical_charge == high

invisible_and_revision:
  invisible_from_this_post: list[string]
  revision_conditions: list[string]
  next_methods_recommended: list[string]
```

Pour chaque unité argumentative (`Unit`) :

```yaml
Unit:
  unit_id: string                    # ex: U3
  text_span: string                  # citation ou paraphrase
  speech_acts: list[SpeechAct]
  presuppositions: list[Presupposition]
  argumentative_vulnerabilities: list[Vulnerability]
  omissions: list[Omission]
  inferred_function: InferredFunction

Vulnerability:
  type: string
  level:                             # selon section 5
    - certain
    - probable
    - possible
  evidence_span: string
  confidence: float                  # 0.0 à 1.0
  confidence_applies_to:             # contrainte section 6 (distinction confidence/truth)
    - inference
    - hypothesis
    - source_reliability
  charitable_alternative: string | null
  hidden_premises: list[string]      # pour vulnérabilités logiques
  defeaters: list[string]            # contrainte section 6.5, min 2 pour règles causales

Omission:
  missing_element: string
  level:                             # selon section 5
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
  epistemic_regime:                  # contrainte section 6.4
    - knows                          # K — savoir factif
    - believes                       # B — croyance
    - asserts                        # Affirme — assertion sans hypothèse de croyance
    - claims_to_know                 # Prétend_savoir — présenté comme certain
  alternative_functions: list[InferredFunction]

DiscourseActGap:
  unit_id_referenced: string
  pattern_type:                      # contrainte section 6.6
    - not_yet_observed
    - never_observed
    - observed_later
    - observed_otherwise
    - observed_by_other_actor
    - prevented_by_constraint
  observation_window: string         # pertinent si pattern == not_yet_observed
  constraint_named: string | null    # pertinent si pattern == prevented_by_constraint
  source_reference: string

Historiography:
  reference_in_text: string
  mobilized: string
  consensus_level_mobilized:         # contrainte sections 5 + 6 + charte 6.4
    - disqualified
    - marginal
    - contested
    - strong_consensus
  competing: string | null
  consensus_level_competing: string | null
  what_competing_would_say: string | null
```

Le YAML est validé par schéma Pydantic à chaque ingestion. Toute analyse non valide est rejetée et renvoyée à l'agent analyste pour correction.

---

## 12. Articulation au graphe cognitif

Toute méthode déclare ses *exports graphe* — nœuds et arêtes à ingérer dans le graphe à partir de la sortie machine. Le gabarit v2 fixe les types canoniques de nœuds et arêtes accessibles, sans imposer qu'une méthode les mobilise tous.

*Types de nœuds canoniques.* Speaker, SpeechEvent, SpeechAct, Presupposition, Sophism (ou ArgumentativeVulnerability), Omission, HistoriographyReference, Method, Source, Hypothesis, DiscourseActGap.

*Types d'arêtes canoniques.* utters (Speaker → SpeechEvent), contains_act (SpeechEvent → SpeechAct), presupposes (SpeechAct → Presupposition), produces_vulnerability (SpeechAct → Sophism), omits (SpeechEvent → Omission), mobilizes_historiography (SpeechEvent → HistoriographyReference), competes_with (HistoriographyReference → HistoriographyReference), produced_by_method (annotation → Method), cites (annotation → Source), explains (Hypothesis → SpeechEvent ou SpeechAct), reveals_gap (SpeechEvent → DiscourseActGap).

Chaque arête porte au minimum les attributs suivants : `causality_type` (efficient_strong, efficient_weak, correlational, structural), `weight` (0.0 à 1.0), `evidence` (référence textuelle), `confidence` (0.0 à 1.0), `confidence_applies_to` (inference, hypothesis, source_reliability), `method_id` (l'identifiant de la méthode qui a produit l'annotation).

Le graphe est versionné. L'ontologie (types de nœuds et arêtes) évolue selon les besoins, et les évolutions sont tracées dans le journal méthodologique. Toute méthode déclare la version de l'ontologie graphe qu'elle utilise.

---

## 13. Critères d'évaluation

Toute méthode déclare comment elle s'évalue — quels critères distinguent une analyse réussie d'une analyse ratée.

Le gabarit v2 fixe six critères transversaux applicables à toute méthode du catalogue.

*Conformité de format.* La sortie machine valide le schéma. La sortie humaine respecte la structure en huit blocs avec les sous-blocs obligatoires. La sortie publique respecte les cinq éléments imposés.

*Discipline de la gradation.* Sophismes certains rares et justifiés par les trois critères cumulatifs. Omissions intentionnelles non prouvées rares et signalées comme telles. Pas de niveau "certain" sans démonstration soutenable.

*Présence d'un bloc résultats nuls substantiel.* Au moins quatre points distincts dans le bloc résultats nuls. La méthode produit ce qu'elle n'a pas trouvé aussi soigneusement que ce qu'elle a trouvé.

*Présence d'hypothèses non intentionnelles concurrentes.* Au moins deux hypothèses non intentionnelles dans la synthèse, formulées comme alternatives sérieuses, pas comme paille pour relever l'hypothèse intentionnelle.

*Cohérence avec la pondération des historiographies.* Toute historiographie concurrente déclarée est qualifiée selon la typologie en quatre niveaux. Pas de fausse symétrie.

*Conformité à la règle opérationnelle de la charité.* La reconstruction charitable ne contient pas de termes évaluatifs du locuteur non marqués.

Un critère décisif pour les cas-jouets *sans cible* (cas 2 du jeu de tests) : la méthode appliquée à un discours sobre produit zéro sophisme certain et un bloc résultats nuls substantiel. Si la méthode produit des sophismes certains sur un discours sobre, elle a un défaut.

Un critère décisif pour les cas-jouets *adversariaux* (cas 4 du jeu de tests) : la méthode appliquée à un discours conçu pour piéger l'analyse bascule en mode dégradé plutôt que produire un résultat trompeur présenté comme complet.

---

## 14. Cas-jouets normés

Toute méthode dispose d'un jeu de cas-jouets normés pour la calibration. Le gabarit v2 fixe six types de cas-jouets canoniques que toute méthode doit avoir.

*Cas 1 — simple.* Discours avec sophisme certain et omission structurelle évidents. Critère décisif : la méthode identifie les deux sans hésitation.

*Cas 2 — sans cible.* Discours sobre, sans sophisme majeur, sans omission stratégique probable. Critère décisif : la méthode produit zéro sophisme certain et un bloc résultats nuls substantiel.

*Cas 3 — ambigu.* Discours avec une omission qui peut être significative ou non selon le contexte. Critère décisif : la méthode classifie l'omission au bon niveau de gradation et justifie son choix.

*Cas 4 — adversarial.* Discours conçu pour piéger l'analyse, avec surcharge contextuelle, cadrage affectif fort, ironie, polyphonie. Critère décisif : la méthode bascule en mode dégradé plutôt que produire un résultat trompeur.

*Cas 5 — écart réel.* Discours qui annonce un acte et acte effectivement non réalisé dans la fenêtre de vérification close. Critère décisif : la méthode identifie l'écart "jamais observé" et le documente correctement.

*Cas 6 — écart apparent.* Discours qui annonce un acte non réalisé, mais avec une contrainte institutionnelle documentable qui explique la non-réalisation. Critère décisif : la méthode identifie l'écart "empêché par une contrainte" et nomme la contrainte.

Les cas-jouets sont inscrits dans le repo de la méthode comme fixtures de test. Toute modification substantielle de la méthode (passage de version) déclenche un rejeu des six cas-jouets, dont le résultat est inscrit au journal.

---

## 15. Limites du gabarit

Le gabarit v2 ne traite pas explicitement plusieurs questions que les méthodes futures pourraient soulever.

*Méthodes non textuelles.* Le gabarit est conçu pour les méthodes qui analysent des productions textuelles. Une méthode qui analyserait des images, des vidéos, des données quantitatives demanderait des contraintes adaptées. À traiter quand le besoin se présentera.

*Méthodes de synthèse multi-textuelle.* Le gabarit traite l'analyse d'un texte à la fois. Une méthode qui compare systématiquement plusieurs textes ou qui agrège un corpus demanderait des contraintes supplémentaires (cohérence inter-textuelle, gestion des contradictions entre textes). À traiter quand le besoin se présentera.

*Méthodes prédictives.* Le gabarit traite l'analyse rétrospective ou contemporaine. Une méthode prédictive devrait formaliser ses incertitudes et ses conditions de révision différemment. Le projet est plutôt orienté vers l'enquête sur ce qui est, que vers la prédiction de ce qui sera ; mais une méthode contrefactuelle pourrait éventuellement s'inscrire dans le gabarit moyennant adaptations.

*Articulation au mode 2.* Les contraintes spécifiques aux méthodes du mode 2 (conseiller du prince) ne sont pas explicitées dans le gabarit v2. Elles relèvent du distribution restreinte (charte v2 section 8.2) et seront fixées dans une extension dédiée du gabarit.

---

## 16. Journal méthodologique de la méthode

Toute méthode tient un journal méthodologique propre, distinct du journal général du projet. Le journal de la méthode trace les évolutions de la méthode (passages de version, frictions identifiées, corrections intégrées), les exécutions notables (cas-jouets rejoués, rejeux comparatifs), les audits.

Le journal de la méthode est versionné en Git, append-only en pratique, accessible aux analystes en lecture seule et à l'auteur de la méthode en écriture.

Une catégorie d'entrée canonique du journal est *failure_pattern* — recensement des erreurs de raisonnement identifiées au fil des analyses. Six patterns documentés à la date du gabarit v2 : valid_form_with_false_premise, hidden_premise_not_marked, confidence_treated_as_truth, temporal_sequence_treated_as_causality, omission_treated_as_intention, speaker_belief_treated_as_knowledge. Cette mémoire d'échecs est le dispositif d'apprentissage cumulatif de la méthode.

---

*Gabarit v2 — entrée en vigueur immédiate. Toute méthode du catalogue (M01 actuelle, M02 à venir) doit être révisée pour conformité au présent gabarit avant exécution sur de nouvelles analyses. Les analyses déjà produites sous gabarit v1 demeurent valables mais ne bénéficient pas des disciplines v2 sauf rejeu explicite.*
