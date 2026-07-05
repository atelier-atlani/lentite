# Rapport d'implémentation — plan_action_002

*Rédigé par l'Implementer (Claude Code) à destination du Mode Reviewer, conformément à `plan_action_002.md` §6. Couvre l'intégralité des séquences 0, 1 et 2 — dix lots de session, du premier commit (`63a5203`) à la clôture du lot {2.7}. Sans jugement de conformité au-delà des constats factuels ci-dessous — l'arbitrage revient au Reviewer.*

---

## 1. Synthèse par séquence

### Séquence 0 — Hygiène et fondation

**Fait.** `git init`, purge des copies obsolètes (README, journal), rapatriement des analyses orphelines vers `analyses/`/`pipeline/analyses/`, cannibalisation d'`observatrice_complet/` (cinq prompts extraits vers `pipeline/agents/`, reste archivé), tri-partition de licences posée (`LICENSE`, `LICENSES/`, en-têtes SPDX sur tout le code), README resynchronisé, `gouvernance/CLA.md` rédigé, conventions de front matter et de commit ajoutées à `conventions.md`.

**Friction majeure — échec puis succès du test d'onboarding à froid.** Un premier test a échoué sur deux blocages indépendants : la commande d'installation documentée (`pip install --break-system-packages ...`) est invalide sous macOS (`pip` n'existe pas, seul `pip3` ; l'option n'est pas reconnue) ; et le `python3` par défaut (3.9.6, Xcode Command Line Tools) est incompatible avec la syntaxe `X | None` (PEP 604) de `schemas.py`, alors que le README annonçait « Python 3.11+ » sans vérification préalable. Correctif poussé, test rejoué intégralement (nouveau clone, séquence documentée suivie sans improvisation) — succès.

**Écart non résolu.** La revalidation réussie a été exécutée par la même instance ayant produit le correctif — pas par un tiers réellement indépendant, condition posée par le critère de sortie littéral (§3 : « un tiers — instance Claude vierge »). **La séquence 0 n'est donc pas formellement close.** Ce point a été signalé à chaque lot suivant sans être traité (hors mandat de l'Implementer, qui n'a pas accès à un tiers indépendant) ; il reste ouvert à ce jour.

### Séquence 1 — Durcissement du gabarit (couche B)

**Fait.** Bloc omission durci à quatre champs obligatoires (`pouvoir_agir`, `opportunite`, `cloture_corpus`, `explications_innocentes`) sur `M01Analysis` (1.1) ; bitemporalité minimale (`date_fait`/`date_connaissance`, sentinelle `non_renseigne`, `gabarit_version` conditionnel) sur quatre modèles d'assertion M01 (1.2), étendue symétriquement à quatre modèles M03 par arbitrage Architecte explicite hors numérotation d'origine (tâche 2.0, exécutée en séquence 2 mais rattachée doctrinalement ici) ; politique de corpus v1 et grille de calibration v1 rédigées comme nouveaux documents doctrinaux, sans révision des documents existants (1.3, 1.4) ; revalidation intégrale des 12 YAML sous le gabarit durci, un commit par fichier, sourcing strict (1.5). Sentinelle `non_documente` ajoutée sur instruction explicite du Dirigeant pour distinguer « recherché, absent des sources » de « non adressé par l'analyse ».

**Séquence close** — entrée de synthèse au journal général, suite de tests verte (12/12 positifs, 5/5 négatifs à la clôture, 6/6 après l'extension M03 de la tâche 2.0).

**Frictions signalées, non arbitrées :**
- Périmètre de la bitemporalité laissé au « minimal » du gabarit v2.1 (quatre modèles M01, quatre modèles M03) — `UpstreamElement`, `Hypothesis`, `Historiography`, `BenefitAsymmetry`, `CrossMatrixCase` et autres non couverts.
- Terminologie « établi » (degré de confiance 0,85–1,00) risque de confusion avec le statut épistémique « fait établi » de la charte — avertissement ajouté au document, pas de révision de la charte.
- Bande de confiance « faible » (< 0,40) sans cas-étalon sur le corpus actuel.
- Bloc omission M03 explicitement hors scope (pas d'équivalent `Omission` dans `M03Analysis`) — question doctrinale renvoyée au Reviewer.
- Asymétrie de datation constatée à la revalidation (21 dates réelles sur 57 champs `date_fait`, 36 `non_documente`) — voir rendement empirique n°1 ci-dessous.

### Séquence 2 — Prototype pipeline

**Fait.** `validate.py` M01 restauré par dérivation de `validate_m03.py` (2.1) ; `graph_builder.py` construisant un `networkx.MultiDiGraph` unique à partir de tout le corpus M01+M03, fusion des nœuds de personne par identifiant partagé `PRENOM_NOM` (pont M01↔M03, décision 002) (2.2) ; trois audits (`intentionality_bias_audit`, `hypothesis_gap_audit`, `typology_audit`) implémentés comme parcours de graphe, exécutables en CLI (2.3) ; orchestrateur hexagonal à quatre agents fonctionnels avec boucle de réinjection bornée à deux itérations sur l'agent Synthèse (2.4) ; quatre prompts versionnés dérivés de la méthode M01 v2.1 §6 (2.5) ; format de log JSON à huit champs par appel d'agent (2.6) ; test de bout en bout sur le texte réel de la Déclaration de Politique Générale de Sébastien Lecornu du 14 octobre 2025 (2.7).

**Résultat de 2.7 — échec documenté, pas de YAML validé produit.** Deux défauts d'intégration réels, découverts uniquement par l'exécution sur texte réel (jamais rencontrés par la vérification de plomberie par substitution du lot {2.4–2.6}) : sur `claude-sonnet-5`, l'omission du paramètre `thinking` engage un raisonnement adaptatif par défaut qui a consommé l'intégralité du budget de sortie sur le prompt Charité (long — texte source intégral inclus), laissant une réponse vide ; corrigé par désactivation explicite (`thinking={"type": "disabled"}`). Une fois corrigé, `max_tokens=16000` s'est révélé encore insuffisant pour la réponse réelle de Charité, tronquée en plein YAML ; corrigé par passage à `max_tokens=64000` en mode streaming. Deux exécutions complètes post-correction ont ensuite échoué pour une cause distincte, structurelle et non liée aux paramètres d'appel : du texte en langage naturel généré par les agents (citations entre guillemets, deux-points introduisant une clause) rompt la syntaxe YAML des scalaires non guillemetés. Confirmé indépendamment sur trois appels d'agent distincts (Vulnérabilités une fois, Synthèse deux fois). Voir rendement empirique n°3 ci-dessous et §5 (comptabilité API) pour le détail chiffré des quatre exécutions réelles.

**Conséquence sur `exports/etalonnage_001.md` — non produit.** Ce document suppose un YAML automatique validé à comparer à l'analyse manuelle ; aucun n'existe. Conforme à l'instruction explicite du lot 2.7 (« si l'orchestrateur échoue après ses 2 retries, l'échec documenté avec logs EST le livrable, ne force pas ») — mais cela laisse le critère d'acceptation « Étalonnage » du plan (§3) non satisfait au sens strict. Voir §2.

**Point non arbitré par l'Implementer — statut de clôture de la séquence 2.** Toutes les tâches numérotées (2.0 à 2.7) ont été exécutées et commitées. Mais le critère de sortie littéral de la séquence (§4 du plan : « critères d'acceptation §3 lignes pipeline, orchestrateur et étalonnage satisfaits ») n'est pas atteint pour les lignes orchestrateur et étalonnage — voir §2. Le lot {2.7} lui-même conclut, dans sa propre note de fin de lot, que « l'échec documenté avec logs est le livrable » satisfait la lettre de l'instruction du lot ; ce rapport distingue explicitement ce constat (l'instruction du lot a été suivie à la lettre) de la question séparée (le critère d'acceptation §3 du plan reste non satisfait). Aucune entrée de clôture de séquence 2 n'a été écrite au journal général à ce jour — cohérent avec ce constat, pas un oubli. **Ce point est remonté au Reviewer/Architecte tel quel, sans arbitrage de l'Implementer** (discipline §9 du plan : « l'Implementer ne prend aucune décision structurante »).

---

## 2. État des critères d'acceptation (`plan_action_002.md` §3)

| # | Critère | Statut | Justification |
|---|---|---|---|
| 1 | **Repo** — privé existe, arborescence assainie, onboarding à froid par un tiers vierge | **Partiel** | Repo et arborescence conformes. Onboarding réussi mais rejoué par l'instance ayant produit son propre correctif, pas par un tiers indépendant au sens littéral du critère — écart §9 ouvert depuis la séquence 0, jamais résolu. |
| 2 | **Licences** — `LICENSE`, `LICENSES/` (3 textes), SPDX, section README | **Satisfait** | Vérifié directement : `LICENSE` + 3 textes dans `LICENSES/` + en-têtes SPDX sur les 7 fichiers Python de `pipeline/` + section 7 du README documentant la tri-partition. |
| 3 | **Gabarit durci** — 4 chantiers B + tests négatifs + 12 YAML revalident | **Satisfait** | 1.1/1.2 (M01) + extension symétrique M03 (2.0) ; 1.3/1.4 (doctrine) ; 12/12 YAML revalidés (1.5) ; 6/6 tests négatifs (3 préexistants + 2 M01 + 1 M03). |
| 4 | **Pipeline** — `validate.py` restauré, `graph_builder.py` opérationnel, 3 audits en CLI | **Satisfait** | 2.1, 2.2, 2.3 tous exécutés et vérifiés sur le corpus complet (12 YAML, 121 nœuds/291 arêtes de graphe). |
| 5 | **Orchestrateur** — produit un YAML M01-M validé sur un texte réel, retry ≤ 2, log complet par appel | **Non satisfait** | L'architecture (retry borné, logs JSON à 8 champs) fonctionne exactement comme spécifié — mais aucune des quatre exécutions réelles (2.7) n'a produit de YAML passant `validate.py`. Le sous-critère « log complet par appel » est, lui, pleinement satisfait (16 logs, tous les 8 champs présents). |
| 6 | **Étalonnage** — sortie automatique comparée à l'analyse manuelle, écarts documentés | **Non satisfait** | Aucune sortie automatique valide à comparer ; `exports/etalonnage_001.md` non produit, conformément à l'instruction explicite de 2.7 en cas d'échec. |
| 7 | **Gouvernance** — CLA rédigé et versionné avant toute PR externe | **Partiel** | `gouvernance/CLA.md` rédigé et versionné (commit `0235076`, explicitement marqué « projet, non signé »). Aucune PR externe n'a eu lieu (cohérent, jalon 2 non atteint) donc la condition « avant toute PR externe » n'est pas mise en défaut — mais la validation du texte par le Dirigeant (prévue tâche 0.6 du plan) n'est pas actée au journal à ce jour. |
| 8 | **Journal** — chaque séquence close = une entrée journal | **Partiel** | Séquence 1 : entrée de clôture présente. Séquence 0 : pas d'entrée de clôture, cohérent avec le fait qu'elle reste ouverte (critère 1). Séquence 2 : aucune entrée de clôture — cohérent avec le constat du §1 ci-dessus (critère de sortie de la séquence non atteint au sens strict). |

**Synthèse** : 3/8 satisfaits sans réserve (licences, gabarit durci, pipeline), 3/8 partiels (repo/onboarding, gouvernance, journal), 2/8 non satisfaits (orchestrateur, étalonnage). Le prototype technique est complet et opérationnel de bout en bout ; ce qui manque est la démonstration réussie sur texte réel, pas une pièce d'architecture absente.

---

## 3. Trois rendements empiriques

### (a) Datation bitemporelle du corpus M01 — 21/36 (lot {1.5})

Sur 57 champs `date_fait` renseignés à la revalidation du corpus M01 (10 analyses), 21 portent une date réelle sourcée (extraite du YAML existant ou, pour un cas, croisée avec le document markdown correspondant — précédent Vallaud, 49.3 rompu le 19 janvier 2026), 36 sont restés à la sentinelle `non_documente` après recherche documentée et infructueuse (grep ciblé sur chaque markdown source, pas une absence de recherche). Constat consigné dans `journal/lentite_journal_m01.md` — asymétrie structurelle entre faits ponctuels datables et faits diffus non datés dans le corpus actuel, candidat à un futur `typology_audit`.

### (b) Alerte `intentionality_bias_audit` — 80–83% (lot {2.3})

Premier audit réel du corpus. Sur la fenêtre roulante nominale de 10 analyses : 8/10 (80%), exactement au seuil d'alerte. Sur l'ensemble du corpus (12 analyses) : 10/12 (83%). Verdict d'alerte identique dans les deux cadrages. C'est une confirmation empirique mécanique — non plus une estimation manuelle éparse — d'un biais déjà pressenti dans plusieurs analyses individuelles. Nuance signalée : toutes les analyses partagent le même `execution_date` de production par lot, donc la notion de « fenêtre roulante » chronologique réelle n'a pas encore de support de données propre ; le tri de repli (date puis alphabétique) exclut arbitrairement deux analyses de la fenêtre-10, sans changer le verdict sur ce corpus.

### (c) Échec YAML structurel de l'orchestrateur — lot {2.7}

Deux défauts de configuration d'appel API (thinking non désactivé, `max_tokens` insuffisant) ont été diagnostiqués et corrigés en cours de lot — voir §1. Une fois ces deux défauts corrigés, **deux exécutions complètes supplémentaires ont échoué pour une troisième cause, indépendante des paramètres d'appel** : la génération de texte en langage naturel par les agents (citations entre guillemets suivies de texte, deux-points introduisant une clause dans une phrase argumentative) produit des scalaires YAML syntaxiquement invalides. Constaté trois fois indépendamment (Vulnérabilités une fois, Synthèse à ses deux itérations, sur des contenus textuels différents à chaque fois — donc pas un artefact de contenu répété, mais un mode de défaillance récurrent de la génération). C'est un résultat réel du prototype, pas un défaut de l'orchestrateur lui-même (la boucle de réinjection a fonctionné exactement comme conçu aux deux tentatives de Synthèse) — voir §4 pour les deux directions de correction possibles, non tranchées ici.

---

## 4. Recommandations ouvertes

1. **Discipline de guillemetage YAML dans les prompts d'agents.** Ajouter aux quatre prompts fonctionnels une instruction explicite de guillemetage systématique (guillemets doubles, ou bloc littéral `|`) pour tout champ texte libre susceptible de contenir des citations ou des deux-points. Correction ciblée, cohérente avec l'architecture actuelle (YAML en texte libre parsé après coup).

   **Alternative anticipée de l'Architecte — sortie structurée JSON.** Le SDK Anthropic expose `output_config.format` (schéma JSON, sortie garantie conforme côté serveur) — une bascule des agents fonctionnels du format YAML-en-texte-libre vers une sortie JSON structurée éliminerait cette classe entière d'erreurs à la racine (plus de parsing après coup, plus de piège de guillemetage), au prix d'une réécriture du format de sortie de chaque agent et de la logique de fusion des fragments (`merge_fragments`). Les deux directions sont signalées ici sans arbitrage — c'est un choix structurant (format d'échange inter-agents), hors mandat de l'Implementer.

2. **Re-test d'onboarding à froid par un tiers réellement indépendant** (écart §9, ouvert depuis la séquence 0) — condition de clôture formelle du critère d'acceptation §3 « Repo ».

3. **Validation/signature du CLA par le Dirigeant** (tâche 0.6 du plan) — rédigé et versionné, non encore actée comme validée au journal.

4. **Statut de clôture de la séquence 2** — décision explicite requise : le critère de sortie §4 (« lignes pipeline, orchestrateur et étalonnage satisfaites ») reste non atteint au sens strict malgré l'exécution complète des tâches 2.0–2.7. Trancher si une cinquième exécution de l'orchestrateur (après correction du point 1) est requise avant clôture, ou si le Reviewer/Architecte accepte l'échec documenté de 2.7 comme clôturant la séquence en l'état.

5. **Décisions déjà signalées aux lots antérieurs, toujours ouvertes** : extension du périmètre de bitemporalité au-delà du minimal (séquence 1) ; bloc omission M03 (2.0) ; seuils d'alerte de `hypothesis_gap_audit` non sourcés dans la doctrine (2.3) ; horodatage de production distinct de `execution_date` pour une vraie fenêtre roulante (2.3) ; cas-étalon manquant en bande de confiance faible (1.4).

---

## 5. Comptabilité API complète — lot {2.7}

Modèle : `claude-sonnet-5`. Tarification intro en vigueur (jusqu'au 2026-08-31) utilisée pour le calcul ci-dessous : $2,00 / 1M tokens d'entrée, $10,00 / 1M tokens de sortie. *(Tarif standard post-intro, pour référence future : $3,00 / $15,00.)* Première donnée de comptabilité de l'axe 8 — méthode reproductible pour les lots suivants : extraction de `usage_tokens` depuis chaque log JSON.

### Quatre exécutions réelles de l'orchestrateur

| Exécution | Horodatage (UTC) | Résultat | Appels | Tokens entrée | Tokens sortie | Coût |
|---|---|---|---:|---:|---:|---:|
| A | 2026-07-04 16:36 | Échec — crash parsing YAML (pré-correctifs) | 4 | 55 358 | 25 627 | 0,3670 $ |
| B | 2026-07-04 16:45 | Échec — validation (Charité vide, thinking non coupé) | 5 | 74 413 | 50 448 | 0,6533 $ |
| C | 2026-07-05 00:32 | Échec — YAML mal formé (Vulnérabilités) | 2 | 35 627 | 22 578 | 0,2970 $ |
| D | 2026-07-05 06:43 | Échec — YAML mal formé (Synthèse, 2 itérations épuisées) | 5 | 184 389 | 75 001 | 1,1188 $ |
| **Sous-total** | | | **16** | **349 787** | **173 654** | **2,4361 $** |

Détail par appel d'agent (source : `pipeline/analyses/M01_LECORNU_DPG_20251014_AUTO_v1/logs/`) :

| Log | Agent | Itération | Entrée | Sortie |
|---|---|---:|---:|---:|
| `1_charite_...163619` (A) | charite | 1 | 13 686 | 8 192 |
| `2_vulnerabilites_...163750` (A) | vulnerabilites | 1 | 13 610 | 1 051 |
| `3_chaines_causales_...163804` (A) | chaines_causales | 1 | 13 951 | 8 192 |
| `4_synthese_...163934` (A) | synthese | 1 | 14 111 | 8 192 |
| `1_charite_...164538` (B) | charite | 1 | 13 686 | 16 000 |
| `2_vulnerabilites_...164815` (B) | vulnerabilites | 1 | 13 610 | 1 278 |
| `3_chaines_causales_...164832` (B) | chaines_causales | 1 | 13 951 | 12 092 |
| `4_synthese_...165036` (B) | synthese | 1 | 16 504 | 9 428 |
| `5_synthese_...165210` (B) | synthese | 2 | 16 662 | 11 650 |
| `1_charite_...003214` (C) | charite | 1 | 13 686 | 8 619 |
| `2_vulnerabilites_...003340` (C) | vulnerabilites | 1 | 21 941 | 13 959 |
| `1_charite_...064356` (D) | charite | 1 | 13 686 | 10 832 |
| `2_vulnerabilites_...064543` (D) | vulnerabilites | 1 | 23 906 | 20 967 |
| `3_chaines_causales_...064905` (D) | chaines_causales | 1 | 45 251 | 5 171 |
| `4_synthese_...064958` (D) | synthese | 1 | 50 684 | 19 483 |
| `5_synthese_...065253` (D) | synthese | 2 | 50 862 | 18 548 |

### Appels diagnostiques hors orchestrateur (reproduction directe du prompt Charité, hors pipeline, pour isoler la cause des échecs A et B)

| Appel | Objet | Entrée | Sortie | Coût |
|---|---|---:|---:|---:|
| Diag. 1 (session antérieure) | Prompt trivial de contrôle (comportement normal sans `thinking`) | `non_documente` | `non_documente` | `non_documente` |
| Diag. 2 (session antérieure) | Reproduction exacte du prompt Charité, `thinking` omis — confirme la consommation totale du budget par le raisonnement | ≈ 13 686 *(estimé — même prompt, non re-mesuré isolément)* | 16 000 (dont 16 000 de raisonnement, 0 texte) | ≈ 0,187 $ *(estimé)* |
| Diag. 3 (ce lot) | Reproduction exacte, `thinking` désactivé, non-streaming — confirme le texte produit mais tronqué | 13 686 | 16 000 | 0,1874 $ |
| Diag. 4 (ce lot) | Reproduction exacte, `thinking` désactivé, streaming, `max_tokens=64000` — confirme la correction | 13 686 | 15 661 | 0,1840 $ |
| **Sous-total mesuré (Diag. 3+4)** | | **27 372** | **31 661** | **0,3714 $** |

Diag. 1 n'a laissé aucune trace exploitable (appel de contrôle éphémère, non journalisé en fichier) — sentinelle `non_documente` retenue plutôt qu'une estimation inventée, cohérent avec la discipline du gabarit. Diag. 2 est reconstitué à partir du compte rendu de session (thinking_tokens=16000 confirmé, input_tokens non re-capturé isolément pour cet appel précis mais quasi certainement identique aux autres appels sur le même prompt de 33 855 caractères) — signalé comme estimation, pas une valeur extraite d'un artefact log.

### Total comptabilisable du lot {2.7}

| | Entrée | Sortie | Coût |
|---|---:|---:|---:|
| 4 exécutions orchestrateur (16 appels) | 349 787 | 173 654 | 2,4361 $ |
| 2 appels diagnostiques mesurés | 27 372 | 31 661 | 0,3714 $ |
| **Total mesuré** | **377 159** | **205 315** | **2,8075 $** |

Deux appels supplémentaires (Diag. 1, contrôle trivial ; Diag. 2, non re-capturé isolément) ne sont pas inclus dans le total mesuré — leur coût réel est marginal (Diag. 1 : prompt court) à modéré (Diag. 2 : même ordre de grandeur que Diag. 3, ≈ 0,19 $) mais non comptabilisé par discipline de non-invention plutôt qu'estimé au total.

---

## 6. Conclusion pour le Mode Reviewer

Le prototype technique est **architecturalement complet** : gabarit durci et testé, pipeline de validation et de graphe opérationnel, trois audits produisant des résultats réels et interprétables, orchestrateur avec boucle de réinjection fonctionnant exactement comme spécifié. Ce qui reste ouvert n'est pas une pièce manquante mais une démonstration non aboutie : aucune exécution réelle de l'orchestrateur n'a encore produit de YAML M01-M validé, pour une cause de génération (discipline de guillemetage YAML) diagnostiquée avec précision mais non corrigée dans ce plan (hors mandat du lot {2.7}, qui portait sur l'exécution, pas la révision des prompts). Trois décisions structurantes attendent l'arbitrage du Reviewer/Architecte : le choix entre quotage renforcé et sortie JSON structurée (§4.1), le statut de clôture formelle de la séquence 2 (§4.4, §1), et la disposition à prendre sur l'écart §9 de la séquence 0 (onboarding par un tiers réellement indépendant).
