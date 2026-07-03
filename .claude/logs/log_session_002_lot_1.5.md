# Log de session — plan_action_002, lot {1.5} (dernier lot de la séquence 1)

*Mode opérationnel : Implementer. Plan référencé : `.claude/plans/plan_action_002.md` §4 séquence 1.*

---

## Tâches accomplies

**1.5 — Revalidation intégrale.** Les 12 YAML du corpus (7 analyses M01 réelles, 3 cas-jouets, 2 M03) sont passés en revue individuellement.

- **10 YAML M01** amendés individuellement, un commit par fichier — `gabarit_version: "2.1-durci-seq1"` ajouté à la racine ; `date_fait`/`date_connaissance` ajoutés sur chaque `Vulnerability`/`DiscourseActGap`/`ObservableEffect` existant (aucun `Omission` peuplé dans le corpus — le bloc 1.1 n'a donc aucun objet dans ce lot). Sourcing strict — dates extraites du texte déjà présent dans le YAML (`observation`/`description`/`declared`) ou, à défaut, du document d'analyse markdown correspondant (`analyses/m01/*.md`, `analyses/cas_jouets/*.md`). Un cas de sourcing croisé documenté explicitement — l'engagement 3 de Vallaud (49.3 rompu) n'a pas de jour précis dans le YAML mais en a un dans `lentite_analyse_vallaud_v2_1.md` ligne 141 (« renié le 19 janvier 2026 »), utilisé et cité en commentaire dans le YAML amendé. Sur 57 champs `date_fait` : 21 dates réelles, 36 `non_documente` — voir détail et lecture dans `journal/lentite_journal_m01.md`.
- **2 YAML M03** revalidés sans amendement — `schemas_m03.py` n'a reçu aucune contrainte nouvelle en 1.1/1.2 (question ouverte déjà signalée au lot {1.1–1.2}), donc rien à amender ; validation confirmée telle quelle.
- **Extension de schéma nécessaire non anticipée** — sentinelle `NON_DOCUMENTE` (`"non_documente"`) ajoutée à `pipeline/schemas.py`, distincte de `NON_RENSEIGNE` (`"non_renseigne"`). Le validateur conditionnel de la tâche 1.2 ne rejette que `non_renseigne` (défaut schéma, analyse non adressée) — `non_documente` (recherché, absent des sources) satisfait la contrainte durcie. Décision motivée par l'instruction explicite du Dirigeant sur ce lot, pas une improvisation.

**Arbitrages Architecte intégrés.**

- **(a)** Type `extension_corpus` ajouté à `conventions.md` §6.9 — résout le point ouvert signalé dans `lentite_politique_corpus_v1.md` §3 (tâche 1.3) sur l'absence de type de front matter pour une source ajoutée en cours d'enquête.
- **(b)** `journal/lentite_journal_m01.md` créé, initialisé selon la convention de front matter (décision 003), avec les quatre catégories propres au gabarit v2.1 §16 (`method_evolution`/`case_execution`/`failure_pattern`/`typology_audit`) plutôt que la taxonomie du journal général. Première entrée actant la création elle-même ; deuxième entrée documentant le constat de datation de la revalidation (21/57 réel, 36/57 `non_documente`).

**Clôture de séquence.** Suite de tests complète vérifiée verte — 12/12 YAML positifs, 5/5 tests négatifs (3 préexistants + 2 du lot {1.1–1.2}). Entrée de clôture de séquence 1 écrite dans `journal/lentite_journal.md`, citant les frictions ouvertes désignées par le Dirigeant (bande faible, terminologie établi) et deux frictions supplémentaires identifiées pendant ce lot (M03 non durci, asymétrie de datation), plus le rappel que l'écart au §9 (séquence 0 non close) reste indépendant et non résolu par cette clôture.

## Frictions et choix d'implémentation signalés

1. **Sentinelle `non_documente` — extension de schéma non prévue par les tâches 1.1/1.2.** Ajoutée sur instruction explicite du Dirigeant pour ce lot. Cohérente avec la discipline conditionnelle déjà en place (seul `non_renseigne` fait échouer la validation durcie) — aucune régression sur les tests existants.
2. **Convention de `date_connaissance` uniforme = `execution_date`.** Pour les 10 YAML M01, `date_connaissance` est réglé à la date d'exécution de l'analyse (déjà présente dans chaque document, jamais inventée) plutôt que recherchée entrée par entrée — convention documentée ici, pas testée entrée par entrée faute de granularité disponible dans les sources.
3. **Sourcing croisé limité à un cas (Vallaud).** Un seul cas de consultation du document markdown correspondant a été nécessaire pour obtenir un jour précis absent du YAML ; les autres `non_documente` ont été vérifiés par grep ciblé dans le markdown correspondant sans succès (pas juste supposés faute de recherche) — voir les recherches menées sur Barnier, Bayrou, Fabius, Panot, Lecornu, Ciotti pendant la session.
4. **cas_jouet_1 sans assertion structurée.** Le sophisme et l'omission testés par ce cas-jouet ne sont pas encodés en objets `Vulnerability`/`Omission` dans le YAML pipeline (seulement en `inferences`/`null_results`) — l'amendement s'est donc limité à `gabarit_version`, sans que cela indique un défaut de l'amendement lui-même. Signalé, pas corrigé (correction éventuelle de la structuration du cas-jouet 1 hors périmètre de ce lot).

## État des tests

12/12 YAML positifs valident sous `gabarit_version=2.1-durci-seq1` (10 M01) ou sans changement (2 M03). 5/5 tests négatifs rejetés (3 préexistants + `negatif_omission_sans_cloture_corpus` + `negatif_bitemporalite_manquante_gabarit_durci`). Suite complète verte, vérifiée par script Python direct (`M01Analysis.model_validate`/`M03Analysis.model_validate`) — pas de CLI `validate.py` M01 (restauration prévue tâche 2.1).

## Modifications de code / documents

- `pipeline/schemas.py` — ajout `NON_DOCUMENTE`, extension du type `BitemporalDate`.
- 10 YAML `pipeline/analyses/*.yaml` (M01 + cas-jouets) amendés individuellement, un commit chacun.
- 2 YAML M03 vérifiés, non modifiés.
- `.claude/context/conventions.md` §6.9 — ajout du type `extension_corpus`.
- `journal/lentite_journal_m01.md` — nouveau fichier.
- `journal/lentite_journal.md` — entrée de clôture de séquence 1.

## État du système

**Séquence 1 close.** Séquence 2 (prototype pipeline) peut commencer. L'écart au §9 signalé aux lots précédents (séquence 0 non formellement close, re-test d'onboarding par un tiers indépendant toujours dû) reste ouvert, indépendamment de la clôture de la séquence 1 — non traité dans ce lot, pas de mandat pour le faire ici.

## Recommandations pour la suite

- Avant ou pendant la séquence 2 : statuer sur le re-test d'onboarding à froid par un tiers réellement indépendant (clôture formelle de la séquence 0, écart §9).
- Séquence 2, tâche 2.1 (`validate.py` M01) : premier point où un harnais de test automatisé pourrait raisonnablement couvrir les 5 tests négatifs + 12 YAML positifs en CLI plutôt qu'en script Python ad hoc.
- Décision à prendre (Architecte/Dirigeant, pas tranchée par l'Implementer) : étendre `gabarit_version` + bitemporalité à `schemas_m03.py`, ou acter formellement que M03 reste hors périmètre du durcissement séquence 1.
- Le constat de `journal/lentite_journal_m01.md` (asymétrie datation ponctuel/diffus) est candidat à un `typology_audit` — pas urgent, à accumuler avec de futures analyses.

---

*Commits de ce lot : voir historique git, préfixes `feat(schemas)` / `feat(analyses)` / `docs(conventions)` / `docs(journal)` / `docs(logs)`.*
