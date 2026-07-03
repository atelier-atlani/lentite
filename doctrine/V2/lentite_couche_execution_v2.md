# L'Entité — Couche d'exécution v2

*Architecture technique réactualisée selon la doctrine v2 (charte v2, gabarit v2, méthode 01 v2), le rapport sur l'intégration de la logique, et les ajouts retenus de la lecture sur les axes inédits. Remplace la couche d'exécution v1.*

---

## 0. Nature et portée

La couche d'exécution traduit la doctrine et les méthodes en infrastructure technique. Les principes directeurs restent ceux de la v1 — séparation LLM / graphe / journal, anonymisation des agents, validation par schéma à chaque interface. La v2 modifie incrémentalement la v1 : ajouts de modules, enrichissements de schéma, distinction des distributions, sans refonte structurelle. Le pipeline en huit étapes est maintenu ; il accueille des modules optionnels supplémentaires.

Les décisions politiques de la restructuration v2 (distribution duale publique/restreinte, report conditionné du Mode 3, premier déploiement Mode 1 limité) sont matérialisées dans cette couche. Les corrections logiques retenues (factivité, défaisabilité, distinction confidence/truth, patterns temporels, module Elenchus, bloc de clôture M01-P) y trouvent leur expression technique.

---

## 1. Principes directeurs (inchangés depuis v1)

*Séparation LLM / graphe / journal.* Le modèle de langage exécute l'analyse, le graphe stocke les nœuds et arêtes typés, le journal trace les décisions méthodologiques. Pas de fusion. Interfaces explicites entre composants, schémas de données stables, journalisation systématique.

*Anonymisation des agents.* Pas de persona dans les system prompts. Instructions opérationnelles uniquement. Identifiants internes aléatoires. Prompts identiques pour tâches identiques.

*Validation par schéma à chaque interface.* Pydantic comme source canonique, JSON Schema dérivé automatiquement. Toute sortie qui ne valide pas est rejetée et corrigée avant transmission au composant suivant.

---

## 2. Architecture en trois couches techniques

**C1 — Couche d'analyse.** Orchestration LLM, application des méthodes, génération des sorties M01-H, M01-M et M01-P, examen logique des requêtes utilisateur (module Elenchus en Mode 3). Stateless par défaut.

**C2 — Couche de persistance.** Stockage durable des textes sources (filesystem hash-adressé), des analyses produites (markdown + YAML versionnés Git), du graphe enrichi (PostgreSQL + Apache AGE), du journal méthodologique (PostgreSQL append-only). Une seule base à administrer.

**C3 — Couche d'interaction.** Trois modalités prévues, dont une seulement nécessaire au MVP : CLI Python pour les analystes (MVP), interface Streamlit pour exploration (v1), API FastAPI + frontend React pour usage public (v2, sous condition de financement Mode 3).

Pas d'interface tant que la chaîne d'analyse n'est pas stable. C2 est construite avec C1.

---

## 3. Stack technique principal

*Langage d'orchestration* : Python 3.11+. Typage statique en mode strict pour C1.

*Validation des schémas* : Pydantic v2. Source canonique de tous les schémas. JSON Schema généré par `model_json_schema()`.

*Modèle de langage* : API Anthropic Claude. Modèle par défaut Claude Opus 4.6 ou 4.7 selon disponibilité. Fallback Sonnet 4.6 pour les tâches non critiques (auditeur, générateur M01-P, générateur argument_graph). Pas de bascule vers autres providers en v2 — la cohérence rhétorique des sorties dépend du modèle.

*Base de données* : PostgreSQL 16 + Apache AGE pour le graphe Cypher-compatible. Une base, deux usages.

*Sérialisation* : YAML pour M01-M, Markdown pour M01-H, prose pour M01-P, DOT pour les graphes d'arguments.

*Versionnage* : Git. Méthodes, charte, gabarit, analyses produites — toutes versionnées. Repo dédié séparé de toute application web qui consommera les résultats.

*Tests* : pytest. Tests unitaires sur les validateurs, tests d'intégration sur le pipeline complet avec cas-jouets comme fixtures.

Pas de framework d'orchestration LLM lourd. Pas de LangChain, pas de LlamaIndex. Code Python explicite, appels API directs, journalisation triviale.

---

## 4. Architecture des agents et anonymisation

Quatre rôles distincts dans la chaîne d'analyse. Chaque rôle est instancié à la demande pour une tâche donnée et oublié après.

**Agent analyste.** Reçoit en entrée : texte source, métadonnées d'énonciation, spec de la méthode (charte v2 + gabarit v2 + instance M01 v2). Produit en sortie : M01-H markdown + M01-M YAML. System prompt sans persona. Modèle : Claude Opus 4.6/4.7.

**Agent contradicteur.** Reçoit en entrée : M01-H et M01-M de l'analyste, plus le texte source. Produit en sortie : red team objections structurées. System prompt mobilisant les objections génériques de section 6 du gabarit (sycophantie, surcharge, charge affective, biais de soupçon, biais de fausse symétrie). Modèle : Claude Opus.

**Agent auditeur.** Reçoit en entrée : tout le résultat (texte, analyse, objections, sortie publique). Produit en sortie : verdict structuré sur la cohérence globale, la conformité au gabarit, l'éventuelle nécessité de relancer l'analyse en mode dégradé. Modèle : Sonnet 4.6 (suffisant pour la tâche de conformité).

**Agent Elenchus.** Reçoit en entrée : la requête utilisateur (en Mode 3, automatique ; en Mode 1, sur demande). Produit en sortie : verdict sur la requête (validée, à reformuler) avec, le cas échéant, une reformulation coopérative. Détecte présuppositions chargées, dichotomies imposées, attributions causales non démontrées, attributions mentales sans validation. Modèle : Sonnet 4.6.

Anonymisation stricte. Pas de retour itératif libre entre agents — une passe d'analyste, une passe de contradicteur, une passe d'auditeur, puis génération M01-P et éventuellement argument_graph. Si l'auditeur signale un défaut majeur, l'orchestrateur peut relancer l'analyste en mode dégradé avec les frictions identifiées, mais pas dans une boucle libre.

Journalisation systématique de chaque appel d'agent : prompt complet utilisé, réponse complète reçue, modèle utilisé avec version, paramètres, latence, coût en tokens. Journal append-only, immutable, lié à l'identifiant d'analyse.

---

## 5. Pipeline d'ingestion détaillé

Le pipeline a huit étapes contrôlées, identiques à la v1 dans leur structure, enrichies des composants v2.

**Étape 1 — Saisie de la source.** Input : URL, fichier texte, ou chaîne brute. Sortie : objet `RawSource` avec champs canoniques. Validation : la source doit être identifiable, sinon rejet motivé.

**Étape 2 — Extraction des métadonnées d'énonciation.** Input : `RawSource`. Sortie : `EnonciationSheet`. Inclut obligatoirement (en plus des champs v1) : `affective_charge` et `ethical_charge` codées en trois niveaux selon gabarit v2 section 5. En v2, manuelle ou supervisée — l'automatisation reste un objectif v3.

**Étape 3 — Décision d'applicabilité.** Input : `RawSource` + `EnonciationSheet`. Sortie : `ApplicabilityDecision` avec mode (`applicable_complete`, `applicable_degraded`, `not_applicable`) et raison. Décision prise par l'analyste après vérification des conditions du gabarit v2 section 4. Le mode dégradé est documenté et plafonne les confidences à 0,85.

**Étape 4 — Sélection de la méthode.** Input : `ApplicabilityDecision` + objectif de l'analyste. Sortie : `MethodSelection` (M01 par défaut en v2). En v2, M01 seule disponible. M03 prévue après stabilisation.

**Étape 5 — Exécution par l'agent analyste.** Input : tout ce qui précède + spec M01 v2 complète. Sortie : M01-H markdown + M01-M YAML. Appel LLM journalisé intégralement. Si l'agent ne produit pas un YAML parsable, retry avec correction explicite. Trois tentatives maximum, sinon escalade en mode dégradé manuel.

**Étape 6 — Validation du YAML M01-M.** Input : M01-M. Sortie : `ValidatedAnalysis` ou `ValidationFailure`. Le validateur Pydantic vérifie conformité au schéma M01-M v2 (cf section 6). Toute analyse non valide est renvoyée à l'agent analyste pour correction ciblée.

**Étape 7 — Passe du contradicteur et de l'auditeur.** Input : `ValidatedAnalysis`. Sorties : `RedTeamObjections` (par contradicteur) + `AuditVerdict` (par auditeur). Journalisées avec prompts utilisés.

**Étape 8 — Génération des sorties dérivées et ingestion.** Input : `ValidatedAnalysis` + objections + verdict. Actions parallèles : (a) génération M01-P par le module dédié `lentite.outputs.public` ; (b) optionnellement, génération argument_graph par le module `lentite.outputs.argument_graph` ; (c) extraction des nœuds et arêtes depuis le bloc `graph_exports` du YAML et insertion dans Apache AGE ; (d) écriture de l'entrée journal avec liens vers les artefacts. Sortie : `IngestedAnalysis` avec identifiants stables.

En Mode 3, l'étape 0 (préalable au pipeline) est l'examen Elenchus de la requête utilisateur — voir section 7 ci-après.

---

## 6. Schéma de validation Pydantic pour M01-M v2

Source canonique : modèles Pydantic v2 dans le module `lentite.schemas.m01_v2`. JSON Schema dérivé automatiquement. Validation à chaque ingestion.

Différences avec le schéma v1, en plus de la structure générale du gabarit v2 section 11 :

```python
# Pseudocode Pydantic v2 — additions et modifications v2

class EnonciationSheet(BaseModel):
    # ... champs v1
    affective_charge: Literal["low", "medium", "high"]
    ethical_charge: Literal["low", "medium", "high"]  # nouveau v2

class CharityReconstruction(BaseModel):
    content: str = Field(min_length=100)
    borrowed_terms_handled: list[BorrowedTerm]  # nouveau v2

class BorrowedTerm(BaseModel):
    term: str
    handling: Literal["quoted", "attributed", "reformulated_neutral"]

class Vulnerability(BaseModel):
    type: str
    level: Literal["certain", "probable", "possible"]
    evidence_span: str
    confidence: float = Field(ge=0.0, le=1.0)
    confidence_applies_to: Literal["inference", "hypothesis", "source_reliability"]  # nouveau v2
    charitable_alternative: str | None
    hidden_premises: list[str] = Field(default_factory=list)  # nouveau v2
    defeaters: list[str] = Field(default_factory=list)  # nouveau v2, min 2 si famille causale/comportementale

class InferredFunction(BaseModel):
    label: str
    confidence: float
    confidence_applies_to: Literal["inference"] = "inference"
    epistemic_regime: Literal["knows", "believes", "asserts", "claims_to_know"]  # nouveau v2
    alternative_functions: list["InferredFunction"] = Field(default_factory=list)

class DiscourseActGap(BaseModel):
    unit_id_referenced: str
    declared: str
    pattern_type: Literal[  # nouveau v2
        "not_yet_observed",
        "never_observed",
        "observed_later",
        "observed_otherwise",
        "observed_by_other_actor",
        "prevented_by_constraint"
    ]
    observation_window: str | None  # pertinent si not_yet_observed
    constraint_named: str | None  # pertinent si prevented_by_constraint
    source_reference: str

class Historiography(BaseModel):
    reference_in_text: str
    mobilized: str
    consensus_level_mobilized: Literal[  # nouveau v2
        "disqualified",
        "marginal",
        "contested",
        "strong_consensus"
    ]
    competing: str | None
    consensus_level_competing: Literal[
        "disqualified", "marginal", "contested", "strong_consensus"
    ] | None
    what_competing_would_say: str | None

class Presupposition(BaseModel):
    type: Literal["doxic", "ideological", "pragmatic"]
    subtype: Literal["modal_shift"] | None = None  # nouveau v2, signale glissement fait→obligation
    content: str
    evidence_span: str
    confidence: float
    confidence_applies_to: Literal["inference"] = "inference"

class NullResults(BaseModel):
    searched_not_found: SearchedNotFound
    rhetorically_ordinary_elements: list[str]
    non_convergent_indices: list[str]
    what_the_discourse_states_correctly: list[str]
    ethical_content_not_neutralized: str | None  # nouveau v2, obligatoire si ethical_charge == high

class EpistemicSynthesis(BaseModel):
    established_facts: list[str]
    inferences: list[Inference]
    competing_hypotheses: list[Hypothesis] = Field(min_length=3)
    # validation : au moins 2 hypothèses non intentionnelles
    hypothesis_gap: float  # nouveau v2 : écart confiance entre dominante et 2e
    hypothesis_status: Literal[  # nouveau v2 : verdict de la convention 6.7 du gabarit
        "zone_of_indetermination",
        "uncertain_dominance",
        "clear_dominance"
    ]
    red_team_objections: list[str]
```

Validation supplémentaire au niveau du M01-M complet : si `ethical_charge == "high"`, alors `null_results.ethical_content_not_neutralized` est obligatoire et non vide.

Validation supplémentaire sur les vulnérabilités de famille causale ou comportementale (familles 2 et 5 de M01 v2) : `defeaters` doit contenir au moins deux entrées.

Le schéma v2 est versionné. Toute évolution majeure produit une nouvelle version (2.1, 3.0) et l'orchestrateur sait quelle version traiter selon le `method_version` déclaré dans l'analyse.

---

## 7. Module Elenchus — examen logique de la requête

Composant `lentite.input.elenchus`. Activé automatiquement en Mode 3 (chat public), à la demande en Mode 1 (analyse interne). Pas activé en Mode 2 par défaut (les utilisateurs Mode 2 sont des partenaires sous contrat qui maîtrisent leurs requêtes).

Input : la requête utilisateur en langue naturelle. Output : un verdict structuré.

```python
class ElenchusVerdict(BaseModel):
    request_id: str
    original_query: str
    presuppositions_detected: list[str]
    hidden_dichotomies: list[str]
    causal_attributions_without_proof: list[str]
    mental_attributions_without_validation: list[str]
    epistemic_status_imposed: str | None
    verdict: Literal["validated", "reformulation_proposed", "out_of_scope"]
    reformulated_query: str | None  # si verdict == reformulation_proposed
    rationale: str
```

Exemples opérationnels.

*Requête utilisateur* : "Pourquoi le gouvernement a-t-il menti sur cette réforme ?"
*Verdict Elenchus* : `reformulation_proposed`. Présupposition détectée : "le gouvernement a menti" — proposition non établie dans le contexte. Reformulation proposée : "Quels écarts peut-on documenter entre les engagements du gouvernement sur cette réforme et les actes observés, et quelles hypothèses explicatives ces écarts permettent-ils de formuler ?"

*Requête utilisateur* : "Analyse rhétorique du discours de Lecornu du 14 octobre 2025."
*Verdict Elenchus* : `validated`. Pas de présupposition chargée. Le pipeline d'analyse engage.

*Requête utilisateur* : "Donne-moi une bonne raison de voter pour la réforme."
*Verdict Elenchus* : `out_of_scope`. La demande est partisane et sollicite une production qui n'est pas dans la finalité analytique de M01.

Le module Elenchus est codé comme appel LLM dédié (Sonnet 4.6 suffisant) avec un system prompt strict tiré de la spec de gabarit v2 sections 5 et 6 (régime épistémique, factivité, défaisabilité).

---

## 8. Module de génération M01-P

Composant `lentite.outputs.public`. Activé à la suite de l'étape 8 du pipeline pour toute analyse validée. Input : `ValidatedAnalysis` (M01-M conforme). Output : `PublicSummary` (M01-P en prose continue, 150-300 mots, cinq éléments imposés).

```python
class PublicSummary(BaseModel):
    analysis_id: str
    enonciation: str  # élément 1
    dominant_fact_or_inference: str  # élément 2
    competing_hypotheses: str  # élément 3
    references: list[str]  # élément 4 : liens M01-H + source
    logical_closure: LogicalClosure  # élément 5

class LogicalClosure(BaseModel):
    main_inference_qualification: Literal["solid", "plausible", "fragile"]
    implicit_premise: str
    revision_conditions: list[str] = Field(min_length=2, max_length=3)
```

Validation : longueur totale entre 150 et 300 mots, présence des cinq éléments dans l'ordre, absence de termes évaluatifs du locuteur non marqués (vérification automatique partielle par comparaison au texte source — heuristique).

Le générateur M01-P utilise un appel LLM dédié (Sonnet 4.6 suffisant) avec system prompt strict qui contraint le format. Coût marginal par analyse : environ 0,1 à 0,2 $ supplémentaires.

---

## 9. Module de génération argument_graph

Composant `lentite.outputs.argument_graph`. Activé automatiquement en Mode 3 (le graphe accompagne la sortie publique), à la demande en Mode 1. Input : `ValidatedAnalysis`. Output : un graphe au format DOT (Graphviz) qui visualise la structure argumentative — prémisses, prémisses cachées, conclusions, vulnérabilités identifiées.

```python
class ArgumentGraph(BaseModel):
    analysis_id: str
    dot_source: str  # code DOT prêt à compiler
    rendered_svg: str | None  # rendu SVG si Graphviz disponible
    description: str  # une phrase qui décrit le graphe pour intégration dans M01-P
```

La génération extrait les éléments suivants du M01-M et les organise visuellement : pour chaque unité argumentative, les actes de langage clés ; les prémisses cachées identifiées ; les présuppositions principales ; les vulnérabilités argumentatives. Les arêtes du graphe représentent les relations argumentatives (supports, contredit, présuppose, défait).

La génération n'effectue pas de calcul de propagation logique (qu'est-ce qui s'effondre si telle prémisse est fausse) — c'est une visualisation, pas un raisonneur formel. La propagation a été écartée au test 3 du rapport sur la logique (risque d'imprécision LLM trop élevé).

Coût marginal : environ 0,1 à 0,3 $ supplémentaires par analyse selon richesse argumentative. Modèle : Sonnet 4.6 suffisant.

En Mode 3, la description courte (`description`) est ajoutée à la M01-P pour donner au lecteur public une indication visuelle. Le SVG est accessible via lien.

---

## 10. Architecture du graphe cognitif

Apache AGE en PostgreSQL. Inchangé en structure depuis v1.

*Types de nœuds canoniques v2.* Speaker, SpeechEvent, SpeechAct, Presupposition (avec sous-type `modal_shift` éventuel), ArgumentativeVulnerability, HiddenPremise (nouveau v2 — issu de la discipline des passages), Defeater (nouveau v2), Omission, HistoriographyReference, Method, Source, Hypothesis, DiscourseActGap.

*Types d'arêtes canoniques v2.* utters, contains_act, presupposes, produces_vulnerability, depends_on_hidden_premise (nouveau v2), defeated_by (nouveau v2), omits, mobilizes_historiography, competes_with (avec attribut `consensus_level` sur l'arête), produced_by_method, cites, explains, reveals_gap.

Attributs obligatoires sur les arêtes : `causality_type` (efficient_strong, efficient_weak, correlational, structural), `weight` (0.0-1.0), `evidence`, `confidence`, `confidence_applies_to` (inference, hypothesis, source_reliability — jamais truth_itself), `method_id`.

Le graphe est versionné. L'ontologie évolue selon les besoins, et les évolutions sont tracées dans le journal méthodologique.

---

## 11. Journal méthodologique

Append-only, PostgreSQL, table `methodological_journal`. Chaque entrée a : identifiant unique, horodatage, type d'entrée, contenu structuré, liens vers artefacts concernés, auteur.

*Types d'entrées v2.*

`method_revision` — modification d'une méthode (passage de version). Pointe vers diffs Git.

`analysis_execution` — exécution d'une analyse complète. Pointe vers artefacts M01-H, M01-M, M01-P, objections, verdict d'audit.

`friction_identified` — friction méthodologique identifiée durant une analyse. Pointe vers passage concerné.

`case_toy_validated` — cas-jouet passé. Pointe vers l'analyse correspondante.

`audit_finding` — résultat d'audit régulier (cf section 12). Pointe vers statistiques produites.

`failure_pattern` (nouveau v2) — recensement des erreurs de raisonnement détectées au fil des analyses. Six patterns documentés à la date du gabarit v2 : valid_form_with_false_premise, hidden_premise_not_marked, confidence_treated_as_truth, temporal_sequence_treated_as_causality, omission_treated_as_intention, speaker_belief_treated_as_knowledge. Cette catégorie est le dispositif d'apprentissage cumulatif du projet.

`charter_revision` (nouveau v2) — modification de la charte. Pointe vers le diff Git de la charte.

`gabarit_revision` (nouveau v2) — modification du gabarit. Pointe vers le diff Git du gabarit.

Le journal est lisible en CLI et exposé via une interface web minimale (Streamlit v1, frontend dédié v2 si déployé) qui expose les méthodes versionnées, les frictions identifiées, les audits agrégés. Cette interface est l'instrument de la transparence épistémique du projet.

---

## 12. Audit régulier

Quatre modules d'audit prévus, exécutables hebdomadairement ou à la demande.

**Module A — Distribution des sources par poste d'observation.** Pour chaque analyse récente, relève des sources convoquées et distribution agrégée (institutionnelles vs presse vs académiques, alignées vs critiques, françaises vs internationales). Signal d'alerte si distribution fortement asymétrique pour un poste donné.

**Module B — Distribution des hypothèses (intentionnelles vs non intentionnelles).** Pour chaque analyse récente, comptage des hypothèses concurrentes et de leur typage. Signal d'alerte si la production penche systématiquement (biais de soupçon ou biais d'angélisme). Le gabarit v2 exige au moins deux hypothèses non intentionnelles par analyse.

**Module C — Distribution des sophismes par genre et locuteur.** Pour chaque analyse récente, comptage des sophismes/vulnérabilités par niveau et par genre de discours, par locuteur. Signal d'alerte si un genre ou un locuteur reçoit systématiquement plus de sophismes certains qu'un autre.

**Module D (nouveau v2) — Distribution du consensus académique sur historiographies mobilisées.** Pour chaque analyse récente, agrégation des qualifications de consensus (fort / contesté / marginal / disqualifié). Signal d'alerte si une catégorie est sur-représentée par rapport à l'attente raisonnable du corpus (par exemple si toutes les historiographies concurrentes mentionnées sur discours politiques contemporains sont qualifiées *marginales*, signal de biais possible de sélection).

Implémentation : requêtes SQL sur tables d'analyses + agrégations Cypher sur le graphe. Sorties humaines lisibles (Streamlit) + sorties machine pour le journal.

Les modules sont activés à partir d'un corpus minimal défini par méthode. Pour M01 v2 : seuil de vingt analyses par poste d'observation pour les modules A, B, C ; seuil de dix analyses pour le module D.

---

## 13. Distribution duale du code

Décision tranchée dans la restructuration v2. Matérialisation technique.

**Distribution publique.** Repo Git ouvert sous licence permissive (Apache 2.0 ou MIT — arbitrage à conduire selon objectifs stratégiques). Contient : charte v2, gabarit v2, M01 v2, schémas Pydantic, modules de pipeline standard (analyste, contradicteur, auditeur, Elenchus, M01-P, argument_graph), persistance PostgreSQL/AGE, journal, CLI minimal, modules d'audit, cas-jouets normés.

Cette distribution permet à quiconque de reproduire les analyses, d'auditer le code, de proposer des contributions.

**Distribution restreinte.** Repo Git privé sous licence à définir, accès par authentification, traçabilité obligatoire. Contient les composants spécifiques au Mode 2 — méthodes spécialisées (à instancier), prompts d'agents adaptés au Mode 2, modules d'inférence sur les rapports de force, orchestration spécifique. Accessible à un nombre restreint de partenaires identifiés sous contrat.

Matérialisation : deux repos Git distincts, avec dépendances claires (la distribution restreinte importe les schémas et le pipeline de base de la distribution publique).

---

## 14. Phasing MVP → v1 → v2

**MVP (1-2 mois, équipe seule).** Pipeline minimal de bout en bout sur le cas Fabius via agent anonymisé. Composants minimaux : `lentite.schemas.m01_v2`, `lentite.agents.analyst`, `lentite.pipeline`, `lentite.storage.postgres`, `lentite.journal`, CLI Python avec quatre commandes (ingest, analyze, audit-light, journal-show), cas-jouets 1, 3, 5 instanciés comme fixtures pytest.

Critère de fin de MVP : pipeline déterministe sur les cas-jouets existants, sorties stables d'une exécution à l'autre, journal complet. Le test décisif est le rejeu Fabius par agent anonymisé comparé à la sortie manuelle — passe ou échoue selon similarité substantielle des sorties.

**v1 (3-6 mois après MVP).** Application au corpus de 20-30 textes politiques contemporains. Validation de robustesse. Instanciation de M03 (analyse comparative multi-acteurs sur même controverse).

Composants ajoutés : `lentite.outputs.public` (génération M01-P), `lentite.outputs.argument_graph`, `lentite.input.elenchus`, modules d'audit A, B, C, D activables, interface Streamlit pour exploration. M03 dans le catalogue. Itération sur le gabarit et M01 selon frictions identifiées.

Critère de fin de v1 : corpus exploitable, audits qui produisent des alertes non triviales, M03 prête.

**v2 (au-delà).** Sous condition de financement Mode 3 (cf restructuration v2 section 4.2). Ouvre à usage externe (chercheurs, journalistes, citoyens informés en Mode 3, partenaires sous contrat en Mode 2 avec distribution restreinte). Composants ajoutés : API FastAPI + frontend React/Next.js, authentification, instanciation de M02 (lecture indiciaire) et M06 (analyse contrefactuelle), plateforme de contribution communautaire sous revue.

Critère de fin de v2 : usage public mesurable.

---

## 15. Catalogue de méthodes — file d'attente

À l'état v2, le catalogue contient une méthode stabilisée (M01) et identifie cinq méthodes candidates avec leur ordre prioritaire.

*M01 — Analyse rhétorique d'un discours public.* Stabilisée en v2. À éprouver par le test décisif (pipeline minimal sur Fabius).

*M03 candidate — Analyse comparative multi-acteurs sur même controverse.* Prioritaire après stabilisation de M01. Production caractéristique : matrice des positions épistémiques (K, B, Affirme, Prétend_savoir) des acteurs sur la controverse. Réutilise les sorties M01 existantes, agrégation par méthode dédiée. Justification de la priorité : proche de M01, exploite l'investissement déjà fait.

*M02 candidate — Lecture indiciaire selon Ginzburg.* Deuxième dans l'ordre. Production caractéristique : repérage et interprétation d'indices marginaux, traces involontaires, lapsus, omissions structurelles signifiantes. Demande une instanciation méthodologique plus complexe que M01 (paradigme indiciaire, lecture des marges). À engager après M03.

*M06 candidate — Analyse contrefactuelle.* Troisième dans l'ordre. Production caractéristique : arbre de scénarios alternatifs (qu'aurait-il pu se passer si X avait choisi différemment) avec defeaters et conditions de bascule. Plus utile pour le Mode 2 que pour le Mode 1. À engager après M02.

*M04 candidate — Triangulation historiographique.* Quatrième dans l'ordre. Production caractéristique : situation d'un événement dans la trajectoire longue, mobilisation de plusieurs historiographies avec leur consensus académique. À engager selon les besoins du corpus.

*M05 candidate — Pondération de causalité efficiente.* Cinquième dans l'ordre. Production caractéristique : qualification de l'intensité, de l'échelle, de la réversibilité d'une causalité documentée. À engager selon les besoins.

L'ordre est révisable selon les frictions identifiées au fil des analyses. Le journal méthodologique trace les arbitrages d'ordre.

---

## 16. Risques et frictions techniques

Inchangés depuis v1 dans leur structure, avec deux ajouts v2.

*Risque coût LLM.* Une analyse M01 v2 (analyste + contradicteur + auditeur + M01-P + argument_graph) sur un discours de 5000 mots consomme environ 50k-80k tokens entrée et 15k-30k tokens sortie. Sur Claude Opus pour analyste/contradicteur et Sonnet pour les autres : coût total estimé 1,5-3 $ par analyse. Pour un corpus v1 de 30 analyses : 45-90 $. Acceptable. Pour usage Mode 3 à échelle : à modéliser quand le financement sera engagé.

*Risque de dérive du modèle sous-jacent.* Anthropic peut modifier le comportement de Claude entre versions. Une analyse rejouée six mois plus tard peut produire des résultats différents. Mitigation : journal enregistre le modèle utilisé avec version exacte ; la reproducibilité est documentaire. Le test décisif (Fabius par agent anonymisé) doit être rejoué périodiquement.

*Risque de sycophantie multi-agent.* Inchangé v1. Agents tous Claude, risque de convergence sur biais similaires. Mitigation v1 : test périodique du contradicteur avec analyses dont les défauts ont été insérés manuellement. Mitigation v2 : triangulation multi-modèle reportée (hors v2 immédiat).

*Risque sur les présuppositions du graphe.* Typologie des nœuds et arêtes (`causality_type`, `epistemic_status`, `epistemic_regime`, `consensus_level`) impose une ontologie qui pré-cadre les analyses. Si la typologie se révèle mal calibrée sur certains genres, le graphe devient menteur. Mitigation : versionner l'ontologie, accepter qu'elle évolue, tracer les évolutions dans le journal.

*Risque sur la décision d'applicabilité (v1).* Étape 3 semi-manuelle. Maintenue en v2. L'automatisation par classifieur dédié est inscrite comme objectif v3.

*Risque nouveau v2 — sur-charge du schéma Pydantic.* Le schéma M01-M v2 est substantiellement plus riche que le v1 (nouveaux champs ethical_charge, defeaters, confidence_applies_to, epistemic_regime, pattern_type, consensus_level, etc.). Risque que l'agent analyste ne remplisse pas tous les champs ou les remplisse incorrectement. Mitigation : validation stricte par Pydantic avec retry, et instruction explicite dans le system prompt sur les champs obligatoires et leurs critères opérationnels.

*Risque nouveau v2 — sur-multiplication des modules.* Avec l'ajout de Elenchus, M01-P, argument_graph, le pipeline mobilise plusieurs appels LLM séquentiels. Augmentation de latence (de quelques secondes à plusieurs dizaines de secondes par analyse) et de coût (par facteur 1,5 environ). Mitigation : parallélisation possible des modules indépendants (M01-P et argument_graph peuvent tourner en parallèle de l'auditeur), modèle Sonnet pour les modules secondaires.

---

## 17. Décisions ouvertes (en attente d'arbitrage)

*Choix de licence open source pour la distribution publique* — Apache 2.0, MIT, AGPLv3, ou autre selon objectifs juridiques et stratégiques.

*Modèle d'accès à la distribution restreinte* — contrat individuel, partenariat institutionnel, club fermé.

*Premier groupe d'utilisateurs Mode 1* — identification, contact, négociation des conditions.

*Trajectoire de financement Mode 3* — sondage des fondations, programmes de recherche, partenaires institutionnels.

Ces décisions relèvent d'arbitrages politiques et stratégiques hors compétence technique du présent document. Elles sont à conduire en parallèle de l'implémentation MVP.

---

## 18. Premiers livrables à coder pour démarrer

Quatre artefacts minimaux pour le MVP, inchangés depuis v1 mais avec schéma v2.

1. `lentite/schemas/m01_v2.py` — modèles Pydantic complets pour M01-M v2, génération JSON Schema validable. Test : les fichiers `lentite_rejeu_v2_lecornu_fabius.md` et le cas Fabius v1 doivent valider après mise en conformité v2.

2. `lentite/agents/analyst.py` — wrapper minimal autour de l'API Anthropic avec injection des instructions de méthode v2 et journalisation systématique. Test : ré-exécuter l'analyse Fabius via agent anonymisé doit produire un YAML structurellement comparable à la sortie produite par Claude conversationnel orchestré, avec écart documenté.

3. `lentite/storage/postgres.py` — connexion PostgreSQL + AGE, schéma SQL initial (tables `texts`, `analyses`, `methodological_journal`), schéma Cypher initial (labels et types d'arêtes v2). Test : ingestion d'une analyse Fabius produit les bons nœuds et arêtes.

4. `lentite/cli.py` — CLI Python avec quatre commandes : `ingest`, `analyze`, `audit-light`, `journal-show`. Test : `lentite analyze --source fabius_voeux_2024.txt --method M01_v2` produit M01-H, M01-M, M01-P, ingestion graphe, et entrée journal.

Avec ces quatre artefacts, le pipeline est démontrable de bout en bout en version v2. Le reste s'ajoute incrémentalement.

Décision finale (inchangée depuis v1) : commencer par les schémas. Tout le reste dépend de la stabilité du contrat M01-M. Si les schémas tiennent, le pipeline se construit. Si les schémas dérivent, le projet patine.

---

*Couche d'exécution v2 — entrée en vigueur immédiate comme document de référence. L'implémentation technique reste à engager. Le test décisif (pipeline minimal sur Fabius via agent anonymisé) demeure la condition de la validation effective de la doctrine v2.*
