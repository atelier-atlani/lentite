# Log de session — plan_action_003, séquence B, lot {B.1}

*Mode opérationnel : Implementer. Plan référencé : `.claude/plans/plan_action_003.md` §5 (séquence B — constitution des corpus), sur la base de `decision_006_cas_dossier_zero.md`.*

---

## Préalable — classement de `decision_006_cas_dossier_zero.md`

Non explicitement demandé par l'instruction du lot, mais nécessaire à sa cohérence : `decision_006_cas_dossier_zero.md` n'était pas encore présent dans le dépôt (déposé par le Dirigeant dans `~/Downloads/`, retrouvé lors du micro-lot de rangement précédent puis relu ici). Classé dans `.claude/decisions/decision_006_cas_dossier_zero.md`, sans modification de contenu. Décision actée : **Option A — réforme des retraites 2023, arc complet** (conception → adoption → application → suspension), retenue contre les quatre candidats initiaux de `plan_action_003.md` §4 (Pinel, Climat & Résilience, ALUR, Élan) pour son pouvoir discriminant — verdict institutionnel non écrit, contrairement à Pinel. Bornage T0 : `date_connaissance ≤ 2023-06-30`.

## Tâches accomplies

**Liste des sources candidates du corpus T0** — `corpus/dossier_zero/candidats_T0_lot_B1.md` (nouveau). 29 sources réparties en trois catégories reprenant exactement le découpage de la décision 006 et de l'instruction du lot :

- **Amont documentaire (8 sources)** — rapport Delevoye 2019, projet de loi et étude d'impact de la réforme par points 2019-2020, volet pénibilité, conférence de financement (lancement et issue), deux rapports annuels du COR (2021, 2022).
- **Séquence d'adoption (19 sources)** — conférence de presse et dossier de presse du 10 janvier 2023, premier communiqué intersyndical, PLFRSS et son étude d'impact, avis du Conseil d'État, prises de parole syndicales majeures (CFDT/CGT), débats parlementaires, engagement de responsabilité du 49.3 (16 mars), deux motions de censure et intervention d'opposition majeure au débat du 20 mars, trois saisines du Conseil constitutionnel (députés, sénateurs, Président de la République), décision 2023-849 DC, décision(s) sur le référendum d'initiative partagée, loi promulguée.
- **Réactions immédiates post-promulgation (5 sources)** — déclaration de la Première ministre, communiqué intersyndical, couverture de presse recoupée de la soirée du 14 avril, mobilisation du 1er mai, réactions des oppositions.

Pour chaque source : type (typologie à cinq entrées de `doctrine/V2.1/lentite_politique_corpus_v1.md`), provenance, accessibilité, `date_fait`/`date_connaissance`. Sous le plafond de 30 sources fixé pour la première passe.

**Aucune ingestion.** Conformément à l'instruction explicite du lot — la liste est un objet de délibération, pas un corpus constitué. Aucun fichier n'est créé dans `corpus/dossier_zero/T0/` (réservé à la tâche B.2, après arbitrage).

## Discipline d'invention appliquée à une liste, pas encore à un corpus

Treize entrées portent une date marquée « à vérifier avant ingestion » (jour exact d'un dépôt, mois exact d'une publication COR, numéro et date d'une décision RIP dont ma confiance est modérée) — signalé explicitement plutôt que présenté avec une précision que je ne peux pas garantir à ce stade. Aucune date n'est inventée ; là où ma connaissance générale ne suffit pas à une précision au jour près, je le dis. La vérification effective revient à la constitution du corpus (B.2), contre la source primaire elle-même.

Un point d'attention est signalé sans être résolu : aucune source de la liste ne documente à elle seule, au niveau de détail qu'exige une omission qualifiée (bloc durci, tâche 1.1 séquence 1), le pouvoir d'agir non exercé sur la conférence de financement — un travail de sourcing plus fin sera nécessaire à B.2 si cette omission doit être assertée avec les quatre champs requis.

## Modifications de code / documents

- `.claude/decisions/decision_006_cas_dossier_zero.md` — classé (préalable, non demandé explicitement mais nécessaire).
- `corpus/dossier_zero/candidats_T0_lot_B1.md` — nouveau, liste seule.

## État du système

Lot B.1 exécuté au sens de son livrable propre (liste de sources candidates) — mais la lettre du plan (§5 : « B.1 : périmètre et T0/T1 fixés en décision 006 ; politique de corpus v1 appliquée ») a son volet « périmètre et bornage » déjà réglé par la décision 006 elle-même (§5 de cette décision) ; ce lot complète B.1 par la matière première (candidats) que B.2 constituera en corpus effectif. Séquence B non close — reste B.2 (constitution effective, un commit par source ou lot cohérent), B.3 (corpus T1, scellé), B.4 (source piégée, insérée par le Dirigeant sans en informer l'Implementer).

## Recommandations pour la suite

- **Arbitrage du Dirigeant attendu avant B.2** — validation ou retrait de chaque entrée, tranchage des choix multiples (intervenant syndical CFDT vs CGT à retenir en priorité, intervenant d'opposition au débat du 20 mars), confirmation des dates marquées incertaines.
- **B.4 (source piégée)** — rappel de la discipline du plan : à insérer par le Dirigeant seul, non annoncée, sans consigner au journal avant la séquence E. Cette liste ne préjuge d'aucune insertion de ce type — elle ne recense que des sources réelles et publiques.
- **Sous-périmétrage éventuel** (décision 006 §7) — si le corpus effectif dépasse ~50 sources après sélection fine des débats parlementaires (B9) ou des interventions syndicales/oppositions multiples, resserrer sur une fenêtre plus étroite (ex. janvier-avril 2023) reste une option légère au journal, pas une réouverture de la décision 006.

## Correctif — recomptage et élagage (même lot, tour suivant)

**Friction constatée.** La synthèse de `candidats_T0_lot_B1.md` annonçait 29 sources et 6 dates à vérifier ; le compte réel du corps du document était 32 sources et, après une première correction encore approximative, s'est avéré être 14 dates à vérifier (une entrée, B3, avait été omise deux fois de suite avant d'être trouvée par un script de vérification colonne par colonne plutôt que par relecture visuelle). Trois erreurs de dénombrement successives sur le même document — matière suffisante pour une convention dédiée plutôt qu'une simple correction ponctuelle.

**Élagage à 30 (arbitrage du Dirigeant, option b).**
1. Fusion des deux motions de censure du 20 mars 2023 (LIOT + RN), même événement institutionnel, en une entrée.
2. Retrait du rapport COR 2021, redondant avec le rapport COR 2022 conservé (poste identique — bilan annuel du COR — et c'est le rapport de 2022 qui est effectivement mobilisé dans le débat public de janvier 2023, pas celui de 2021) ; signalé explicitement avec motif, comme demandé, plutôt que fait silencieusement.

État final vérifié mécaniquement (script Python, comptage par colonne de tableau, pas par relecture) : **30 sources, 13 dates à vérifier** — reproductible, chiffres inscrits dans la synthèse du document lui-même.

**Convention nouvelle.** `.claude/context/conventions.md` §6.10 (discipline de recomptage des synthèses) — tout décompte de synthèse est recompté au moment de l'écriture, plus jamais reporté par mémoire. Motivée explicitement par cette friction.
