# Étape 5 — Guide MVP
## Implémentation minimale en 2 semaines

---

## OBJECTIF DU MVP

Produire une analyse complète T1-T8 sur un dossier réel,
avec mémoire persistante entre les runs.
Pas d'interface web. Pas de VectorStore sophistiqué.
Juste le protocole qui tourne en ligne de commande.

---

## PRÉREQUIS

```bash
pip install anthropic sqlite3 chromadb python-dotenv
```

```bash
# .env
ANTHROPIC_API_KEY=sk-ant-...
DB_PATH=data/memory.db
OUTPUTS_DIR=outputs/
PROMPTS_DIR=agents/prompts/
```

---

## SEMAINE 1 — FONDATIONS

### Jour 1-2 : DocumentStore + ingestion

```python
# documents/ingest.py

import anthropic
import sqlite3
from pathlib import Path

def ingest_source(dossier_id: str, content: str,
                  source_type: str, url: str = None,
                  metadata: dict = None) -> str:
    """Ingère une source dans le DocumentStore."""

    source_id = generate_uuid()

    db = sqlite3.connect("data/memory.db")
    db.execute("""
        INSERT INTO sources
        (id, dossier_id, url, type_source, contenu, fiabilite)
        VALUES (?, ?, ?, ?, ?, ?)
    """, [source_id, dossier_id, url, source_type, content,
          metadata.get("fiabilite", "moyenne")])
    db.commit()

    return source_id


def build_dossier_context(dossier_id: str) -> str:
    """Construit le contexte textuel du dossier pour les agents."""

    db = sqlite3.connect("data/memory.db")
    sources = db.execute("""
        SELECT type_source, auteur, date_source, contenu
        FROM sources WHERE dossier_id = ?
        ORDER BY type_source, date_source
    """, [dossier_id]).fetchall()

    context = "## SOURCES DU DOSSIER\n\n"
    for source_type, auteur, date, contenu in sources:
        context += f"### [{source_type}] {auteur or ''} ({date or 'date inconnue'})\n"
        context += f"{contenu[:2000]}\n\n"  # Tronquer si trop long

    return context
```

### Jour 3-4 : AgentPool

```python
# agents/pool.py

import anthropic
from pathlib import Path

class AgentPool:
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.prompts_dir = Path("agents/prompts")

    def get_prompt(self, agent_type: str) -> tuple[str, str]:
        """Retourne (version, contenu) du prompt courant."""
        version_file = self.prompts_dir / agent_type / "current.txt"
        version = version_file.read_text().strip()
        prompt_file = self.prompts_dir / agent_type / f"{version}.md"
        return version, prompt_file.read_text()

    def call(self, agent_type: str, user_message: str,
             max_tokens: int = 4000) -> dict:
        """Appelle un agent et retourne son output."""

        version, system_prompt = self.get_prompt(agent_type)

        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=max_tokens,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}]
        )

        content = response.content[0].text

        return {
            "agent_type": agent_type,
            "version": version,
            "content": content,
            "tokens_input": response.usage.input_tokens,
            "tokens_output": response.usage.output_tokens
        }
```

### Jour 5 : MemoryStore (version JSON simple)

```python
# memory/store.py

import json
from pathlib import Path
from datetime import datetime

class MemoryStore:
    def __init__(self, path: str = "data/memory.json"):
        self.path = Path(path)
        self._ensure_exists()

    def _ensure_exists(self):
        if not self.path.exists():
            self.path.write_text(json.dumps({
                "r1_analyses": [],
                "r2_errors": [],
                "r3_hypotheses": [],
                "r4_calibrations": [],
                "r5_patterns": []
            }, indent=2))

    def _load(self) -> dict:
        return json.loads(self.path.read_text())

    def _save(self, data: dict):
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False))

    def consult(self, dossier_meta: dict) -> str:
        """Retourne un résumé de consultation pour injection dans le prompt."""
        data = self._load()

        # Trouver dossiers similaires
        similar = [a for a in data["r1_analyses"]
                   if a.get("type_objet") == dossier_meta.get("type_objet")][-3:]

        # Erreurs à surveiller
        errors = [e for e in data["r2_errors"]
                  if dossier_meta.get("type_objet") in e.get("condition_declenchante", "")]

        # Patterns applicables
        patterns = data["r5_patterns"][-5:]  # Les 5 plus récents

        consultation = "## CONSULTATION MÉMOIRE\n\n"

        if similar:
            consultation += "### Dossiers similaires\n"
            for a in similar:
                consultation += f"- {a['dossier']} ({a['date']}) : {a['hypothese_principale']}\n"

        if errors:
            consultation += "\n### Erreurs à surveiller\n"
            for e in errors:
                consultation += f"- {e['type_erreur']} : {e['regle_apprise']}\n"

        if patterns:
            consultation += "\n### Patterns applicables\n"
            for p in patterns:
                consultation += f"- {p['observation'][:100]}...\n"

        return consultation

    def archive_analysis(self, dossier: str, type_objet: str,
                         hypothese: str, confiance: str,
                         analyse_complete: str):
        data = self._load()
        data["r1_analyses"].append({
            "id": generate_uuid(),
            "date": datetime.now().isoformat(),
            "dossier": dossier,
            "type_objet": type_objet,
            "hypothese_principale": hypothese,
            "degre_confiance": confiance,
            "analyse": analyse_complete[:500]  # résumé
        })
        self._save(data)

    def add_error(self, type_erreur: str, condition: str, regle: str):
        data = self._load()
        data["r2_errors"].append({
            "id": generate_uuid(),
            "date": datetime.now().isoformat(),
            "type_erreur": type_erreur,
            "condition_declenchante": condition,
            "regle_apprise": regle
        })
        self._save(data)

    def add_pattern(self, type_pattern: str, observation: str):
        data = self._load()
        data["r5_patterns"].append({
            "id": generate_uuid(),
            "date": datetime.now().isoformat(),
            "type_pattern": type_pattern,
            "observation": observation,
            "degre_confiance": "faible"
        })
        self._save(data)
```

---

## SEMAINE 2 — WORKFLOW COMPLET

### Jour 6-7 : WorkflowEngine séquentiel

```python
# workflow/engine.py

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from datetime import datetime

class WorkflowEngine:
    def __init__(self):
        self.agents = AgentPool()
        self.memory = MemoryStore()

    def run(self, dossier_id: str, dossier_titre: str,
            dossier_context: str) -> dict:
        """Exécute le workflow complet T1-T8."""

        run_id = generate_uuid()
        state = {"run_id": run_id, "outputs": {}}

        print(f"\n{'='*60}")
        print(f"DOSSIER : {dossier_titre}")
        print(f"Run ID  : {run_id}")
        print(f"{'='*60}\n")

        # --- CONSULTATION MÉMOIRE ---
        print("📚 Consultation mémoire...")
        memory_context = self.memory.consult({"type_objet": "decision_formelle"})

        # --- T1 : Analyse principale ---
        print("🔍 T1 — Analyse principale...")
        t1_prompt = f"""
{memory_context}

---

## DOSSIER À ANALYSER

{dossier_context}

---

Produis une analyse complète de ce dossier en suivant ton protocole.
"""
        t1 = self.agents.call("entity", t1_prompt)
        state["outputs"]["T1"] = t1
        self._save_step(run_id, "T1", t1)
        print(f"   ✓ {t1['tokens_output']} tokens")

        # --- T2 : Contradicteur ---
        print("⚔️  T2 — Agent contradicteur...")
        t2_prompt = f"""Analyse à attaquer :

{t1['content']}"""
        t2 = self.agents.call("contradictory", t2_prompt, max_tokens=2000)
        state["outputs"]["T2"] = t2
        self._save_step(run_id, "T2", t2)
        print(f"   ✓ {t2['tokens_output']} tokens")

        # --- T3 : Révision ---
        print("🔄 T3 — Révision après contradicteur...")
        t3_prompt = f"""Tu as produit cette analyse :

{t1['content']}

L'agent contradicteur a formulé ces objections :

{t2['content']}

Réponds à chaque objection et produis l'analyse révisée."""
        t3 = self.agents.call("entity", t3_prompt)
        state["outputs"]["T3"] = t3
        self._save_step(run_id, "T3", t3)
        print(f"   ✓ {t3['tokens_output']} tokens")

        # --- T4 : Agents spécialisés EN PARALLÈLE ---
        print("🔬 T4 — Agents spécialisés (parallèle)...")
        specialized_agents = ["economist", "jurist", "sociologist", "discourse_analyst"]

        t4_prompt_base = f"""Analyse révisée à examiner :

{t3['content']}

Dossier original :
{dossier_context[:3000]}"""

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {
                executor.submit(
                    self.agents.call, agent, t4_prompt_base, 2500
                ): agent
                for agent in specialized_agents
            }
            state["outputs"]["T4"] = {}
            for future in as_completed(futures):
                agent = futures[future]
                result = future.result()
                state["outputs"]["T4"][agent] = result
                print(f"   ✓ {agent} : {result['tokens_output']} tokens")

        # --- T5 : Synthèse finale ---
        print("📝 T5 — Synthèse finale...")
        t5_prompt = self._build_synthesis_prompt(state)
        t5 = self.agents.call("entity", t5_prompt)
        state["outputs"]["T5"] = t5
        self._save_step(run_id, "T5", t5)
        print(f"   ✓ {t5['tokens_output']} tokens")

        # --- SAUVEGARDE + MÉMOIRE ---
        print("💾 Sauvegarde et mise à jour mémoire...")
        self._save_final(run_id, dossier_titre, state)
        self._update_memory(state, dossier_titre)

        total_tokens = sum(
            o.get("tokens_input", 0) + o.get("tokens_output", 0)
            for o in self._flatten_outputs(state["outputs"])
        )
        print(f"\n{'='*60}")
        print(f"✅ TERMINÉ — {total_tokens} tokens utilisés")
        print(f"   Coût estimé : ${total_tokens * 0.000005:.4f}")
        print(f"{'='*60}\n")

        return state

    def _build_synthesis_prompt(self, state: dict) -> str:
        t4_summaries = "\n\n".join([
            f"### {agent.upper()}\n{output['content'][:1000]}..."
            for agent, output in state["outputs"]["T4"].items()
        ])
        return f"""Tu as produit l'analyse révisée suivante :

{state['outputs']['T3']['content']}

Les agents spécialisés ont produit ces analyses :

{t4_summaries}

Produis la synthèse finale consolidée selon le format de conclusion
en 5 rubriques, en intégrant les apports des agents spécialisés."""

    def _save_step(self, run_id: str, step: str, output: dict):
        path = Path(f"outputs/runs/{run_id}/{step}.md")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(output["content"])

    def _save_final(self, run_id: str, dossier: str, state: dict):
        path = Path(f"outputs/analyses/{dossier.replace(' ', '_')}.md")
        path.write_text(state["outputs"]["T5"]["content"])
        print(f"   → {path}")

    def _update_memory(self, state: dict, dossier: str):
        # Archiver l'analyse
        self.memory.archive_analysis(
            dossier=dossier,
            type_objet="decision_formelle",
            hypothese="[à extraire de T5]",
            confiance="modere",
            analyse_complete=state["outputs"]["T5"]["content"]
        )

    def _flatten_outputs(self, outputs: dict) -> list:
        flat = []
        for v in outputs.values():
            if isinstance(v, dict) and "content" in v:
                flat.append(v)
            elif isinstance(v, dict):
                flat.extend(v.values())
        return flat
```

### Jour 8-9 : Interface CLI

```python
# main.py

import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Entité IA d'observation critique du réel"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Analyser un dossier
    analyze_parser = subparsers.add_parser("analyze")
    analyze_parser.add_argument("--dossier", required=True)
    analyze_parser.add_argument("--sources-dir", required=True)
    analyze_parser.add_argument("--titre", required=True)

    # Voir la mémoire
    memory_parser = subparsers.add_parser("memory")
    memory_parser.add_argument("--register", choices=["1","2","3","4","5","all"])

    args = parser.parse_args()

    if args.command == "analyze":
        # Charger les sources
        sources_dir = Path(args.sources_dir)
        sources = []
        for f in sources_dir.glob("*.txt"):
            sources.append({
                "content": f.read_text(),
                "type": "texte",
                "nom": f.stem
            })

        # Construire le contexte
        context = build_dossier_context_from_sources(sources)

        # Lancer le workflow
        engine = WorkflowEngine()
        result = engine.run(
            dossier_id=generate_uuid(),
            dossier_titre=args.titre,
            dossier_context=context
        )

        print(f"\nAnalyse disponible dans outputs/analyses/")

    elif args.command == "memory":
        memory = MemoryStore()
        data = memory._load()

        register_map = {
            "1": ("r1_analyses", "ANALYSES ARCHIVÉES"),
            "2": ("r2_errors", "ERREURS ET CORRECTIONS"),
            "3": ("r3_hypotheses", "HYPOTHÈSES OUVERTES"),
            "4": ("r4_calibrations", "CALIBRATION MÉTHODES"),
            "5": ("r5_patterns", "PATTERNS RÉCURRENTS")
        }

        registers = register_map.keys() if args.register == "all" \
                    else [args.register]

        for r in registers:
            key, label = register_map[r]
            print(f"\n{'='*40}")
            print(f"REGISTRE {r} — {label}")
            print(f"{'='*40}")
            items = data[key]
            print(f"{len(items)} entrées")
            for item in items[-3:]:  # 3 plus récents
                print(f"\n  [{item.get('date', '?')[:10]}]")
                for k, v in item.items():
                    if k not in ["id", "date", "analyse"]:
                        print(f"  {k}: {str(v)[:80]}")

if __name__ == "__main__":
    main()
```

### Jour 10 : Test end-to-end

```bash
# Préparer un dossier test
mkdir -p dossiers/loi_immigration_2024/sources

# Ajouter les sources (textes extraits)
echo "Loi n°2024-42 du 26 janvier 2024..." > \
  dossiers/loi_immigration_2024/sources/01_texte_loi.txt

echo "Dispositions métiers en tension..." > \
  dossiers/loi_immigration_2024/sources/02_vie_publique.txt

# Lancer l'analyse
python main.py analyze \
  --titre "Loi Immigration 2024" \
  --sources-dir dossiers/loi_immigration_2024/sources/

# Consulter la mémoire après
python main.py memory --register all
```

---

## ÉVOLUTION VERS PRODUCTION

### Phase 2 (mois 2)

```
+ VectorStore (ChromaDB) pour recherche sémantique dans les sources
+ SQLite → PostgreSQL pour la mémoire
+ Ingestion PDF (pdfplumber)
+ API REST (FastAPI) pour appels externes
```

### Phase 3 (mois 3)

```
+ LangGraph pour orchestration plus robuste
+ Reprise de workflow en cas d'échec
+ Interface web minimaliste (lecture des analyses)
+ Monitoring des coûts API
```

### Phase 4 (mois 4+)

```
+ Fine-tuning des prompts basé sur les erreurs mémorisées
+ Alertes sur nouveaux dossiers (flux d'actualité)
+ Export des analyses en formats structurés
+ API publique (si ouverture)
```

---

## CHECKLIST MVP

```
□ Structure des répertoires créée
□ Schema SQLite initialisé
□ Prompts copiés dans agents/prompts/
□ AgentPool : appels Claude fonctionnels
□ MemoryStore : lecture/écriture JSON
□ WorkflowEngine : T1-T5 séquentiel
□ Parallélisme T4 avec ThreadPoolExecutor
□ CLI : analyze + memory
□ Test end-to-end sur Loi Climat
□ Test end-to-end sur Loi Immigration
□ Mémoire mise à jour après les deux tests
□ Pattern H001 visible dans le registre 3
```
