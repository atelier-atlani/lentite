# Log de session — plan_action_002, lot {2.9} (correctif final Phase 0)

*Mode opérationnel : Implementer. Lot prescrit en Mode Reviewer, en complément de `.claude/reviews/revue_002.md` §4, sur le seul point resté ouvert à la clôture du lot {2.8} : l'échec de contenu ordinaire (bitemporalité incomplète produite par l'agent Vulnérabilités).*

---

## Tâches accomplies

**1. Schémas de sortie agent — champs bitemporels requis.** `pipeline/agent_schemas.py` ajoute quatre nouveaux modèles par sous-classement des modèles normatifs de `schemas.py` — `VulnerabilityOutput`, `OmissionOutput`, `DiscourseActGapOutput`, `ObservableEffectOutput` — qui redéfinissent uniquement `date_fait`/`date_connaissance` en champs requis, de type `date | "non_documente"` (la sentinelle `non_renseigne`, défaut silencieux du schéma de validation finale, est retirée du schéma de sortie agent). Le schéma de validation finale (`schemas.py`) reste inchangé — cette contrainte ne s'applique qu'à la génération, pas à la revalidation du corpus existant (séquence 1). Vérifié : les quatre schémas se transforment sans erreur via `transform_schema` (pas de référence circulaire réintroduite), les deux champs figurent dans `required`, aucune trace de `non_renseigne` dans leur définition de type.

**2. Prompts v2.1 — règle sémantique explicite.** `prompt_vulnerabilites_v2_1.md` et `prompt_chaines_causales_v2_1.md` (nouveaux, v2.0 conservés) ajoutent une règle dédiée : « pour chaque champ bitemporel, pose-toi la question directement — la source donne-t-elle une date précise ? Si oui, écris-la. Si non, écris `non_documente`. Ne laisse jamais un champ à une valeur par défaut implicite. » Les deux prompts reçoivent aussi une section « Comportement en cas de réinjection d'erreurs », absente en v2.0 (où seul Synthèse pouvait être réinjecté) — nécessaire depuis que ces deux agents sont individuellement réinjectables (tâche 3).

**3. Routage de réinjection par agent propriétaire.** `route_validation_errors` (nouveau) attribue chaque erreur de `M01Analysis.model_validate` à l'agent dont le fragment contient le champ fautif :
- Erreurs de champ (`loc` non vide) — routées par le premier segment du chemin, avec un cas spécial pour `units[i].<champ>` (le sous-champ distingue Charité de Vulnérabilités).
- Erreurs racine (`loc` vide, ex. `validate_bitemporal_when_durci`) — le chemin précis n'est pas structuré par Pydantic dans ce cas ; une expression régulière extrait les chemins embarqués dans le texte du message et les répartit, une même erreur brute pouvant donc se scinder entre Vulnérabilités et Chaînes causales.
- Erreur non routable (champ défaulté par l'orchestrateur lui-même, ex. `method_version`) — interrompt la passe immédiatement, sans consommer de budget de réinjection, plutôt que d'attribuer l'erreur à un agent au hasard.

`run_pipeline` réécrit en conséquence : une passe initiale (un appel par agent, ordre linéaire), puis un budget global de 3 appels de réinjection par passe, partagé entre les agents qui en ont besoin (pas 3 par agent). `OrchestrationResult.iterations_used` renommé `agent_calls_used` (la notion d'« itération » anchée à Synthèse n'a plus de sens). Un agent réinjecté revoit exactement le même contexte amont que lors de son appel initial (fragments des agents qui le précèdent dans l'ordre linéaire), jamais ceux des agents suivants — pipeline toujours linéaire, conformément à l'instruction du lot.

**Tests.** 8 tests unitaires nouveaux sur le routage (champs de premier niveau vers chaque agent, sous-champ d'unité, erreur racine bitemporelle scindée entre deux agents, cas non routable) + 1 test sur les schémas de sortie (champs requis, absence de `non_renseigne`). Suite complète de l'orchestrateur : 27/27 verts. Aucune régression sur le corpus existant (12/12 YAML positifs, 6/6 tests négatifs).

**4. Ré-exécution sur `corpus/lecornu_dpg_20251014.md` — succès dès la première tentative.** Quatre appels d'agent, aucune réinjection nécessaire, validation Pydantic réussie du premier coup. Première production automatique complète et validée du prototype, sur les six tentatives cumulées depuis le lot {2.7}.

**5. `exports/etalonnage_001.md` produit.** Comparaison factuelle contre l'analyse manuelle canonique (`pipeline/analyses/lecornu_v2_1.yaml`, même texte source) — objets thématiques/visés (identifiés/manqués/ajoutés), unités (comparaison impossible, la manuelle n'a pas de découpage en unités), chaînes amont/aval, engagements V.3 et patterns, hypothèses et confidences vs grille de calibration, historiographies, résultats nuls, omissions. Sans jugement de conformité, conformément à l'instruction — les écarts sont classés en cinq catégories factuelles (granularité, base d'information disponible, angle des objets visés, profil de confidence, structuration nouvelle) et remontés tels quels au Mode Reviewer.

Point préalable signalé explicitement dans le document (§0) : l'automatique n'a reçu que le texte du discours, sans contexte documentaire sur les suites — à la différence de la manuelle, rédigée sept mois plus tard avec recherche des événements survenus depuis. Cette différence de base d'information explique mécaniquement la totalité des écarts sur les blocs V.3/V.4/chaînes avales, ce n'est pas une différence de capacité d'observation sur un même fait disponible aux deux analyses.

**6. Addendum comptabilité API** ajouté à `.claude/logs/rapport_implementation_002.md` (§8, append-only) — quatre appels, aucune réinjection, 0,4985 $, et cumul des trois lots (2.7+2.8+2.9) : 750 903 tokens d'entrée, 287 625 de sortie, 4,3781 $.

## Constat notable — absence d'invention sur les suites du discours

La sortie automatique assigne `not_yet_observed` aux quatre engagements V.3 qu'elle documente et laisse le bloc des effets observables vide, plutôt que d'halluciner des suites qu'elle ne pouvait pas connaître (aucun contexte externe fourni). C'est un résultat épistémique positif, directement vérifiable dans le YAML produit — signalé ici et dans `etalonnage_001.md` comme un point favorable à la discipline d'invention zéro du pipeline, pas comme un jugement de conformité sur la qualité de l'analyse.

## État des tests

12/12 YAML positifs, 6/6 tests négatifs — aucune régression. 27/27 tests unitaires de l'orchestrateur (19 hérités des lots {2.8}, 8 nouveaux pour le routage de réinjection).

## Modifications de code / documents

- `pipeline/agent_schemas.py` — quatre nouveaux modèles de sortie (`VulnerabilityOutput`, `OmissionOutput`, `DiscourseActGapOutput`, `ObservableEffectOutput`), type `RequiredBitemporalDate`.
- `pipeline/orchestrateur.py` — `route_validation_errors` (nouveau), `run_pipeline` réécrit (routage par agent, budget de réinjection global), `OrchestrationResult.agent_calls_used` (renommé), `PIPELINE_ORDER`/`AGENT_PROMPT_FILES` (remplacent `PRIOR_AGENTS`/`SYNTHESE_AGENT`/`MAX_ITERATIONS`).
- `pipeline/agents/fonctionnels/prompt_{vulnerabilites,chaines_causales}_v2_1.md` — nouveaux (v2.0 conservés).
- `pipeline/tests/test_orchestrateur.py` — 9 tests nouveaux (schémas + routage).
- `pipeline/analyses/M01_LECORNU_DPG_20251014_AUTO_v1/` — YAML final produit et validé (nouveau), quatre nouveaux logs JSON.
- `exports/etalonnage_001.md` — nouveau (forcé au commit malgré `exports/` dans `.gitignore` — voir note ci-dessous).
- `.claude/logs/rapport_implementation_002.md` — addendum §8 (append-only).

## Note sur `exports/etalonnage_001.md` et `.gitignore`

Le répertoire `exports/` est intégralement ignoré par `.gitignore` (décision 002 — vues dérivées du graphe non versionnées : `graphe.graphml`, `graphe.json`, `exports/audits/`). `etalonnage_001.md` n'est pas une vue mécaniquement régénérable à partir du graphe — c'est un document d'analyse comparative explicitement nommé comme livrable attendu par `plan_action_002.md` §6 (« Output attendu »). Ajouté au commit avec `git add -f` — décision signalée ici plutôt que silencieusement contournée ; le Reviewer/Architecte peut juger si une exception dédiée au fichier doit être ajoutée à `.gitignore` plutôt que de dépendre d'un `-f` répété à chaque nouvel étalonnage.

## État du système

Lot 2.9 exécuté conformément à l'instruction — les cinq points prescrits sont tous réalisés, y compris le point conditionnel (item 4 : YAML valide obtenu, `etalonnage_001.md` donc produit). Les huit critères d'acceptation §3 du plan (`rapport_implementation_002.md` §2) sont à revisiter par le Reviewer à la lumière de ce lot — les lignes « Orchestrateur » et « Étalonnage », non satisfaites à la fin du lot {2.7} et toujours non satisfaites à la fin du lot {2.8}, sont désormais satisfaites : un YAML M01-M automatique valide existe, avec logs complets, et la comparaison factuelle à l'analyse manuelle est produite. Le statut de clôture de la séquence 2 et de la Phase 0 reste un arbitrage du Reviewer/Architecte, pas de l'Implementer (discipline §9 du plan) — non tranché dans cette note.

## Recommandations pour la suite

- **Critères d'acceptation à revisiter.** Sur les huit critères de `plan_action_002.md` §3, seuls trois restent probablement partiels après ce lot (repo/onboarding — écart §9 toujours ouvert ; gouvernance — validation Dirigeant déjà actée le 5 juillet, CLA v0.2.1 ; journal — clôture de séquence 2 et de Phase 0 encore à écrire). C'est un arbitrage de synthèse pour le Reviewer, pas une action supplémentaire de l'Implementer dans ce lot.
- **`.gitignore` de `exports/`** — décision à prendre sur une exception dédiée à `etalonnage_00X.md` si d'autres étalonnages sont produits à l'avenir (dossier zéro, `plan_action_003.md`).
- **Généralisation du routage de réinjection à Charité et Synthèse** — ces deux agents n'ont pas reçu de section « comportement en cas de réinjection » dans ce lot (hors périmètre explicite de la tâche 2, qui ne visait que les « agents producteurs d'assertions »), bien qu'ils soient désormais techniquement réinjectables via le routage générique. Aucune occurrence réelle observée sur les exécutions de ce lot — signalé comme point d'attention pour un futur texte source qui déclencherait une erreur sur un champ de Charité ou de Synthèse.
