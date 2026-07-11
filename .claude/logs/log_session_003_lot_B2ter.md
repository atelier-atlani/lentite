# Note de fin de lot — plan_action_003, séquence B, lot B.2-ter

*Mode opérationnel : Implementer. Lot ciblé, déclenché par un inventaire par acteur demandé par le Dirigeant après B.2-bis, qui a révélé deux gaps réels (oppositions parlementaires mono-source, expertise/contrôle mono-source faute de COR).*

---

## Sources ingérées (4, un commit chacune)

1. **`2022-09-01_cor-rapport-annuel-2022-synthese.md`** (T0-EXPERT-01) — synthèse du rapport annuel COR septembre 2022, comble le candidat A7 jamais ingéré depuis B.1. PDF officiel lu intégralement par extraction directe (une première tentative de récupération via l'outil web avait échoué sur ce fichier). Intégrité `certified`.
2. **`2023-05-03_rn-proposition-loi-retraites.md`** (T0-OPPOSITION-01) — communiqué RN, proposition de loi alternative chiffrée (60→62 ans, 40-42 annuités). Intégrité `partial`.
3. **`2023-01-30_lfi-autre-reforme-retraites.md`** (T0-OPPOSITION-02) — communiqué LFI, « Une autre réforme des retraites est possible », proposition de changement de logique (35h→32h, 60 ans/40 annuités). Intégrité `partial`.
4. **`2022-10-29_lr-ciotti-proposition-retraites.md`** (T0-OPPOSITION-03) — déclaration de Ciotti (LR), système à choix (65 ans ou 45 annuités). Intégrité `uncertain` (source primaire Le JDD bloquée, contenu repris via un site tiers). Antérieure de plus de deux mois à l'annonce gouvernementale — signalé explicitement, pas présenté comme une réaction au texte final.

## Les deux gaps sont-ils comblés ?

**Oppositions parlementaires** — oui, avec une nuance. Les trois partis (RN, LFI, LR) disposent désormais chacun d'une source primaire dédiée, documentant une position développée et distincte (paramétrage alternatif pour le RN, changement de logique pour LFI, système à choix pour LR), en plus des citations déjà enchâssées dans le verbatim du 49.3. Nuance : les trois nouvelles sources ne sont pas strictement synchrones entre elles ni avec l'annonce du 10 janvier — LR (29 octobre 2022) précède l'annonce, LFI (30 janvier) et RN (3 mai) la suivent à des distances différentes. Cette asynchronie est documentée dans chaque fichier, pas lissée.

**Expertise/contrôle** — oui. Le COR est désormais présent avec une source `certified`, apportant un chiffrage officiel indépendant directement comparable à la fois à l'étude d'impact gouvernementale (T0-ADOPTION-11) et à la note CAEPS (T0-CAEPS-2023-07). **Point notable non tranché** : pour l'année 2022, le COR chiffre un excédent de 3,2 Md€ quand CAEPS affirme un déficit de 148 Md€ — écart de signe et d'ordre de grandeur majeur entre une source officielle et une source non vérifiée du corpus, explicitement laissé à l'analyse en aval (M01/M03), pas arbitré ici.

## État du corpus T0 consolidé

**30 sources** dans `corpus/dossier_zero/T0/` (26 après B.2-bis + 4 nouvelles). Couverture de `candidats_T0_lot_B1.md` : **18/30** candidats désormais couverts avec un degré de confiance raisonnable (17 après B.2-bis + A7/COR). Les trois nouvelles sources d'opposition (RN, LFI, LR) ne correspondent à aucun candidat numéroté de la liste B.1 d'origine — cette liste ne prévoyait pas de poste dédié aux oppositions parlementaires en tant que sources primaires (seul B12, « intervention d'opposition majeure », s'en approchait, et reste non ingéré comme tel — voir ci-dessous). Elles comblent un gap identifié a posteriori, pas un candidat pré-arbitré.

**B12 reste distinct et non ingéré** — l'intervention d'opposition lors du débat sur les motions de censure du 20 mars (candidat B12) documentait un moment précis (le débat du 20 mars lui-même), distinct des trois sources de position générale ajoutées ici. Ce gap spécifique subsiste, signalé dans `log_session_003_lot_B2_final.md`.

## Modifications de code / documents

- `corpus/dossier_zero/T0/2022-09-01_cor-rapport-annuel-2022-synthese.md` — nouveau.
- `corpus/dossier_zero/T0/2023-05-03_rn-proposition-loi-retraites.md` — nouveau.
- `corpus/dossier_zero/T0/2023-01-30_lfi-autre-reforme-retraites.md` — nouveau.
- `corpus/dossier_zero/T0/2022-10-29_lr-ciotti-proposition-retraites.md` — nouveau.
- `.claude/logs/log_session_003_lot_B2ter.md` — cette note.

Lot B.2-ter clos sur cet état : les deux gaps identifiés par l'inventaire par acteur sont comblés. Arrêt conforme à l'instruction.
