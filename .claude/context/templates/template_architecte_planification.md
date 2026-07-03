# Template Mode Architecte — Planification

*Template pour lancer une session Mode Architecte (Claude.ai Opus 4.7) destinée à produire un plan d'action standardisé.*

---

## Quand utiliser ce template

- En début de phase de développement (avant de lancer Mode Implementer).
- À chaque jalon majeur.
- Sur frictions doctrinales identifiées dans une revue précédente.
- Quand une décision structurante doit être prise et formalisée.

---

## Prompt à coller dans Claude.ai

```
Mode opérationnel : Architecte.

Contexte du projet : Lis d'abord les trois fichiers de contexte du projet
L'Entité — doctrine_resume.md, etat_projet.md, conventions.md (je vais te
les fournir ou tu les as déjà). 

Lis aussi le plan d'action précédent et la revue précédente si elles existent
(je te les fournis ci-dessous).

Objectif de cette session : [DESCRIPTION COURTE DE L'OBJECTIF, 1-2 PHRASES]

Contraintes spécifiques : [SI APPLICABLE — par exemple budget temps, modèle
de Claude Code recommandé, dépendances]

Production attendue : Un plan d'action au format standardisé du projet
(11 sections — contexte, objectif, critères d'acceptation, tâches détaillées,
anti-tâches, output attendu, modèle recommandé, estimation durée et coût).

Le plan sera placé dans `.claude/plans/plan_action_XXX.md` où XXX est le
numéro séquentiel suivant. Tu peux me proposer le numéro après examen des
plans existants.

Discipline : pas de production de code substantiel dans cette session
(délégué à Mode Implementer). Concentration sur la structuration de l'objectif
et la décomposition en tâches actionnables avec critères d'acceptation
objectifs.

Je suis prêt — commence par confirmer la lecture des fichiers de contexte
puis demande-moi les compléments d'information nécessaires.
```

---

## Variables à remplir

- `[DESCRIPTION COURTE DE L'OBJECTIF]` — 1-2 phrases précises.
- `[CONTRAINTES SPÉCIFIQUES]` — optionnel.

## Pièces jointes systématiques

À fournir à l'instance Claude.ai en début de session si non déjà chargées —

- `.claude/context/doctrine_resume.md`
- `.claude/context/etat_projet.md`
- `.claude/context/conventions.md`
- Plan d'action précédent si applicable (`.claude/plans/plan_action_XXX-1.md`).
- Revue précédente si applicable (`.claude/reviews/revue_XXX-1.md`).

## Critères d'acceptation de la session

- Plan d'action produit au format standardisé (11 sections complètes).
- Critères d'acceptation objectivement vérifiables.
- Modèle Claude Code recommandé par tâche.
- Estimation durée et coût marginal.

## Durée typique

- 30-60 minutes selon complexité du plan.

---

*Template v1.0 — créé le 17 mai 2026.*
