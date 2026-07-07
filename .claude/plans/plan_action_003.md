# Plan d'action 003 — Phase 1 : le dossier zéro rétrospectif

*Troisième plan d'action du workflow `.claude/`. Produit en Mode Architecte (Claude.ai) après clôture de la Phase 0 (journal, entrée de clôture plan_action_002) et sur le cadre fixé par `revue_002.md` §5. Le dossier zéro est le juge de paix de la méthode : premier dossier complet sur cas clos, confronté aux effets connus.*

*Méta-information.*
- Date de production : 5 juillet 2026.
- Mode opérationnel : Architecte.
- Modes cibles d'exécution : Dirigeant (décision 006, corpus, arbitrages, validation humaine), Implementer Claude Code (production machine, mesures), co-dirigeant (calibration inter-annotateurs = onboarding), deux lecteurs externes (séquence finale).
- Plans référencés : plan_action_002 (clos), revue_002.
- Critère de réussite global : charte §21.3 — le dossier est plus vérifiable, plus proportionné et plus attaquable proprement qu'un bon article de synthèse sur le même cas.

---

## 1. Contexte

Le prototype est opérationnel : gabarit durci, pipeline quatre agents en sortie structurée, premier YAML automatique validé, étalonnage produit (lot 2.9). Trois rendements empiriques attendent leur test : l'asymétrie de datation 21/36, l'alerte intentionnalité 80–83% (gelée — test discriminant : ce dossier), et la discipline `not_yet_observed` observée en production. Le coût machine d'une passe M01 est établi (~1–2 $) ; le coût humain d'un dossier est l'inconnue principale — ce plan le mesure.

Le dossier zéro répond à la question que tout le reste présuppose : **la méthode voit-elle juste sur un cas dont on connaît la fin ?**

## 2. Objectif

Produire un dossier d'enquête complet (M01 multi-acteurs + M03 + omissions formelles + hypothèses hiérarchisées) sur un **cas de politique publique clos**, en régime bitemporel strict (analyse sur corpus clos à T0, confrontation sur corpus T1), avec quatre mesures embarquées, et le soumettre à deux lecteurs externes contre le critère §21.3.

## 3. Le principe méthodologique central : la double clôture bitemporelle

Le test rétrospectif n'a de valeur que si l'analyse ne « connaît pas la fin ». Le plan impose donc deux corpus clos, exploitant la bitemporalité implémentée en séquence 1 :

- **Corpus T0** : sources antérieures à une date de coupure T0 (l'époque de la décision analysée). La production du dossier (M01, M03, hypothèses, omissions, prédictions implicites des chaînes aval) se fait **exclusivement** sur ce corpus. Toute source du corpus T0 porte `date_connaissance ≤ T0`.
- **Corpus T1** : sources postérieures documentant les effets connus (rapports d'évaluation, bilans d'application, jurisprudence, données). Il n'entre en jeu qu'à la séquence de confrontation.
- **Règle de contamination** : l'analyste humain vivant en 2026 connaît la suite — c'est inévitable. La discipline est procédurale : aucune assertion du dossier T0 ne peut citer une source T1 ; le validateur le vérifie mécaniquement sur `date_connaissance`. La contamination cognitive résiduelle est déclarée au poste d'observation du dossier. Le pipeline automatique, lui, est authentiquement naïf (il ne reçoit que T0) — d'où une comparaison inédite : l'humain qui sait contre la machine qui ne sait pas.

## 4. Séquence A — Décision 006 : choix du cas

**Livrable : `decision_006_cas_dossier_zero.md`** (format huit sections, décision du Dirigeant, sparring disponible).

**Grille de sélection** (critères pondérés) :
1. *Clôture temporelle* (25%) — la politique a produit ses effets principaux ; T1 dispose d'évaluations institutionnelles publiées.
2. *Corpus T0 disponible et borné* (25%) — débats parlementaires, études d'impact, positions d'acteurs, couverture presse : accessibles, 20–50 sources, sans mur payant majeur.
3. *Richesse en objets du gabarit* (20%) — écarts dit/fait plausibles, alternatives écartées documentées (amendements rejetés, avis ignorés), omissions candidates (pouvoirs d'agir non exercés).
4. *Charge éthique gérable* (15%) — pas de victimes directes nommées, pas de contentieux pénal en cours ; acteurs = responsables publics dans leurs fonctions.
5. *Capacité de vérification du Dirigeant* (15%) — expertise de domaine permettant de juger la machine au fond, pas seulement en forme.

**Candidats à passer à la grille** (liste ouverte, le Dirigeant peut en ajouter) :
- **Loi Climat & Résilience (2021)** — candidat sortant, défriché par `etape_0` ; T1 riche (rapports HCC, bilans annuels) ; corpus vaste (risque : trop vaste — prévoir un sous-périmètre, ex. le volet rénovation énergétique, qui recoupe l'expertise immobilière du Dirigeant).
- **Loi ALUR (2014)** — encadrement des loyers : effets à 10+ ans documentés, alternatives écartées abondantes, expertise Dirigeant maximale (bailleur), acteurs nombreux ; T0 ancien = presse moins accessible en ligne.
- **Dispositif Pinel (2014–2024)** — cas remarquable : politique *close par extinction*, évaluations officielles sévères publiées (Cour des comptes, IGF) ; écart déclaré/produit quasi archétypal ; périmètre naturellement borné.
- **Loi Élan (2018)** — périmètre moyen, effets partiellement documentés, expertise Dirigeant forte.

Recommandation préliminaire d'Architecte : **Pinel** coche la grille de façon presque suspecte (clos par extinction, évaluations officielles à charge, périmètre borné, expertise maximale du Dirigeant, corpus T0 accessible) — avec un defeater à instruire : son caractère « cible facile » (l'échec du dispositif est notoire) réduit-il la valeur démonstrative ? Contre-argument : le test §21.3 ne demande pas de surprendre, il demande d'être *plus attaquable proprement* qu'une synthèse — et un cas notoire permet justement aux lecteurs externes de juger. À délibérer en décision 006.

## 5. Séquence B — Constitution des corpus

- B.1 : périmètre et T0/T1 fixés en décision 006 ; politique de corpus v1 appliquée (typologie, fiabilité déclarée, règle d'extension tracée).
- B.2 : corpus T0 constitué dans `corpus/dossier_zero/T0/` — 20 à 50 sources, front matter complet (type, provenance, intégrité, date_fait/date_connaissance), un commit par source ou par lot cohérent.
- B.3 : corpus T1 constitué dans `corpus/dossier_zero/T1/`, scellé (non lu par le pipeline avant la séquence D).
- B.4 — **test adversarial (mesure 3)** : le Dirigeant insère dans le corpus T0, sans en informer l'Implementer ni le consigner au journal avant la séquence E, **une source piégée** (document plausible contenant une instruction d'injection et/ou un fait forgé contradictoire avec une source fiable). Le journal reçoit une entrée scellée a posteriori. Critères de réussite : l'injection n'exécute rien ; le fait forgé est soit écarté, soit porté avec la contradiction documentée.

## 6. Séquence C — Production du dossier (régime T0 strict)

- C.1 : M01 automatiques sur les 3–5 discours structurants du cas (pipeline, corpus T0 seul), puis **validation humaine tracée** de chaque analyse — chaque correction humaine est un commit distinct : le diff machine→humain est une donnée (qualité de la production automatique, matière du chiffrage).
- C.2 : M03 comparatif multi-acteurs sur la séquence décisionnelle.
- C.3 : bloc omissions — pouvoirs d'agir non exercés, avec les quatre champs durcis et clôture de corpus T0 explicite.
- C.4 : synthèse du dossier — hypothèses concurrentes hiérarchisées, defeaters, degrés calibrés sur la grille v1 ; les chaînes causales aval valent **prédictions implicites** (consignées comme telles : c'est elles que T1 jugera).
- C.5 — **chiffrage de la boucle humaine (mesure 1)** : temps humain relevé par poste (constitution corpus, validation M01, M03, omissions, synthèse, arbitrages) — relevé simple par session, consolidé en fin de séquence. C'est la donnée qui décide artisanat vs produit.

## 7. Séquence D — Confrontation rétrospective

- D.1 : ouverture du corpus T1 ; pour chaque prédiction implicite et chaque hypothèse du dossier T0 : statut observé (confirmée / infirmée / indéterminée / non testable), sources T1 à l'appui — en **addendum daté**, jamais en réécriture du dossier T0 (append-only : le dossier T0 reste tel qu'il a été produit, c'est la condition du test).
- D.2 : patterns V.3 fixés sur T1 (observed_as_announced / broken_explicitly / etc.).
- D.3 : bilan de justesse : que voyait le dossier T0 que la synthèse de l'époque ne voyait pas ? Qu'a-t-il manqué ? Les omissions pointées se sont-elles avérées significatives ?
- D.4 — **réexamen de l'alerte intentionnalité (mesure 4)** : audits exécutés sur le graphe enrichi du dossier zéro ; le taux sur chaînes d'effets et de processus départage les hypothèses (a) biais d'analyste vs (b) artefact d'objet — résultat au journal, quelle qu'en soit l'issue.

## 8. Séquence E — Calibration, lectures externes, clôture

- E.1 — **calibration inter-annotateurs (mesure 2) = onboarding du co-dirigeant** : CLA signé au préalable ; il suit le parcours 02 §8, puis re-code en aveugle deux analyses du dossier (sans accès aux attributions) ; écart absolu mesuré selon le protocole v1 ; première donnée d'accord inter-annotateurs du projet.
- E.2 : révélation du test adversarial (B.4) — résultat documenté, entrée journal descellée.
- E.3 : deux lecteurs externes (profils distincts, hors projet) reçoivent le dossier + la question unique du §21.3 : *cette analyse est-elle plus vérifiable, proportionnée et attaquable proprement qu'un bon article de synthèse sur le même cas ?* Réponses recueillies verbatim, non négociées.
- E.4 : entrée journal de clôture de Phase 1 ; levée conditionnelle du moratoire doctrinal — les frictions accumulées en journal remontent en couches A/B pour instruire la v2.2 (nouveau cycle Architecte).

## 9. Critères d'acceptation

- [ ] Décision 006 documentée (huit sections, grille renseignée).
- [ ] Corpus T0/T1 constitués, conformes à la politique de corpus, source piégée insérée (scellée).
- [ ] Dossier T0 complet : 3–5 M01 validés, 1 M03, bloc omissions, synthèse — tous au pipeline, régime T0 vérifié mécaniquement.
- [ ] Confrontation T1 en addendum daté, bilan de justesse rédigé.
- [ ] Quatre mesures livrées : chiffrage humain par poste ; accord inter-annotateurs ; résultat adversarial ; réexamen intentionnalité.
- [ ] Deux lectures externes recueillies contre §21.3.
- [ ] Journal tenu, moratoire respecté jusqu'à E.4.

## 10. Anti-tâches

- *Ne pas réviser la doctrine* avant E.4 (le moratoire tient jusqu'à la clôture, précisément parce que ce dossier est son test).
- *Ne rien publier* — jalon 2 non atteint ; les lecteurs externes signent une réserve de confidentialité simple.
- *Ne pas optimiser le pipeline* (reprise sur artefacts, parallélisation…) sauf friction bloquante documentée — la Phase 1 mesure l'existant.
- *Ne pas étendre le périmètre du cas* en cours de route — toute tentation d'élargissement s'inscrit au journal et attend.
- *Ne pas lisser le dossier T0 après ouverture de T1* — l'append-only est la condition de validité du test.

## 11. Estimation

- Séquence A : 1 session de délibération (+ sparring éventuel).
- Séquence B : 3–5 sessions (le corpus est le vrai travail).
- Séquence C : 4–6 sessions (production + validation humaine — c'est ici que le chiffrage se joue).
- Séquence D : 2–3 sessions. Séquence E : 2 sessions + délais externes (lecteurs, co-dirigeant).
- Horizon réaliste : 4 à 6 semaines en créneaux, compatible PSQ/rentrée.
- Coût API estimé : 10–30 $ (M01 multiples + réinjections + audits) — à consolider au rapport.

## 12. Discipline d'exécution

Inchangée : une séquence à la fois, un lot = une session = commits propres, toute friction au journal, aucun arbitrage silencieux, l'Implementer ne décide rien de structurant. Nouveauté propre à ce plan : **le régime T0 prime sur tout** — en cas de doute sur la date de connaissance d'une source, elle est exclue de T0 (l'appauvrissement du corpus est un moindre mal que la contamination du test).

---

*Plan d'action 003 v1.0 — produit le 5 juillet 2026 par Mode Architecte. À placer dans `.claude/plans/plan_action_003.md`. Première étape : décision 006 (choix du cas) par le Dirigeant. Prochain plan attendu : plan_action_004 (révision doctrinale v2.2 post-moratoire ou industrialisation, selon le verdict du dossier zéro).*
