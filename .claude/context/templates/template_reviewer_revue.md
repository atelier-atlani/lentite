# Template Mode Reviewer — Revue

*Template pour lancer une session Mode Reviewer (Claude.ai Opus 4.7) destinée à examiner le travail produit par Mode Implementer et planifier la suite.*

---

## Quand utiliser ce template

- En fin de chaque session Mode Implementer substantielle.
- Avant de produire le plan d'action suivant.
- En fin de jalon majeur.

---

## Prompt à coller dans Claude.ai

```
Mode opérationnel : Reviewer.

Contexte du projet : Tu as accès aux fichiers de contexte du projet via
Cowork. Lis ou rappelle-toi les fichiers .claude/context/doctrine_resume.md,
.claude/context/etat_projet.md, et .claude/context/conventions.md.

Documents à examiner :
1. Plan d'action exécuté — `.claude/plans/plan_action_XXX.md`.
2. Log de session produit par Mode Implementer — 
   `.claude/logs/log_session_XXX.md`.
3. État du repo après exécution (code modifié, tests).

Objectif de la session : Produire un rapport de revue qui examine :

a) Conformité doctrinale — le travail respecte-t-il la doctrine v2.1.1 
   (charte, gabarit, méthodes) ?
b) Conformité aux critères d'acceptation du plan — sont-ils tous remplis ?
c) Qualité du code — lisibilité, conventions, tests, documentation.
d) Frictions identifiées — méthodologiques, techniques, doctrinales.
e) Dette technique introduite — refactoring nécessaire dans une session
   Maintainer ultérieure.

Production attendue :
- Rapport de revue dans `.claude/reviews/revue_XXX.md` au format standardisé
  du projet.
- Plan d'action suivant dans `.claude/plans/plan_action_XXX+1.md` qui :
  - Prend en compte les frictions identifiées.
  - Corrige les écarts par rapport à la doctrine si applicable.
  - Progresse vers l'objectif suivant.
  - Respecte le format standardisé (11 sections).

Discipline : revue rigoureuse mais constructive. Pas de pathos. Pas de 
critique sans proposition. Friction productive = inscription au journal
méthodologique général si elle révèle un pattern transversal.

Je suis prêt — commence par confirmer la lecture des documents puis présente
ta revue structurée.
```

---

## Variables à remplir

- `[XXX]` — numéro de la session Implementer à examiner.

## Pièces jointes systématiques

- Plan d'action exécuté.
- Log de session Implementer.
- État du repo (via Cowork ou résumé si fourni manuellement).

## Critères d'acceptation de la session

- Rapport de revue produit avec examen des cinq dimensions (a-e).
- Plan d'action suivant produit au format standardisé.
- Frictions identifiées documentées avec recommandation.

## Durée typique

- 20-45 minutes.

---

*Template v1.0 — créé le 17 mai 2026.*
