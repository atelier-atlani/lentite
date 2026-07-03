# Template — Décision structurante

*Template de format pour documenter une décision structurante dans `.claude/decisions/`. À utiliser pour toute décision qui affecte l'architecture, la doctrine, ou la trajectoire du projet de manière non triviale.*

---

## Format à respecter

```markdown
# Décision XXX — [Titre court de la décision]

*Date de la décision* : YYYY-MM-DD
*Statut* : [PROPOSÉE / VALIDÉE / RÉVISÉE / OBSOLÈTE]
*Porteur* : [NOM]
*Lié à* : [Plan d'action / Revue / Friction de référence si applicable]

---

## 1. Contexte

[1-3 paragraphes sur la situation qui motive la décision. Pourquoi maintenant ?
Quels documents ou frictions ont conduit à devoir trancher ?]

## 2. Problème à résoudre

[1 phrase précise sur le problème ou la question à trancher.]

## 3. Options examinées

### Option A — [Nom court de l'option]

*Description.* [Ce que propose l'option.]

*Avantages.*
- [Point 1]
- [Point 2]

*Inconvénients.*
- [Point 1]
- [Point 2]

*Coût.* [Effort estimé, coût technique ou financier si applicable.]

### Option B — [Nom court de l'option]

[Même structure que Option A.]

### Option C — [Nom court de l'option]

[Même structure si applicable. 2-4 options typiquement.]

## 4. Critères de décision

[Liste des critères utilisés pour évaluer les options — par exemple
maintenabilité, coût, alignement doctrinal, urgence, etc.]

## 5. Décision retenue

**Option retenue** — [Lettre de l'option].

**Motif principal** — [1-2 phrases sur la raison principale du choix.]

**Compromis acceptés** — [Si applicable, ce qu'on accepte de perdre en
choisissant cette option plutôt qu'une autre.]

## 6. Conditions de révision

[Critères ou événements qui justifieraient de revoir cette décision plus tard.
Par exemple — "à réviser si l'écosystème langgraph stagne pendant 12 mois"
ou "à réviser au moment de la décision sur licence définitive".]

## 7. Conséquences immédiates

[Liste des actions concrètes à engager suite à cette décision —
production d'un plan d'action, modification de schéma, mise à jour de
conventions, etc.]

## 8. Inscriptions au journal

- À ajouter au journal méthodologique général comme entrée de la section 8
  (décisions méthodologiques significatives) avec numéro 8.X.
- Référencer dans le README du projet si décision politique structurante.
```

---

## Exemple d'usage typique

Pour les cinq décisions structurantes de la Phase 0 du codage (orchestration multi-agents, persistance graphe, persistance journal, licence, modèle de distribution), produire cinq fichiers —

- `decisions/decision_001_orchestration_multi_agents.md`
- `decisions/decision_002_persistance_graphe.md`
- `decisions/decision_003_persistance_journal.md`
- `decisions/decision_004_licence.md`
- `decisions/decision_005_modele_distribution.md`

Chacun selon le format ci-dessus.

## Discipline d'écriture

- *Factuel et synthétique.* Pas de pathos. Pas de récit. Les options sont présentées sans rhétorique.
- *Honnêteté sur les inconvénients.* L'option retenue garde ses inconvénients documentés — pas de cosmétique.
- *Append-only.* Une décision validée n'est pas modifiée. Une révision = nouvelle entrée référençant la précédente.

---

*Template v1.0 — créé le 17 mai 2026.*
