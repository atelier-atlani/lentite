# Note de fin de lot — plan_action_003, séquence B, lot B.2-bis

*Mode opérationnel : Implementer. Complément ciblé de lot B.2, trois sources demandées. Deux intégrées, une bloquée par une anomalie de fichier signalée ci-dessous plutôt que forcée.*

---

## 1. Étude d'impact PLFRSS 2023 — intégrée

`corpus/dossier_zero/T0/2023-01-23_etude-impact-plfrss-2023.md` (T0-ADOPTION-11), commit `dece8b0`.

Document de 175 pages, lecture **partielle et explicitement signalée** : introduction/sommaire, Article 1 (fermeture des régimes spéciaux, données chiffrées DSS) et Article 7 (relèvement de l'âge légal à 64 ans, rendement financier officiel chiffré : 270 M€ en 2023 puis 3,3 / 5,3 / 7,5 Md€ en 2024-2026) ont été lus intégralement. Les 8 autres articles (2, 3, 8-13 : indicateurs seniors, recouvrement, départs anticipés, usure professionnelle, petites pensions, formation, aidants, transitions) **n'ont pas été lus** — non résumés, non supposés. `url` non_documente (fichier remis sans URL). Intégrité `partial`.

**Point notable pour l'analyse en aval** : le rendement chiffré officiel de l'article 7 (7,5 Md€ à l'horizon 2026) est du même ordre de grandeur que la part que la note CAEPS (T0-CAEPS-2023-07) attribue elle-même au relèvement d'âge (« 8 à 10 Md€ à l'horizon 2030 ») — alors que la note CAEPS présente ce chiffre comme dérisoire face à son estimation du déficit total (148 Md€). La comparaison n'est pas tranchée ici, volontairement laissée à l'analyse en aval (M01/M03).

## 2. Verbatim du 49.3 de Borne (16 mars 2023) — **BLOQUÉ, non intégré, ne rien forcer**

`Ajout du dirigeant/verbatim_493_borne_20230316.pdf` a été lu intégralement (26 pages, en deux passes). **Ce document n'est pas le verbatim de la déclaration du 49.3.** C'est le compte rendu intégral de la **3e séance du jeudi 16 mars 2023** de l'Assemblée nationale, qui porte exclusivement sur un débat totalement différent : le projet de loi relatif à l'accélération des procédures liées à la construction de nouvelles installations nucléaires. La séance se déroule de 21h30 à 00h02, couvre des amendements sur le nucléaire (fermeture de Fessenheim, EPR, radioprotection, etc.), et se termine sur l'annonce de la séance suivante portant sur les Jeux olympiques 2024 — **aucune mention de Borne, du 49.3, de la réforme des retraites ou du PLFRSS nulle part dans les 26 pages.**

Je n'ai ni inventé un contenu de remplacement, ni supprimé la source existante (`2023-03-16_borne-declaration-49-3.md`, T0-ADOPTION-04, sourcée en B.2 via LCP avec ses limites déjà documentées — citations rendues en anglais par l'outil de récupération). **L'ancienne source reste en l'état, le remplacement n'a pas eu lieu.**

Deux hypothèses possibles, non tranchées ici — décision du Dirigeant nécessaire :
- **Mauvais fichier déposé par erreur** (confusion entre deux comptes rendus de séance du même jour — l'Assemblée a tenu plusieurs séances le 16 mars 2023, dont probablement une où le 49.3 a été annoncé, distincte de cette 3e séance).
- **Fichier intentionnel** (test de vigilance) — je n'ai pas de moyen de trancher entre les deux hypothèses et je ne dois pas présumer laquelle est la bonne.

**Action recommandée** : le Dirigeant peut redéposer le bon fichier (probablement un compte rendu d'une séance antérieure du même jour, ou une source `assemblee-nationale.fr` distincte couvrant spécifiquement l'annonce du 49.3), ou confirmer que la source LCP actuelle doit être conservée telle quelle.

## 3. Saisines du Conseil constitutionnel — contradiction résolue

`corpus/dossier_zero/T0/2023-03-21_2023-03-23_saisines-conseil-constitutionnel.md` (T0-ADOPTION-07, renommé depuis `2023-03-20_...`), commit `813de9c`.

Récupération ciblée directement sur la page de la décision 2023-849 DC, recoupée par une recherche indépendante — **les deux convergent** sur quatre saisines distinctes : Première ministre (21 mars), députés RN menés par Marine Le Pen (21 mars, même jour), députés de gauche menés par Mathilde Panot (22 mars), sénateurs menés par Patrick Kanner (23 mars).

**Contradiction B.2 résolue** : la mention du « 21 mars 2023 » déjà signalée comme contradiction non résolue dans le dossier législatif PLFRSS (T0-ADOPTION-01) correspond à un événement réel (la double saisine de ce jour), pas à une erreur de récupération — confusion entre date de saisine et date de décision (14 avril) dans la restitution automatisée d'origine, maintenant clarifiée.

**B15 (« saisine par le Président de la République »)** — **toujours non confirmée**, par aucune des deux sources de cette reprise. Statut inchangé depuis B.2 : gap constaté, pas une incertitude, `non_documente` maintenu.

Intégrité relevée `uncertain` → `partial` (deux sources indépendantes concordantes plutôt que contradictoires).

## État du corpus T0 consolidé (B.2 + B.2-bis)

**26 sources** dans `corpus/dossier_zero/T0/` : 25 issues de B.2, +1 nouvelle (étude d'impact, T0-ADOPTION-11). La correction des saisines (T0-ADOPTION-07) modifie une source existante sans en ajouter — total net +1 par rapport à la clôture de B.2.

Couverture des 30 candidats de `candidats_T0_lot_B1.md` : 17/30 désormais couverts avec un degré de confiance raisonnable (16 précédemment + B5, étude d'impact). B10 (49.3) reste comptée comme couverte au même niveau qu'à la fin de B.2 (source LCP, `uncertain`, limites déjà documentées) — **pas améliorée par ce lot**, le fichier destiné à la remplacer ne convenait pas.

Gap inchangé pour le reste (13 candidats non couverts, cf. `log_session_003_lot_B2_final.md` pour le détail complet) — non repris ici pour éviter la duplication.

## Modifications de code / documents

- `corpus/dossier_zero/T0/2023-01-23_etude-impact-plfrss-2023.md` — nouveau.
- `corpus/dossier_zero/T0/2023-03-21_2023-03-23_saisines-conseil-constitutionnel.md` — remplace et renomme `2023-03-20_2023-03-23_saisines-conseil-constitutionnel.md`.
- `corpus/dossier_zero/T0/2023-03-16_borne-declaration-49-3.md` — **inchangé**, remplacement non effectué faute de matériau valide.
- `.claude/logs/log_session_003_lot_B2bis.md` — cette note.

Lot B.2-bis clos sur cet état : 2 des 3 demandes traitées, 1 bloquée et signalée plutôt que forcée. Arrêt conforme à l'instruction — décision du Dirigeant nécessaire sur le point 2 avant toute nouvelle tentative.
