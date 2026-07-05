# Log de session — plan_action_002, lot {2.7} (dernier lot de la séquence 2)

*Mode opérationnel : Implementer. Plan référencé : `.claude/plans/plan_action_002.md` §4 séquence 2, tâche 2.7. Texte d'étalonnage : Déclaration de Politique Générale de Sébastien Lecornu, Assemblée nationale, 14 octobre 2025 (`corpus/lecornu_dpg_20251014.md`).*

---

## Tâches accomplies

**Corpus source.** Le fichier `corpus/lecornu_dpg_20251014.md` (4451 mots) a été extrait verbatim du PDF officiel (`pdftotext -layout`, poppler-utils), nettoyé des artefacts de pagination, sans front-matter ni licence — texte gouvernemental brut, la provenance étant documentée au commit plutôt qu'en en-tête de fichier, puisque l'orchestrateur lit le fichier entier comme `source_text`. Fidélité vérifiée par sondage contre les images du PDF (citations, chiffres budgétaires, nombre de trimestres, etc.) — tout concorde.

**Deux défauts réels trouvés et corrigés dans `AnthropicAgentCaller.__call__` (`pipeline/orchestrateur.py`), les deux découverts uniquement par l'exécution réelle** — c'est précisément ce que 2.7 devait exercer :

1. **`thinking` non désactivé explicitement.** Sur `claude-sonnet-5`, omettre le paramètre `thinking` active le raisonnement étendu adaptatif par défaut (contrairement à Opus 4.7/4.8, où l'omission signifie l'absence de raisonnement). Sur le prompt Charité (long — texte source intégral + instructions d'extraction, 33855 caractères), le modèle a consacré la totalité du budget de sortie (16000 tokens) au bloc de raisonnement interne, laissant zéro token pour le YAML attendu : `stop_reason="max_tokens"`, un unique bloc `type="thinking"`, aucun bloc `"text"`. Diagnostiqué par reproduction exacte du prompt Charité (extrait du log de l'exécution ratée) en appel direct au SDK. Correction : `thinking={"type": "disabled"}` — les agents fonctionnels sont des tâches d'extraction déterministe suivant une procédure prescrite par le prompt, le raisonnement du modèle n'y apporte rien, donc coupé plutôt que budgété.
2. **`max_tokens=16000` insuffisant même une fois `thinking` coupé.** Une fois le raisonnement désactivé, la réponse Charité sur le discours réel (33855 caractères de prompt) a de nouveau atteint `stop_reason="max_tokens"`, cette fois tronquée en plein YAML à 16000 tokens de texte réel. Relevé à `max_tokens=64000` avec passage en mode streaming (`client.messages.stream(...)` + `get_final_message()`) — le SDK impose le streaming au-delà d'environ 16000 tokens de sortie en mode non-streaming (garde-fou contre les timeouts HTTP). Vérifié directement : `stop_reason="end_turn"`, réponse complète et bien formée jusqu'à la fermeture du bloc YAML.

Les deux corrections ont été vérifiées séparément par appel diagnostique direct au SDK sur le prompt Charité exact avant d'être intégrées à une exécution complète du pipeline, pour ne pas dépenser le budget API sur une hypothèse non confirmée.

## Exécutions réelles de l'orchestrateur (deux, après les corrections ci-dessus)

**Première exécution** — échec après l'agent Vulnérabilités (aucune boucle de réinjection pour les trois premiers agents, par conception — tâche 2.4). YAML mal formé : une valeur de type chaîne combinait un segment entre guillemets doubles suivi de texte hors guillemets sur la même ligne (`"J'ai proposé au Président de la République un gouvernement" (unité ultérieure du texte)`), syntaxe YAML invalide. Erreur de génération du modèle, pas un bug de l'orchestrateur.

**Deuxième exécution** — Charité, Vulnérabilités et Chaînes causales réussissent tous les trois. L'agent Synthèse échoue à ses **deux itérations autorisées** (le rapport d'erreurs de la première itération a été correctement réinjecté dans le prompt de la seconde — vérifié dans le log). Cause identique aux deux itérations, dans le bloc `red_team_objections` : une phrase argumentative en français contient un deux-points suivi d'un espace (`... je le reconnais') : si la nécessité ...`) à l'intérieur d'un scalaire YAML non guillemeté multi-lignes — syntaxe invalide, car `: ` hors guillemets est interprété par le parseur YAML comme un début de mapping. Confirmé indépendamment sur les deux itérations (contenu textuel différent, même piège structurel).

**Diagnostic retenu.** Il s'agit d'une friction réelle et reproductible de génération — le prompt de l'agent Synthèse (et implicitement des autres agents) n'impose pas de discipline de citation YAML stricte pour le texte en langage naturel, et la prose argumentative française use naturellement de deux-points pour introduire une clause. Ce n'est ni un bug de `orchestrateur.py`, ni un défaut de la boucle de réinjection (qui a fonctionné exactement comme conçu). La correction relèverait d'une modification des prompts d'agents fonctionnels (hors périmètre de 2.7, qui est « exécuter l'orchestrateur », pas « réviser les prompts ») ou d'un assouplissement du parseur (refusé — assouplir la validation pour forcer un succès va directement contre la consigne explicite du lot).

## Décision d'arrêt

Conformément à l'instruction explicite du lot — *« Si l'orchestrateur échoue après ses 2 retries, l'échec documenté avec logs EST le livrable (ne force pas) »* — et la deuxième exécution ayant épuisé les deux itérations de la boucle Synthèse avec un échec de validation réel et diagnostiqué à chaque fois, cette exécution constitue le point d'arrêt autorisé. Aucune troisième exécution complète n'a été tentée, aucune modification du parseur YAML ou des prompts d'agents fonctionnels n'a été faite pour contourner le problème.

**Conséquence sur `exports/etalonnage_001.md`.** Ce livrable est conditionné à l'existence d'un YAML M01-M automatique validé (comparaison structurée automatique vs analyse manuelle canonique). Aucun YAML validé n'ayant été produit, ce document n'est pas produit dans ce lot — cohérent avec l'instruction explicite : en cas d'échec documenté, celui-ci EST le livrable, la comparaison n'a pas de matière à traiter.

## État des logs

Les logs JSON des quatre exécutions (deux dans une session antérieure, avant les corrections ; deux dans ce lot, après corrections) sont tous conservés dans `pipeline/analyses/M01_LECORNU_DPG_20251014_AUTO_v1/logs/` — 16 fichiers, huit champs chacun (`agent`, `version_prompt`, `modele`, `horodatage_iso`, `iteration`, `prompt_complet`, `reponse_brute`, `usage_tokens`), conformément au format de la tâche 2.6. Aucun log n'est supprimé — la discipline du projet traite ces traces comme faisant partie de l'audit, pas comme des artefacts jetables à nettoyer après coup.

## Sécurité — gestion de la clé API

La clé API a été fournie par le Dirigeant via un fichier `pipeline/.env` (déjà couvert par `.gitignore` à la racine, vérifié avant toute exécution). Elle n'a jamais été affichée, journalisée dans les logs de l'orchestrateur (les logs ne contiennent que `prompt_complet`, `reponse_brute`, `usage_tokens` — jamais la clé), ni commitée. Une clé antérieure, exposée en clair dans l'historique de conversation d'une session précédente, avait déjà fait l'objet d'une recommandation de rotation au Dirigeant.

## Frictions signalées

1. **`thinking` par défaut adaptatif sur `claude-sonnet-5`** (contrairement à Opus 4.7/4.8) — a consommé silencieusement tout le budget de sortie sur un prompt long, sans produire le moindre texte. Non documenté comme un piège évident avant d'y être confronté ; désormais commenté explicitement dans le code (`orchestrateur.py`).
2. **Discipline de guillemetage YAML non prescrite aux agents fonctionnels.** Les quatre prompts d'agents (tâche 2.5) ne donnent aucune instruction sur l'échappement ou le guillemetage systématique des champs texte libre contenant des citations ou des deux-points — piège récurrent constaté sur deux exécutions indépendantes (Vulnérabilités et Synthèse). Signalé ici comme candidat de révision de prompt pour une itération future (hors périmètre de ce lot, qui n'écrit pas la doctrine ni les prompts).
3. **Le découpage en quatre agents et le rattachement d'`inferred_function`/historiographies** (frictions 1 et 2 du lot 2.4-2.6) restent des choix d'implémentation non re-questionnés ici — l'échec de 2.7 est survenu en amont (génération de YAML syntaxiquement invalide), pas sur le contenu doctrinal des sorties produites par Charité, Vulnérabilités ou Chaînes causales (qui ont, eux, réussi).

## État des tests

Suite `pytest` complète non ré-exécutée dans ce lot (aucune modification de `schemas.py`/`validate.py`/`graph_builder.py`/`audits.py`) — seul `orchestrateur.py` a été modifié (paramètres d'appel API), sans changement de signature ni de logique de fusion/validation. Les trois scénarios de plomberie par substitution (lot 2.4-2.6) restent valides sans reprise.

## Modifications de code / documents

- `pipeline/orchestrateur.py` — `AnthropicAgentCaller.__call__` : `thinking={"type": "disabled"}` ajouté, `max_tokens` porté à 64000, appel converti en streaming (`client.messages.stream(...)` + `get_final_message()`).
- `pipeline/analyses/M01_LECORNU_DPG_20251014_AUTO_v1/logs/` — 16 logs JSON (quatre exécutions, dont deux de ce lot), aucun YAML final produit (échec documenté).
- `corpus/lecornu_dpg_20251014.md` — déjà committé en amont de ce lot (extraction du texte source).

## État du système

Séquence 2 close — 2.0 à 2.7 faits. Le critère de sortie de la séquence 2 (§4 du plan) est satisfait par la lettre de l'instruction du lot : l'orchestrateur a été exécuté de bout en bout sur un texte réel, avec logs complets, et l'échec après épuisement des deux itérations de Synthèse est le livrable documenté conformément à la consigne explicite. `exports/etalonnage_001.md` n'a pas de matière (pas de YAML automatique validé) et n'est donc pas produit.

L'écart au §9 (séquence 0 non formellement close) reste ouvert, indépendant, déjà signalé aux lots précédents.

## Recommandations pour la suite

- **Priorité pour un futur lot (hors moratoire doctrinal, révision de prompts d'implémentation seulement)** : ajouter aux quatre prompts d'agents fonctionnels une instruction explicite de guillemetage systématique (guillemets doubles YAML, ou style bloc littéral `|`) pour tout champ texte libre susceptible de contenir des citations entre guillemets ou des deux-points — les deux échecs de ce lot proviennent exactement de ce piège.
- **Le Mode Reviewer** dispose désormais de deux jeux de logs complets (une exécution pré-corrections avec crash, une exécution post-corrections avec échec structuré après 2 itérations) — matière suffisante pour juger si l'architecture à quatre agents et la boucle de réinjection méritent un ajustement avant le prochain essai réel, sans qu'il soit nécessaire de relancer une troisième fois dans ce lot.
- **Rotation de la clé API** : la clé utilisée dans cette session a été fournie via `pipeline/.env` (jamais commitée, jamais journalisée) — mais reste recommandée en bonne hygiène périodique, indépendamment de cet incident.
