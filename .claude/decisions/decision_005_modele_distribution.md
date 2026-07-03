# Décision 005 — Modèle de distribution

*Décision structurante Phase 0 du codage. Prise en délibération avec sparring partner (Claude.ai, Mode Architecte/sparring). Référence : `plan_action_001.md` §4.5. Append-only — toute révision fera l'objet d'une nouvelle décision référençant celle-ci.*

*Méta-information.*
- Date de décision : 3 juillet 2026.
- Décideur : Seb (Dirigeant).
- Statut : validée.
- Décisions liées : matérialise le mécanisme juridique établi par la décision 004 (tri-partition, AGPL + copyright unique → double licence Mode 2) ; hérite du prérequis git des décisions 002 et 003.

---

## 1. Contexte

L'Entité s'adresse à trois publics selon trois modes doctrinaux : analystes (Mode 1, éclairage médiatique), distribution restreinte sous contrat (Mode 2, conseil), chat public (Mode 3, reporté doctrinalement). La décision 004 a établi la tri-partition des licences : spec/gabarit en Apache 2.0/CC BY 4.0, moteur en AGPL-3.0 à copyright unique, analyses en CC BY-SA 4.0. Le plan d'action 001 recommandait la distribution duale en la datant vaguement (« code source public Phase 2+ »). Par ailleurs, l'audit de l'arborescence (juillet 2026) a constaté l'absence de dépôt git — en contradiction avec la doctrine de traçabilité.

## 2. Problème

Le choix du modèle (dual) étant pré-tranché par la 004 et par le rejet doctrinal du closed transitoire, le problème résiduel est le séquencement : quand le code devient-il public, sous quelles conditions vérifiables, et dans quel ordre s'articulent création du repo, publication du cœur et ouverture commerciale du Mode 2 ? Une « Phase 2 » non définie expose à deux risques symétriques : publier trop tôt (moteur d'analyse d'acteurs nommés exposé sans verrou juridique de responsabilité éditoriale, méthode non éprouvée sur cas clos) ou repousser indéfiniment (dérive closed de fait, contraire à l'engagement de transparence).

## 3. Options examinées

**Option A — Open source complet immédiat.**
Alignement philosophique maximal, mais publie avant le verrou juridique (responsabilité éditoriale non traitée — insuffisance identifiée du cadrage §15.6) et avant la preuve méthodologique (dossier zéro rétrospectif non livré). Exposerait le projet à sa première contestation publique sans défense. Écartée.

**Option B-floue — Distribution duale, publication « Phase 2+ »** (formulation du plan).
Le bon modèle, mais sans critère vérifiable de passage public : la décision resterait à reprendre. Écartée au profit d'une version jalonnée.

**Option B-jalonnée — Distribution duale à trois jalons conditionnels** (retenue).
Repo privé immédiat ; passage public du cœur conditionné à deux critères vérifiables ; ouverture commerciale Mode 2 postérieure au passage public. Détail au §5.

**Option C — Closed transitoire.**
Rejetée par le plan d'action 001 lui-même : incompatible avec la philosophie du projet. Rejet confirmé.

## 4. Critères de décision

- Alignement philosophique : transparence et auditabilité publique comme engagement, non comme slogan — le service commercial ne précède pas l'auditabilité du moteur.
- Gestion du risque juridique : pas de publication d'un outil d'analyse d'acteurs nommés avant traitement de la responsabilité éditoriale.
- Preuve avant exposition : le dossier zéro rétrospectif comme actif de crédibilité conditionnant toute ouverture.
- Critères de jalons vérifiables (gating explicite), conformément à la pratique de pilotage du portefeuille.
- Cohérence avec la décision 004 (le mécanisme de double licence exige le copyright unique, donc le CLA avant toute contribution externe).

## 5. Décision retenue

**Option B-jalonnée** — distribution duale séquencée en trois jalons :

**Jalon 1 — Privé structuré** (immédiat, phase d'hygiène). Création du dépôt `atelier-atlani/lentite` privé, intégrant l'arborescence canonique assainie. Accès : Dirigeant + co-dirigeant, ce dernier sous CLA préalable à toute contribution sur le périmètre AGPL (condition bloquante héritée de la décision 004 §7). Ce jalon résout l'absence de git constatée à l'audit.

**Jalon 2 — Passage public du cœur.** Conditionné à la satisfaction conjointe de deux critères vérifiables :
- (a) dossier zéro rétrospectif (cas clos) livré, validé au pipeline, et relu par au moins deux lecteurs externes ;
- (b) relecture juridique de la responsabilité éditoriale effectuée (consultation droit de la presse : régime de signature, procédure de contestation, exposition diffamation/RGPD) et section correspondante ajoutée à la charte.

Le périmètre spec/gabarit (Apache 2.0/CC BY) peut passer public dès le jalon 2, ou avant si une opportunité de diffusion du standard se présente — décision légère à consigner au journal, sans réouverture de la présente décision.

**Jalon 3 — Ouverture commerciale Mode 2.** Contrats de service sur licence commerciale séparée, ouverts seulement après le jalon 2. Motif : vendre un service adossé à un moteur non publiquement auditable contredirait la promesse constitutive du projet et fragiliserait la position commerciale elle-même (la transparence du cœur est l'argument de vente du Mode 2).

Le Mode 3 (chat public) demeure hors scope de la présente décision, conformément à son report doctrinal.

## 6. Motif principal

La dualité sans jalons est une intention ; avec jalons, c'est un engagement pilotable. Les deux conditions du jalon 2 traitent les deux seuls risques réels de la publication (contestation juridique, méthode non éprouvée), et l'ordre jalon 2 → jalon 3 inscrit dans la distribution ce que la doctrine affirme : l'auditabilité précède la monétisation. Le séquencement transforme par ailleurs une constatation d'audit (absence de git) en première étape du modèle de distribution — l'hygiène devient le jalon 1.

## 7. Conditions de révision

- **Opportunité de financement par subvention/fondation** couvrant les coûts du projet : réexamen vers l'option A (open source complet) — prévue par le plan d'action 001 comme alternative conditionnelle.
- **Échec durable du jalon 2** (impossibilité de livrer le dossier zéro sous douze mois, ou blocage juridique substantiel) : réexamen du séquencement, sans que le closed permanent devienne une option (rejet doctrinal maintenu).
- **Opportunité standard anticipée** : la publication anticipée du seul périmètre spec/gabarit est déjà autorisée au §5 (décision légère au journal) — elle ne constitue pas une révision.
- **Signal de fork hostile ou de capture après passage public** : évaluation des contre-mesures dans le cadre AGPL (enforcement) — nouvelle décision si dépassement du cadre existant.

## 8. Conséquences immédiates

- La phase d'hygiène (git init, purge des doublons, README resynchronisé) devient formellement le jalon 1 du modèle de distribution — à exécuter en priorité, prérequis commun aux décisions 002, 003 et 005.
- Le CLA co-dirigeant doit être rédigé avant sa première PR — à inscrire à `plan_action_002.md` ou en tâche parallèle légère.
- Les critères du jalon 2 activent deux chantiers déjà identifiés à la reprise : dossier zéro rétrospectif (chantier central) et consultation juridique responsabilité éditoriale.
- `plan_action_002.md` : le prototype se développe en privé (jalon 1) ; aucune contrainte de publication ne pèse sur la Phase 0-1.
- Inscription au journal méthodologique général comme entrée 8.10 (numérotation du plan d'action 001 §6).

---

*Décision 005 v1.0 — 3 juillet 2026. Append-only.*
