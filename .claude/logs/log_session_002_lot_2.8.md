# Log de session — plan_action_002, lot {2.8}

*Mode opérationnel : Implementer. Lot prescrit par `.claude/reviews/revue_002.md` §4 (correctif structurel + étalonnage), suite au verdict du Mode Reviewer sur le lot {2.7}.*

---

## Tâches accomplies

**1. Bascule des quatre agents fonctionnels en sortie JSON structurée.** Nouveau module `pipeline/agent_schemas.py` — un modèle Pydantic partiel par agent (`ChariteOutput`, `VulnerabilitesOutput`, `ChainesCausalesOutput`, `SyntheseOutput`), dérivé mécaniquement des modèles déjà normatifs de `pipeline/schemas.py` (jamais redéfinis en parallèle). Le schéma JSON transmis à l'API est construit via `transform_schema`, utilitaire interne du SDK Anthropic (`anthropic==0.116.0`, version épinglée) qui assainit les contraintes non supportées (minLength, minItems, minimum/maximum → déplacées en description) et force `additionalProperties: false`. Choix technique retenu : `client.messages.stream()` + `output_config={"format": {"type": "json_schema", ...}}` plutôt que la méthode publique `client.messages.parse()` — celle-ci force une requête non-streaming côté transport (vérifié empiriquement), ce qui déclenche le garde-fou de timeout SDK à `max_tokens=64000` (nécessaire depuis le lot 2.7). Les quatre prompts sont réécrits en v2.0 (`pipeline/agents/fonctionnels/prompt_*_v2_0.md`) — la section « fragment de schéma alimenté » devient une description des champs JSON attendus (le schéma proprement dit est désormais imposé côté API, plus une simple instruction textuelle) ; le prompt Synthèse est le plus profondément changé, il ne recopie plus les sorties des trois agents précédents ni n'assemble le YAML complet (ce n'est plus structurellement possible avec `output_config.format`, qui interdit tout texte hors du JSON).

**2. Conversion JSON→YAML mécanique dans l'orchestrateur.** `dump_yaml_forcing_quotes` (nouveau, `pipeline/orchestrateur.py`) — dumper YAML dédié forçant le style double-guillemets sur toute chaîne ambiguë (deux-points suivi d'espace, dièse, saut de ligne, caractère indicateur YAML en tête/fin, mot réservé, chaîne ressemblant à un nombre). Remplace `yaml.safe_dump` pour l'écriture du YAML final — c'est désormais la seule fonction du dépôt qui produit le YAML d'une analyse automatique. `merge_fragments` inchangé dans sa logique (le traitement spécial de `units` restait correct) mais désormais structurellement plus sûr : le fragment Synthèse ne contenant plus que ses deux propres blocs, `candidate.update(synthese)` ne risque plus d'écraser un champ d'un autre agent par une recopie dégradée. Dix-neuf tests unitaires (`pipeline/tests/test_orchestrateur.py`) couvrent l'assemblage (fusion par `unit_id`, blocs disjoints) et la conversion (reproduction exacte des deux classes d'erreur YAML du lot 2.7, round-trip de types, non-quotage des chaînes simples). `pytest==9.1.1` ajouté à `requirements.txt`.

**3. Ré-exécution de bout en bout sur `corpus/lecornu_dpg_20251014.md`.** Cinq tentatives complètes ont été nécessaires — voir *Frictions* ci-dessous pour le détail de chacune. La cinquième a exécuté le pipeline intégralement sans aucune erreur d'infrastructure, jusqu'à un échec de validation Pydantic légitime (voir *Résultat*).

**4. `exports/etalonnage_001.md` — non produit.** Condition explicite de la tâche 4 (« si YAML valide ») non remplie : aucune des cinq tentatives n'a produit de candidat passant `M01Analysis.model_validate`.

**5. Addendum comptabilité API** ajouté à `.claude/logs/rapport_implementation_002.md` (§7, append-only) — détail des onze appels facturés et des deux appels rejetés avant génération, plus le cumul lot 2.7 + lot 2.8.

## Frictions et défauts trouvés en cours de lot

Trois défauts réels ont été trouvés et corrigés par l'exécution réelle, aucun anticipé par la conception initiale :

1. **Virgule finale avant crochet/accolade fermante (tentatives 1 et 2).** `output_config.format` réduit fortement mais n'élimine pas en pratique le risque de JSON syntaxiquement malformé — observé deux fois indépendamment sur l'agent Charité, à chaque fois en fin de liste `speech_acts`, avec un volume de sortie (5984-7999 tokens) très inférieur au plafond de 64000 (donc pas une troncature). Corrigé par une réparation mécanique ciblée dans `parse_json_fragment` (expression régulière retirant les virgules immédiatement suivies d'un crochet/accolade fermante) — une classe d'erreur strictement syntaxique et non ambiguë, sans invention de contenu. Confirme la piste de repli anticipée par `revue_002.md` §4 point 1.
2. **Référence circulaire de schéma (tentative 3).** `schemas.InferredFunction` est auto-référent (`alternative_functions: list["InferredFunction"]`) — légitime pour la validation Pydantic finale, rejeté par l'API pour `output_config.format` (« Circular reference detected »). Corrigé par un modèle de sortie structurée plafonnant la récursion à un niveau (`InferredFunctionOutput`/`InferredFunctionAlternative`, nouveau dans `agent_schemas.py`) — la validation finale reste inchangée. Un test de régression (`test_all_agent_output_schemas_transform_without_circular_reference`) vérifie désormais que les quatre schémas se transforment sans appel réseau.
3. **Timeout de compilation de grammaire (tentative 4), non corrigé — infrastructure.** Le schéma de l'agent Chaînes causales (9030 caractères) a échoué avec `Grammar compilation timed out`, alors qu'un schéma plus grand (Vulnérabilités, 9535 caractères) avait réussi dans la même tentative — exclut une limite déterministe de taille, pointe vers une variabilité d'infrastructure côté API. Un nouvel essai complet (tentative 5) a réussi sans aucune erreur de ce type. Non retenu comme un échec structurel au sens de `revue_002.md` §4 point 3 — traité comme une flakiness résolue par un ré-essai, pas par une révision d'architecture.

## Résultat de la tentative 5 (complète, sans erreur d'infrastructure)

Charité, Vulnérabilités, Chaînes causales, puis Synthèse sur ses deux itérations autorisées se sont tous exécutés sans erreur de génération ni de format. Échec final à la validation Pydantic : certaines omissions produites par l'agent Vulnérabilités ont laissé `date_fait`/`date_connaissance` à la sentinelle par défaut `non_renseigne` plutôt qu'à `non_documente` — violation du validateur de bitemporalité durcie (tâche 1.2). L'erreur porte sur des champs de l'agent Vulnérabilités, pas de Synthèse ; conformément à la conception du prompt Synthèse v2.0 (qui ne peut plus corriger un champ hors de son périmètre depuis la bascule JSON), la réinjection à la deuxième itération n'a pas pu la résoudre — comportement attendu, pas un dysfonctionnement de la boucle de réinjection, qui a fonctionné exactement comme conçue (rapport d'erreurs lu, deux itérations consommées, échec propre avec logs complets).

C'est un échec de contenu ordinaire (compliance incomplète d'un agent aux sentinelles prescrites), catégoriquement différent des trois défauts structurels ci-dessus (tous résolus) et du conflit prose-riche/YAML-nu du lot 2.7 (éliminé — zéro occurrence sur les cinq tentatives de ce lot). Conformément à l'instruction du lot 2.8, ce résultat documenté est le livrable recevable de la tâche 3.

## État des tests

12/12 YAML positifs, 6/6 tests négatifs — suite complète verte, aucune régression sur `schemas.py`/`schemas_m03.py`/`validate.py`/`validate_m03.py`/`graph_builder.py`/`audits.py`. 19/19 nouveaux tests unitaires de l'orchestrateur verts (`pipeline/tests/test_orchestrateur.py`), sans appel réseau.

## Modifications de code / documents

- `pipeline/agent_schemas.py` — nouveau (schémas de sortie structurée par agent).
- `pipeline/orchestrateur.py` — sortie JSON structurée (`output_config.format`), `parse_json_fragment` (avec réparation de virgule finale), `dump_yaml_forcing_quotes`, assemblage des fragments en JSON dans les prompts.
- `pipeline/agents/fonctionnels/prompt_{charite,vulnerabilites,chaines_causales,synthese}_v2_0.md` — nouveaux (v1.0 conservés, non supprimés, pour trace de version).
- `pipeline/tests/conftest.py`, `pipeline/tests/test_orchestrateur.py` — nouveaux.
- `requirements.txt` — `pytest==9.1.1` ajouté.
- `.claude/logs/rapport_implementation_002.md` — addendum §7 (append-only).
- `pipeline/analyses/M01_LECORNU_DPG_20251014_AUTO_v1/logs/` — onze nouveaux logs JSON (cinq tentatives).

## État du système

Lot 2.8 exécuté conformément à `revue_002.md` §4 — correctif structurel appliqué et vérifié (le conflit prose-riche/YAML-nu du lot 2.7 est éliminé), ré-exécution complète sans erreur d'infrastructure sur la cinquième tentative, échec documenté recevable sur un point de contenu ordinaire (bitemporalité incomplète d'un agent). `exports/etalonnage_001.md` reste non produit — condition non remplie. Le critère de clôture de la Phase 0 fixé par `revue_002.md` §4 (« les huit critères du §3 du plan revisités ; les partiels résolus ; entrée journal de clôture de séquence 2 et de Phase 0 ») n'est pas encore atteint sur les lignes orchestrateur/étalonnage — point remonté au Reviewer/Architecte, non arbitré par l'Implementer (discipline §9 du plan).

## Recommandations pour la suite

- **Le point qui reste à corriger est de contenu, pas d'architecture** — le prompt Vulnérabilités v2.0 pourrait insister plus explicitement sur l'obligation de la sentinelle `non_documente` (déjà présente, visiblement insuffisamment suivie sur ce run) ; un sixième essai a de bonnes chances de succès sans changement de code, uniquement par la variance stochastique de génération — ou avec un renforcement ciblé du prompt.
- **Timeout de compilation de grammaire (friction 3)** — surveiller si ce type d'erreur d'infrastructure se reproduit sur de futurs runs ; à signaler à Anthropic si la fréquence devient significative, mais insuffisant à ce stade pour justifier un changement d'architecture.
- **`exports/etalonnage_001.md`** reste conditionné à un run réussi — candidat naturel d'un lot 2.9 court (un seul objectif : obtenir un YAML validé, sans autre changement de périmètre).
- Les points ouverts de `revue_002.md` non couverts par le périmètre de ce lot (écart §9 séquence 0, choix quotage vs JSON — désormais tranché en faveur de JSON par ce lot même, alternative de repli conservée dans `parse_json_fragment`) restent à la main du Reviewer/Architecte.
