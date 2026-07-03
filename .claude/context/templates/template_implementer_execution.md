# Template Mode Implementer — Exécution

*Template pour lancer une session Mode Implementer (Claude Code Sonnet 4.6 par défaut) destinée à exécuter un plan d'action produit par Mode Architecte.*

---

## Quand utiliser ce template

- Quand un plan d'action validé est disponible dans `.claude/plans/`.
- Pour exécution autonome de la session sans intervention humaine continue.

---

## Prompt à coller dans Claude Code

```
Mode opérationnel : Implementer.

Avant de commencer :
1. Lis les trois fichiers de contexte — `.claude/context/doctrine_resume.md`,
   `.claude/context/etat_projet.md`, `.claude/context/conventions.md`.
2. Lis le plan d'action de référence — `.claude/plans/plan_action_XXX.md`
   (où XXX est [NUMÉRO DU PLAN]).
3. Confirme-moi avant de commencer que tu as bien compris :
   - L'objectif principal du plan.
   - Les critères d'acceptation.
   - Les anti-tâches (ce qu'il ne faut PAS faire).
   - Les fichiers concernés.

Exécution :
4. Suis le plan tâche par tâche.
5. Pour chaque tâche complétée, ajoute une entrée dans le log de session
   que tu produiras en fin.
6. Si tu rencontres une friction (ambiguïté, dépendance manquante, choix
   non spécifié dans le plan), arrête-toi et signale-la. Ne diverge pas
   du plan sans validation.
7. Commits Git en convention Conventional Commits (`feat`, `fix`, `docs`,
   `refactor`, `test`, `chore`).
8. Tests passants à chaque étape substantielle.

Fin de session :
9. Produis le log de session au format standardisé du projet 
   (`.claude/logs/log_session_XXX.md`).
10. Le log contient — plan référencé, tâches accomplies, frictions identifiées,
    modifications de code, état des tests, commits, état du système,
    recommandations pour Mode Reviewer.

Modèle recommandé pour cette session : [Sonnet 4.6 PAR DÉFAUT, OU OPUS 4.7 SI 
LE PLAN LE JUSTIFIE EXPLICITEMENT].

Discipline : pas de divagation hors du plan. Pas de modification des fichiers
de `.claude/` sauf le log de session. Discipline anti-cumul — pas d'accumulation
de versions parallèles, remplacement des versions antérieures avec entrée au
journal.

Je suis prêt — commence par lire les fichiers de contexte et le plan, puis
confirme-moi ta compréhension.
```

---

## Variables à remplir

- `[NUMÉRO DU PLAN]` — numéro séquentiel du plan d'action à exécuter.
- `[Sonnet 4.6 PAR DÉFAUT OU OPUS 4.7 SI JUSTIFIÉ]` — selon recommandation du plan.

## Pièces jointes systématiques

Cowork donne automatiquement accès aux fichiers via le système de fichiers. Aucune pièce jointe manuelle nécessaire.

## Critères d'acceptation de la session

- Plan exécuté intégralement ou frictions signalées avec arrêt propre.
- Tests passants à la fin.
- Log de session produit au format standardisé.
- Commits Git propres en convention.
- Pas de modification non prévue dans le plan.

## Durée typique

- 1-3 heures selon ampleur du plan. Sessions plus longues = signal de plan trop ambitieux.

---

*Template v1.0 — créé le 17 mai 2026.*
