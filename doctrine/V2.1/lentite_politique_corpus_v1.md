# L'Entité — Politique de corpus v1

*Licence : CC BY 4.0.*

*Document couche B — gabarit v2.1. Version de démarrage (plan_action_002 séquence 1, tâche 1.3). Ne prétend pas à l'exhaustivité — cadre initial appelé à être affiné par l'usage, pas un traité de sourcing.*

---

## 1. Objet

Ce document fixe la typologie des sources mobilisables dans une enquête L'Entité, une qualification de fiabilité déclarée par type, et la règle de traçabilité de toute extension du corpus en cours d'enquête. Il s'articule explicitement avec le champ `cloture_corpus` du bloc omission durci (`pipeline/schemas.py`, tâche 1.1 de `plan_action_002.md`) — voir §4.

## 2. Typologie des sources et fiabilité déclarée

Cinq types, retenus pour leur usage documenté dans les analyses produites à ce jour (Fabius, Ciotti, Lecornu, Vallaud, Panot, Bayrou, Barnier) et dans les cas-jouets de calibration.

### 2.1 Officielle

*Périmètre* — actes, décisions, textes de loi, décisions de justice, communiqués institutionnels, décrets, comptes rendus parlementaires.

*Fiabilité déclarée* — haute sur le fait de l'acte (l'acte a eu lieu, le texte existe, la décision est rendue, la date est certaine) ; variable sur la motivation déclarée de l'acte, qui reste elle-même un objet d'enquête plutôt qu'un fait établi (charte v2.1 — refus de confondre dit/fait/produit/voulu).

*Usage* — source de première instance pour établir des faits établis (bloc VII du gabarit) ; jamais suffisante seule pour clore une attribution causale ou intentionnelle.

### 2.2 Journalistique

*Périmètre* — presse écrite et audiovisuelle identifiée, agences de presse.

*Fiabilité déclarée* — variable, non traitée en bloc : dépend de la ligne éditoriale du média et du respect documenté de pratiques de vérification (recoupement, droit de réponse). Le média est toujours cité nommément dans `source_reference`, jamais anonymisé en « la presse ».

*Usage* — un fait contesté n'est retenu comme établi que sur recoupement d'au moins deux sources journalistiques indépendantes, ou d'une source journalistique et d'une source officielle/statistique.

### 2.3 Statistique

*Périmètre* — instituts publics de statistique, études économiques et sociologiques à comité de lecture, données ouvertes officielles.

*Fiabilité déclarée* — haute sur la mesure elle-même sous réserve de méthodologie publiée et de série continue auditable ; l'interprétation causale d'un chiffre par un tiers n'hérite pas de cette fiabilité — une statistique établit une évolution, pas la cause qu'un locuteur lui attribue (cf. la vulnérabilité testée au cas-jouet 1, attribution causale post hoc ergo propter hoc, `analyses/cas_jouets/lentite_cas_jouets_1_5_6_v2_1.md` §1.3).

*Usage* — support de vérification pour les vulnérabilités de type attribution causale et pour les blocs de chaîne causale amont/aval.

### 2.4 Militante

*Périmètre* — communiqués de partis, syndicats, associations engagées, think tanks partisans identifiés comme tels.

*Fiabilité déclarée* — basse comme source d'un fait contesté indépendant ; haute comme document attestant qu'un acteur affirme, revendique ou dément une position donnée. Une source militante établit ce que l'acteur dit, jamais directement ce qui est vrai.

*Usage* — jamais neutralisée en fait établi sans confirmation indépendante (officielle, journalistique recoupée, ou statistique) ; toujours citée avec son origine et son positionnement explicites.

### 2.5 Académique

*Périmètre* — publications à comité de lecture, ouvrages universitaires, thèses soutenues.

*Fiabilité déclarée* — haute, sous réserve du niveau de consensus dans la communauté pertinente. Pas d'échelle de fiabilité parallèle ici — le gabarit v2.1 dispose déjà d'une typologie de consensus historiographique à quatre niveaux (`ConsensusLevel` — `disqualified`/`marginal`/`contested`/`strong_consensus`, gabarit v2.1 section 5.8, `pipeline/schemas.py`). Une source académique se qualifie par ce niveau, pas par un label de fiabilité générique supplémentaire.

## 3. Règle d'extension tracée

Toute source ajoutée au corpus d'une enquête après la clôture initiale du corpus (`cloture_corpus.date_cloture`, §4) fait l'objet d'une entrée traçable. À ce jour, en l'absence de journal méthodologique de M01 instancié comme fichier séparé (gabarit v2.1 section 16, non encore matérialisé dans le dépôt), l'entrée est consignée dans `journal/lentite_journal.md` selon le format de front matter de la décision 003 (`conventions.md` §6.9).

*Point ouvert signalé.* Aucun des cinq types de front matter actuels (`décision`, `révision doctrinale`, `friction`, `audit`, `reprise`) ne nomme explicitement ce cas. `audit` est retenu par défaut comme le moins inexact (trace de composition du corpus), en attendant une éventuelle extension de la typologie par l'Architecte ou le Dirigeant — pas tranché unilatéralement ici.

Aucune source n'est ajoutée silencieusement une fois le corpus clos — l'ajout non tracé constitue en lui-même un manquement à la discipline de corpus, indépendamment de la qualité de la source ajoutée.

## 4. Articulation avec le bloc omission durci (tâche 1.1)

Le champ `cloture_corpus` du modèle `Omission` (`pipeline/schemas.py`) porte deux informations — `corpus_declare` (déclaration du corpus dans lequel l'absence est constatée) et `date_cloture` (date de clôture de ce corpus). `corpus_declare` référence un ou plusieurs des cinq types du §2 (par exemple : « corpus officiel + journalistique recoupé, clos au 15 mars 2025 »). `date_cloture` est la date-pivot de la règle d'extension du §3 — toute source apparaissant après cette date et mobilisée dans l'analyse relève de l'extension tracée, pas d'un simple complément silencieux au corpus initial.

Cette articulation ne modifie pas `pipeline/schemas.py` (déjà durci en tâche 1.1, qui laisse `corpus_declare` en texte libre) — elle documente l'usage attendu de ce champ.

---

*Politique de corpus v1 — version de démarrage, `plan_action_002.md` séquence 1 tâche 1.3. Non exhaustive par construction — révision attendue à l'usage, notamment sur les cas de sources mixtes (source officielle relayée et commentée par un média, étude académique financée par un acteur partisan) non traités dans cette version.*
