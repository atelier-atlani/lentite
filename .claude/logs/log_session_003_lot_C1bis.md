# Note de fin de lot — plan_action_003, séquence C, lot C.1-bis

*Mode opérationnel : Implementer. Plan référencé : `.claude/plans/plan_action_003.md` §6 (séquence C), suite du lot C.1. Trois M01 produits sur les postes restants (voix syndicale, deux oppositions parlementaires), même régime : corpus T0 uniquement, validation tracée, un commit par correction, régime T0 vérifié mécaniquement. Pas de relevé de temps de validation humaine dans ce lot (mesure 1 déjà établie au journal le 12 juillet 2026 — échantillonnage par le Dirigeant, pas systématique).*

---

## M01 produits

1. **`pipeline/analyses/M01_CGT_ALTFIN_20230302_AUTO_v1/`** — CGT, communiqué du 2 mars 2023 sur les alternatives de financement (T0-ALT-FIN-02, plan en sept axes). 842 lignes.
2. **`pipeline/analyses/M01_LFI_ALTREFORME_20230130_AUTO_v1/`** — LFI, communiqué du 30 janvier 2023 (T0-OPPOSITION-02, changement de logique). 820 lignes.
3. **`pipeline/analyses/M01_RN_PROPOSITION_20230503_AUTO_v1/`** — RN, communiqué du 3 mai 2023 (T0-OPPOSITION-01, proposition de loi alternative). 672 lignes.

Les trois ont validé (`✓ Validation réussie`) sans réinjection (4 appels d'agent chacun).

## Régime T0 strict — confirmation

Tous les champs `date_fait`/`date_connaissance` des trois YAML portent une date ≤ 2023-06-30 ou `non_documente`, à une exception attendue : `date_fait: '1982-01-01'` dans le M01 CGT, référant à la baisse de la part salariale dans la valeur ajoutée *depuis 1982* — un fait historique cité par la CGT elle-même dans le communiqué, pas une source d'analyse externe (même traitement que la citation Rocard 1990 dans le M01 du 49.3, lot C.1). **Aucune assertion ne cite une source postérieure au 30 juin 2023** dans les trois M01.

## Diff machine → humain, par analyse

### M01 CGT (2 mars 2023) — deux corrections, même défaut

`downstream_causal_chains.observable_to_date` et `epistemic_synthesis.established_facts` affirmaient tous deux, comme acquis, que « la réforme des retraites de 2023 a été adoptée par le Parlement », avec un hedging partiel (« non vérifié dans le texte source lui-même ») qui n'empêchait pas l'assertion de figurer dans une liste de faits établis. Incohérence interne : le même document traitait correctement la même question ailleurs (`discourse_action_gaps_on_thematic_objects`, `pattern_type: not_yet_observed`). Corrigé pour aligner les trois emplacements sur la discipline de clôture de corpus correctement appliquée par ailleurs.

### M01 LFI (30 janvier 2023) — une correction, même défaut

`established_facts` contenait une affirmation macroéconomique sur le XXe siècle explicitement qualifiée par l'agent Synthèse lui-même de « fait documenté indépendamment du communiqué » — aveu direct de la même rupture de clôture de corpus. Retirée.

### M01 RN (3 mai 2023) — défaut plus étendu, deux corrections

`established_facts` comportait quatre items sans rapport avec le texte source fourni (recours au 49.3, validation du Conseil constitutionnel, statut minoritaire du RN à l'Assemblée, défaite électorale de Marine Le Pen en 2022) — seul l'item effectivement présent dans le communiqué (la loi n°2023-270 elle-même) est conservé. `upstream_causal_chain` contenait en outre un élément dont le `source_reference` citait un texte n'apparaissant nulle part dans le texte source réellement fourni — une pseudo-citation fabriquée, plus grave qu'une simple injection de connaissance générale puisqu'elle se présente comme une citation exacte. Élément retiré. **Point de vigilance résiduel non corrigé** : les defeaters de l'unité u5 mobilisent les mêmes faits externes (49.3, Conseil constitutionnel) dans un usage argumentatif plus défendable (tester la rhétorique du RN contre des contre-considérations, fonction normale d'un defeater) — laissés en l'état plutôt que corrigés, la limite entre « fait externe injecté à tort » et « contre-argument critique légitime » étant moins nette dans ce cas que pour `established_facts` et le faux `source_reference`.

## Motif structurel commun aux trois corrections

Une même classe de défaut traverse les trois analyses : l'agent Chaînes causales/Synthèse, lorsqu'il connaît par ailleurs (mémoire générale du modèle) la suite réelle des événements de 2023, a tendance à l'injecter comme fait acquis plutôt que de s'en tenir strictement au texte source fourni à cette analyse — alors que l'architecture même du pipeline (un texte source par invocation, aucun accès au reste du corpus T0 pendant l'exécution) est précisément conçue pour garantir une analyse « authentiquement naïve » par discours. Le M01 RN est le cas le plus marqué (quatre items + une pseudo-citation) ; le M01 du 49.3 (lot C.1, verbatim certified) n'en avait présenté aucune occurrence — la dégradation semble corrélée à la brièveté et à la nature secondaire du texte source (résumés courts, communiqués), qui laissent plus de place à l'agent pour « compléter » avec ce qu'il croit savoir par ailleurs. **Point à surveiller sur les M01 suivants du dossier zéro**, potentiellement matière pour un audit dédié si le pattern se confirme sur d'autres analyses.

## Temps de production automatique (donnée fiable, horodatage des logs d'agents)

- M01 CGT : 13:48:49 → 13:51:16 UTC = **2 min 27 s**.
- M01 LFI : 13:52:07 → 13:54:23 UTC = **2 min 16 s**.
- M01 RN : 13:59:07 → 14:01:09 UTC = **2 min 01 s**.

Cohérent avec les deux mesures du lot C.1 (3 min 12 s et 2 min 44 s) — ordre de grandeur stable autour de 2-3 minutes par M01, quatre appels d'agent, aucune réinjection sur les cinq analyses produites à ce jour dans le dossier zéro.

**Pas de relevé de temps de validation humaine** dans ce lot, conformément à l'instruction — la mesure 1 (30 min/M01, ratio ≈1:10) est établie par le Dirigeant sur échantillon (journal, entrée du 12 juillet 2026) et ne sera pas systématiquement recalculée par l'Implementer à chaque pièce.

## Modifications de code / documents

- `pipeline/source_texts/cgt_20230302.txt`, `pipeline/source_texts/lfi_20230130.txt`, `pipeline/source_texts/rn_20230503.txt` — nouveaux.
- `pipeline/analyses/M01_CGT_ALTFIN_20230302_AUTO_v1/`, `pipeline/analyses/M01_LFI_ALTREFORME_20230130_AUTO_v1/`, `pipeline/analyses/M01_RN_PROPOSITION_20230503_AUTO_v1/` — nouveaux (YAML + logs d'agents), corrections appliquées et commitées séparément pour chacun.
- `.claude/logs/log_session_003_lot_C1bis.md` — cette note.

Lot C.1-bis clos sur cet état : trois M01 produits et validés, cinq corrections au total (deux + une + deux), toutes de la même famille (rupture de clôture de corpus), documentée comme motif structurel commun plutôt que trois défauts isolés. Arrêt conforme à l'instruction.
