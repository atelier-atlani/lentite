# L'Entité — État du projet à mai 2026

*Document de cache contextuel pour pré-chargement en début de session par toutes les instances IA. Vue compacte et factuelle de l'état courant. Mise à jour à chaque évolution majeure. Pour navigation détaillée — `README.md` à la racine du projet et `journal/journal.md`.*

---

## Date de référence

**17 mai 2026.** État stable, consolidation doctrinale jugée substantielle, verrou stratégique = décisions structurantes Phase 0 du codage.

---

## Volets opérationnels

| Volet | État |
|---|---|
| Couche A (charte) | v2.1 canonique |
| Couche B (gabarit) | v2.1 + révision mineure v2.1.1 |
| Couche C (méthodes) | M01 v2.1 + M03 v2.1 |
| Cas-jouets canoniques | 6/6 instanciés |
| Analyses M01 sur cas réels | 7 produites |
| Applications M03 sur cas réels | 2 produites |
| Pipeline opérationnel minimal | 10 YAML M01 + 2 YAML M03 validés |
| Tests négatifs pipeline | 3/3 confirment que les contraintes mordent |
| Critique externe formalisée | 1 examinée (Gemini), partiellement intégrée (v2.1.1) |
| Méthodologie de codage | v1 produite, Phase 0 en attente de décisions |
| Méthodologie workflow IA | v1 produite, en cours de mise en place |

---

## Analyses M01 produites

| Analyse | Locuteur | Régime | Pattern V.3 saillant |
|---|---|---|---|
| Fabius | Président Conseil constitutionnel | sobre | `observed_as_announced` × 2 |
| Ciotti | Président groupe UDR | adversarial | V.3 vide motivé |
| Lecornu | Premier ministre (oct 2025) | substantiel | `broken_explicitly` + motivation |
| Vallaud | Président groupe Socialistes | pivot | `observed_otherwise` × 3 |
| Panot | Présidente groupe LFI | adversarial | `never_observed` + `not_yet_observed` |
| Bayrou | Premier ministre (janv 2025) | substantiel | 3 patterns différents |
| Barnier | Premier ministre (oct 2024) | substantiel — censuré | 4 patterns différents (couverture la plus large) |

## Applications M03 produites

| Application | Acteurs | Cas saillants | Statut |
|---|---|---|---|
| Séquence retraites octobre 2025 | Lecornu / Ciotti / Vallaud / Panot | 7 cas saillants | référence sur retraites |
| Séquence Bayrou-Barnier-Lecornu | Barnier / Bayrou / Lecornu | 7 cas saillants | référence sur gouvernement minoritaire |

---

## Documents canoniques

— *Doctrine v2.1.1* — `doctrine/v2.1/` (charte, gabarit + révision mineure, M01, M03).
— *README projet* — `README.md` à la racine.
— *Journal méthodologique général* — `journal/journal.md` (v1.3 à mai 2026).
— *Méthodologie de codage* — `dev/methodologie_codage_v1.md`.
— *Méthodologie workflow collaboratif IA* — `dev/methodologie_workflow_collaboratif_ia_v1.md`.
— *Pipeline opérationnel* — `pipeline/` (schemas Pydantic + validateurs CLI + analyses YAML).

---

## Verrou stratégique actuel — Phase 0 du codage

*Conditions doctrinales satisfaites.* Consolidation jugée substantielle. Les critères 1, 2, 3, 5 de la méthodologie de codage sont satisfaits.

*Verrou unique restant.* Prise des **cinq décisions structurantes** documentées dans `dev/methodologie_codage_v1.md` section 8 — orchestration multi-agents, persistance graphe, persistance journal, licence, modèle de distribution.

*Première mise en œuvre du workflow `.claude/`.* En cours. La Phase 0 du codage sert simultanément à prendre les décisions et à éprouver la méthode de travail collaboratif IA sur un premier cycle réel.

---

## Audits en cours d'accumulation

| Audit | Statut | Données accumulées |
|---|---|---|
| `typology_audit` | deuxième audit ouvert sur deux candidats | `amplification_temporaire_terminee_par_chute` (1 cas — Bayrou) + `never_observed_by_actor_removal` (1 cas — Barnier) |
| `intentionality_bias_audit` | en accumulation | 7/10 analyses M01 cas réels — premier audit possible après 3 analyses supplémentaires |
| `hypothesis_gap_audit` | en accumulation | 10/20-30 analyses M01 + 2 applications M03 — premier audit possible après 10-20 analyses supplémentaires |

---

## Décisions politiques pendantes

— Licence open source (Apache 2.0 recommandé en méthodologie de codage).
— Modèle de distribution (distribution duale recommandée).
— Premier groupe Mode 1 (analystes).
— Trajectoire de financement Mode 3.
— Cinq décisions structurantes Phase 0 codage (voir verrou stratégique ci-dessus).

---

## Patterns d'évolution récents (avril-mai 2026)

— Transition v2 → v2.1 (refonte par stratification — efficience stratifiée, chaînes causales formelles, séparation H/M/P).
— Révision mineure v2.1 → v2.1.1 (deux audits ajoutés au journal).
— Accumulation analytique substantielle — 7 cas réels + 2 applications M03 en quelques semaines.
— Production de la méthodologie de codage v1.
— Critique externe par LLM tiers examinée méthodiquement, partiellement intégrée.
— Production de la méthodologie de workflow collaboratif IA (en cours).
— Mise en place de l'infrastructure `.claude/` (en cours).

---

## Prochaines étapes immédiates

1. *Finaliser la mise en place du workflow* `.claude/` (étapes 2 à 4 en cours).
2. *Premier cycle Mode Architecte → Implementer → Reviewer* sur la Phase 0 du codage.
3. *Prise des cinq décisions structurantes* par Seb.
4. *Production du prototype technique minimal* (Phase 0 du codage).
5. *Engagement de la Phase 1* (pipeline monolithique texte → analyse M01-M).

---

## Contraintes pratiques

— Porteur principal — Seb (CEO Studio ee, professeur Itecom/ComArt).
— Outils utilisés — Claude.ai pour Architecte/Reviewer, Claude Code dans VS Code pour Implementer/Maintainer, Cowork pour accès local au workspace `atlani-ia/`.
— Coût API à maîtriser — modèle par défaut Sonnet 4.6 pour Implementer/Maintainer, Opus 4.7 réservé à Architecte/Reviewer et tâches complexes.
— Environnement — macOS, Python 3.11+, Pydantic 2.13+, environnement local (pas de serveur déployé à ce stade).

---

*État du projet v1.0 — créé le 17 mai 2026. À mettre à jour à chaque évolution majeure (au moins mensuellement en phase active).*

— Documents candidats v2.2 (fondation épistémologique, backlog doctrinal pipeline) — `dev/candidats_v2_2/`, hors canon, sous moratoire jusqu'à clôture du dossier zéro (`plan_action_003` E.4). Voir `journal/lentite_journal.md`, entrée du 12 juillet 2026, pour la matière retenue (items backlog, refus motivés, notes de vigilance, graphe abductif Phase 3).