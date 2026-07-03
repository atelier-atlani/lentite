# Journal méthodologique de M01

*Journal méthodologique propre à M01, conformément au gabarit v2.1 section 16. Distinct du journal méthodologique général (`journal/lentite_journal.md`, décision 003) — porte les entrées spécifiques à la méthode M01 (évolutions de version, exécutions de cas, patterns d'échec, audits de typologie), pas les décisions structurantes de codage ni les frictions de portée projet.*

*Front matter — même format que le journal général (décision 003, `conventions.md` §6.9) : `date`, `type`, `refs`. Le champ `type` prend ici les quatre catégories canoniques du gabarit v2.1 section 16, propres au journal de méthode — `method_evolution` | `case_execution` | `failure_pattern` | `typology_audit` — et non la taxonomie à cinq types du journal général (`décision`/`révision doctrinale`/`friction`/`audit`/`reprise`/`extension_corpus`), qui ne s'applique pas à ce fichier.*

*Régime append-only physique, comme le journal général.*

---

```yaml
date: 2026-07-04
type: method_evolution
refs: [plan_action_002]
```

### Création du journal méthodologique de M01

*Constat.* Le gabarit v2.1 section 16 et `doctrine/V2.1/lentite_methode_01_v2_1.md` section 16 prescrivent un journal méthodologique propre à M01 (catégories canoniques `method_evolution`, `case_execution`, `failure_pattern`, `typology_audit` — ce dernier ajouté en v2.1). Ce journal n'était pas encore instancié comme fichier séparé — les entrées correspondantes (par exemple le passage v2 → v2.1, les rejeux Ciotti/Fabius/Lecornu) restaient documentées uniquement en prose dans les documents de méthode eux-mêmes (`lentite_methode_01_v2_1.md` §16), pas dans un journal append-only versionné et daté. Ce vide avait été signalé comme point ouvert dans `doctrine/V2.1/lentite_politique_corpus_v1.md` §3 et `lentite_calibration_confiance_v1.md` §1 (tâches 1.3, 1.4 de `plan_action_002.md`).

*Décision d'exécution (arbitrage Architecte, tâche 1.5b de `plan_action_002.md`).* Création de `journal/lentite_journal_m01.md`, initialisé selon la convention de front matter de la décision 003 (`conventions.md` §6.9), avec les quatre catégories de type propres au gabarit v2.1 section 16 plutôt que la taxonomie du journal général.

*Conséquence.* Les entrées `method_evolution`, `case_execution`, `failure_pattern`, `typology_audit` relatives à M01 sont désormais consignées ici. Les entrées antérieures à cette création (passage v2 → v2.1, rejeux Ciotti/Fabius/Lecornu documentés en prose dans `lentite_methode_01_v2_1.md` §16) ne sont pas rétrofittées dans ce fichier — même discipline que l'adoption de la convention de front matter dans le journal général (`conventions.md` §6.9, non rétroactive avant le 3 juillet 2026).

---

```yaml
date: 2026-07-04
type: case_execution
refs: [plan_action_002]
```

### Revalidation intégrale du corpus M01 sous le gabarit durci — constat sur la datation

*Constat.* Les 10 YAML M01 du corpus (7 analyses sur cas réels + 3 cas-jouets) ont été amendés et revalidés sous `gabarit_version=2.1-durci-seq1` (tâche 1.5 de `plan_action_002.md` — bitemporalité minimale de la tâche 1.2 appliquée à `argumentative_vulnerabilities`, `discourse_action_gaps_on_thematic_objects`, `observable_effects_on_targeted_objects`). Sur 57 champs `date_fait` renseignés à travers le corpus, 21 portent une date réelle sourcée (dans le YAML lui-même ou, pour un cas, dans le document d'analyse markdown correspondant — `date_fait` de l'engagement 3 de Vallaud sourcé dans `lentite_analyse_vallaud_v2_1.md`, absent du YAML lui-même), et 36 portent la valeur explicite `non_documente`.

*Lecture.* Ce résultat est une donnée sur la pratique de production du corpus pré-durcissement, pas un défaut de l'amendement — les analyses M01 v2.1 documentaient systématiquement le fait (le gap, l'effet) et sa fenêtre d'observation, rarement un jour calendaire précis pour les faits diffus ou continus (narrations, cohésions maintenues, absences). Les faits ponctuels et médiatisés (votes, décisions de justice, décrets, censures) sont presque toujours datés au jour près ; les faits diffus (perception, cohésion, narration) ne le sont presque jamais. Cette asymétrie mériterait un examen en `typology_audit` si elle se confirme sur un corpus élargi — non traité ici, signalé pour une prochaine séquence.

*Détail par analyse* (dates réelles / total gaps+effets bitemporels) — Barnier 3/11, Bayrou 5/11, Ciotti 1/5, Fabius 1/7, Lecornu 4/6, Panot 3/7, Vallaud 2/8, cas-jouet 1 0/0 (aucune assertion structurée — le sophisme et l'omission testés par ce cas sont capturés en `inferences`/`null_results`, pas en objets `Vulnerability`/`Omission`), cas-jouet 5 1/1, cas-jouet 6 1/1.

*Conséquence.* Aucune action corrective requise dans l'immédiat — `non_documente` est une valeur valide et honnête sous le gabarit durci, pas un échec de validation ni une lacune à combler artificiellement. Candidat pour un futur `typology_audit` sur la distinction faits ponctuels/diffus en matière de datation, une fois un corpus plus large disponible pour confirmer ou infirmer l'asymétrie observée.

---

*Journal méthodologique de M01 v1.0 — créé le 4 juillet 2026, `plan_action_002.md` séquence 1 tâche 1.5b.*
