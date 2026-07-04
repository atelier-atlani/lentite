# Log de session — plan_action_002, lot {2.4–2.6}

*Mode opérationnel : Implementer. Plan référencé : `.claude/plans/plan_action_002.md` §4 séquence 2. Point d'attention préalable du Dirigeant intégré (postes disciplinaires ≠ agents fonctionnels).*

---

## Tâches accomplies

**Point d'attention préalable.** Les cinq prompts hérités de mai (`pipeline/agents/prompt_*.md` — contradicteur, analyste discours, économiste, juriste, sociologue) sont notés en tête de fichier comme postes disciplinaires réservés à l'architecture multi-postes post-moratoire, explicitement non mobilisés par le pipeline linéaire v1. Aucune modification de leur contenu.

**2.5 — Quatre agents fonctionnels créés** dans `pipeline/agents/fonctionnels/`, dérivés de `doctrine/V2.1/lentite_methode_01_v2_1.md` §6 (procédure en quatorze étapes) :
- **Charité** (étapes 1-8) — validation matériau, objets thématiques/visés, fiche d'énonciation, découpage en unités, reconstruction charitable, actes de langage, présuppositions.
- **Vulnérabilités** (étapes 9-10) — vulnérabilités argumentatives, omissions qualifiées (les quatre champs du bloc durci 1.1), fonction inférée.
- **Chaînes causales** (étape 11 + 12) — chaînes amont/aval, écarts discours/acte (V.3), effets observables (V.4), historiographies.
- **Synthèse** (étapes 13-14) — hypothèses concurrentes, red team, synthèse épistémique, résultats nuls, assemblage final ; spécifie explicitement son comportement en cas de réinjection du rapport d'erreurs `validate.py`.

Chaque prompt documente sa mission doctrinale, le fragment exact de `pipeline/schemas.py` qu'il alimente, et ses interdictions (aucune invention de source ; sentinelle `non_documente` obligatoire en l'absence de date précise ; pas de modification silencieuse des sorties des agents précédents).

**2.4 — Orchestrateur** (`pipeline/orchestrateur.py`). Architecture hexagonale légère — port `AgentCaller` (Protocol) découplant le pipeline du SDK Anthropic concret ; `AnthropicAgentCaller` est le seul point de dépendance réseau, instancié uniquement pour une exécution réelle. Pipeline linéaire à quatre agents, fusion des fragments (`merge_fragments` — traitement particulier de `units`, complété par Vulnérabilités sans écraser le travail de Charité), validation contre `M01Analysis`, réinjection du rapport d'erreurs à Synthèse sur échec, deux itérations maximum, échec propre avec logs sinon. Clé API lue exclusivement depuis `ANTHROPIC_API_KEY` — erreur explicite si absente, jamais un argument CLI. Modèle par défaut `claude-sonnet-5`, paramétrable (`--model`).

**2.6 — Format de log.** `write_agent_log` produit un JSON par appel d'agent avec exactement les huit champs spécifiés (`agent`, `version_prompt`, `modele`, `horodatage_iso`, `iteration`, `prompt_complet`, `reponse_brute`, `usage_tokens`) dans `pipeline/analyses/<analyse>/logs/`. Non ajouté à `.gitignore` — ces logs se versionnent avec le YAML de l'analyse (traces de production, pas des vues dérivées).

**Dépendance.** `anthropic==0.116.0` ajouté à `requirements.txt` (version installée et confirmée fonctionnelle, même discipline que pydantic/PyYAML/networkx).

## Vérification de la plomberie (sans appel réseau réel)

Conformément à la consigne du lot (« ne lance pas d'exécution sur texte réel »), aucun appel à l'API Anthropic n'a été effectué. La plomberie interne a été vérifiée par substitution — un agent factice (fonction Python) remplaçant `AnthropicAgentCaller`, avec des fragments YAML canoniques minimaux, sur trois scénarios :

1. **Succès direct** — les quatre agents produisent des fragments valides du premier coup ; 1 itération, 4 logs écrits, YAML final conforme à `M01Analysis`.
2. **Échec puis succès** — l'agent Synthèse échoue une première fois (moins de trois hypothèses) ; le rapport d'erreurs est vérifié présent dans le prompt de la deuxième tentative (et absent de la première) ; 2 itérations, 5 logs, succès final.
3. **Échec persistant** — l'agent Synthèse échoue aux deux itérations ; échec propre retourné avec les 5 logs et le rapport d'erreurs de la dernière tentative, pas de troisième essai.

**Bug réel trouvé et corrigé pendant cette vérification.** Le champ `source` (obligatoire au schéma `M01Analysis`) n'était produit par aucun des quatre agents — oubli dans la première version de `run_pipeline`. Correction — `source` est une métadonnée sur l'entrée de l'orchestrateur lui-même (fichier fourni, pas contenu à inférer), donc assemblée par l'appelant et transmise en paramètre explicite `source_metadata` (non silencieusement défaultée), avec `integrity_status="uncertain"` par défaut en CLI réelle (une ingestion automatisée ne certifie rien). C'est exactement le genre d'erreur que cette vérification de plomberie visait à attraper avant la tâche 2.7.

Le garde-fou sur `ANTHROPIC_API_KEY` a été vérifié séparément (erreur claire si absente, sans tenter d'appel réseau).

## Frictions signalées

1. **Découpage en quatre agents non prescrit explicitement par la doctrine.** La méthode M01 v2.1 décrit quatorze étapes sans les grouper nommément en Charité/Vulnérabilités/Chaînes causales/Synthèse. Le mapping retenu (documenté en note de fin du prompt Charité) suit les sous-blocs du schéma `M01Analysis` — choix d'implémentation cohérent, signalé plutôt que présenté comme une prescription doctrinale.
2. **`inferred_function` et les historiographies attribués par choix, pas par prescription.** `inferred_function` (schéma `Unit`) n'a pas d'étape dédiée explicite dans la doctrine — rattaché à l'agent Vulnérabilités par proximité (registre épistémique prudent). Les historiographies (étape 12) sont rattachées à Chaînes causales plutôt qu'à un cinquième agent inexistant.
3. **`source` assemblé par l'orchestrateur, pas halluciné.** Voir le bug corrigé ci-dessus — décision consciente, pas une improvisation de dernière minute : la métadonnée de provenance du fichier ne doit jamais être une inférence d'agent.

## État des tests

12/12 YAML positifs, 6/6 tests négatifs — suite complète verte, aucune régression sur `schemas.py`/`schemas_m03.py`/`validate.py`/`validate_m03.py`/`graph_builder.py`/`audits.py`. Trois scénarios de plomberie de l'orchestrateur vérifiés sans appel réseau.

## Modifications de code / documents

- `pipeline/agents/prompt_*.md` (5 fichiers) — note de statut réservé ajoutée.
- `pipeline/agents/fonctionnels/` — 4 nouveaux prompts versionnés.
- `pipeline/orchestrateur.py` — nouveau.
- `requirements.txt` — `anthropic==0.116.0` ajouté.

## État du système

Séquence 2 en cours — 2.0 à 2.6 faits. Reste 2.7 (test de bout en bout étalonné sur un texte source réel, avec choix du texte par le Dirigeant selon le plan §7). L'écart au §9 (séquence 0 non formellement close) reste ouvert, indépendant.

## Recommandations pour la suite

- 2.7 est le premier test qui exercera réellement `AnthropicAgentCaller` — vérifier `ANTHROPIC_API_KEY` en variable d'environnement avant de lancer, jamais en argument.
- Le choix du texte source d'étalonnage revient au Dirigeant (plan §7) — proposition déjà faite dans le plan : Lecornu ou Fabius, selon disponibilité du texte source original (pas seulement l'analyse déjà produite, le texte brut).
- Les trois points de friction ci-dessus (découpage en quatre agents, rattachement d'`inferred_function` et des historiographies) sont de bons candidats de vérification lors du premier vrai rejeu — si le résultat de 2.7 révèle qu'un agent reçoit une mission mal calibrée, c'est le moment de l'ajuster, pas avant.
