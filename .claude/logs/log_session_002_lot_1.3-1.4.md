# Log de session — plan_action_002, lot {1.3–1.4}

*Mode opérationnel : Implementer. Plan référencé : `.claude/plans/plan_action_002.md` §4 séquence 1.*

---

## Tâches accomplies

**1.3 — Politique de corpus v1.** Nouveau document `doctrine/V2.1/lentite_politique_corpus_v1.md` (CC BY 4.0, ~890 mots). Typologie à cinq types (officielle, journalistique, statistique, militante, académique) avec fiabilité déclarée par type — qualitative et contextuelle (pas de score unique), notamment renvoi explicite à `ConsensusLevel` déjà présent dans `pipeline/schemas.py` pour le type académique plutôt qu'une échelle parallèle. Règle d'extension tracée spécifiée (§3). Articulation explicite avec `cloture_corpus` du bloc omission durci de la tâche 1.1 (§4) — `corpus_declare` référence désormais les cinq types de cette politique, `date_cloture` sert de pivot à la règle d'extension.

**1.4 — Grille de calibration.** Nouveau document `doctrine/V2.1/lentite_calibration_confiance_v1.md` (CC BY 4.0, ~975 mots). Grille à quatre degrés (faible 0,00–0,39 / modéré 0,40–0,59 / fort 0,60–0,84 / établi 0,85–1,00) sur le score `confidence` existant. Cas-jouets 1, 5, 6 promus cas-étalons officiels, avec table de leurs valeurs de confidence réelles extraites de `analyses/cas_jouets/lentite_cas_jouets_1_5_6_v2_1.md` (vérifiées une à une contre la source). Protocole inter-annotateurs spécifié (§4) — sélection de deux analyses existantes (non fixées, arbitrage d'exécution), second annotateur aveugle aux attributions originales, écart absolu simple `|confidence_originale − confidence_second_annotateur|`, seuils de lecture proposés. Exécution explicitement non couverte par ce lot, conformément au plan.

## Frictions et choix d'implémentation signalés

1. **Terminologie « établi ».** Le degré qualitatif « établi » de la grille (1.4) risque de se confondre avec le statut épistémique « fait établi » de la charte v2.1 (catégorie distincte, non notée sur l'échelle 0–1). Un avertissement terminologique explicite a été ajouté en tête du document (§1) pour prévenir ce glissement — pas une révision de la charte, seulement une clarification dans le nouveau document.

2. **Type de front matter pour la règle d'extension tracée (1.3 §3).** Aucun des cinq types de front matter du journal (`décision`, `révision doctrinale`, `friction`, `audit`, `reprise` — `conventions.md` §6.9) ne nomme le cas « source ajoutée en cours d'enquête ». `audit` a été retenu par défaut dans le document comme le moins inexact, et le point est signalé comme ouvert dans le document lui-même plutôt que tranché comme une extension de convention — une extension de la typologie des types de front matter serait une décision relevant de l'Architecte/Dirigeant, hors périmètre de ce lot.

3. **Cas-étalons incomplets sur la bande basse.** Les trois cas-jouets 1/5/6 ne produisent aucune valeur de confidence dominante sous 0,40 — la bande « faible » de la grille (1.4 §2) n'a donc aucun cas-étalon a ce stade. Signalé explicitement dans le document (§3) comme limite déclarée, avec recommandation d'un cas-jouet supplémentaire pour une v2, non traitée ici.

4. **Journal méthodologique de M01 non instancié.** La règle d'extension tracée (1.3 §3) et l'avertissement terminologique (1.4 §1) renvoient tous deux au « journal méthodologique de M01 » (gabarit v2.1 section 16), qui n'existe pas comme fichier séparé dans le dépôt — seul `journal/lentite_journal.md` (journal général) est physiquement instancié. Documenté tel quel, pas de création de fichier non demandée par le plan.

## Modifications de code / documents

- `doctrine/V2.1/lentite_politique_corpus_v1.md` — nouveau.
- `doctrine/V2.1/lentite_calibration_confiance_v1.md` — nouveau.
- Aucune modification aux documents doctrinaux existants (charte, gabarit, méthodes, révisions) — moratoire respecté, ce sont deux documents nouveaux, pas des révisions.
- Aucune modification à `pipeline/schemas.py` ni aux YAML existants — ce lot est de la doctrine seule, pas du code.

## État des tests

Sans objet pour ce lot — pas de code modifié. Les deux documents sont des spécifications textuelles ; leur seule vérification possible à ce stade est la cohérence interne (valeurs de confidence recopiées et vérifiées contre `lentite_cas_jouets_1_5_6_v2_1.md`) et la conformité au périmètre du plan.

## État du système

Séquence 1 non close — reste 1.5 (revalidation intégrale du corpus + entrée journal de synthèse de clôture, seule entrée portant le critère de sortie §4 du plan). L'écart au §9 signalé au lot précédent (séquence 1 ouverte par anticipation, séquence 0 non formellement close) reste en l'état — non aggravé ni résolu par ce lot.

## Recommandations pour la suite

- Lot `1.5` : revalidation des 12 YAML sous le gabarit durci (1.1+1.2), entrée de synthèse de séquence, et décision explicite sur les trois points ouverts ci-dessus (type de front matter pour l'extension de corpus, cas-étalon manquant en bande faible, statut du journal méthodologique de M01).
- Suggestion hors périmètre de ce lot — ajouter une référence aux deux nouveaux documents dans la section 4 du README (« Documents canoniques v2.1.1 »), non faite ici pour respecter la discipline de lot minimal (le plan ne le demande pas explicitement en 1.3/1.4).

---

*Commits de ce lot : voir historique git, préfixe `docs(doctrine)` / `docs(logs)` / `docs(journal)`.*
