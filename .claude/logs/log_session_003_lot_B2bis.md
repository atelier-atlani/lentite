# Note de fin de lot — plan_action_003, séquence B, lot B.2-bis

*Mode opérationnel : Implementer. Complément ciblé de lot B.2, trois sources demandées. Deux intégrées, une bloquée par une anomalie de fichier signalée ci-dessous plutôt que forcée.*

---

## 1. Étude d'impact PLFRSS 2023 — intégrée

`corpus/dossier_zero/T0/2023-01-23_etude-impact-plfrss-2023.md` (T0-ADOPTION-11), commit `dece8b0`.

Document de 175 pages, lecture **partielle et explicitement signalée** : introduction/sommaire, Article 1 (fermeture des régimes spéciaux, données chiffrées DSS) et Article 7 (relèvement de l'âge légal à 64 ans, rendement financier officiel chiffré : 270 M€ en 2023 puis 3,3 / 5,3 / 7,5 Md€ en 2024-2026) ont été lus intégralement. Les 8 autres articles (2, 3, 8-13 : indicateurs seniors, recouvrement, départs anticipés, usure professionnelle, petites pensions, formation, aidants, transitions) **n'ont pas été lus** — non résumés, non supposés. `url` non_documente (fichier remis sans URL). Intégrité `partial`.

**Point notable pour l'analyse en aval** : le rendement chiffré officiel de l'article 7 (7,5 Md€ à l'horizon 2026) est du même ordre de grandeur que la part que la note CAEPS (T0-CAEPS-2023-07) attribue elle-même au relèvement d'âge (« 8 à 10 Md€ à l'horizon 2030 ») — alors que la note CAEPS présente ce chiffre comme dérisoire face à son estimation du déficit total (148 Md€). La comparaison n'est pas tranchée ici, volontairement laissée à l'analyse en aval (M01/M03).

## 2. Verbatim du 49.3 de Borne (16 mars 2023) — **repris et intégré après correction du fichier**

Premier dépôt bloqué (voir constat initial ci-dessous, conservé pour traçabilité) : `verbatim_493_borne_20230316.pdf` contenait par erreur le compte rendu de la 3e séance du 16 mars 2023 (débat sur un projet de loi nucléaire, sans rapport). Le Dirigeant a redéposé le bon fichier le 11 juillet — compte rendu intégral de la **2e séance du jeudi 16 mars 2023** (Journal officiel n°33 [2] A.N.), qui contient bien la déclaration d'engagement de responsabilité.

**Remplacement effectué** : `corpus/dossier_zero/T0/2023-03-16_borne-declaration-49-3.md` (T0-ADOPTION-04) réécrit intégralement à partir d'une lecture directe des 31 pages du document officiel — citation de Michel Rocard reprise par Borne, justification du recours au 49.3 (incertitude du vote, risque pour le compromis de CMP), formule d'engagement de responsabilité, confirmation procédurale de la présidente de séance, réactions immédiates en hémicycle. Remplace la version LCP (citations retraduites en anglais par l'outil de récupération). Intégrité relevée `uncertain` → `certified` (transcription directe d'un document officiel, pas de résumé par un outil intermédiaire).

*Constat initial (premier dépôt, avant correction) : le fichier lu ne contenait, sur ses 26 pages, aucune mention de Borne, du 49.3 ou des retraites — c'était le compte rendu d'une séance ultérieure du même jour, portant sur un tout autre texte. Signalé au Dirigeant plutôt que forcé ; correction reçue et traitée le jour même.*

## 3. Saisines du Conseil constitutionnel — contradiction résolue

`corpus/dossier_zero/T0/2023-03-21_2023-03-23_saisines-conseil-constitutionnel.md` (T0-ADOPTION-07, renommé depuis `2023-03-20_...`), commit `813de9c`.

Récupération ciblée directement sur la page de la décision 2023-849 DC, recoupée par une recherche indépendante — **les deux convergent** sur quatre saisines distinctes : Première ministre (21 mars), députés RN menés par Marine Le Pen (21 mars, même jour), députés de gauche menés par Mathilde Panot (22 mars), sénateurs menés par Patrick Kanner (23 mars).

**Contradiction B.2 résolue** : la mention du « 21 mars 2023 » déjà signalée comme contradiction non résolue dans le dossier législatif PLFRSS (T0-ADOPTION-01) correspond à un événement réel (la double saisine de ce jour), pas à une erreur de récupération — confusion entre date de saisine et date de décision (14 avril) dans la restitution automatisée d'origine, maintenant clarifiée.

**B15 (« saisine par le Président de la République »)** — **toujours non confirmée**, par aucune des deux sources de cette reprise. Statut inchangé depuis B.2 : gap constaté, pas une incertitude, `non_documente` maintenu.

Intégrité relevée `uncertain` → `partial` (deux sources indépendantes concordantes plutôt que contradictoires).

## État du corpus T0 consolidé (B.2 + B.2-bis)

**26 sources** dans `corpus/dossier_zero/T0/` : 25 issues de B.2, +1 nouvelle (étude d'impact, T0-ADOPTION-11). La correction des saisines (T0-ADOPTION-07) modifie une source existante sans en ajouter — total net +1 par rapport à la clôture de B.2.

Couverture des 30 candidats de `candidats_T0_lot_B1.md` : 17/30 désormais couverts avec un degré de confiance raisonnable (B5 étude d'impact ajoutée). B10 (49.3) reste comptée comme couverte, mais sa qualité de sourcing est nettement améliorée (`uncertain` → `certified`), désormais l'une des sources les plus fiables du corpus.

Gap inchangé pour le reste (13 candidats non couverts, cf. `log_session_003_lot_B2_final.md` pour le détail complet) — non repris ici pour éviter la duplication.

## Modifications de code / documents

- `corpus/dossier_zero/T0/2023-01-23_etude-impact-plfrss-2023.md` — nouveau.
- `corpus/dossier_zero/T0/2023-03-21_2023-03-23_saisines-conseil-constitutionnel.md` — remplace et renomme `2023-03-20_2023-03-23_saisines-conseil-constitutionnel.md`.
- `corpus/dossier_zero/T0/2023-03-16_borne-declaration-49-3.md` — réécrit intégralement, verbatim officiel remplace la version LCP.
- `.claude/logs/log_session_003_lot_B2bis.md` — cette note.

Lot B.2-bis clos sur cet état : les 3 demandes traitées (2 dès la première passe, la 3e après correction du fichier par le Dirigeant). Arrêt conforme à l'instruction.
