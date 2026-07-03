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

**Licence non exclusive, cession du droit d'exploiter en double licence.** Le contributeur conserve la titularité de son droit d'auteur sur sa contribution. Il concède au Porteur :

1. Une licence irrévocable, mondiale, gratuite, non exclusive d'utiliser, reproduire, modifier, distribuer et sous-licencier sa contribution — y compris sous une licence commerciale distincte de l'AGPL-3.0, pour les besoins du Mode 2 (décision 005, jalon 3).
2. La garantie que la contribution est une œuvre originale du contributeur, ou que celui-ci dispose des droits nécessaires pour la soumettre sous les termes du présent CLA (pas de code tiers incompatible introduit sans déclaration).
3. L'acceptation que la contribution reste, par ailleurs, distribuée sous AGPL-3.0 dans le dépôt public (jalon 2 de la décision 005) — le CLA n'exclusive pas d'AGPL, il s'y ajoute pour permettre la double licence côté Porteur.

**Motif du choix.** Ce mécanisme (licence non exclusive plutôt que cession intégrale du droit d'auteur) est le standard documenté des projets AGPL à double licence commerciale (modèle historique de MongoDB, MySQL, Grafana pré-relicensing) — il préserve la reconnaissance d'auteur du contributeur tout en garantissant au Porteur la liberté d'exploitation commerciale nécessaire au Mode 2.

## 4. Procédure de signature

1. Avant toute première Pull Request sur le périmètre AGPL, le contributeur signe le présent CLA (mécanisme de signature à préciser — CLA-bot GitHub ou signature manuelle archivée, à trancher par le Dirigeant lors de l'onboarding du premier contributeur externe).
2. Le Dirigeant conserve une trace signée (nom, date, périmètre accepté) — archivage recommandé hors du dépôt public (le CLA lui-même est public ; les signatures individuelles ne le sont pas nécessairement).
3. Aucune PR sur le périmètre AGPL n'est mergée sans CLA signé préalable. Vérification manuelle par le Dirigeant tant qu'aucune automatisation n'est en place.

## 5. Limites et statut

Ce texte est un projet de CLA produit par l'Implementer en exécution de la tâche 0.6. **Il n'a pas fait l'objet d'une relecture juridique** et ne doit pas être présenté à un contributeur externe pour signature effective sans cette relecture — en particulier sur la validité du mécanisme de licence non exclusive en droit français (régime du droit d'auteur, distinct du copyright anglo-saxon dont ce type de CLA est historiquement issu), et sur la clarté de la garantie d'originalité (point 3.2) au regard du droit de la contrefaçon.

**Validation requise avant tout usage effectif** — le Dirigeant (Seb) valide ce texte avant merge dans le dépôt, conformément à la note de méta-information de `plan_action_002.md` §5 tâche 0.6.

---

*CLA v0.1 — projet, produit le 3 juillet 2026. Non signé, non validé juridiquement. Voir `.claude/decisions/decision_004_licence.md` §7 et `.claude/decisions/decision_005_modele_distribution.md` §5 (jalon 1).*
