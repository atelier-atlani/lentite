# Étape 5 — Architecture technique
## Entité IA d'observation critique du réel
## Design complet du système

---

## PRINCIPE D'ARCHITECTURE

Le protocole est un **workflow multi-agents avec état persistant**.
Trois contraintes structurantes :

1. **État persistant** : la mémoire (5 registres) survit entre les dossiers
2. **Multi-agents séquentiels/parallèles** : T1→T2→T3 séquentiel,
   T4 (4 agents) parallèle, T5→T6 séquentiel
3. **Traçabilité totale** : chaque affirmation doit être reliée
   à sa source et à la version du prompt qui l'a produite

---

## VUE D'ENSEMBLE

```
┌─────────────────────────────────────────────────────────────────┐
│                        INTERFACE                                │
│           (CLI / API REST / Interface web future)               │
└─────────────────────┬───────────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│                   ORCHESTRATEUR                                 │
│         Gère le workflow T1→T8, le routage entre agents,        │
│         la gestion des erreurs et la reprise d'état             │
└──┬──────────┬──────────┬──────────┬──────────┬─────────────────┘
   │          │          │          │          │
   ▼          ▼          ▼          ▼          ▼
┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────────────┐
│Agent │  │Agent │  │Agent │  │Agent │  │   Agent       │
│Entité│  │Contrad│  │Éco.  │  │Juris.│  │Socio./Discours│
│v1.2  │  │v1.1  │  │v1.1  │  │v1.0  │  │v1.0 / v1.1   │
└──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘  └──────┬────────┘
   │         │          │          │             │
   └─────────┴──────────┴──────────┴─────────────┘
                         │
┌─────────────────────────▼───────────────────────────────────────┐
│                    COUCHE DE DONNÉES                            │
├────────────┬────────────┬────────────┬───────────┬─────────────┤
│DocumentStore│VectorStore │MemoryStore │OutputStore│PromptStore  │
│(sources brutes│(embeddings│(5 registres│(analyses  │(versions    │
│+ metadata) │sémantiques)│persistants)│versionnées)│des prompts) │
└────────────┴────────────┴────────────┴───────────┴─────────────┘
```

---

## COMPOSANTS

### 1. DocumentStore

Stocke les sources brutes d'un dossier avec leurs métadonnées.

```python
# Structure d'un document
{
  "id": "doc_uuid",
  "dossier_id": "dossier_uuid",
  "source_url": "https://...",
  "source_type": "loi|rapport|presse|discours|statistique",
  "date": "2024-01-26",
  "auteur": "Légifrance",
  "institution": "Parlement français",
  "fiabilite_estimee": "haute|moyenne|faible",
  "biais_possible": "officiel|militant|...",
  "contenu_brut": "...",
  "contenu_extrait": "...",  # après preprocessing
  "langue": "fr",
  "indexe_le": "2026-05-14T10:00:00"
}
```

**Technologie** : PostgreSQL avec extension `pgvector`
ou SQLite pour le MVP.

---

### 2. VectorStore

Embeddings sémantiques des documents pour la recherche
par concept plutôt que par mot-clé exact.

Usage principal :
- Trouver les passages sources lors de la construction d'analyses
- Relier une affirmation à ses sources (traçabilité)
- Trouver des dossiers similaires dans la mémoire

```python
# Requête type
results = vector_store.search(
    query="métiers en tension régularisation employeur",
    dossier_id="dossier_immigration_2024",  # limiter au dossier courant
    top_k=5
)
# → retourne les passages sources les plus pertinents
```

**Technologie** : `pgvector` (PostgreSQL) ou `Chroma`/`Qdrant`
pour le MVP.

---

### 3. AgentPool

Gère les appels aux modèles de langage avec injection
des prompts système corrects et gestion du contexte.

```python
class AgentPool:
    def __init__(self, prompt_store: PromptStore):
        self.prompts = prompt_store
        self.client = anthropic.Anthropic()

    def call(
        self,
        agent_type: str,           # "entity" | "contradictory" | "economist" ...
        prompt_version: str,       # "v1.2" | "v1.1" ...
        user_message: str,
        context: dict,             # dossier, outputs précédents, mémoire consultée
        max_tokens: int = 4000
    ) -> AgentOutput:

        system = self.prompts.get(agent_type, prompt_version)

        # Injection du contexte mémoire dans le user_message
        full_message = self._build_message(user_message, context)

        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": full_message}]
        )

        return AgentOutput(
            agent_type=agent_type,
            prompt_version=prompt_version,
            content=response.content[0].text,
            tokens_used=response.usage.input_tokens + response.usage.output_tokens,
            timestamp=datetime.now()
        )
```

---

### 4. WorkflowEngine

Orchestre la séquence complète T1→T8.
Gère l'état du workflow pour permettre la reprise en cas d'échec.

```python
class WorkflowEngine:
    def __init__(self, agent_pool, memory_store, output_store):
        self.agents = agent_pool
        self.memory = memory_store
        self.outputs = output_store

    def run(self, dossier: Dossier) -> AnalysisResult:

        state = WorkflowState(dossier_id=dossier.id)

        # --- PRÉ-ANALYSE : consultation mémoire ---
        state.memory_consultation = self.memory.consult(dossier)

        # --- T1 : Analyse principale ---
        state.t1 = self.agents.call(
            agent_type="entity",
            prompt_version="v1.2",
            user_message=self._build_t1_prompt(dossier, state.memory_consultation),
            context={"dossier": dossier, "memory": state.memory_consultation}
        )
        self.outputs.save(state.t1, step="T1", dossier_id=dossier.id)

        # --- T2 : Agent contradicteur ---
        state.t2 = self.agents.call(
            agent_type="contradictory",
            prompt_version="v1.1",
            user_message=state.t1.content,
            context={"dossier": dossier}
        )

        # --- T3 : Réponse entité aux objections ---
        state.t3 = self.agents.call(
            agent_type="entity",
            prompt_version="v1.2",
            user_message=self._build_t3_prompt(state.t1, state.t2),
            context={"dossier": dossier, "t1": state.t1, "t2": state.t2}
        )

        # --- T4 : Agents spécialisés EN PARALLÈLE ---
        specialized = ["economist", "jurist", "sociologist", "discourse_analyst"]
        previous_outputs = []  # pour non-répétition

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {
                executor.submit(
                    self.agents.call,
                    agent_type=agent,
                    prompt_version="v1.1" if agent in ["economist","discourse_analyst"] else "v1.0",
                    user_message=self._build_t4_prompt(state.t3, previous_outputs),
                    context={"dossier": dossier, "t3": state.t3, "previous": previous_outputs}
                ): agent
                for agent in specialized
            }
            state.t4 = {futures[f]: f.result() for f in as_completed(futures)}

        # --- T5 : Intégration + synthèse finale ---
        state.t5 = self.agents.call(
            agent_type="entity",
            prompt_version="v1.2",
            user_message=self._build_synthesis_prompt(state),
            context={"all_outputs": state}
        )

        # --- POST-ANALYSE : mise à jour mémoire ---
        self.memory.update(state)

        return AnalysisResult(state=state, dossier=dossier)
```

---

### 5. MemoryStore

Implémentation des 5 registres avec consultation et mise à jour.

```python
class MemoryStore:

    # --- CONSULTATION PRÉ-ANALYSE ---
    def consult(self, dossier: Dossier) -> MemoryConsultation:
        return MemoryConsultation(
            similar_dossiers=self._find_similar(dossier),      # Registre 1
            errors_to_watch=self._get_errors(dossier.type),    # Registre 2
            open_hypotheses=self._get_open_hypotheses(dossier), # Registre 3
            method_recommendation=self._get_method(dossier.type), # Registre 4
            applicable_patterns=self._get_patterns(dossier)    # Registre 5
        )

    # --- MISE À JOUR POST-ANALYSE ---
    def update(self, state: WorkflowState):
        with self.db.transaction():
            self._archive_analysis(state)        # Registre 1
            self._record_errors(state)           # Registre 2
            self._update_hypotheses(state)       # Registre 3
            self._update_method_calibration(state) # Registre 4
            self._update_patterns(state)         # Registre 5

    # Registre 1 — trouver des dossiers similaires
    def _find_similar(self, dossier: Dossier) -> List[ArchivedAnalysis]:
        # Recherche par type d'objet + registre discursif + secteurs
        return self.db.query("""
            SELECT * FROM analyses
            WHERE object_type = ? OR discourse_register = ?
            ORDER BY date DESC
            LIMIT 5
        """, dossier.object_type, dossier.discourse_register)
```

**Schéma de base de données** → voir `etape_5_schemas_donnees.md`

---

### 6. PromptStore

Versionne les prompts système. Permet de tracer quelle version
a produit quelle analyse.

```python
class PromptStore:
    def get(self, agent_type: str, version: str) -> str:
        # Charge depuis le système de fichiers
        path = f"prompts/{agent_type}/{version}.md"
        return open(path).read()

    def get_current(self, agent_type: str) -> tuple[str, str]:
        # Retourne (version_actuelle, contenu)
        return self.versions[agent_type], self.get(agent_type, self.versions[agent_type])
```

Structure des fichiers :
```
prompts/
  entity/
    v1.0.md
    v1.1.md
    v1.2.md         ← current
    current.txt     ← contient "v1.2"
  contradictory/
    v1.0.md
    v1.1.md         ← current
    current.txt
  economist/
    v1.0.md
    v1.1.md         ← current
    current.txt
  jurist/
    v1.0.md         ← current
    current.txt
  sociologist/
    v1.0.md         ← current
    current.txt
  discourse_analyst/
    v1.0.md
    v1.1.md         ← current
    current.txt
```

---

## FLUX DE DONNÉES COMPLET

```
1. Utilisateur soumet un dossier
   → liste de sources (URLs, PDFs, textes)

2. DocumentStore ingère les sources
   → préprocessing, extraction, métadonnées

3. VectorStore indexe les documents
   → embeddings pour recherche sémantique

4. MemoryStore consulté
   → dossiers similaires, erreurs à surveiller,
     patterns applicables, méthode recommandée

5. WorkflowEngine lance T1
   → AgentPool appelle l'entité avec :
     - prompt système v1.2
     - dossier preprocessé
     - résultat consultation mémoire
     - §0 pre-rempli avec patterns

6. T2 : contradicteur reçoit output T1
7. T3 : entité reçoit T1 + T2
8. T4 : 4 agents en parallèle reçoivent T3
9. T5 : entité reçoit T3 + tous T4

10. OutputStore sauvegarde l'analyse finale
    → markdown + JSON structuré + liens sources

11. MemoryStore mis à jour
    → 5 registres actualisés atomiquement
```

---

## CHOIX TECHNOLOGIQUES

### MVP (implémentable en 1-2 semaines)

| Composant | Technologie | Justification |
|-----------|-------------|---------------|
| Orchestrateur | Python pur | Simple, debuggable |
| Agents | Anthropic SDK | Direct |
| DocumentStore | SQLite | Pas de serveur |
| VectorStore | ChromaDB local | Pas de serveur |
| MemoryStore | JSON files / SQLite | Simple |
| OutputStore | Fichiers markdown | Lisibles directement |
| Parallélisme T4 | `concurrent.futures` | Natif Python |

### Production (2-3 mois)

| Composant | Technologie | Justification |
|-----------|-------------|---------------|
| Orchestrateur | LangGraph | Workflow graphe, reprise d'état |
| Agents | Anthropic SDK | Direct |
| DocumentStore | PostgreSQL | Robuste, requêtes |
| VectorStore | pgvector | Intégré PostgreSQL |
| MemoryStore | PostgreSQL | Transactions ACID |
| OutputStore | S3 + PostgreSQL | Scalable |
| API | FastAPI | Async, rapide |
| Interface | React | À construire si besoin |

---

## STRUCTURE DU PROJET

```
entite_observatrice/
├── main.py                    # Point d'entrée CLI
├── config.py                  # Configuration
│
├── workflow/
│   ├── engine.py              # WorkflowEngine
│   ├── state.py               # WorkflowState, AgentOutput
│   └── steps.py               # Logique T1-T8
│
├── agents/
│   ├── pool.py                # AgentPool
│   └── prompts/               # ← contenu des fichiers .md
│       ├── entity/
│       ├── contradictory/
│       ├── economist/
│       ├── jurist/
│       ├── sociologist/
│       └── discourse_analyst/
│
├── memory/
│   ├── store.py               # MemoryStore
│   ├── consultation.py        # Logique de consultation
│   ├── update.py              # Logique de mise à jour
│   └── schemas.py             # Modèles de données
│
├── documents/
│   ├── store.py               # DocumentStore
│   ├── ingest.py              # Ingestion de sources
│   └── preprocessor.py        # Nettoyage, extraction
│
├── vectors/
│   └── store.py               # VectorStore
│
├── outputs/
│   ├── store.py               # OutputStore
│   ├── formatters.py          # Markdown, JSON
│   └── analyses/              # Analyses sauvegardées
│
├── data/
│   ├── memory.db              # SQLite (MVP)
│   └── vectors/               # ChromaDB (MVP)
│
└── tests/
    ├── test_workflow.py
    ├── test_memory.py
    └── fixtures/
        └── loi_climat_dossier.json
```

---

## POINTS DE DÉCISION TECHNIQUES

### PD1 — Gestion du contexte entre agents

Problème : chaque agent doit recevoir les outputs précédents
sans dépasser la fenêtre de contexte.

Solution MVP :
```python
def _build_t4_prompt(self, t3_output: AgentOutput, agent_type: str) -> str:
    # Résumer T1+T2+T3 si trop longs
    summary = self._summarize_if_needed(t3_output, max_tokens=2000)
    return f"""
Voici l'analyse révisée (après contradicteur) :
{summary}

Tu es l'agent {agent_type}. Applique ton angle disciplinaire.
Ne répète pas les objections déjà formulées.
"""
```

### PD2 — Traçabilité des affirmations

Problème : chaque [Fait établi] doit être relié à une source.

Solution : après T1, faire un second appel pour extraire
les sources citées et vérifier qu'elles existent dans le DocumentStore.

```python
def _verify_sources(self, analysis: str, dossier: Dossier) -> dict:
    # Demander à Claude d'extraire toutes les affirmations [Fait établi]
    # et de les relier à leurs sources dans le dossier
    extraction = self.agents.call(
        agent_type="source_extractor",  # prompt dédié
        user_message=f"Extrait toutes les affirmations [Fait établi] et leurs sources :\n{analysis}"
    )
    return self._parse_extraction(extraction)
```

### PD3 — Mise à jour atomique de la mémoire

Problème : si T8 réussit mais la mise à jour mémoire échoue,
l'état est incohérent.

Solution : transaction SQLite avec rollback.

```python
def update(self, state: WorkflowState):
    try:
        with self.db.transaction():
            self._archive_analysis(state)
            self._record_errors(state)
            self._update_hypotheses(state)
            self._update_method_calibration(state)
            self._update_patterns(state)
    except Exception as e:
        # Rollback automatique
        logger.error(f"Memory update failed: {e}")
        # Sauvegarder l'état pour reprise manuelle
        self._save_pending_update(state)
        raise
```

### PD4 — Reprise de workflow en cas d'échec

Problème : si T5 échoue après T4 (4 appels API payants),
ne pas relancer depuis T1.

Solution : sauvegarder l'état à chaque étape.

```python
class WorkflowState:
    def save(self, step: str):
        state_path = f"data/states/{self.run_id}_{step}.json"
        with open(state_path, "w") as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def resume(cls, run_id: str, from_step: str) -> "WorkflowState":
        state_path = f"data/states/{run_id}_{from_step}.json"
        return cls.from_dict(json.load(open(state_path)))
```

---

## ESTIMATION DES COÛTS API

Pour un dossier complet T1-T8 avec claude-sonnet-4 :

| Étape | Tokens input (est.) | Tokens output (est.) |
|-------|---------------------|----------------------|
| T1 Entité | ~4 000 | ~3 000 |
| T2 Contradicteur | ~5 000 | ~1 500 |
| T3 Entité révision | ~7 000 | ~2 000 |
| T4 Économiste | ~6 000 | ~2 000 |
| T4 Juriste | ~6 000 | ~2 000 |
| T4 Sociologue | ~6 000 | ~2 000 |
| T4 Analyste discours | ~6 000 | ~2 000 |
| T5 Synthèse | ~12 000 | ~3 000 |
| **TOTAL** | **~52 000** | **~17 500** |

À ~$3/MTok input et ~$15/MTok output pour claude-sonnet-4 :
≈ **$0.42 par dossier complet**

MVP : acceptable pour développement et tests.
Production : optimiser en résumant les contextes longs.
