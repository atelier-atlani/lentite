# L'Entité — Contributor License Agreement (CLA)

*Document de gouvernance. Rédigé en exécution de la tâche 0.6 de `plan_action_002.md`, en application de la décision 004 (licence, §7) et de la décision 005 (distribution, jalon 1). Périmètre — contributions sur le code et les documents sous licence AGPL-3.0 (le « moteur », voir `LICENSE` et `LICENSES/`). Validation par le Dirigeant requise avant merge de toute contribution externe ; une relecture juridique reste recommandée avant la première signature effective.*

---

## 1. Objet

La décision 004 retient une tri-partition des licences pour préserver, sur le périmètre moteur (`pipeline/` hors spécification et schémas — orchestration, agents, ingestion, graphe cognitif, synthèse), le droit du porteur principal (Seb, ci-après « le Porteur ») d'opérer une double licence commerciale pour le Mode 2. Ce droit n'est défendable que si le Porteur détient — ou dispose d'une licence suffisante sur — l'intégralité des droits d'auteur du périmètre AGPL. Sans engagement du contributeur, chaque contribution externe fragmenterait la titularité et rendrait la double licence juridiquement incertaine.

Ce CLA est donc une condition bloquante, explicitement posée par la décision 004 §7 : *« avant acceptation de la première PR externe sur le périmètre AGPL, mise en place obligatoire d'un CLA [...] ou d'un DCO avec cession, faute de quoi le droit de double licence Mode 2 est perdu »*. La condition s'applique à tout contributeur, y compris le co-dirigeant pressenti (AXON-1).

## 2. Périmètre couvert

- Le CLA couvre exclusivement les contributions apportées au périmètre sous `LICENSES/AGPL-3.0.txt` — le moteur d'orchestration, `pipeline/agents/`, `pipeline/orchestrateur.py` (à venir), `graph_builder.py` (à venir), et tout module qui en dépend selon la partition par répertoire décrite dans la section Licences du README.
- Le périmètre spécification/schémas (`schemas.py`, `schemas_m03.py`, validateurs, gabarit — Apache 2.0/CC BY 4.0) et le périmètre analyses (CC BY-SA 4.0) ne sont **pas** couverts par ce CLA : ce sont des licences permissives ou à copyleft faible, où la fragmentation de titularité ne menace aucun mécanisme de double licence.

## 3. Mécanisme retenu

**Cession exclusive irrévocable des droits d'exploitation, avec licence de retour non concurrente (modèle CLA fort, type Harmony CA — variante « assignment »).**

### 3.1 Cession et licence de retour

Le contributeur cède au Porteur, à titre exclusif, irrévocable, mondial et pour la durée légale de protection du droit d'auteur, l'intégralité des droits patrimoniaux d'exploitation sur sa contribution — reproduction, représentation, adaptation, traduction, distribution et sous-licence — pour tout mode d'exploitation connu ou inconnu à la date de la cession, y compris l'exploitation sous licence commerciale distincte de l'AGPL-3.0 pour les besoins du Mode 2 (décision 005, jalon 3).

En contrepartie, le Porteur concède au contributeur une licence de retour (« license-back ») mondiale, gratuite, non exclusive et perpétuelle, l'autorisant à utiliser, reproduire et modifier sa propre contribution originale, **à l'exclusion de tout usage concurrent** de l'exploitation du Porteur — notamment la commercialisation, la mise à disposition à des tiers ou l'intégration dans un produit ou service se substituant à celui opéré par le Porteur sous licence commerciale (Mode 2). Cette licence de retour ne restreint pas l'usage de la contribution par le contributeur dans le cadre de la distribution publique sous AGPL-3.0 (voir 3.3).

### 3.2 Garanties du contributeur

Le contributeur garantit :
1. que sa contribution est une œuvre originale, ou qu'il dispose des droits nécessaires pour la soumettre sous les termes du présent CLA (pas de code tiers incompatible introduit sans déclaration) ;
2. qu'aucun employeur, donneur d'ordre, ou tiers au titre d'un contrat de travail, de prestation ou de commande, ne détient de droit sur la contribution qui ferait obstacle à la cession prévue au 3.1 — ou, à défaut, que l'accord exprès de ce tiers a été obtenu préalablement à la contribution et peut être produit sur demande du Porteur.

### 3.3 Maintien de la distribution AGPL

La cession prévue au 3.1 n'exclut pas la distribution de la contribution sous AGPL-3.0 dans le dépôt public (jalon 2 de la décision 005) : elle s'y ajoute, précisément pour permettre au Porteur d'opérer une double licence sans dépendre du consentement individuel de chaque contributeur à chaque nouvel usage commercial.

### 3.4 Cessibilité du bénéfice du CLA

Le bénéfice du présent CLA — y compris la cession prévue au 3.1 — est cessible par le Porteur à toute structure (société, association, ou autre entité juridique) qu'il contrôle directement ou indirectement, sans qu'un accord supplémentaire du contributeur soit requis. Le contributeur en est informé a posteriori si une telle cession intervient.

### 3.5 Droits moraux

Conformément au droit d'auteur français, les droits moraux (paternité, respect de l'intégrité de l'œuvre, droit de divulgation, droit de retrait) sont incessibles et demeurent la propriété du contributeur, y compris après la cession des droits patrimoniaux prévue au 3.1. Le contributeur s'engage toutefois à ne pas exercer ces droits d'une manière qui ferait obstacle à l'exploitation convenue par le présent CLA — notamment il ne s'opposera pas aux modifications, adaptations ou intégrations de sa contribution réalisées par le Porteur dans le cadre normal du projet, ni à la coexistence de la distribution AGPL-3.0 et de l'exploitation commerciale Mode 2 prévues au présent CLA.

**Motif du choix.** Ce mécanisme (cession exclusive avec licence de retour non concurrente, plutôt qu'une licence non exclusive simple) correspond à la variante forte des modèles de CLA de type Harmony (Harmony Contributor Agreements — Harmony CA), qui propose alternativement une cession avec licence de retour et une licence non exclusive seule. La variante forte a été retenue ici pour asseoir plus solidement la titularité exclusive du Porteur sur le périmètre moteur, condition posée par la décision 004 §7 pour la viabilité juridique de la double licence Mode 2 — au prix d'un engagement contributeur plus exigeant que le modèle initial (v0.1), compensé par la licence de retour non concurrente qui préserve l'usage personnel et non commercial de la contribution par son auteur, et par le maintien des droits moraux (3.5).

## 4. Procédure de signature

1. Avant toute première Pull Request sur le périmètre AGPL, le contributeur signe le présent CLA (mécanisme de signature à préciser — CLA-bot GitHub ou signature manuelle archivée, à trancher par le Dirigeant lors de l'onboarding du premier contributeur externe).
2. Le Dirigeant conserve une trace signée (nom, date, périmètre accepté) — archivage recommandé hors du dépôt public (le CLA lui-même est public ; les signatures individuelles ne le sont pas nécessairement).
3. Aucune PR sur le périmètre AGPL n'est mergée sans CLA signé préalable. Vérification manuelle par le Dirigeant tant qu'aucune automatisation n'est en place.

## 5. Limites et statut

Ce texte est un projet de CLA produit par l'Implementer en exécution de la tâche 0.6. **Il n'a pas fait l'objet d'une relecture juridique** et ne doit pas être présenté à un contributeur externe pour signature effective sans cette relecture — en particulier sur la validité du mécanisme de cession exclusive avec license-back en droit français — en particulier le formalisme de l'article L.131-3 CPI (mentions d'étendue, destination, lieu, durée) (régime du droit d'auteur, distinct du copyright anglo-saxon dont ce type de CLA est historiquement issu), et sur la clarté de la garantie d'originalité (point 3.2) au regard du droit de la contrefaçon.

**Validation requise avant tout usage effectif** — le Dirigeant (Seb) valide ce texte avant merge dans le dépôt, conformément à la note de méta-information de `plan_action_002.md` §5 tâche 0.6.

---

*CLA v0.2.1 — projet, amendé le 5 juillet 2026 (v0.2 du même jour : mécanisme de licence non exclusive de v0.1 remplacé au §3 par une cession exclusive avec licence de retour non concurrente ; ajout des clauses de cessibilité du bénéfice du CLA, de droits moraux, et de garantie d'absence de droits d'employeur/donneur d'ordre. v0.2.1 : correctif ciblé au §5, référence au mécanisme mise à jour pour citer la cession exclusive et le formalisme de l'article L.131-3 CPI). Non signé, non validé juridiquement. Voir `.claude/decisions/decision_004_licence.md` §7 et `.claude/decisions/decision_005_modele_distribution.md` §5 (jalon 1).*
