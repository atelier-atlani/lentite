# L'Entité — Conventions de code et de projet

*Document de cache contextuel pour pré-chargement en début de session par toutes les instances IA, particulièrement Mode Implementer et Mode Maintainer. Conventions opérationnelles à respecter dans toute session de code. À lire avant toute modification du repo.*

---

## 1. Conventions Python

### 1.1 Version et environnement

- *Python 3.11+* (requis pour cohérence avec pipeline existant).
- *Pydantic 2.13+* pour tous les modèles de données.
- *PyYAML* pour parsing YAML.
- *Environnement virtuel recommandé* — venv ou poetry selon préférence à arbitrer en Phase 0.
- *Installation des dépendances* avec `pip install --break-system-packages` sur macOS (contrainte environnement).

### 1.2 Style

- *PEP 8 strict* — appliqué automatiquement par `black`.
- *Black* pour formatage (ligne max 100 caractères).
- *Ruff* pour linting (configuration permissive au démarrage, durcissement progressif).
- *mypy* pour type checking statique (mode `strict` quand possible).

### 1.3 Typage

- *Typage obligatoire* sur toute fonction publique (signature + retour).
- *Pydantic v2* pour tous les modèles de données échangés (schémas d'analyses).
- *typing* standard pour types internes (`List`, `Dict`, `Optional`, `Union`, `Tuple`).
- *Pas de `Any`* sauf justification explicite en commentaire.

### 1.4 Docstrings

- *Format Google* préféré (ou NumPy selon convention équipe future).
- *Obligatoires* sur tout module exposé (fonctions, classes, méthodes publiques).
- *Première ligne* — résumé court (une phrase, terminée par un point).
- *Sections* — `Args:`, `Returns:`, `Raises:`, `Examples:` quand pertinent.

### 1.5 Organisation des fichiers

- *Un fichier par responsabilité* (module avec rôle clair).
- *Pas de fichiers de plus de 500 lignes* — refactorer en sous-modules.
- *Imports* triés (`isort` ou équivalent) — standard library, third-party, local.

---

## 2. Conventions de nommage

### 2.1 Fichiers et dossiers

- *Snake_case* pour les fichiers Python et YAML.
- *kebab-case* possible pour fichiers markdown destinés à la lecture humaine si plus naturel.
- *Pas d'espaces* ni *caractères spéciaux* dans les noms de fichiers de code.
- *Pas d'accents* dans les noms (réservés à la documentation humaine).

### 2.2 Versions de documents canoniques

- Format — `nom_du_document_vX_Y.md` (par exemple `gabarit_v2_1.md`).
- *Versions mineures* (v2_1, v2_2) — évolutions compatibles.
- *Versions majeures* (v2, v3) — refonte invalidant rétrocompatibilité.

### 2.3 Identifiants d'analyses

- Format — `METHODE_LOCUTEUR_DOCUMENT_DATE_vX_Y` (par exemple `M01_BAYROU_DPG_20250114_v2_1`).
- *Dates* en format `YYYYMMDD`.
- *Pas d'espaces*, *pas de caractères spéciaux*.

### 2.4 Identifiants d'objets thématiques et visés

- Objets thématiques — `OT1`, `OT2`, `OT3`, etc.
- Objets visés — `OV1`, `OV2`, `OV3`, etc. (ou `OV_A`, `OV_B` dans applications M03).
- Unités argumentatives — `U1`, `U2`, `U3`, etc.
- Propositions structurantes (M03) — `P1`, `P2`, `P3`, etc.

---

## 3. Conventions Git

### 3.1 Branches

- `main` — production stable, code testé et validé.
- `develop` — intégration des features en cours.
- `feature/nom-feature` — développement d'une feature isolée.
- `fix/nom-bug` — correction de bug.
- `release/vX_Y` — préparation d'une release.

### 3.2 Commits — Conventional Commits

Format — `<type>(<scope>): <description>`

Types principaux —
- `feat` — nouvelle feature.
- `fix` — correction de bug.
- `docs` — documentation.
- `refactor` — refactoring sans changement de comportement.
- `test` — ajout ou modification de tests.
- `chore` — tâches de maintenance.

Exemples —
- `feat(m01): add validator for hypothesis_gap`
- `fix(schemas): correct EnumValue in ObservableEffectType`
- `docs(README): update analyses count to 7 M01`
- `refactor(validate): split CLI logic from validation logic`

### 3.3 Pull requests

- *Une PR par feature ou correction*.
- *Description claire* — contexte, changements, tests effectués.
- *Lien vers le plan d'action* `.claude/plans/plan_action_XXX.md` si applicable.

### 3.4 Tags

- *Semver strict* — `vMAJOR.MINOR.PATCH`.
- Cohérent avec la version de doctrine quand approprié.
- Tags signés recommandés à partir de v1.0.0.

---

## 4. Conventions YAML d'analyses

### 4.1 Structure conforme aux schémas Pydantic

- *Tout YAML d'analyse* doit valider contre `pipeline/schemas.py` (M01) ou `pipeline/schemas_m03.py` (M03).
- *Pas de modification ad hoc* de typologie — friction productive → inscription au `typology_audit` pour examen ultérieur.

### 4.2 Champs obligatoires

- `method_id`, `method_version`, `analysis_id`, `execution_date`, `execution_mode`.
- *Champs typés* selon les enum Pydantic (jamais de valeurs libres en français).

### 4.3 Style YAML

- *Indentation* — 2 espaces (jamais de tabs).
- *Listes en notation tirets* (`- item`) pour lisibilité.
- *Strings longues* en pipe (`|`) ou folded (`>`) selon besoin.
- *Pas de guillemets* sauf nécessaire (caractères spéciaux, ambiguïté).

---

## 5. Conventions de tests

### 5.1 Structure

- *Tests unitaires* dans `tests/unit/` (cœur métier — schemas, validators, logique).
- *Tests d'intégration* dans `tests/integration/` (pipeline complet).
- *Tests de régression* dans `tests/regression/` (cas de référence).
- *Tests négatifs* dans `pipeline/tests/` (YAML invalides validant les contraintes mordantes).

### 5.2 Convention de nommage

- *Test files* — `test_<module>.py`.
- *Test functions* — `test_<comportement_attendu>`.
- *Fixtures* — dans `conftest.py` du répertoire concerné.

### 5.3 Couverture

- *Couverture cible* — 80% minimum sur cœur métier.
- *Couverture comparative* pour pipeline — concordance avec analyses humaines validées.

---

## 6. Disciplines spécifiques au projet

### 6.1 Discipline anti-cumul

- *Un seul document canonique par version*.
- *Versions antérieures* archivées au journal, pas accumulées en parallèle.
- Lors de mise à jour — *remplacement*, pas accumulation.

### 6.2 Discipline append-only sur journaux et logs

- *Entrées datées* dans le journal méthodologique général et les journaux des méthodes.
- *Pas de suppression* d'entrées passées — révisions par nouvelle entrée référençant la précédente.
- *Logs de session* dans `.claude/logs/` jamais supprimés.

### 6.3 Discipline de séparation H/M/P

- *Sorties M01* — trois fichiers distincts (M01-H humaine, M01-M machine, M01-P publique).
- *Pas de mélange* — chaque format respecte son public et ses contraintes.

### 6.4 Discipline du typology_audit

- *Friction productive du pipeline* → inscription au typology_audit dans le journal de l'analyse.
- *Pas de modification ad hoc* de la typologie ObservableEffectType ou ArenaRelationType.
- *Extension typologique* uniquement après accumulation de 2-3 cas externes documentables.

### 6.5 Discipline de validation Pydantic

- *Aucune sortie M01-M ou M03-M* ne quitte le système sans avoir validé contre le schéma.
- *Tests négatifs* obligatoires pour toute contrainte critique ajoutée au schéma.

### 6.6 Discipline d'anonymisation des agents IA (architecture cible v2)

- Chaque agent ne connaît que son rôle.
- Pas de partage d'identité entre agents dans l'architecture multi-agents future.
- Cohérent avec l'autonomie épistémique du projet.

---

## 7. Conventions du workflow collaboratif IA

### 7.1 Référence

Méthode complète dans `dev/methodologie_workflow_collaboratif_ia_v1.md`.

### 7.2 Discipline minimale opérationnelle

- *Tout cycle de travail substantiel* — passage par un plan d'action dans `.claude/plans/` puis log de session dans `.claude/logs/`.
- *Le copier-coller manuel entre instances est proscrit* — fichiers comme pont.
- *Modèles hiérarchisés* — Sonnet 4.6 par défaut pour code, Opus 4.7 pour architecture/revue, Haiku 4.5 pour tâches déterministes.

---

*Conventions v1.0 — créé le 17 mai 2026. À mettre à jour aux évolutions des bonnes pratiques (par exemple migration vers Python 3.13, adoption de uv pour gestion d'environnement, etc.). Document de référence opérationnelle, à lire en début de toute session de code.*
