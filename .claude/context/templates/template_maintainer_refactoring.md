# Template Mode Maintainer — Refactoring et maintenance

*Template pour lancer une session Mode Maintainer (Claude Code Sonnet 4.6 ou Haiku 4.5 selon tâche) destinée à du refactoring, ajout de tests, mise à jour de documentation, gestion de dette technique.*

---

## Quand utiliser ce template

- Entre deux sessions Implementer substantielles.
- Quand une revue (Mode Reviewer) a identifié de la dette technique à traiter.
- Pour mise à jour groupée de docstrings, formatage, tests.
- Mode batch quand plusieurs tâches similaires sont à faire.

---

## Prompt à coller dans Claude Code

```
Mode opérationnel : Maintainer.

Avant de commencer :
1. Lis les fichiers de contexte — `.claude/context/doctrine_resume.md`,
   `.claude/context/etat_projet.md`, `.claude/context/conventions.md`.
2. Si une revue récente identifie la dette à traiter, lis-la — 
   `.claude/reviews/revue_XXX.md`.

Tâches à effectuer dans cette session :
[LISTE DÉTAILLÉE DES TÂCHES — par exemple :
- Ajouter des docstrings au format Google sur tous les modèles Pydantic de schemas.py
- Refactorer la fonction validate_pattern_constraints en plusieurs sous-fonctions
- Ajouter des tests unitaires sur ObservableEffectType
- Mettre à jour le README technique du pipeline]

Pour chaque tâche :
3. Suis les conventions du projet (PEP 8 strict, Black formatting, mypy).
4. Discipline anti-cumul — remplace les versions antérieures, n'accumule pas.
5. Tests passants après chaque tâche substantielle.
6. Commits Git en convention Conventional Commits.

Fin de session :
7. Produis un log de session dans `.claude/logs/log_session_XXX.md`
   au format standardisé.

Modèle recommandé pour cette session : [SONNET 4.6 SI REFACTORING SUBSTANTIEL, 
HAIKU 4.5 SI TÂCHES DÉTERMINISTES — docstrings, formatage, tests unitaires
simples].

Discipline : pas de modification du comportement existant. Refactoring 
sans changement de fonctionnalité. Tests existants doivent rester passants.

Je suis prêt — commence par confirmer la lecture des contextes et la 
compréhension des tâches.
```

---

## Variables à remplir

- `[LISTE DÉTAILLÉE DES TÂCHES]` — précise, actionnable, par tâche.
- `[Sonnet 4.6 OU Haiku 4.5]` — selon nature des tâches.

## Quand préférer Haiku 4.5 plutôt que Sonnet 4.6

- Génération de docstrings selon template.
- Génération de tests unitaires sur fonctions pures avec signature claire.
- Formatage et linting (mais préférer pre-commit hooks automatisés).
- Mise à jour de messages de commit en convention.

## Quand préférer Sonnet 4.6

- Refactoring substantiel (split de modules, restructuration de code).
- Ajout de tests d'intégration ou de tests qui demandent compréhension du métier.
- Mise à jour substantielle de documentation technique.

## Critères d'acceptation de la session

- Toutes les tâches exécutées.
- Tests existants restent passants.
- Conventions respectées (Black, Ruff, mypy).
- Commits Git propres.
- Log de session produit.

## Durée typique

- Variable selon ampleur. Mode batch favorisé.

---

*Template v1.0 — créé le 17 mai 2026.*
