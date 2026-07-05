# Revue 002 — Phase 0 (plan_action_002)

*Mode opérationnel : Reviewer (Claude.ai). Pièces examinées : `rapport_implementation_002.md`, notes de lots 0.x/1.x/2.x, journal méthodologique, résultats d'audits, logs du lot 2.7. Destinataires : Dirigeant, puis Mode Architecte (plan_action_003).*

*Date : 5 juillet 2026.*

---

## 1. Verdict d'ensemble

**Phase 0 substantiellement réussie, non close.** Sur les huit critères d'acceptation du plan : trois satisfaits (licences, gabarit durci + corpus revalidé, pipeline outillé), trois partiels (repo/onboarding, gouvernance/CLA, journal), deux non satisfaits (YAML automatique validé, étalonnage). Les deux critères manquants partagent une cause racine unique, identifiée, corrigeable en une session. **Décision de revue : la Phase 0 ne se clôt pas sur critères partiels — un lot correctif 2.8 est prescrit** (§4). Motif : l'étalonnage n'est pas un ornement, c'est la donnée qui dimensionne le dossier zéro (qualité de la production automatique = combien d'heures humaines par dossier) ; le clore maintenant reviendrait à ouvrir la Phase 1 en aveugle sur le paramètre principal de son estimation.

La conduite d'exécution est saluée : trois rendements empiriques produits avant tout dossier réel, aucun arbitrage silencieux détecté sur l'ensemble des lots, comptabilité API tenue avec sentinelle `non_documente` sur les mesures manquantes plutôt qu'estimation — la discipline d'invention zéro appliquée à la comptabilité elle-même est exactement l'esprit du gabarit.

## 2. Lecture des trois rendements empiriques

**2.1 — Asymétrie de datation (21/36).** Confirmée comme donnée méthodologique de premier ordre : le flux médiatique date les événements, pas les processus. Statut : acquise, publiable (note courte, corpus anonymisé, calage jalon 2). Aucune action Phase 1 requise au-delà de la rédaction.

**2.2 — Alerte intentionnalité (80–83%).** Deux hypothèses concurrentes documentées : (a) biais réel de l'analyste, capté par son propre instrument ; (b) artefact de composition — M01 analyse des discours, objets intentionnels par nature. **Prescription de revue : interdiction de retoucher le corpus ou les seuils pour éteindre l'alerte** (Goodhart auto-appliqué). Test discriminant : le dossier zéro, dont les chaînes causales porteront sur effets et processus — si le taux persiste, (a) l'emporte. L'alerte est gelée en l'état, datée, réexamen inscrit d'office à la revue du dossier zéro.

**2.3 — Échec YAML du lot 2.7.** Requalification par la revue : le rapport parle de « formatting slips » ; trois occurrences indépendantes d'une même classe d'erreur (deux-points/guillemets en scalaire non quoté, prose analytique française) sur deux passes ne sont pas du bruit — c'est un **conflit structurel prose-riche/YAML-nu**. La recommandation « discipline de quotage dans les prompts » est requalifiée en atténuation optionnelle, non en correction. Correction structurelle adoptée : **sortie structurée JSON par les agents, conversion mécanique JSON→YAML par l'orchestrateur**. Le YAML demeure le format de la source de vérité humaine (décisions 002/003 inchangées) ; le JSON devient le format d'échange machine. Ceci est un détail d'implémentation de la décision 001, pas une révision : consigné ici, pas de nouvelle décision structurante requise.

## 3. Arbitrages sur les points remontés sans tranche

**3.1 — Critère de sortie de séquence 2.** Tranché : non satisfait, lot correctif prescrit (§4). L'Implementer a eu raison de ne pas l'arbitrer.

**3.2 — Écart §9 séquence 0 (test d'onboarding par tiers indépendant).** Le rapport le note irrésolu ; le Dirigeant a affirmé en cours de phase que le re-test a été passé. Divergence de trace, pas nécessairement de fait. Prescription : si un rapport de re-test par session vierge existe, l'entrée de clôture de séquence 0 est écrite avec sa référence et sa date, point final ; s'il n'existe pas de trace, le test est réputé non fait — dix minutes en session vierge, consigne inchangée, avant la première session du co-dirigeant. La règle générale en découle : **une affirmation sans trace ne clôt pas un critère** — c'est le projet appliqué à lui-même.

**3.3 — CLA.** État : v0.1 non validée ; amendements v0.2 demandés par l'Architecte (mécanisme cession/licence exclusive + license-back, cessibilité à structure, droits moraux, déclaration employeur). Prescription : la v0.2 et la validation du Dirigeant sont **bloquantes pour la première PR du co-dirigeant**, pas pour le lot 2.8 (exécuté par l'Implementer sous le régime actuel). Relecture juridique maintenue comme condition du jalon 2, couplée à la consultation responsabilité éditoriale.

**3.4 — Fusion de fragments (traitement spécial `units`).** Examiné : logique d'assemblage acceptable en l'état, à couvrir d'un test unitaire dédié au lot 2.8 (l'assemblage est le seul code de l'orchestrateur qui touche à la structure du contenu — il doit être le mieux testé).

## 4. Prescription — Lot 2.8 (correctif structurel + étalonnage)

Périmètre, une session :

1. **Sortie structurée JSON** : les quatre agents fonctionnels produisent du JSON (via le mécanisme de sortie structurée de l'API — output_config/tool-use selon l'état du SDK épinglé — sinon consigne de format stricte + parsing JSON). Adaptation des quatre prompts (le fragment de schéma cible devient un schéma JSON), version des prompts incrémentée.
2. **Conversion JSON→YAML** dans l'orchestrateur : mécanique, déterministe, avec sérialiseur forçant le quotage des chaînes contenant des caractères ambigus. Test unitaire sur l'assemblage (`units` inclus) et sur la conversion.
3. **Ré-exécution 2.7** sur `corpus/lecornu_dpg_20251014.md` — mêmes règles : ≤ 2 réinjections Synthèse, échec documenté recevable (mais un second échec structurel remonterait en révision d'architecture, pas en re-essai).
4. **`exports/etalonnage_001.md`** si un YAML valide : comparaison factuelle sortie automatique vs analyse canonique (objets, unités, chaînes, engagements V.3 et patterns, hypothèses, confidences vs grille) — sans jugement de conformité.
5. **Comptabilité API complète** de la passe, ajoutée au tableau du rapport 002 (addendum, append-only).

Critère de clôture de la Phase 0 : les huit critères du §3 du plan revisités ; les partiels résolus (3.2 trace onboarding, 3.3 explicitement reporté à la première PR sans bloquer la clôture) ; entrée journal de clôture de séquence 2 et de Phase 0.

## 5. Préparation de la Phase 1 (plan_action_003 — dossier zéro)

Le plan sera produit en Mode Architecte après clôture du 2.8. La revue fixe d'ores et déjà son cadre :

- **Objet** : premier dossier rétrospectif complet sur cas clos — M01 multi-acteurs + M03 + omissions formelles + hypothèses, confronté aux effets connus (test §22.2 du cadrage, critère §21.3 de la charte).
- **Décision d'entrée (Dirigeant, avec grille)** : choix du cas. Candidat sortant : loi Climat-Résilience 2021 (défrichée par `etape_0`, effets à 5 ans documentés — rapports HCC, bilans d'application). La grille de sélection (clôture temporelle, disponibilité du corpus, présence d'omissions et d'alternatives écartées, charge éthique gérable, existence d'un contrefactuel documenté) sera le premier livrable du plan.
- **Mesures embarquées** : chiffrage de la boucle humaine poste par poste (axe 8 — la comptabilité API du 2.7/2.8 en est l'amorce) ; protocole inter-annotateurs exécuté (onboarding du co-dirigeant *par* la calibration) ; test adversarial minimal (une source piégée au corpus) ; réexamen de l'alerte intentionnalité (§2.2).
- **Bornes** : moratoire doctrinal maintenu jusqu'à livraison ; toute friction en journal ; le dossier est relu par deux lecteurs externes (préfiguration du comité de lecture).

## 6. Gouvernance — actions Dirigeant en cours

| Action | Statut | Échéance |
|---|---|---|
| Validation CLA v0.2 | En attente (amendements demandés) | Avant première PR co-dirigeant |
| Trace du re-test onboarding (§3.2) | À produire ou à exécuter | Avant première session co-dirigeant |
| Choix du cas dossier zéro | À délibérer sur grille | Ouverture plan_action_003 |
| Consultation juridique (CLA + responsabilité éditoriale) | Programmée | Avant jalon 2 |

---

*Revue 002 v1.0 — 5 juillet 2026, Mode Reviewer. Emplacement cible : `.claude/reviews/revue_002.md`. Prochaine pièce attendue : note de fin de lot 2.8, puis clôture de Phase 0 et production de `plan_action_003.md` en Mode Architecte.*
