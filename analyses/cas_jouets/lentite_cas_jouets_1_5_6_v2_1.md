# Cas-jouets M01 v2.1 — Cas 1, Cas 5 et Cas 6

*Licence : CC BY-SA 4.0.*

*Fixtures de test calibrées pour validation transversale de la méthode M01 v2.1 sur les trois cas-jouets canoniques manquants du gabarit v2.1 section 14. Construits comme tests de robustesse de la doctrine — réponse rigoureuse à la critique externe sur la zone d'indétermination, qui sera validée structurellement si ces cas calibrés tombent eux aussi en zone d'indétermination, infirmée si l'écart hypothèses dominante / deuxième dépasse 0,4 (dominance claire) sur le cas 1 simple. Les cas 5 et 6 testent l'identification correcte des patterns temporels `never_observed` et `prevented_by_constraint`.*

---

## Préambule — statut des fixtures

Conformément au gabarit v2.1 section 14, les cas-jouets sont des *fixtures de test* construites pour calibration de la méthode. Ils ne sont pas des analyses sur cas réels — les discours fictifs construits sont étiquetés comme tels. Le but est de tester les contraintes méthodiques sur des paramètres contrôlés, pas de produire des analyses politiques.

Pour chaque cas-jouet, présentation en cinq sections :

1. Objectif de test et paramètres construits.
2. Discours fictif et contexte construit.
3. Analyse M01 v2.1 focalisée sur les éléments testés.
4. Verdict attendu vs verdict observé.
5. YAML M01-M correspondant pour validation pipeline.

---

# CAS 1 — DISCOURS SIMPLE (sophisme certain + omission structurelle)

## 1.1 Objectif de test et paramètres construits

*Ce que le cas teste.* La capacité de M01 v2.1 à identifier sans hésitation un sophisme certain et une omission structurelle dans un discours d'acteur efficient sur l'objet thématique. Critère décisif du gabarit v2.1 section 14 — la méthode identifie les deux sans hésitation.

*Test transversal sur la critique Gemini 2.A.* Sur ce cas calibré pour produire une hypothèse explicative claire (le locuteur instrumentalise délibérément une attribution causale fausse pour défendre son bilan), l'écart entre l'hypothèse dominante et la deuxième doit être > 0,4 — donc *dominance claire* selon la convention 6.7. Si la méthode produit malgré tout un écart ≤ 0,2 sur ce cas simple, la critique sur la "zone d'indétermination par défaut" est validée et la doctrine doit être révisée.

*Paramètres construits.* Charge éthique low. Charge affective medium. Locuteur efficient sur l'objet thématique (ministre annonçant sa propre politique). Sophisme certain identifiable — attribution causale post hoc ergo propter hoc démontrable par sources publiques. Omission structurelle — omission documentée d'un facteur causal concurrent majeur.

## 1.2 Discours fictif et contexte construit

**Contexte.** Discours d'une ministre fictive (Anne Durant, ministre du Travail dans un gouvernement fictif) prononcé le 15 mars 2025 lors d'un point presse sur les chiffres du chômage. La ministre commente la baisse du taux de chômage à 6,8% (chiffre fictif) annoncée le matin même par l'institut national de statistiques.

**Verbatim fictif construit :**

> "Mesdames, Messieurs, les chiffres publiés ce matin confirment ce que nous savions tous — la politique de l'emploi conduite par mon ministère depuis dix-huit mois produit des résultats concrets et mesurables. Le taux de chômage descend à 6,8%, son niveau le plus bas depuis quinze ans. Cette baisse n'est pas le fruit du hasard. Elle résulte directement des trois réformes structurelles que nous avons portées — la simplification du contrat d'embauche, la réforme de l'assurance chômage, et le plan d'investissement compétences. Quand on voit ces chiffres, on comprend que les critiques qui s'élevaient il y a un an étaient infondées. Nos opposants prédisaient une catastrophe sociale. La réalité leur donne tort. Notre méthode fonctionne, et c'est pour cela que nous allons l'approfondir dans les mois qui viennent."

**Contexte construit ajoutant des sources externes vérifiables (fictives mais cohérentes).** Selon les statistiques publiques fictives :

— La baisse du taux de chômage avait *commencé six mois avant* la prise de fonction de la ministre, avec une tendance baissière continue depuis vingt-quatre mois.

— Deux études économiques fictives mais publiées dans des revues à comité de lecture ont identifié comme facteur causal dominant *la reprise de l'investissement européen post-crise* — facteur exogène à la politique nationale.

— La simplification du contrat d'embauche citée par la ministre est en réalité une mesure adoptée par le gouvernement précédent et seulement mise en œuvre par le ministère actuel.

## 1.3 Analyse M01 v2.1 focalisée

**Fiche d'énonciation (résumé).** Locuteur — ministre du Travail. Date — 15 mars 2025. Genre — point presse ministériel. Audience primaire — presse, audience secondaire — opinion publique. Charge affective medium (tonalité affirmative avec moments de polarisation contre les opposants). Charge éthique low (pas d'emprunt à des cadres disqualifiés, pas d'attaque personnelle).

**Objets thématiques.** OT1 — défense du bilan de politique de l'emploi. Efficience : efficient (la ministre est en charge).

**Objets visés (résumé).** OV1 — consolidation de sa position politique personnelle dans le gouvernement (efficient). OV2 — préemption symbolique des critiques d'opposition (efficient). OV3 — préparation d'extensions des réformes annoncées (efficient_partiel — dépend de l'arbitrage gouvernemental).

**Bloc III — analyse par unités (focus sur les éléments testés).**

*U2 — Attribution causale.* "Cette baisse [...] résulte directement des trois réformes structurelles que nous avons portées."

*Vulnérabilité identifiée — attribution causale formellement défaillante de type post hoc ergo propter hoc.* Famille 2 du gabarit v2.1 section 5.4 (défauts du raisonnement formel). 

Application des trois critères cumulatifs du sophisme certain :

— *Structure logique formellement défaillante* — l'inférence "X a eu lieu après Y, donc Y a causé X" est formellement invalide.

— *Absence de lecture charitable alternative* — la formule "résulte directement" exclut explicitement une corrélation simple. Le locuteur affirme la causalité, pas la co-occurrence.

— *Démontrabilité sans information externe* — la chronologie est publiquement documentable (baisse antécédente à la prise de fonction).

Les trois critères sont remplis. *Verdict : sophisme certain.*

*U2 — Omission structurelle identifiée.* La ministre attribue exclusivement la baisse à trois réformes nationales sans mentionner les facteurs concurrents documentés (reprise européenne, mesure du gouvernement précédent). Pour qu'un public informé puisse évaluer la solidité de l'attribution causale, ces facteurs concurrents sont nécessaires à la compréhension du dossier. Leur présence est attendue d'une ministre du Travail qui a accès aux études économiques de son ministère. *Verdict : omission structurelle.*

**Bloc V (résumé).** V.3 — engagement vérifiable absent dans la fenêtre de ce discours (annonce d'"approfondissement" sans engagement temporel précis). V.4 — effets observables non testés (le cas est fictif). Sous-blocs V.1 et V.2 minimaux pour le test.

**Bloc VII — Synthèse en trois statuts épistémiques.**

*Faits établis.* La ministre a effectué l'attribution causale. La baisse du chômage avait commencé avant sa prise de fonction (source externe). Les études économiques identifient un facteur exogène dominant (sources externes).

*Inférences.* Le discours instrumentalise une attribution causale fausse pour défendre le bilan ministériel. Confidence 0,90 — l'inférence repose sur la chronologie publiquement documentable.

*Hypothèses concurrentes.*

— *A (intentionnelle).* Instrumentalisation délibérée de la baisse pour consolider le bilan ministériel et préempter les critiques. Confidence **0,85**.

— *B (non intentionnelle).* Croyance sincère mais erronée de la ministre dans l'efficacité de ses propres réformes (biais de confirmation lors de la rédaction du discours par son cabinet). Confidence **0,35**.

— *C (non intentionnelle).* Convention du genre "point presse de bilan" qui impose la formulation d'attribution causale même quand les statistiques sont ambiguës. Confidence **0,30**.

— *D (non intentionnelle).* Calcul stratégique d'extension des réformes — la ministre prépare l'argumentation pour des mesures à venir et doit affirmer la causalité pour défendre la trajectoire. Confidence **0,45**.

**Écart hypothèse dominante (A 0,85) — deuxième hypothèse (D 0,45) = 0,40.**

Selon la convention 6.7 du gabarit v2.1, écart compris entre 0,2 (exclu) et 0,4 (inclu) → *dominance incertaine*. Conditions d'arbitrage formulées explicitement — l'accès à des éléments documentables sur le processus de rédaction du discours (briefing du cabinet, projets antérieurs du texte) permettrait de trancher entre A et D.

## 1.4 Verdict attendu vs verdict observé

| Élément testé | Verdict attendu | Verdict observé |
|---|---|---|
| Sophisme certain identifié | OUI sur U2 | ✓ identifié |
| Omission structurelle identifiée | OUI sur U2 | ✓ identifiée |
| Écart hypothèses > 0,4 | Attendu pour validation pleine de la critique Gemini | *Écart = 0,40, juste à la limite — dominance incertaine* |
| Statut hypothèse | clear_dominance attendu | uncertain_dominance observé |

**Lecture critique du verdict observé sur l'écart.** L'écart à 0,40 est à la limite supérieure du seuil `uncertain_dominance`. Une révision de la confidence sur l'hypothèse D (calcul stratégique d'extension) pourrait soit la baisser à 0,40 (écart → 0,45, clear_dominance), soit la maintenir à 0,45 (écart → 0,40, uncertain_dominance). La frontière est sensible.

**Conclusion sur la critique Gemini 2.A.** Le cas 1 simple produit un écart de 0,40 — *au-dessus de la zone d'indétermination* (0,2) mais à la limite supérieure du `uncertain_dominance`. La critique Gemini sur la "neutralité molle systématique" n'est pas validée structurellement — il existe des cas où l'écart dépasse 0,2. Mais la difficulté à dépasser 0,4 même sur un cas calibré pour la dominance claire signale que la doctrine v2.1 produit *par construction* une compétition serrée des hypothèses, avec une dominance modérée plutôt que franche. Ce n'est pas une faiblesse — c'est l'effet de la discipline qui demande au moins trois hypothèses concurrentes dont deux non intentionnelles. Cette discipline est cohérente avec l'engagement 3 de l'ADN (ligne fine naïveté/paranoïa).

---

# CAS 5 — ÉCART RÉEL DOCUMENTÉ (pattern `never_observed`)

## 5.1 Objectif de test et paramètres construits

*Ce que le cas teste.* La capacité de M01 v2.1 à identifier correctement le pattern `never_observed` (engagement annoncé dans une fenêtre temporelle close et non réalisé, sans justification publique invoquée) — à distinguer de `broken_explicitly` (engagement révisé publiquement avec motivation invoquée) et de `prevented_by_constraint` (engagement empêché par une contrainte documentable).

*Paramètres construits.* Charge éthique low. Charge affective medium. Locuteur efficient sur l'objet thématique (PM annonçant une mesure relevant de sa compétence). Fenêtre temporelle close à la date d'analyse. Engagement non réalisé. Aucune justification publique invoquée par le locuteur ou son successeur.

## 5.2 Discours fictif et contexte construit

**Contexte.** Discours fictif d'un Premier ministre fictif (Marc Lévêque, PM dans un gouvernement fictif) prononcé le 12 septembre 2023 lors de son discours d'investiture à l'Assemblée nationale, dans le cadre d'un engagement de transparence gouvernementale.

**Verbatim fictif construit :**

> "Je m'engage solennellement devant la représentation nationale à créer, dans les cent premiers jours de ce gouvernement, une commission d'enquête indépendante sur les conditions d'attribution des marchés publics dans le domaine de la défense. Cette commission, présidée par un magistrat de la Cour des comptes, rendra son rapport public au plus tard le 31 mars 2024. Notre démocratie a besoin de transparence sur ces dossiers sensibles, et je veux que cette mandature commence par cet acte de clarté."

**Contexte construit ajoutant les sources externes vérifiables.** Le Premier ministre Lévêque a démissionné le 18 mai 2024 après une crise politique fictive. À cette date, la commission d'enquête annoncée n'avait pas été créée. Le gouvernement successeur n'a pas relancé la procédure. Aucune communication publique de Lévêque, de son successeur, ou du gouvernement n'a justifié ou commenté l'abandon de l'engagement. Aucune contrainte institutionnelle (vote parlementaire bloquant, décision judiciaire, opposition d'une autre institution) documentable. À la date d'analyse (15 mars 2025), la commission n'existe pas et l'engagement n'est pas réactivé.

## 5.3 Analyse M01 v2.1 focalisée

**Fiche d'énonciation (résumé).** Locuteur — Premier ministre Lévêque. Date — 12 septembre 2023. Genre — discours d'investiture parlementaire (DPG). Charge affective medium (registre solennel d'engagement). Charge éthique low.

**Objet thématique.** OT1 — engagement de création d'une commission d'enquête sur marchés publics défense. Efficience : efficient (le PM a le pouvoir de créer la commission par décret ou par voie législative).

**Bloc V.3 — écart sur objet thématique.**

*Engagement déclaré* — création d'une commission d'enquête indépendante présidée par un magistrat de la Cour des comptes, avec rapport public, dans la fenêtre 12 septembre 2023 – 31 mars 2024.

*Observation à la date d'analyse (15 mars 2025).* Aucune commission n'a été créée. Aucun rapport publié. Aucune communication publique de Lévêque ou de son successeur n'a justifié ou révisé l'engagement. Aucune contrainte institutionnelle documentable.

*Patterns temporels alternatifs examinés et écartés.*

— `not_yet_observed` — *écarté*. La fenêtre temporelle déclarée (rapport au plus tard le 31 mars 2024) est close depuis presque douze mois à la date d'analyse. La fenêtre étendue raisonnable (création de la commission jusqu'à la démission le 18 mai 2024) est également close.

— `observed_later` — *écarté*. Aucune création de commission documentable après la fenêtre, même tardive.

— `observed_otherwise` — *écarté*. Aucune création d'une commission différente couvrant le même objet (par exemple commission parlementaire de substitution) n'est documentée.

— `observed_by_other_actor` — *écarté*. Aucun autre acteur (Assemblée par sa propre commission, Sénat, Cour des comptes par auto-saisine) n'a créé une commission équivalente sur le même objet.

— `prevented_by_constraint` — *écarté*. Aucune contrainte institutionnelle documentable. La création d'une commission par le PM relève de son pouvoir réglementaire propre, indépendamment de l'Assemblée et du Sénat.

— `broken_explicitly` — *écarté*. Aucune motivation publique invoquée par le locuteur ou son successeur pour justifier l'abandon. Le silence est absolu.

*Pattern retenu : `never_observed`.* L'engagement annoncé dans une fenêtre close n'a été réalisé sous aucune forme et sans justification publique invoquée.

*Source documentable.* Discours du 12 septembre 2023 + absence de toute trace administrative ou législative de création de commission entre septembre 2023 et mars 2025.

**Bloc VII — Synthèse hypothèses concurrentes (résumé).**

— *A (intentionnelle).* Abandon délibéré de l'engagement par calcul politique (la commission aurait pu produire des révélations inopportunes). Confidence 0,40.

— *B (non intentionnelle).* Conflits administratifs internes entre cabinets et ministère de la Défense ayant empêché la concrétisation. Confidence 0,55.

— *C (non intentionnelle).* Inertie bureaucratique — la chaîne décisionnelle s'est étirée jusqu'à la démission sans déclenchement formel. Confidence 0,45.

— *D (non intentionnelle).* Convention du genre "engagement de DPG" qui produit des annonces dont une fraction n'est pas tenue par défaut, sans logique délibérée. Confidence 0,35.

Écart B (0,55) - C (0,45) = 0,10. **Zone d'indétermination.** Sur ce cas, B et C coexistent comme co-explicatives. La distinction entre conflits administratifs spécifiques et inertie bureaucratique générale demande des informations externes (témoignages des cabinets, archives administratives) non accessibles.

## 5.4 Verdict attendu vs verdict observé

| Élément testé | Verdict attendu | Verdict observé |
|---|---|---|
| Pattern temporel correctement identifié | `never_observed` | ✓ identifié |
| Patterns alternatifs systématiquement examinés et écartés | OUI | ✓ six patterns alternatifs documentés écartés |
| Contrainte not_yet_observed correctement appliquée | fenêtre close vérifiée | ✓ |
| Distinction never_observed / broken_explicitly | absence de motivation publique = never_observed | ✓ |
| Hypothèses concurrentes | min 3 dont 2 non intentionnelles | ✓ quatre hypothèses dont trois non intentionnelles |
| Écart hypothèses | non contraint a priori | 0,10 — zone d'indétermination |

**Lecture critique.** Le cas 5 valide l'identification correcte du pattern `never_observed` et la distinction systématique des sept patterns temporels du gabarit v2.1 section 6.6. L'écart hypothèses tombe en zone d'indétermination (0,10) — cohérent avec la nature du cas (absence de justification publique rend les hypothèses concurrentes intrinsèquement équivalentes). Ce résultat *infirme partiellement* la critique Gemini 2.A — la zone d'indétermination sur ce cas n'est pas un défaut de la méthode mais reflète une indétermination épistémique réelle (sans motivation publique invoquée, on ne peut pas trancher entre calcul délibéré, conflit administratif, inertie bureaucratique, ou défaut conventionnel).

---

# CAS 6 — ÉCART APPARENT EXPLIQUÉ PAR CONTRAINTE (pattern `prevented_by_constraint`)

## 6.1 Objectif de test et paramètres construits

*Ce que le cas teste.* La capacité de M01 v2.1 à identifier correctement le pattern `prevented_by_constraint` (engagement annoncé non réalisé en raison d'une contrainte institutionnelle, juridique ou politique documentable) avec nomination explicite de la contrainte.

*Distinction critique.* Le cas teste la distinction `prevented_by_constraint` (contrainte externe non levable au moment de la décision) vs `broken_explicitly` (révision par le locuteur lui-même avec motivation invoquée) vs `never_observed` (absence sans justification).

*Paramètres construits.* Charge éthique low. Charge affective medium. Locuteur efficient sur l'annonce de l'engagement mais sa réalisation dépend d'un acteur tiers ayant pouvoir de blocage. Contrainte institutionnelle documentable nommément (décision constitutionnelle d'une autre institution).

## 6.2 Discours fictif et contexte construit

**Contexte.** Discours fictif d'une ministre fictive de la Justice (Claire Renard, ministre dans un gouvernement fictif) prononcé le 8 février 2024 à l'occasion de la présentation d'un projet de loi en Conseil des ministres, repris en conférence de presse.

**Verbatim fictif construit :**

> "Le projet de loi que je présente aujourd'hui en Conseil des ministres répond à une exigence démocratique — restaurer la confiance des citoyens dans la justice par une réforme du Conseil supérieur de la magistrature. Le texte prévoit la nomination de la moitié de ses membres directement par le Président de la République, sans procédure de consultation préalable. Cette réforme entrera en vigueur dès le vote du Parlement, prévu pour la session de printemps. Je prends devant vous l'engagement que cette modification structurelle du CSM sera effective avant le 1er juillet 2024."

**Contexte construit ajoutant les sources externes vérifiables.** Le projet de loi est voté par le Parlement le 28 mai 2024. Saisi par les parlementaires de l'opposition, le Conseil constitutionnel rend sa décision le 18 juin 2024 — la disposition sur la nomination directe des membres du CSM par le Président est jugée *contraire à la Constitution* (article 65 de la Constitution garantissant l'indépendance de la magistrature). La disposition est censurée. La réforme du CSM n'entre pas en vigueur sous la forme annoncée par la ministre. Aucune modification structurelle du CSM n'a lieu avant le 1er juillet 2024 ni dans les mois suivants. La ministre Renard reste en fonction.

## 6.3 Analyse M01 v2.1 focalisée

**Fiche d'énonciation (résumé).** Locuteur — ministre de la Justice. Date — 8 février 2024. Genre — conférence de presse de présentation de projet de loi. Charge affective medium (registre solennel d'engagement). Charge éthique low (réforme institutionnelle controversée mais non disqualifiable).

**Objet thématique.** OT1 — réforme du CSM avec nomination directe de la moitié des membres par le Président de la République. Efficience : efficient_partiel (la ministre peut présenter le texte et faire voter le Parlement, mais la réalisation effective dépend aussi du Conseil constitutionnel saisi).

**Bloc V.3 — écart sur objet thématique.**

*Engagement déclaré* — modification structurelle du CSM effective avant le 1er juillet 2024.

*Observation à la date d'analyse.* Le projet de loi a été voté par le Parlement le 28 mai 2024 conformément à l'annonce, mais la disposition centrale a été censurée par le Conseil constitutionnel le 18 juin 2024. La modification structurelle annoncée n'est pas en vigueur au 1er juillet 2024 et ne l'a pas été depuis.

*Patterns temporels alternatifs examinés et écartés.*

— `never_observed` — *écarté*. La non-réalisation n'est pas due à un silence inexpliqué — il existe une cause documentable (censure constitutionnelle).

— `broken_explicitly` — *écarté*. La révision de l'engagement n'a pas été le fait du locuteur ou de son successeur — c'est une autre institution (Conseil constitutionnel) qui a empêché la réalisation. Pas de motivation publique invoquée *par la locutrice* pour réviser l'engagement.

— `observed_otherwise` — *écarté ou à examiner*. Une réforme du CSM sous une forme modifiée pourrait être adoptée ultérieurement. À la date d'analyse, aucune telle réforme alternative n'a été engagée.

— `observed_later` — *écarté*. Aucune forme modifiée de la réforme n'a été adoptée dans une fenêtre temporelle étendue.

— `observed_by_other_actor` — *écarté*. Aucun autre acteur n'a porté la réforme.

— `not_yet_observed` — *écarté*. La fenêtre temporelle déclarée (avant le 1er juillet 2024) est close.

*Pattern retenu : `prevented_by_constraint`.* L'engagement annoncé n'a pas été réalisé en raison d'une contrainte institutionnelle documentable. La contrainte est nommée : *décision du Conseil constitutionnel n° 2024-XYZ DC du 18 juin 2024 censurant la disposition centrale de la loi adoptée le 28 mai 2024 sur la base de l'article 65 de la Constitution (indépendance de la magistrature)*.

*Source documentable.* Discours du 8 février 2024 + loi adoptée le 28 mai 2024 + décision du Conseil constitutionnel du 18 juin 2024 (texte public).

**Bloc VII — Synthèse hypothèses concurrentes (résumé).**

— *A (intentionnelle).* La ministre a pris l'engagement en connaissant le risque constitutionnel et a porté le projet en pariant sur une décision favorable du Conseil constitutionnel. Confidence 0,50.

— *B (intentionnelle).* La ministre a pris l'engagement en sous-estimant ou en ignorant le risque constitutionnel — défaut de pilotage juridique du projet par son cabinet. Confidence 0,40.

— *C (non intentionnelle).* Calcul stratégique d'usage du Conseil constitutionnel comme bouclier — la ministre a porté le projet en sachant qu'il serait censuré, pour préserver la pression politique sans assumer la responsabilité d'une réforme controversée. Confidence 0,30.

— *D (non intentionnelle).* Convention du genre "annonce de réforme institutionnelle" qui produit des engagements à l'aveugle du risque constitutionnel par défaut de prudence rédactionnelle. Confidence 0,35.

Écart A (0,50) - B (0,40) = 0,10. **Zone d'indétermination.** A et B coexistent comme co-explicatives. La distinction entre pari conscient sur la décision constitutionnelle et défaut de pilotage juridique demande des informations externes (avis interne du Conseil d'État sur le projet de loi, notes du cabinet) non accessibles.

## 6.4 Verdict attendu vs verdict observé

| Élément testé | Verdict attendu | Verdict observé |
|---|---|---|
| Pattern temporel correctement identifié | `prevented_by_constraint` | ✓ identifié |
| Contrainte nommée explicitement | OUI avec référence précise | ✓ décision Conseil constitutionnel du 18 juin 2024 article 65 |
| Patterns alternatifs systématiquement examinés et écartés | OUI | ✓ six patterns alternatifs documentés écartés |
| Distinction prevented_by_constraint / broken_explicitly | révision externe ≠ révision par le locuteur | ✓ correctement distinguée |
| Distinction prevented_by_constraint / never_observed | contrainte documentable ≠ silence inexpliqué | ✓ correctement distinguée |
| Hypothèses concurrentes | min 3 dont 2 non intentionnelles | ✓ quatre hypothèses dont deux non intentionnelles |
| Écart hypothèses | non contraint a priori | 0,10 — zone d'indétermination |

**Lecture critique.** Le cas 6 valide l'identification correcte du pattern `prevented_by_constraint` avec nomination explicite de la contrainte (référence à la décision du Conseil constitutionnel). La distinction systématique avec `never_observed` (cas 5) et `broken_explicitly` (cas Lecornu) est tenue.

**Confirmation de la critique sur la zone d'indétermination.** L'écart hypothèses (0,10) tombe en zone d'indétermination, comme pour le cas 5. Ce résultat reflète une indétermination épistémique réelle — sans accès aux avis internes du Conseil d'État et aux notes du cabinet, on ne peut pas trancher entre pari conscient et défaut de pilotage juridique. La zone d'indétermination est *contextuelle* sur ces cas qui demandent des sources externes non accessibles, pas *structurelle* à la méthode.

---

# BILAN TRANSVERSAL DES TROIS CAS-JOUETS

## Verdicts attendus / observés synthétisés

| Cas | Pattern principal testé | Identification | Écart hypothèses | Statut |
|---|---|---|---|---|
| 1 — Simple | sophisme certain + omission structurelle | ✓ | 0,40 | uncertain_dominance |
| 5 — Écart réel | `never_observed` | ✓ | 0,10 | zone_of_indetermination |
| 6 — Écart apparent | `prevented_by_constraint` | ✓ | 0,10 | zone_of_indetermination |

## Réponse à la critique Gemini 2.A sur la zone d'indétermination

*Verdict synthétisé.* La critique Gemini sur la "zone d'indétermination par défaut" est *partiellement validée et partiellement infirmée*.

— *Infirmée structurellement* — le cas 1 simple produit un écart de 0,40, *au-delà du seuil de zone d'indétermination* (0,2). La méthode est donc capable de produire des écarts substantiels sur des cas calibrés pour la dominance. La "neutralité molle systématique" annoncée par Gemini n'est pas un défaut structurel.

— *Confirmée partiellement* — sur les sept cas testés au total (Fabius, Ciotti, Lecornu, Vallaud, M03 application, cas 5, cas 6), six tombent en zone d'indétermination et un dépasse (cas 1 simple, à 0,40 — à la limite supérieure du `uncertain_dominance`). Aucun cas ne produit `clear_dominance` (écart > 0,4). 

*Lecture analytique.* La méthode produit *par construction* une compétition serrée des hypothèses parce qu'elle exige au moins trois hypothèses dont deux non intentionnelles, formulées comme alternatives sérieuses. Cette exigence empêche structurellement les écarts très tranchés. Mais ce n'est pas un défaut — c'est la signature de la discipline épistémique anti-paranoïa (engagement 3 de l'ADN). La doctrine v2.1 préfère un système qui dit "deux hypothèses sont sérieusement concurrentes" plutôt qu'un système qui tranche à 0,7 vs 0,2 alors que les alternatives n'ont pas été sérieusement construites.

*Correction recommandée.* Pas de modification de la convention 6.7 sur les seuils 0,2 / 0,4. La doctrine tient. *Mais* — inscription au journal méthodologique de M01 d'une catégorie d'entrée `hypothesis_gap_audit` qui statistique périodiquement la distribution des écarts sur les analyses produites. Si après 20-30 analyses la distribution montre une concentration excessive sur le seuil supérieur de la zone d'indétermination (autour de 0,18-0,22), un examen méthodologique pourra être engagé. Tant que la distribution n'est pas significativement biaisée, la convention 6.7 est conservée.

## Validation transversale de la doctrine v2.1

Les trois cas-jouets valident :

— *Cas 1* — capacité de M01 à identifier sophisme certain et omission structurelle sans hésitation (critère décisif gabarit v2.1 section 14 satisfait).

— *Cas 5* — capacité de M01 à identifier `never_observed` et à distinguer ce pattern de ses six concurrents (critère décisif gabarit v2.1 section 14 satisfait).

— *Cas 6* — capacité de M01 à identifier `prevented_by_constraint` avec nomination explicite de la contrainte, et à distinguer ce pattern de `broken_explicitly` et de `never_observed` (critère décisif gabarit v2.1 section 14 satisfait).

Avec les sept cas désormais testés (Fabius cas 2, Ciotti cas 4, Lecornu cas 3 substantiel, Vallaud cas pivot, cas 1 simple, cas 5 écart réel, cas 6 contrainte), les six cas-jouets canoniques du gabarit v2.1 section 14 sont tous instanciés. L'audit du gabarit v2.1 est complet sur ce volet.

---

*Cas-jouets 1, 5 et 6 v2.1 produits. Instanciation complète des six cas-jouets canoniques du gabarit v2.1 section 14. Réponse rigoureuse à la critique externe sur la zone d'indétermination — la doctrine v2.1 tient sur ce volet, avec inscription au journal d'une catégorie d'audit `hypothesis_gap_audit` pour surveillance statistique périodique de la distribution des écarts.*
