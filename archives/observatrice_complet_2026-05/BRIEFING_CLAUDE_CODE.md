# BRIEFING — Entité IA d'observation critique du réel
## Pour Claude Code — Lire en premier

---

## CE QU'ON CONSTRUIT

Un système multi-agents Python qui :
1. Prend un dossier de sources textuelles en entrée
2. Lance un workflow séquentiel/parallèle avec 6 agents Claude
3. Produit une analyse structurée et révisée
4. Maintient une mémoire persistante entre les runs

---

## ARCHITECTURE CIBLE

```
entite_observatrice/
├── main.py                    # CLI
├── requirements.txt
├── .env
├── config.py
│
├── agents/
│   ├── pool.py                # AgentPool — appels Anthropic API
│   └── prompts/               # Prompts système par agent
│       ├── entity/
│       │   ├── v1.2.md        ← EXISTE déjà (voir plus bas)
│       │   └── current.txt    ← contient "v1.2"
│       ├── contradictory/
│       │   ├── v1.1.md        ← EXISTE déjà
│       │   └── current.txt
│       ├── economist/
│       │   ├── v1.1.md        ← EXISTE déjà
│       │   └── current.txt
│       ├── jurist/
│       │   ├── v1.0.md        ← EXISTE déjà
│       │   └── current.txt
│       ├── sociologist/
│       │   ├── v1.0.md        ← EXISTE déjà
│       │   └── current.txt
│       └── discourse_analyst/
│           ├── v1.1.md        ← EXISTE déjà
│           └── current.txt
│
├── workflow/
│   ├── engine.py              # WorkflowEngine
│   └── state.py               # WorkflowState
│
├── memory/
│   ├── store.py               # MemoryStore (JSON → SQLite)
│   └── schemas.py             # Modèles de données
│
├── documents/
│   ├── store.py               # DocumentStore
│   └── ingest.py              # Chargement des sources
│
├── data/
│   ├── memory.json            # Mémoire persistante (MVP)
│   └── memory_initial.json    ← EXISTE déjà (voir plus bas)
│
└── outputs/
    ├── runs/                  # Étapes intermédiaires par run
    └── analyses/              # Analyses finales
```

---

## WORKFLOW DÉTAILLÉ

```
T1  Entité (entity v1.2) — Analyse principale
T2  Contradicteur (contradictory v1.1) — Attaque
T3  Entité — Révision après contradicteur
T4  4 agents en PARALLÈLE :
     - Économiste (economist v1.1)
     - Juriste (jurist v1.0)
     - Sociologue (sociologist v1.0)
     - Analyste discours (discourse_analyst v1.1)
T5  Entité — Synthèse finale consolidée
```

---

## MODÈLE

```python
MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS_MAIN = 4000    # T1, T3, T5
MAX_TOKENS_ATTACK = 2000  # T2
MAX_TOKENS_SPEC = 2500    # T4 agents spécialisés
```

---

## MÉMOIRE INITIALE

Le fichier `data/memory_initial.json` contient déjà 3 dossiers
analysés (Loi Climat, Guerre Iran, Loi Immigration), 6 erreurs
typées, 2 hypothèses ouvertes, et 4 patterns.

À copier vers `data/memory.json` au premier lancement si
`memory.json` n'existe pas.

Structure JSON :
```json
{
  "r1_analyses": [],
  "r2_errors": [],
  "r3_hypotheses": [],
  "r4_calibrations": [],
  "r5_patterns": []
}
```

---

## RÈGLES D'IMPLÉMENTATION

1. **Pas de framework agent** (LangGraph, LangChain, etc.)
   → Python pur + anthropic SDK + concurrent.futures

2. **Sauvegarde à chaque étape**
   → Si T5 plante, ne pas relancer depuis T1

3. **Mémoire en JSON pour le MVP**
   → Pas de SQLite tout de suite

4. **Prompts chargés depuis fichiers**
   → Ne jamais hardcoder un prompt dans le code

5. **Logs clairs**
   → Afficher quelle étape tourne, combien de tokens

6. **Variables d'environnement**
   → ANTHROPIC_API_KEY dans .env, jamais dans le code

---

## ORDRE DE BUILD

Session 1 : Structure + AgentPool
Session 2 : MemoryStore + consultation
Session 3 : WorkflowEngine T1-T3
Session 4 : WorkflowEngine T4 parallèle + T5
Session 5 : CLI + test end-to-end complet
Session 6 : Fix bugs + polish

---

## PREMIER TEST ATTENDU

```bash
python main.py analyze \
  --titre "Test minimal" \
  --source "La loi X a été adoptée le Y."

# Doit produire :
# outputs/analyses/Test_minimal.md
# data/memory.json mis à jour
```
