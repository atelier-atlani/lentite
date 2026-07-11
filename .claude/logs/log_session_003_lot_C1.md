# Note de fin de lot — plan_action_003, séquence C, lot C.1

*Mode opérationnel : Implementer. Plan référencé : `.claude/plans/plan_action_003.md` §6 (séquence C), sur la base de `decision_006_cas_dossier_zero.md`. Deux M01 produits sur les discours structurants sélectionnés par le Dirigeant, chacun passé à l'orchestrateur puis validé humainement (validation tracée, un commit par correction).*

---

## M01 produits

1. **`pipeline/analyses/M01_BORNE_PRESENTATION_20230110_AUTO_v1/`** — déclaration Borne du 10 janvier 2023 (T0-ADOPTION-03). Source : `pipeline/source_texts/borne_20230110.txt`.
2. **`pipeline/analyses/M01_BORNE_493_20230316_AUTO_v1/`** — engagement de responsabilité 49.3 du 16 mars 2023 (T0-ADOPTION-04, verbatim certified). Source : `pipeline/source_texts/borne_20230316_493.txt`.

Les deux ont validé (`✓ Validation réussie`) sans réinjection (4 appels d'agent chacun, un par étape du pipeline — Charité, Vulnérabilités, Chaînes causales, Synthèse — aucun échec de schéma Pydantic nécessitant une seconde passe).

## Régime T0 strict — confirmation

Vérification mécanique effectuée sur les deux YAML produits : tous les champs `date_fait`/`date_connaissance` portent soit une date ≤ 2023-06-30, soit `non_documente`. Un seul cas de date antérieure à retenir avec attention méthodologique : dans le M01 du 49.3, `date_fait: '1990-11-15'` (unit u1) réfère à la citation historique de Michel Rocard mobilisée *par Borne elle-même dans le discours* — ce n'est pas une source externe injectée par le pipeline mais un fait cité à l'intérieur du texte source fourni, correctement daté par l'agent Charité. **Aucune assertion ne cite une source d'analyse (au sens d'un document utilisé comme preuve) postérieure au 30 juin 2023** dans les deux M01. Régime T0 confirmé.

## Diff machine → humain, par discours

### M01 #1 — Borne, 10 janvier 2023

**Une correction retenue** (commit `3a26b7e`) : le terme « carrières hachées » était classé `handling: quoted` dans `borrowed_terms_handled` alors qu'il n'apparaît entre guillemets ni dans le texte source fourni ni dans le corpus T0 d'origine (source dégradée, résumé de couverture journalistique, `execution_mode: applicable_degraded` — explicitement signalé au pipeline). Reclassé `attributed`, cohérent avec le traitement du terme voisin « concertation étendue ». Le reste de l'analyse (10 unités, omissions, vulnérabilités, synthèse épistémique) a été jugé correctement hedgé compte tenu du statut dégradé de la source — aucune autre correction retenue.

### M01 #2 — Borne, 49.3, 16 mars 2023

**Une correction retenue** (commit `9b98a36`) : `source.integrity_status` était fixé à `uncertain` par défaut de l'orchestrateur (valeur automatique appliquée à toute ingestion, indépendamment du statut réel de la source). Relevé à `certified`, cohérent avec le statut déjà établi de T0-ADOPTION-04 (lecture directe et intégrale du compte rendu officiel, sans résumé intermédiaire — voir `corpus/dossier_zero/T0/2023-03-16_borne-declaration-49-3.md`). Contenu substantiel (6 unités, dont un sophisme classé `certain` — glissement du jugement de valeur « cette réforme est nécessaire » présenté comme fait établi — et 4 hypothèses concurrentes en zone d'indétermination) jugé rigoureux, sans autre correction nécessaire.

**Aucun des deux M01 n'a nécessité de correction substantielle du contenu analytique** (unités, vulnérabilités, chaînes causales, hypothèses) — dans les deux cas, la seule correction portait sur un champ de métadonnées (statut d'un terme, statut d'intégrité de la source), pas sur le raisonnement du pipeline lui-même. C'est une donnée en soi pour la mesure 1 : la qualité de production automatique semble haute sur ces deux passes, au moins pour ce type de discours institutionnel structuré.

## Temps par poste (mesure 1) — donnée et limite méthodologique explicite

**Production automatique (donnée fiable, horodatage des logs d'agents)** :
- M01 #1 : 17:41:44 → 17:44:56 UTC = **3 min 12 s** (4 appels d'agent).
- M01 #2 : 18:13:21 → 18:16:05 UTC = **2 min 44 s** (4 appels d'agent).

**Validation humaine — limite méthodologique à signaler explicitement avant tout chiffre.** La validation de ce lot a été effectuée par l'Implementer (moi), pas par un humain. Le temps écoulé entre la fin de production et le commit de correction pour chacun des deux M01 (environ 9 minutes pour le premier, environ 59 minutes pour le second, mesurés par horodatage de commit) **ne constitue pas une mesure valide du temps de validation humaine** — il reflète un mélange de temps de lecture/raisonnement de l'IA, de latence de session, et d'autres facteurs propres à l'exécution d'un agent conversationnel, sans rapport démontrable avec l'effort cognitif qu'un relecteur humain consacrerait à la même tâche. **La mesure 1 du plan (chiffrage de la boucle humaine, §C.5) requiert une validation effectuée et chronométrée par un humain réel** — le Dirigeant ou un lecteur externe — pour produire une donnée exploitable. Présenter le temps de session de l'Implementer comme un proxy de ce chiffre serait une invention déguisée en mesure ; je m'en abstiens explicitement.

**Recommandation** : si la mesure 1 doit être établie sur ces deux M01, elle nécessite une relecture humaine indépendante, chronométrée séparément, des deux fichiers `*_AUTO_v1.yaml` produits ici (avant ou après les deux corrections déjà appliquées, selon ce que le Dirigeant souhaite isoler — temps de relecture pure vs. temps incluant la correction).

## Frictions et notes techniques

- **Environnement** : `orchestrateur.py` nécessite Python ≥ 3.10 (README §6.1) ; l'interpréteur `python3` par défaut de la machine est en 3.9.6, remplacé par `python3.11` (Homebrew) pour l'exécution des deux passes.
- **Naming** : les deux analyses suivent la convention `METHODE_LOCUTEUR_DOCUMENT_DATE_vX_Y` (`conventions.md` §2.3) avec le suffixe `_AUTO_v1` observé sur un exemple antérieur (`M01_LECORNU_DPG_20251014_AUTO_v1`) pour distinguer sortie brute et version promue. **Aucune promotion vers un nom court validé (ex. `borne_493_v2_1.yaml`, sur le modèle de `lecornu_v2_1.yaml`) n'a été faite** — cette convention de promotion n'étant pas documentée explicitement dans `conventions.md`, je ne l'ai pas inventée ; les fichiers restent dans leur répertoire `_AUTO_v1/` d'origine, corrigés sur place. À trancher par l'Architecte/Dirigeant si une promotion est souhaitée.
- **Erreur de discipline signalée** : le fichier RN de B.2-ter (`2023-05-03_rn-proposition-loi-retraites.md`) avait été écrit mais pas commité en temps voulu lors du lot précédent — rattrapé en tout début de ce lot (commit `c42ba39`) avant de démarrer la production M01, par souci de ne pas laisser un gap de discipline non signalé.

## Modifications de code / documents

- `pipeline/source_texts/borne_20230110.txt`, `pipeline/source_texts/borne_20230316_493.txt` — nouveaux, textes source préparés pour l'orchestrateur.
- `pipeline/analyses/M01_BORNE_PRESENTATION_20230110_AUTO_v1/` — nouveau (YAML + logs d'agents), une correction appliquée.
- `pipeline/analyses/M01_BORNE_493_20230316_AUTO_v1/` — nouveau (YAML + logs d'agents), une correction appliquée.
- `.claude/logs/log_session_003_lot_C1.md` — cette note.

Lot C.1 clos sur cet état : les deux M01 demandés sont produits et validés, chaque correction est un commit distinct et lisible, le régime T0 est confirmé mécaniquement. La mesure 1 (temps humain) reste à établir par une validation humaine réelle — non simulée par l'Implementer. Arrêt conforme à l'instruction.
