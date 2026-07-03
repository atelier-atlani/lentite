# L'Entité — Méthode 03 v2 : Analyse comparative multi-acteurs sur même controverse

*Couche C — deuxième instance de méthode dans le catalogue après M01 v2. Implémente le gabarit v2 pour le type d'objet "controverse politique avec multiplicité de discours d'acteurs sur une même séquence". Articule la distinction acteur efficient vs acteur non-efficient. Production caractéristique : matrice des positions épistémiques K/B/Affirme/Prétend_savoir des acteurs sur les propositions structurantes de la controverse.*

---

## 1. Métadonnées

```yaml
method_id: M03_ANALYSE_COMPARATIVE_MULTI_ACTEURS
method_name: "Analyse comparative multi-acteurs sur même controverse"
method_version: 2.0
charter_version_required: 2.0
gabarit_version_required: 2.0
upstream_methods: [M01_ANALYSE_RHETORIQUE]
authors: [équipe projet L'Entité]
last_revision_date: 2026-05-17
```

M03 s'appuie sur les analyses M01 disponibles pour les discours individuels et y ajoute la couche comparative. Une analyse M03 ne peut pas être conduite à partir de discours non analysés au préalable par M01 — elle agrège des sorties M01-M validées.

---

## 2. Type d'objet

M03 couvre les *controverses politiques avec multiplicité de discours d'acteurs sur une même séquence temporelle*. Plus précisément, M03 s'applique quand quatre conditions cumulatives sont réunies. *Première condition* : une controverse identifiable existe (objet politique structuré qui suscite des prises de position publiques contestées). *Deuxième condition* : plusieurs acteurs ont pris position publiquement sur cette controverse dans une séquence temporelle restreinte (typiquement quelques semaines, exceptionnellement quelques mois). *Troisième condition* : les positions sont accessibles dans leurs textes substantiels (discours, déclarations, communiqués) et non seulement dans des paraphrases de presse. *Quatrième condition* : la diversité des acteurs couvre au minimum trois positions politiques distinctes — sinon, l'analyse comparative dégénère en analyse bilatérale qui relève d'autres méthodes.

M03 ne couvre pas l'*analyse d'opinion publique* (qui relève d'enquêtes sociologiques quantitatives), ni l'*analyse de réception médiatique* (méthode candidate M04 — analyse de réception, distincte de M04 candidate triangulation historiographique inscrite dans M01 v2 limites), ni l'*analyse longitudinale d'un acteur sur le temps long* (qui relève d'une méthode M02 candidate de lecture indiciaire élargie).

*Cas-types couverts.* Séquence retraites octobre 2025 (Lecornu DPG + réponses Wauquiez, Chatelain, Chenu, Ciotti, Panot, Peu sur les mêmes propositions). Séquence Conseil constitutionnel 2023-2024 (décisions retraites avril 2023 et immigration janvier 2024 avec positions Conseil constitutionnel, gouvernement, opposition, presse spécialisée). Séquence accords de Bougival Nouvelle-Calédonie 2025 (positions gouvernement, indépendantistes, loyalistes, autorités coutumières). Séquences de débats internationaux où plusieurs États prennent position sur une crise commune dans un délai court.

---

## 3. Finalité analytique

M03 cherche à *rendre visible la structure épistémique* d'une controverse politique en distinguant ce que chaque acteur *sait* (K — savoir factif), *croit* (B — croyance), *affirme* (assertion sans hypothèse de croyance) et *prétend savoir* (présentation comme certain sans validation indépendante) sur les propositions structurantes de la controverse. La méthode rend visibles : (a) les *désaccords factuels* — où deux acteurs ont K(p) et K(¬p), donc l'un au moins se trompe ou prétend savoir indûment ; (b) les *désaccords normatifs* — où plusieurs acteurs partagent K(p) sur le diagnostic mais divergent sur l'action ; (c) les *asymétries d'expertise* — où certains acteurs ont accès à un savoir K que d'autres ne peuvent que croire B ; (d) les *constructions de récit* — où des acteurs sans pouvoir d'agir effectif construisent des cadres interprétatifs qui structurent l'arène dans laquelle les acteurs efficients agissent.

M03 introduit la *distinction explicite entre acteurs efficients et acteurs non-efficients*. Un *acteur efficient* sur une controverse donnée est un acteur dont les décisions sont productrices d'actes effectifs sur la controverse (Premier ministre sur une réforme, président d'institution sur une décision, dirigeant d'organisation syndicale sur un mouvement social). Un *acteur non-efficient* sur la même controverse est un acteur dont le discours est mobilisateur ou positionneur mais ne produit pas d'actes effectifs sur la controverse (opposant parlementaire sans pouvoir gouvernemental, commentateur, philosophe public, dirigeant de groupe minoritaire). La distinction est *relative à la controverse* — un même acteur peut être efficient sur une controverse et non-efficient sur une autre. M03 analyse les deux types d'acteurs mais avec des grilles distinctes.

M03 sert : à l'analyse critique du débat public structuré, à l'évaluation comparée de la qualité épistémique des positions des acteurs, à la cartographie des cadres interprétatifs concurrents, à la mise en évidence des asymétries d'information ou d'expertise. M03 ne sert pas : à arbitrer entre positions politiques en compétition, à prédire l'issue de la controverse, à identifier la "vraie" position du point de vue de l'analyste. La méthode rend visible la structure ; elle ne tranche pas le débat.

---

## 4. Décision d'applicabilité

M03 applique la procédure de décision d'applicabilité du gabarit section 4 avec cinq conditions opérationnelles spécifiques.

*Condition d'identification de la controverse.* La controverse doit être identifiable par : un objet politique structurant (loi, décision institutionnelle, événement public), une séquence temporelle restreinte, des acteurs publiquement identifiables ayant pris position. Si l'objet est diffus ("la situation économique") ou la séquence trop large ("les dix dernières années"), basculement vers méthode plus appropriée ou décomposition en sous-controverses.

*Condition de couverture des acteurs.* Au minimum trois acteurs avec positions distinctes. Idéalement entre quatre et huit acteurs — au-delà, surcharge analytique et perte de la lisibilité comparative. Si plus de huit acteurs sont pertinents, M03 sélectionne les acteurs structurants (selon critères : pouvoir d'agir, audience, originalité de la position, représentativité d'un courant) et signale les exclusions.

*Condition d'accès aux textes substantiels.* Pour chaque acteur retenu, au minimum un texte substantiel (discours, déclaration officielle, communiqué) accessible dans son intégralité ou ses extraits convergents représentant au moins soixante pour cent du contenu. Si seulement des paraphrases médiatiques sont disponibles, basculement en mode dégradé avec plafonnement de confidence.

*Condition de qualification acteur efficient vs non-efficient.* Pour chaque acteur, qualification documentable de son statut sur la controverse spécifique. Le critère opérationnel : l'acteur a-t-il pu ou peut-il directement produire des actes effectifs sur l'objet de la controverse dans la fenêtre temporelle pertinente ? Si oui, *efficient*. Si non, *non-efficient*. Les cas ambigus (acteur efficient sur une dimension de la controverse, non-efficient sur une autre) sont documentés.

*Condition de finalité analytique.* La demande qui motive l'analyse doit être compatible avec la finalité de M03 (section 3). Une demande qui sollicite implicitement un arbitrage politique entre acteurs ou une qualification "qui a raison" est traitée par le module Elenchus qui reformule la demande en termes compatibles avec M03 avant l'exécution.

Le détecteur de surcharge contextuelle bascule M03 en mode dégradé quand plus de huit acteurs sont impliqués ou quand la fenêtre temporelle excède quelques mois sans permettre une analyse séquentielle propre.

---

## 5. Définitions opératoires propres à M03

M03 hérite des huit définitions du gabarit section 5 et des quatre définitions propres à M01 section 5 (unité argumentative, typologie actes de langage, typologie présuppositions, typologie vulnérabilités). Elle y ajoute cinq définitions propres.

### 5.1 Controverse

Définition opératoire : une *controverse* est un ensemble structuré de positions publiques contestées sur un objet politique commun. Une controverse est composée de : (a) un objet structurant (loi, décision, événement, principe), (b) un noyau de propositions sur lesquelles les acteurs prennent position, (c) une séquence temporelle dans laquelle les positions sont produites, (d) un ensemble d'acteurs publiquement identifiables.

Le *noyau de propositions* est explicité par M03 — typiquement entre trois et sept propositions identifiables sur lesquelles les acteurs s'accordent ou se divisent. Sur la séquence retraites octobre 2025, le noyau pourrait être : (P1) "le système de retraite par répartition est en déséquilibre démographique structurel", (P2) "la réforme de 2023 a un déficit de légitimité démocratique", (P3) "la suspension de la réforme est une solution adéquate", (P4) "le 49.3 est un outil de contournement parlementaire à éviter", (P5) "l'élection présidentielle 2027 est l'horizon démocratique légitime pour trancher la réforme".

### 5.2 Acteur efficient et acteur non-efficient

*Acteur efficient sur une controverse* : acteur qui, à la date d'analyse, a le pouvoir documentable de produire des actes effectifs sur l'objet de la controverse. Critères opérationnels : pouvoir institutionnel direct (Premier ministre sur une loi qu'il propose, président d'institution sur une décision qu'il rend, dirigeant d'organisation syndicale sur un mouvement qu'il appelle), pouvoir indirect mais documentable (groupe parlementaire majoritaire ou pivot pour le vote d'une loi), pouvoir reconnu juridiquement (Conseil constitutionnel sur la conformité d'une loi).

*Acteur non-efficient sur une controverse* : acteur dont le discours est mobilisateur, positionneur ou commentateur, mais qui ne peut pas produire d'actes effectifs sur la controverse dans la fenêtre temporelle pertinente. Critères : opposition parlementaire sans majorité (sur une loi qu'elle ne peut pas faire adopter), commentateur public ou intellectuel, dirigeant de groupe minoritaire sans pouvoir de blocage, expert sans mandat exécutif.

*Cas ambigus*. Un acteur peut être efficient sur une dimension de la controverse et non-efficient sur une autre. Exemple : le Parti socialiste sur la séquence retraites octobre 2025 est efficient sur la dimension "votera-t-il la motion de censure ?" (son vote est décisif) et non-efficient sur la dimension "que doit contenir la réforme ?" (il ne dirige pas le gouvernement). M03 documente ces cas et qualifie l'efficience par dimension.

### 5.3 Matrice des positions épistémiques

La *matrice des positions épistémiques* est la production caractéristique de M03. Elle croise les acteurs (en lignes) et les propositions du noyau (en colonnes). Chaque cellule porte le régime épistémique de l'acteur sur la proposition, parmi quatre valeurs : K (savoir factif), B (croyance), Affirme (assertion sans hypothèse), Prétend_savoir (présentation comme certain sans validation).

La matrice est complétée par : (a) une cellule supplémentaire indiquant si l'acteur est efficient ou non-efficient sur la controverse, (b) des annotations pour les positions silencieuses (acteur n'a pas pris position sur la proposition), (c) des annotations pour les positions ambiguës (ne tranche pas entre B et Affirme).

Lecture de la matrice : les *désaccords factuels* apparaissent quand deux acteurs ont K(p) et K(¬p). Les *désaccords normatifs* apparaissent quand les acteurs ont K(p) ou B(p) sur le diagnostic mais divergent sur la prescription. Les *asymétries d'expertise* apparaissent quand certains acteurs ont K et d'autres B sur une même proposition factuelle. Les *prétentions abusives de savoir* apparaissent quand un acteur a Prétend_savoir(p) alors que K(p) ne peut pas être établi indépendamment.

### 5.4 Cadres interprétatifs concurrents

Un *cadre interprétatif* est un système de présuppositions, de catégorisations et de cadrages qui structure la lecture de la controverse par un acteur. Sur une même controverse, plusieurs cadres concurrents peuvent coexister. M03 les identifie, les nomme, et les pondère par leur audience dans le débat public et leur consensus dans la communauté académique pertinente (selon les quatre niveaux du gabarit).

Sur la séquence retraites octobre 2025, les cadres concurrents identifiables sont : *technocratique-actuariel* (le système est une équation à résoudre par paramètres), *social-démocrate* (le système est un acquis social à défendre par négociation), *libéral-individualiste* (le système doit évoluer vers la capitalisation et l'individualisation), *souverainiste-protectionniste* (le système doit privilégier les contributeurs nationaux), *écologiste-décroissant* (le système doit s'articuler à un modèle économique transformé). Ces cinq cadres ne sont pas exhaustifs ; M03 les identifie en fonction des discours analysés.

### 5.5 Structure de l'arène

L'*arène* est la configuration relationnelle des acteurs sur la controverse — qui parle à qui, qui répond à qui, qui ignore qui, qui forme alliance avec qui. M03 cartographie l'arène par un graphe orienté où les nœuds sont les acteurs et les arêtes sont les relations identifiables (réponse à, alliance avec, opposition à, ignore, cite).

L'arène n'est pas la structure politique formelle — elle est la structure relationnelle effective révélée par les discours. Sur la séquence retraites octobre 2025, l'arène fait apparaître : Lecornu adressé à PS et CFDT explicitement, Wauquiez adressé contre LFI et RN simultanément, Ciotti allié explicite avec RN, Chatelain alliée tactique avec PS sur la suspension mais distincte sur le fond, etc. La structure de l'arène est elle-même un objet d'analyse.

---

## 6. Procédure en treize étapes

M03 procède en treize étapes ordonnées. Les étapes 1-4 sont préparatoires (constitution du corpus), les étapes 5-9 sont analytiques (analyse des discours et croisements), les étapes 10-13 sont synthétiques (matrices, cadres, arène, sortie).

### Étape 1 — Identification de la controverse

Délimitation de l'objet, de la séquence temporelle, et identification préliminaire des acteurs. Verdict : la controverse satisfait-elle les conditions d'applicabilité de la section 4 ? Si non, basculement vers autre méthode ou décomposition.

### Étape 2 — Sélection des acteurs

Application des critères de sélection (pouvoir d'agir, audience, originalité, représentativité). Production de la liste des acteurs retenus avec justification de leur inclusion. Liste des acteurs exclus avec justification.

### Étape 3 — Constitution du corpus

Pour chaque acteur retenu, identification du ou des textes substantiels accessibles. Vérification de l'intégrité du verbatim. Décision sur le mode d'exécution (complet, dégradé) pour chaque acteur.

### Étape 4 — Analyse M01 préalable pour chaque acteur

M01 v2 est exécutée individuellement sur chaque texte du corpus. Les sorties M01-M validées sont la matière première de M03. Si M01 n'a pas été conduite, M03 ne peut pas démarrer — l'agrégation comparative présuppose la rigueur sur chaque discours individuel.

Cette étape peut être longue. Sur une controverse à six acteurs, M01 v2 doit être conduite six fois avant que M03 ne commence. C'est un coût d'entrée important mais nécessaire — il garantit que l'analyse comparative n'agrège pas des lectures bâclées.

### Étape 5 — Qualification efficient / non-efficient par acteur

Pour chaque acteur, qualification documentable de son statut sur la controverse spécifique selon les critères de la section 5.2. Les cas ambigus sont documentés (efficience par dimension).

### Étape 6 — Identification du noyau de propositions

Extraction du noyau de propositions structurantes de la controverse (typiquement trois à sept). Les propositions sont formulées dans des termes neutres qui permettent l'attribution sans ambiguïté des positions des acteurs. Le noyau est validé par retour aux textes — chaque acteur doit pouvoir être positionné sur chaque proposition.

### Étape 7 — Attribution des régimes épistémiques par acteur et par proposition

Pour chaque cellule de la matrice (acteur × proposition), application du gabarit section 6.4 sur le régime épistémique. K si la proposition est factuelle et l'acteur affirme la savoir sur la base de sources externes indépendamment vérifiables. B si l'acteur exprime une croyance sans hypothèse de factivité indépendante. Affirme si l'acteur assertien la proposition sans hypothèse sur sa croyance ou son savoir. Prétend_savoir si l'acteur présente la proposition comme certaine sans validation indépendante établissable.

Cette étape est délicate. L'attribution doit être documentée par citation précise. Les cas où l'analyse hésite entre deux régimes (K ou Prétend_savoir notamment) sont signalés comme indices non convergents.

### Étape 8 — Identification des désaccords factuels et normatifs

Croisement systématique de la matrice. Pour chaque paire d'acteurs et chaque proposition : si l'un a K(p) et l'autre K(¬p), désaccord factuel signalé (au moins l'un des deux se trompe ou prétend savoir indûment). Si les deux ont K(p) ou B(p) mais divergent sur la prescription liée à p, désaccord normatif signalé.

### Étape 9 — Identification des asymétries d'expertise et des prétentions abusives

Pour chaque proposition, examen de la distribution K/B/Affirme/Prétend_savoir. Si une asymétrie significative apparaît (un acteur a K, les autres B), signalement et documentation de la source d'expertise. Si un acteur a Prétend_savoir(p) alors qu'aucun acteur ne peut établir K(p) avec sources indépendantes, signalement de la prétention abusive.

### Étape 10 — Identification des cadres interprétatifs concurrents

À partir des sorties M01-M de chaque acteur (notamment les blocs `lexicon_analysis` et `historiographies`), identification des cadres interprétatifs concurrents (section 5.4). Pondération par audience et consensus académique. Identification des cadres qui structurent le discours de chaque acteur (un acteur peut mobiliser plusieurs cadres).

### Étape 11 — Cartographie de la structure de l'arène

À partir des sorties M01-M (notamment les blocs sur l'audience visée, les références aux autres acteurs, les alliances déclarées), construction du graphe relationnel de l'arène (section 5.5).

### Étape 12 — Synthèse comparative et hypothèses concurrentes

Production de la synthèse en trois niveaux. *Faits établis* sur la controverse — propositions sur lesquelles convergent K de plusieurs acteurs avec sources indépendantes établies. *Inférences* sur la structure de la controverse — caractérisation des désaccords (factuels, normatifs, asymétries, prétentions). *Hypothèses concurrentes* sur la dynamique de la controverse — au moins trois hypothèses, dont au moins deux portant sur les acteurs non-efficients (effet de leur discours sur l'arène).

Application de la convention 6.7 du gabarit sur l'écart de confidence des hypothèses.

### Étape 13 — Production des sorties M03

Production de la sortie humaine M03-H (structurée différemment de M01-H pour refléter la dimension comparative), de la sortie machine M03-M (YAML avec schéma propre intégrant la matrice), et de la sortie publique M03-P (en cinq éléments comme M01-P, adaptée à la dimension comparative).

---

## 7. Contrôles internes propres à M03

M03 hérite des contrôles du gabarit section 7 et y ajoute trois contrôles propres.

*Contrôle de couverture du noyau.* Chaque acteur doit pouvoir être positionné sur chaque proposition du noyau. Si un acteur n'a pas pris position sur une proposition, c'est documenté comme position silencieuse — pas comme défaut analytique. Mais si plusieurs acteurs sont silencieux sur une même proposition, c'est signal d'un défaut de couverture (la proposition n'est peut-être pas centrale) ou d'un évitement collectif (la proposition est tabou).

*Contrôle de cohérence matrice / texte source.* Pour chaque attribution de régime épistémique dans la matrice, citation précise du texte source qui la justifie. L'auditeur vérifie par échantillonnage que la citation supporte effectivement l'attribution.

*Contrôle de la distinction efficient / non-efficient.* La qualification doit être documentable et tracée. L'auditeur vérifie que la qualification reflète la situation effective de l'acteur sur la controverse spécifique, pas une qualification générique de son rôle politique.

---

## 8. Dégradation gracieuse

M03 applique les quatre paliers du gabarit section 8 avec adaptations spécifiques.

*Palier 1 — verbatim partiel pour certains acteurs.* Si une partie du corpus est en mode dégradé pour certains acteurs, M03 peut produire une analyse substantielle en signalant pour chaque acteur le mode d'exécution. La matrice porte alors des annotations de confidence variable par cellule.

*Palier 2 — contexte difficile à reconstruire.* L'étape 11 (cartographie de l'arène) est la plus affectée. La structure relationnelle peut être partielle si certaines relations entre acteurs ne sont pas documentables.

*Palier 3 — saturation cognitive sur grande controverse.* Au-delà de huit acteurs, basculement en analyse séquentielle (sous-groupes) avec synthèse de synthèses. Risque de dérive entre sous-groupes signalé.

*Palier 4 — rentabilité épistémique insuffisante.* Si la matrice révèle une convergence quasi-totale des acteurs ou une dispersion sans structure, M03 produit une sortie minimale qui déclare l'insuffisance — la controverse n'a peut-être pas la structure attendue.

---

## 9. Sortie humaine M03-H

M03 produit une sortie humaine structurée en huit blocs, distincte de celle de M01 par sa dimension comparative.

*Bloc I — Fiche de la controverse.* Identification de l'objet, séquence, acteurs retenus, mode d'exécution.

*Bloc II — Acteurs efficients et non-efficients.* Qualification documentable de chaque acteur sur la controverse spécifique, avec justification.

*Bloc III — Noyau de propositions.* Présentation du noyau structurant avec justification de son extraction.

*Bloc IV — Matrice des positions épistémiques.* La matrice elle-même, avec annotations sur les cas ambigus, les positions silencieuses, et les indices non convergents. C'est la pièce centrale de la sortie.

*Bloc V — Désaccords identifiés.* Désaccords factuels (K vs K(¬p)), désaccords normatifs, asymétries d'expertise, prétentions abusives. Chaque désaccord documenté par citations.

*Bloc VI — Cadres interprétatifs concurrents.* Identification, pondération par consensus académique, distribution parmi les acteurs.

*Bloc VII — Structure de l'arène.* Graphe relationnel avec commentaire interprétatif. Distinction entre relations explicites (déclarées) et relations inférées.

*Bloc VIII — Synthèse, hypothèses concurrentes, résultats nuls et conditions de révision.* Faits établis sur la controverse, inférences, hypothèses concurrentes (au moins trois, dont au moins deux sur les acteurs non-efficients). Résultats nuls substantiels — ce que la matrice ne montre pas malgré l'examen systématique. Conditions de révision.

**Cinquième sous-bloc obligatoire si charge éthique élevée pour au moins un acteur.** Comme M01, M03 active le sous-bloc "Contenu éthiquement non neutralisé par la charité" si au moins un acteur du corpus a une charge éthique codée *high*, ou *medium* avec emprunts à cadres idéologiques disqualifiés ou attaques personnelles cumulées (recommandation issue du cas-jouet 4 M01 v2).

*Lisibilité.* La sortie humaine M03-H est conçue pour être lisible par un lecteur humain non-analyste — pas par un auditeur de la conformité v2. Les notes méthodologiques sur les choix d'interprétation, les recommandations pour révision de gabarit, les frictions identifiées ne figurent *pas* dans la M03-H. Elles vont dans le journal méthodologique séparé. Cette discipline corrige le défaut identifié sur M01 v2 cas-jouet 4 Ciotti.

---

## 10. Sortie publique M03-P

M03 produit la sortie publique selon le format en cinq éléments du gabarit section 10, adaptée à la dimension comparative. Plage 200-400 mots (élargie par rapport à M01-P pour refléter la complexité comparative).

*Élément 1 — Énonciation.* Présentation de la controverse, séquence, acteurs retenus.

*Élément 2 — Fait dominant ou inférence principale.* Sur la structure épistémique de la controverse (typiquement : la controverse révèle tel désaccord factuel et tel désaccord normatif).

*Élément 3 — Hypothèses concurrentes.* Au moins deux hypothèses sur la dynamique de la controverse, avec écart de confidence et application de la convention 6.7.

*Élément 4 — Renvois.* Liens vers M03-H et vers les analyses M01 individuelles des acteurs.

*Élément 5 — Bloc de clôture logique.* Qualification de l'inférence principale (solide / plausible / fragile), prémisse implicite, conditions de révision.

---

## 11. Sortie machine M03-M

YAML conforme à un schéma propre intégrant la matrice. Le schéma Pydantic est versionné dans `lentite.schemas.m03_v2`. Différences principales par rapport au schéma M01-M v2 :

```python
class ControversyDescription(BaseModel):
    object: str
    temporal_window: tuple[date, date]
    actors: list[ActorReference]
    selected_actors_count: int
    excluded_actors: list[ExcludedActor]
    
class ActorReference(BaseModel):
    actor_id: str
    name: str
    role: str
    efficiency_status: Literal["efficient", "non_efficient", "ambiguous"]
    efficiency_justification: str
    upstream_m01_analysis_id: str  # référence à l'analyse M01 préalable
    execution_mode_for_this_actor: Literal["complete", "degraded", "vigilance_adversariale"]

class CoreProposition(BaseModel):
    proposition_id: str
    text: str
    justification_for_inclusion: str

class EpistemicMatrixCell(BaseModel):
    actor_id: str
    proposition_id: str
    epistemic_regime: Literal["knows", "believes", "asserts", "claims_to_know", "silent", "ambiguous"]
    evidence_span: str  # citation du texte source
    confidence: float
    confidence_applies_to: Literal["inference"] = "inference"
    note: str | None

class Disagreement(BaseModel):
    type: Literal["factual", "normative", "expertise_asymmetry", "abusive_knowledge_claim"]
    propositions_involved: list[str]
    actors_involved: list[str]
    description: str

class InterpretiveFrame(BaseModel):
    frame_id: str
    name: str
    consensus_level: Literal["disqualified", "marginal", "contested", "strong_consensus"]
    mobilized_by_actors: list[str]
    presuppositions_typical: list[str]

class ArenaEdge(BaseModel):
    source_actor: str
    target_actor: str
    relation: Literal["addresses", "responds_to", "allies_with", "opposes", "ignores", "cites"]
    explicit_or_inferred: Literal["explicit", "inferred"]
    evidence: str
```

Validation supplémentaire : la matrice doit avoir au moins une cellule renseignée par actor × proposition (silent compte comme renseignée). Les désaccords factuels (K vs K(¬p)) génèrent une alerte automatique pour vérification renforcée.

---

## 12. Articulation au graphe cognitif

M03 ajoute au graphe les types de nœuds : Controversy, CoreProposition, EpistemicMatrixCell (typé), InterpretiveFrame, ArenaEdge (typé comme arête entre Speaker).

Arêtes typiques : `has_position_on` (Actor → CoreProposition, attribut epistemic_regime), `mobilizes_frame` (Actor → InterpretiveFrame), `disagrees_with` (Actor → Actor, typé par nature du désaccord), `relates_in_arena_to` (Actor → Actor, typé par relation).

Le graphe permet ensuite des requêtes comparatives : "quels acteurs ont K(p) sur la proposition P3 ?", "quels désaccords factuels persistent au-delà de la controverse étudiée ?", "quels cadres interprétatifs sont mobilisés simultanément par les acteurs efficients et non-efficients ?".

---

## 13. Critères d'évaluation propres à M03

M03 hérite des critères transversaux du gabarit section 13 et des critères propres à M01 section 13. Elle y ajoute quatre critères propres.

*Couverture systématique du noyau.* Chaque acteur retenu doit être positionné sur chaque proposition du noyau (avec valeur `silent` si position non prise). Pas de cellule vide non documentée.

*Traçabilité des attributions.* Chaque attribution de régime épistémique doit être documentée par citation précise. L'auditeur vérifie par échantillonnage.

*Discipline de la distinction efficient / non-efficient.* La qualification doit être documentable et cohérente avec la pratique politique observable, pas avec une catégorisation générique.

*Calibration de la couverture des hypothèses.* Les hypothèses concurrentes doivent couvrir explicitement les acteurs non-efficients — au moins deux des trois hypothèses minimum portent sur l'effet de leur discours sur la dynamique de la controverse. Sans cette discipline, M03 risque de réduire la controverse à la dynamique des seuls acteurs efficients.

---

## 14. Cas-jouets de M03

M03 dispose de quatre cas-jouets canoniques. À la date d'entrée en vigueur de M03 v2, aucun n'est encore instancié sur source réelle.

*Cas A — controverse à acteurs efficients dominants.* Une controverse où deux ou trois acteurs efficients structurent l'arène avec quelques acteurs non-efficients périphériques. *Candidat naturel* : séquence retraites octobre 2025 — Lecornu (efficient PM) + CFDT (efficient sur la mobilisation) + PS (efficient pivot censure) + LFI, RN, UDR, EcoS, GDR (non-efficients sur la séquence immédiate, efficients sur la perspective présidentielle 2027). À produire en première application.

*Cas B — controverse à acteurs non-efficients dominants.* Une controverse où les acteurs structurants sont des opposants, commentateurs ou intellectuels publics, sans acteur efficient direct. *Candidat* : débat public sur une question morale ou philosophique (laïcité, fin de vie, intelligence artificielle) où les acteurs efficients sont peu identifiables ou peu mobilisés. À identifier ultérieurement.

*Cas C — controverse à structure d'arène complexe.* Une controverse où la structure relationnelle est centrale (alliances tactiques, oppositions croisées, ignorements stratégiques). *Candidat* : séquence accords de Bougival Nouvelle-Calédonie 2025-2026 avec gouvernement, indépendantistes, loyalistes, autorités coutumières, opposition parlementaire métropolitaine. À envisager.

*Cas D — controverse internationale.* Une controverse impliquant plusieurs États ou acteurs internationaux. *Candidat* : positions des États européens sur une crise commune dans une fenêtre temporelle restreinte. À envisager.

Toute modification majeure de M03 déclenche un rejeu des cas-jouets instanciés.

---

## 15. Limites de M03

M03 ne traite pas l'*évolution longitudinale* d'une controverse sur le temps long — relève d'une méthode dédiée à instancier ultérieurement.

M03 ne traite pas l'*analyse de réception* — comment les positions des acteurs sont reçues par les auditoires, comment les coalitions de public se forment. Relève d'une méthode dédiée.

M03 ne tranche pas la controverse — elle en rend visible la structure. La qualification "qui a raison" n'est pas dans le périmètre.

M03 ne produit pas d'analyse contrefactuelle — qu'aurait-il pu se passer si tel acteur avait pris telle autre position. Relève de M06 candidate (analyse contrefactuelle).

M03 ne traite pas la dimension non-publique des controverses (négociations privées, arbitrages internes des organisations). Limite imposée par l'accès aux textes publics.

---

## 16. Journal méthodologique de M03

*Inscription au journal du projet à la date d'entrée en vigueur de M03 v2.*

M03 v2 entre en vigueur immédiatement après les trois cas-jouets M01 v2 (Fabius, Lecornu, Ciotti) qui ont validé la discipline v2 sur trois régimes. M03 traite explicitement la friction identifiée par le cas-jouet 4 Ciotti : *la distinction entre discours d'acteur efficient et discours d'acteur non-efficient*. M01 v2 a été calibrée principalement sur des acteurs efficients ; M03 v2 articule les deux types d'acteurs par sa structure même.

Deux corrections incorporées dès M03 v2 par rapport aux frictions M01 v2 :

*Première correction — lisibilité de la sortie humaine.* La M03-H est conçue pour être lisible par un lecteur humain non-analyste. Les notes méthodologiques sur les choix d'interprétation, les recommandations pour révision de gabarit, les frictions identifiées sont *exclues* de la M03-H et inscrites au journal méthodologique séparé. Cette discipline corrige le défaut identifié sur M01 v2 Ciotti (M01-H surchargée de méta-discours méthodologique). Recommandation pour gabarit v3 : étendre cette discipline à toutes les méthodes du catalogue par révision du gabarit section 9.

*Deuxième correction — distinction efficient / non-efficient.* Inscrite comme définition opératoire propre à M03 (section 5.2) avec qualification documentable par acteur et par dimension. Sur les analyses M01 préalables, la fiche d'énonciation gagnerait à porter cette distinction dès M01 — recommandation pour révision M01 v2.1 : ajouter dans la fiche d'énonciation un champ `efficiency_status_on_topic` qualifiant l'acteur sur l'objet du discours.

Frictions identifiées à surveiller v3 :

— Le seuil minimum de trois acteurs avec positions distinctes pourrait être restrictif sur certaines controverses bilatérales structurantes.

— Le noyau de propositions à extraire (entre trois et sept) est sensible à l'analyste. Test inter-analyste à conduire.

— La qualification efficient / non-efficient est relative à la controverse et peut évoluer dans le temps. Sur une fenêtre temporelle longue, l'acteur peut basculer.

— La matrice des positions épistémiques, comme tout outil de visualisation, peut faire écran à la richesse des positions. À ne pas substituer aux lectures M01 individuelles, à articuler avec elles.

*M03 v2 — entrée en vigueur immédiate. Première application prévue : cas A sur la séquence retraites octobre 2025, mobilisant les analyses M01 v2 disponibles (Lecornu complet, Ciotti complet) et les analyses M01 à produire (PS via Boris Vallaud, EcoS via Chatelain, RN via Chenu, GDR via Peu, LFI via Panot si verbatim accessible, CFDT via communiqué officiel).*
