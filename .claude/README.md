# `.claude/` — Système de fichiers partagés pour la collaboration humain ↔ instances IA

*Répertoire de coordination pour la méthode de travail collaboratif IA du projet L'Entité. Pont entre instances Claude.ai (Mode Architecte / Reviewer) et instances Claude Code (Mode Implementer / Maintainer). Élimine le copier-coller manuel entre instances et permet l'asynchronisation des sessions.*

---

## Vocation

Ce répertoire est un *protocole de communication* entre les instances IA qui travaillent sur le projet. Les instances Claude.ai (accédées par Cowork) écrivent des plans, revues, décisions dans ce répertoire ; les instances Claude Code (dans VS Code) les lisent et exécutent.

Les fichiers de ce répertoire sont *append-only en pratique* — les versions antérieures ne sont pas écrasées sans inscription au journal. Chaque fichier est identifié par un numéro séquentiel pour traçabilité (`plan_action_001.md`, `log_session_001.md`, etc.).

---

## Structure

| Sous-répertoire | Contenu | Écrit par | Lu par |
|---|---|---|---|
| `plans/` | Plans d'action standardisés | Mode Architecte (Claude.ai Opus 4.7) | Mode Implementer (Claude Code Sonnet 4.6) |
| `logs/` | Logs de session d'exécution | Mode Implementer ou Maintainer (Claude Code) | Mode Reviewer (Claude.ai Opus 4.7) |
| `reviews/` | Rapports de revue post-session | Mode Reviewer (Claude.ai Opus 4.7) | Seb + Mode Architecte (cycle suivant) |
| `decisions/` | Décisions structurantes documentées | Mode Architecte avec validation Seb | Toutes instances (contexte permanent) |
| `context/` | Documents de contexte pré-chargés | Mode Architecte + Seb | Toutes instances (lecture en début de session) |
| `context/templates/` | Templates de prompts standardisés | Mode Architecte | Seb (à utiliser pour lancer les sessions) |

---

## Cycle de travail standard

```
[Mode Architecte] → plans/plan_action_XXX.md
                        ↓
                  (Seb examine et valide)
                        ↓
[Mode Implementer] → lit plans/plan_action_XXX.md
                  → exécute (code, tests, commits)
                  → produit logs/log_session_XXX.md
                        ↓
[Mode Reviewer] → lit code + logs/log_session_XXX.md
                → produit reviews/revue_XXX.md
                → produit plans/plan_action_XXX+1.md
                        ↓
                  (Seb examine et valide)
                        ↓
              [retour cycle]
```

---

## Discipline d'usage

**Pour les instances Claude.ai (Mode Architecte / Reviewer).**

- Écrire toujours dans le répertoire approprié (`plans/`, `reviews/`, `decisions/`, `context/`), jamais directement dans le code source du projet.
- Respecter les formats standardisés (voir `context/templates/`).
- Numéroter les fichiers par ordre séquentiel.

**Pour les instances Claude Code (Mode Implementer / Maintainer).**

- Lire systématiquement le plan d'action de référence et les fichiers de contexte (`context/`) en début de session.
- Modifier le code source du projet uniquement (pas les fichiers de `.claude/` sauf production de `logs/log_session_XXX.md` en fin de session).
- Produire le log de session en fin avec le format standardisé.

**Pour Seb.**

- Examiner et valider les plans d'action avant lancement de Mode Implementer.
- Examiner les revues avant validation du plan d'action suivant.
- Maintenir `context/etat_projet.md` à jour aux évolutions majeures.
- Documenter les décisions structurantes dans `decisions/`.

---

## Modèles recommandés par mode

| Mode | Modèle par défaut | Modèle si tâche complexe |
|---|---|---|
| Architecte | Claude.ai Opus 4.7 | — |
| Implementer | Claude Code Sonnet 4.6 | Claude Code Opus 4.7 (sur tâche explicitement marquée) |
| Reviewer | Claude.ai Opus 4.7 | — |
| Maintainer | Claude Code Sonnet 4.6 ou Haiku 4.5 | Claude Code Sonnet 4.6 (refactoring substantiel) |

---

## Documents de référence

- *Méthode complète.* `lentite/dev/methodologie_workflow_collaboratif_ia_v1.md`
- *Méthodologie de codage.* `lentite/dev/methodologie_codage_v1.md`
- *Doctrine.* `lentite/doctrine/v2.1/` (charte, gabarit, méthodes)
- *Journal méthodologique général.* `lentite/journal/journal.md`
- *Résumé doctrine pour pré-chargement.* `lentite/.claude/context/doctrine_resume.md` (à créer étape 2)

---

*README v1.0 — créé le 17 mai 2026. Document court qui sert de point d'entrée du répertoire. À réviser après premier cycle complet d'application de la méthode.*
