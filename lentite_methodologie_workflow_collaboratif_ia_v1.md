# Méthode de travail collaboratif IA pour L'Entité — v1

*Document de méthode opérationnelle pour la collaboration humain ↔ instances IA dans le projet L'Entité. Répond à deux frictions identifiées — perte de temps par copier-coller manuel entre instances, coût élevé du couple Opus 4.7 + Claude Code en usage non hiérarchisé. Distinct du document `methodologie_codage_v1.md` qui spécifie le contenu à coder. Ce document spécifie *comment travailler* avec les IA.*

---

## 1. Diagnostic du workflow actuel

**Workflow observé.** Seb travaille avec une instance Claude.ai (modèle Opus 4.7) pour l'architecture et la doctrine. Il copie-colle les instructions produites par Claude.ai vers Claude Code dans VS Code (modèle également Opus 4.7) pour exécution. Le code produit est testé, le résultat est rapporté à Claude.ai pour validation et planification de la suite.

**Friction 1 — perte de temps par synchronisation manuelle.** Le copier-coller demande la présence active de Seb pour transférer instructions et résultats entre instances. Chaque tour de boucle nécessite intervention humaine. La productivité est plafonnée par le temps de présence du porteur — typiquement une à deux heures par session intensive de développement.

**Friction 2 — coût élevé par usage non hiérarchisé.** Opus 4.7 est utilisé pour l'ensemble des tâches dans Claude Code, y compris des tâches qui ne nécessitent pas la capacité de raisonnement la plus avancée. Le coût marginal par session devient prohibitif au-delà d'un usage quotidien régulier.

**Diagnostic structurel.** Les deux frictions partagent une cause racine — *absence de discipline méthodologique sur la collaboration IA*. Chaque session est conduite de manière implicite, sans cycle formalisé ni discipline de routage des tâches vers le modèle approprié.

---

## 2. Principes méthodologiques

Cinq principes structurants.

### 2.1 Séparation explicite des rôles

Chaque session IA correspond à un rôle distinct dans le cycle de développement. Quatre rôles identifiés — *Architecte* (conception, doctrine, décisions structurantes), *Implementer* (exécution du plan), *Reviewer* (validation cohérence et qualité), *Maintainer* (refactoring, tests, dette technique). Pas d'usage mixte — chaque session a un rôle déclaré.

### 2.2 Hiérarchie des modèles par tâche

Trois modèles disponibles dans la gamme Claude 4 — Opus 4.7 (capacité maximale, coût élevé), Sonnet 4.6 (capacité élevée, coût modéré), Haiku 4.5 (capacité standard, coût faible). *Le modèle par défaut est Sonnet 4.6 pour Claude Code.* Opus 4.7 est réservé aux tâches qui le justifient (architecture, raisonnement complexe, doctrine). Haiku 4.5 pour tâches répétitives ou de validation simple.

### 2.3 Asynchronisation par défaut

Les sessions Claude.ai (Architecte, Reviewer) produisent des *plans d'action en fichiers* — formalisés, complets, autoportants. Les sessions Claude Code (Implementer, Maintainer) lisent ces fichiers et exécutent en autonomie. Le copier-coller manuel est éliminé. La présence humaine n'est requise que pour l'examen des résultats et la planification de la suite.

### 2.4 Fichiers comme pont entre instances

Le système de fichiers partagés (via Cowork pour Seb, déjà infrastructuré) sert de protocole de communication entre instances IA. Pas de communication synchronisée par chat copié-collé. Un répertoire dédié (`.claude/` à la racine du projet) contient plans d'action, logs de session, états du système.

### 2.5 Discipline de prompt par templates

Les prompts type sont formalisés en templates réutilisables. Pas de prompts ad hoc reconstruits à chaque session. Les templates encodent les critères d'acceptation, le contexte minimal nécessaire, les sorties attendues. Économise le temps de prompting et améliore la prévisibilité des résultats.

---

## 3. Architecture du workflow optimisé

### 3.1 Quatre modes opérationnels distincts

**Mode Architecte (Claude.ai Opus 4.7).**

*Fonction.* Conception doctrinale, décisions structurantes, planification stratégique, élaboration des plans d'action.

*Caractéristiques de session.* Durée typique 30-60 minutes. Densité élevée. Output systématique en fichier markdown structuré (plan d'action, document doctrinal, décision documentée). Pas de production de code substantiel — le code est délégué à Mode Implementer.

*Fréquence.* En début de phase, à chaque jalon majeur, sur frictions doctrinales identifiées.

*Coût horaire estimé.* Élevé (Opus 4.7) mais durée courte. Coût marginal par session typique 2-5 €.

**Mode Implementer (Claude Code Sonnet 4.6 par défaut).**

*Fonction.* Exécution du plan d'action, écriture du code, exécution des tests, gestion des dépendances.

*Caractéristiques de session.* Durée typique 1-3 heures. Autonomie élevée. Lecture du plan d'action en début de session. Production de code, commits Git, rapports de session en fin.

*Fréquence.* Sessions principales du cycle de développement. Plusieurs sessions par semaine en phase active.

*Coût horaire estimé.* Modéré (Sonnet 4.6). Coût marginal par session typique 3-8 €. *Opus 4.7 réservé aux tâches du plan qui le justifient explicitement* (algorithmes complexes, refactoring de grande envergure, debugging difficile).

**Mode Reviewer (Claude.ai Opus 4.7).**

*Fonction.* Validation cohérence doctrinale, identification des frictions, qualité du code produit, recommandations pour la session suivante.

*Caractéristiques de session.* Durée typique 20-45 minutes. Input — état du repo (via Cowork) + logs de session Implementer. Output — rapport de revue en fichier markdown + plan d'action pour session suivante.

*Fréquence.* En fin de chaque session Implementer substantielle ou en fin de jalon.

*Coût horaire estimé.* Élevé (Opus 4.7) mais durée courte. Coût marginal par session typique 2-4 €.

**Mode Maintainer (Claude Code Sonnet 4.6 ou Haiku 4.5 selon tâche).**

*Fonction.* Refactoring, ajout de tests, mise à jour de documentation, dette technique courante.

*Caractéristiques de session.* Durée variable. Autonomie complète sur tâches bien définies. Sonnet 4.6 pour refactoring substantiel, Haiku 4.5 pour formatage, génération de tests unitaires simples, mise à jour de docstrings.

*Fréquence.* Périodique entre les sessions Implementer. Mode batch possible.

*Coût horaire estimé.* Faible à modéré. Coût marginal par session typique 1-4 €.

### 3.2 Cycle de travail standard

```
[Mode Architecte] → produit plan_action_XXX.md dans .claude/plans/
                        ↓
                  (Seb examine et valide)
                        ↓
[Mode Implementer] → lit plan_action_XXX.md, exécute, produit code + log_XXX.md
                        ↓
[Mode Reviewer] → lit code + log, produit revue_XXX.md + plan_action_XXX+1.md
                        ↓
                  (Seb examine et valide)
                        ↓
              [retour Mode Implementer ou Maintainer]
```

*Discipline du cycle.* Chaque transition entre modes passe par un fichier formalisé. Le copier-coller manuel disparaît. La présence de Seb se concentre sur les *points de validation* (examen du plan, examen de la revue), pas sur les *transitions* entre instances.

### 3.3 Discipline de session

*Mode Architecte.* Sessions limitées à 60 minutes. Output obligatoire en fichier. Pas de session ouverte sans plan en sortie.

*Mode Implementer.* Sessions ouvertes par lecture du plan d'action. Critères d'acceptation explicites. Output en code + log de session. Pas de divagation hors du plan — friction signalée et revuée en Mode Reviewer.

*Mode Reviewer.* Sessions limitées à 45 minutes. Input — état du repo + log. Output — rapport de revue + plan suivant.

*Mode Maintainer.* Sessions batch quand possible. Tâches bien définies en amont.

---

## 4. Infrastructure et outils

### 4.1 Système de fichiers partagés

Structure recommandée à la racine du projet `lentite/` :

```
lentite/
├── .claude/
│   ├── plans/                  ← plans d'action produits par Architecte
│   │   ├── plan_action_001.md
│   │   ├── plan_action_002.md
│   │   └── ...
│   ├── logs/                   ← logs de session produits par Implementer
│   │   ├── log_session_001.md
│   │   └── ...
│   ├── reviews/                ← rapports de revue produits par Reviewer
│   │   ├── revue_001.md
│   │   └── ...
│   ├── decisions/              ← décisions structurantes documentées
│   │   ├── decision_001_orchestration_multi_agents.md
│   │   └── ...
│   ├── context/                ← documents de contexte pré-chargés
│   │   ├── doctrine_resume.md  ← résumé court de la doctrine v2.1.1
│   │   ├── etat_projet.md      ← état courant du projet
│   │   └── conventions.md      ← conventions de code et de commit
│   └── README.md               ← point d'entrée du répertoire .claude/
├── (reste du projet)
```

### 4.2 Cowork comme pont d'instances

Seb utilise déjà Cowork pour l'accès aux fichiers locaux dans `atlani-ia/`. *Cowork peut servir de pont entre instances IA* — Claude.ai écrit dans `atlani-ia/lentite/.claude/plans/`, Claude Code dans VS Code lit ces fichiers directement. *Élimination du copier-coller manuel.*

*Discipline d'usage.* Claude.ai (Mode Architecte ou Reviewer) écrit toujours dans le répertoire `.claude/` du projet, jamais directement dans le code source. Le code source est modifié uniquement par Mode Implementer ou Maintainer en Claude Code.

### 4.3 Templates de prompts standardisés

Cinq templates principaux à maintenir dans `.claude/context/templates/`.

— *Template_Architecte_planification.md* — formule pour lancer une session Mode Architecte avec objectif et contraintes.

— *Template_Implementer_execution.md* — formule pour lancer une session Mode Implementer avec référence au plan d'action.

— *Template_Reviewer_revue.md* — formule pour lancer une session Mode Reviewer avec référence au code et au log.

— *Template_Maintainer_refactoring.md* — formule pour lancer une session Mode Maintainer.

— *Template_decision_structurante.md* — formule pour documenter une décision avec options examinées, recommandation, motif.

### 4.4 Format standardisé des plans d'action

Tout plan d'action produit par Mode Architecte respecte un format pour faciliter sa lecture par Mode Implementer.

```markdown
# Plan d'action XXX — [Titre court]

## 1. Contexte
[1-3 paragraphes sur la situation actuelle, l'historique pertinent, les décisions déjà prises]

## 2. Objectif
[1 phrase sur l'objectif principal de la session Implementer]

## 3. Critères d'acceptation
- [ ] Critère 1 — vérifiable de manière objective
- [ ] Critère 2 — vérifiable de manière objective
- [ ] Critère 3 — vérifiable de manière objective

## 4. Tâches détaillées
### 4.1 Tâche A
Description, fichiers concernés, dépendances, livrable attendu.
### 4.2 Tâche B
...

## 5. Anti-tâches
[Choses à NE PAS faire dans cette session — délimite le périmètre]

## 6. Output attendu en fin de session
- Code écrit/modifié dans les fichiers X, Y, Z
- Tests passants
- Commit Git avec message conventionnel
- Log de session log_session_XXX.md produit

## 7. Modèle recommandé
[Sonnet 4.6 par défaut / Opus 4.7 si justifié]

## 8. Estimation
- Durée : X minutes
- Coût marginal estimé : Y €
```

### 4.5 Format standardisé des logs de session

Tout log produit par Mode Implementer respecte un format pour faciliter la lecture par Mode Reviewer.

```markdown
# Log de session XXX — [Date]

## 1. Plan d'action référencé
plan_action_XXX.md

## 2. Tâches accomplies
- [x] Tâche A — résumé court
- [x] Tâche B — résumé court
- [ ] Tâche C — non terminée, raison

## 3. Frictions identifiées
[Éventuelles frictions méthodologiques, choix interprétatifs, ambiguïtés du plan]

## 4. Modifications de code
[Liste des fichiers modifiés avec résumé en une ligne par fichier]

## 5. Tests
[État des tests — passants, ajoutés, modifiés]

## 6. Commits
[Liste des commits avec hash court et message]

## 7. État du système
[Le code est-il fonctionnel ? Y a-t-il des dépendances cassées ?]

## 8. Recommandations pour Mode Reviewer
[Éventuels points à examiner en priorité]
```

---

## 5. Hiérarchie des modèles par tâche

Table de référence pour le routage. *À utiliser systématiquement pour chaque tâche.*

| Type de tâche | Modèle recommandé | Justification |
|---|---|---|
| Conception architecturale | Opus 4.7 | raisonnement complexe sur trade-offs |
| Décision doctrinale | Opus 4.7 | examen multi-critères et écriture argumentée |
| Production de plan d'action | Opus 4.7 | qualité de structuration des tâches |
| Revue de cohérence doctrinale | Opus 4.7 | identification fine des frictions |
| Implémentation de fonction | Sonnet 4.6 | équilibre qualité/coût pour code standard |
| Refactoring substantiel | Sonnet 4.6 | compréhension du code existant |
| Ajout de tests d'intégration | Sonnet 4.6 | conception cohérente du parcours testé |
| Debugging complexe | Opus 4.7 | raisonnement sur causes multiples |
| Génération de tests unitaires simples | Haiku 4.5 | tâche bien définie, peu créative |
| Formatage / linting | Haiku 4.5 | tâche déterministe |
| Mise à jour de docstrings | Haiku 4.5 | tâche standardisée |
| Génération de commits message | Haiku 4.5 | format standard |
| Validation YAML / schémas | Haiku 4.5 | tâche déterministe |

**Règle d'or.** En cas de doute, *partir du modèle moins capable et basculer vers le modèle plus capable seulement si nécessaire*. La friction productive révèle le besoin du modèle supérieur. Ne pas surdimensionner par anticipation.

---

## 6. Discipline anti-coût

Cinq disciplines opérationnelles pour maîtriser le coût d'usage.

### 6.1 Sessions Claude.ai limitées en durée

Sessions Mode Architecte et Mode Reviewer plafonnées à 45-60 minutes. La densité est privilégiée sur la durée. *Si une session dépasse 60 minutes, c'est un signal de planification insuffisante en amont.*

### 6.2 Claude Code Sonnet 4.6 par défaut

Configuration Claude Code en Sonnet 4.6 comme modèle par défaut. Opus 4.7 activé uniquement sur tâches explicitement marquées dans le plan d'action ou sur friction non résolue par Sonnet.

### 6.3 Cache contextuel par fichiers de référence

Le répertoire `.claude/context/` contient résumé doctrine, état projet, conventions. *Le système doit lire ces fichiers une fois par session, pas re-saisir le contexte à chaque prompt.* Réduit les tokens entrants substantiellement.

### 6.4 Mode batch quand possible

Tâches Maintainer (refactoring, tests, documentation) regroupées en sessions batch plutôt que dispersées. Économise les coûts d'initialisation de session.

### 6.5 Évaluation périodique des coûts

Mensuellement, examen des coûts API par mode opérationnel. Si un mode dépasse le budget, examen des prompts et des sessions pour identifier les inefficacités.

---

## 7. Estimation des gains

Hypothèses de calcul — workflow actuel vs workflow optimisé sur projet L'Entité au rythme actuel.

| Dimension | Workflow actuel | Workflow optimisé | Gain |
|---|---|---|---|
| Temps de présence Seb par cycle | 2-3h synchronisé | 30-45 min validation | ~70% |
| Coût API par cycle | ~25-40 € (Opus partout) | ~10-15 € (modèles hiérarchisés) | ~55% |
| Copier-coller manuel | systématique | éliminé (Cowork pont) | 100% |
| Latence entre conception et exécution | immédiate mais bloquante | différée, non bloquante | conception/exécution découplées |
| Traçabilité (fichiers logs) | minimale | systématique | substantielle |

Estimation conservatrice — *au moins 50% de gain sur temps et coût combinés*. Plus probable — 60-70% de gain sur le temps de présence du porteur, 40-60% de gain sur le coût API.

---

## 8. Mise en œuvre progressive

Quatre phases d'adoption sur 2-3 semaines.

### Phase 1 — Mise en place de l'infrastructure (jour 1-3)

— Création du répertoire `.claude/` dans `atlani-ia/lentite/`.

— Production des fichiers de contexte initiaux (`doctrine_resume.md`, `etat_projet.md`, `conventions.md`).

— Configuration de Cowork pour accès à `.claude/`.

— Configuration de Claude Code en Sonnet 4.6 par défaut.

### Phase 2 — Production des templates de prompts (jour 3-7)

— Production des cinq templates principaux.

— Test de chaque template sur une tâche pilote.

— Itération sur la qualité des templates.

### Phase 3 — Cycles asynchrones (semaine 2)

— Premier cycle complet Architecte → Implementer → Reviewer sur tâche réelle (par exemple Phase 0 codage — production du Plan de codage v0.1).

— Examen des frictions, ajustement des templates et de la méthode.

### Phase 4 — Optimisation continue (semaine 3+)

— Mesure des coûts et temps réels.

— Ajustement de la hiérarchie des modèles selon retours.

— Documentation des leçons apprises au journal méthodologique.

---

## 9. Application immédiate à la Phase 0 du codage de L'Entité

La Phase 0 du codage (cinq décisions structurantes + prototype technique minimal) peut être *le premier cycle de mise en œuvre de cette méthode*.

**Cycle proposé.**

1. *Mode Architecte (Claude.ai Opus 4.7) — session 1.* Production du document `plan_action_phase_0.md` qui détaille les cinq décisions structurantes avec options examinées et recommandations. Output dans `.claude/plans/`.

2. *Seb examine et prend position* sur les cinq décisions. Production de cinq fichiers de décision dans `.claude/decisions/`.

3. *Mode Architecte — session 2.* Production du document `plan_action_phase_0_prototype.md` qui spécifie le prototype technique minimal sur la base des décisions prises.

4. *Mode Implementer (Claude Code Sonnet 4.6) — session 1.* Exécution du plan de prototype. Output — code dans `prototype/` + log de session.

5. *Mode Reviewer (Claude.ai Opus 4.7) — session 1.* Examen du prototype. Identification des frictions. Production de `revue_001.md` et `plan_action_phase_1_pipeline.md`.

6. *Itération.*

**Bénéfice attendu.** La Phase 0 sert simultanément à (a) prendre les décisions structurantes nécessaires au codage substantiel, (b) éprouver la méthode de travail collaboratif IA sur un cycle réel, (c) générer les premiers logs de session qui alimentent l'apprentissage de la méthode elle-même.

---

## 10. Inscription au projet et discipline

**Inscription.** Document `dev/methodologie_workflow_collaboratif_ia_v1.md` à archiver dans la couche méthodologique de développement, en complément de `dev/methodologie_codage_v1.md`. Les deux documents sont complémentaires — l'un spécifie le quoi coder, l'autre spécifie le comment travailler avec les IA pour coder.

**Discipline anti-cumul.** Les versions successives de cette méthode remplacent les précédentes (v1.0 → v1.1 → v2 si refonte). Pas d'accumulation de versions parallèles.

**Inscription au journal général.** Décision méthodologique 8.6 (nouvelle) — *adoption d'une méthode de travail collaboratif IA distincte de la méthode de codage*. À ajouter dans le journal méthodologique général à la prochaine révision.

**Discipline append-only sur les logs.** Les logs de session, les revues, les plans d'action ne sont jamais supprimés. Ils alimentent la mémoire institutionnelle de la collaboration humain ↔ IA sur le projet.

---

## 11. Limites de la méthode et garde-fous

Cinq limites identifiées avec garde-fous.

*Limite 1 — la méthode présuppose une qualité minimale des plans d'action.* Si Mode Architecte produit des plans flous ou incomplets, Mode Implementer perd en autonomie et la friction réapparaît. *Garde-fou* — discipline de critères d'acceptation explicites, format standardisé.

*Limite 2 — les sessions Implementer en autonomie longue peuvent diverger de la doctrine.* *Garde-fou* — Mode Reviewer systématique en fin de session substantielle, frictions tracées au log.

*Limite 3 — le cache contextuel par fichiers peut devenir obsolète.* *Garde-fou* — discipline de mise à jour de `.claude/context/` à chaque évolution doctrinale majeure.

*Limite 4 — la hiérarchie des modèles peut être trop conservatrice et brider la qualité.* *Garde-fou* — révision périodique du routage par retour d'expérience, basculement vers modèle supérieur sur friction.

*Limite 5 — la méthode demande discipline du porteur (Seb).* *Garde-fou* — templates qui rendent la discipline opérationnelle plus naturelle, mesure périodique des gains pour maintenir la motivation.

---

## 12. Premier livrable concret recommandé

Après validation de cette méthode par Seb, *production immédiate du `plan_action_phase_0.md`* qui sera le premier plan produit selon la méthode. Document qui formalise la demande des cinq décisions structurantes de la Phase 0 du codage avec options, recommandations, format de réponse attendu.

*Volume estimé du plan d'action Phase 0.* ~2000-2500 mots. Production en une session Mode Architecte.

*Une fois le plan validé par Seb, le premier cycle complet de la méthode est engagé.* La méthode s'éprouve sur cas réel — la Phase 0 du codage de L'Entité.

---

*Méthode v1.0 — édité le 17 mai 2026. À réviser après premier cycle complet d'application (Phase 0 codage). Inscrit dans la couche méthodologique de développement du projet. Document opérationnel adressé au porteur principal.*
