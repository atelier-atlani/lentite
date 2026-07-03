# Étape 5 — Schémas de données
## Modèles pour la mémoire et les analyses

---

## BASE DE DONNÉES — SCHÉMA COMPLET

```sql
-- ============================================================
-- DOSSIERS ET SOURCES
-- ============================================================

CREATE TABLE dossiers (
    id              TEXT PRIMARY KEY,  -- UUID
    titre           TEXT NOT NULL,
    date_creation   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    type_objet      TEXT,              -- 'decision_formelle' | 'conflit' | ...
    registre_discursif TEXT,           -- 'souverain' | 'economique' | ...
    output_type     TEXT,              -- 'analyse_reel' | 'carte_discours'
    statut          TEXT DEFAULT 'actif'  -- 'actif' | 'archive'
);

CREATE TABLE sources (
    id              TEXT PRIMARY KEY,
    dossier_id      TEXT REFERENCES dossiers(id),
    url             TEXT,
    type_source     TEXT,  -- 'loi' | 'rapport' | 'presse' | 'discours' | 'stat'
    date_source     DATE,
    auteur          TEXT,
    institution     TEXT,
    fiabilite       TEXT,  -- 'haute' | 'moyenne' | 'faible'
    biais_possible  TEXT,
    contenu         TEXT,
    langue          TEXT DEFAULT 'fr',
    indexee_le      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- WORKFLOW RUNS
-- ============================================================

CREATE TABLE workflow_runs (
    id              TEXT PRIMARY KEY,
    dossier_id      TEXT REFERENCES dossiers(id),
    date_debut      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_fin        TIMESTAMP,
    statut          TEXT DEFAULT 'en_cours',  -- 'en_cours' | 'termine' | 'echec'
    etape_courante  TEXT,  -- 'T1' | 'T2' | ... | 'T8'
    version_entity  TEXT,
    version_contradictory TEXT,
    cout_tokens_total INTEGER
);

CREATE TABLE agent_outputs (
    id              TEXT PRIMARY KEY,
    run_id          TEXT REFERENCES workflow_runs(id),
    etape           TEXT,        -- 'T1' | 'T2' | ...
    agent_type      TEXT,
    prompt_version  TEXT,
    contenu         TEXT,        -- sortie brute de l'agent
    tokens_input    INTEGER,
    tokens_output   INTEGER,
    timestamp       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- REGISTRE 1 — ANALYSES ARCHIVÉES
-- ============================================================

CREATE TABLE analyses (
    id              TEXT PRIMARY KEY,
    run_id          TEXT REFERENCES workflow_runs(id),
    dossier_id      TEXT REFERENCES dossiers(id),
    date_analyse    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Métadonnées du dossier
    type_objet      TEXT,
    registre_discursif TEXT,
    output_type     TEXT,

    -- Question §0
    profiteurs_crise    TEXT,  -- JSON : qui bénéficie
    interet_cadrage     TEXT,  -- qui bénéficie du cadrage
    interet_timing      TEXT,
    invisibles_economiques TEXT,

    -- Résultats
    hypothese_principale TEXT,
    degre_confiance_global TEXT,  -- 'faible' | 'modere' | 'fort'
    ce_qui_ferait_changer TEXT,

    -- Agents utilisés
    agents_utilises     TEXT,  -- JSON : liste

    -- Synthèse
    tension_centrale    TEXT,
    risque_erreur       TEXT,

    -- Contenu complet
    analyse_complete    TEXT,  -- markdown complet T1-T8

    statut              TEXT DEFAULT 'ferme'  -- 'ferme' | 'ouvert'
);

-- ============================================================
-- REGISTRE 2 — ERREURS ET CORRECTIONS
-- ============================================================

CREATE TABLE erreurs (
    id              TEXT PRIMARY KEY,
    date_erreur     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dossier_id      TEXT REFERENCES dossiers(id),
    run_id          TEXT REFERENCES workflow_runs(id),

    agent_correcteur TEXT,  -- 'contradictory' | 'economist' | 'humain' | ...

    -- Classification
    type_erreur     TEXT,  -- 'O1' | 'O2' | 'O2bis' | 'EO1' | 'JO1' | ...
    type_label      TEXT,  -- libellé humain

    -- Contenu
    affirmation_originale TEXT,
    affirmation_corrigee  TEXT,
    raison                TEXT,

    -- Généralisation
    condition_declenchante TEXT,  -- sur quel type d'objet cette erreur se produit
    regle_apprise          TEXT,  -- formulation de la règle
    integre_protocole      BOOLEAN DEFAULT FALSE,
    fichier_modifie        TEXT
);

-- ============================================================
-- REGISTRE 3 — HYPOTHÈSES OUVERTES
-- ============================================================

CREATE TABLE hypotheses (
    id              TEXT PRIMARY KEY,
    date_ouverture  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    formulation     TEXT NOT NULL,

    -- Statut
    degre_confiance TEXT DEFAULT 'faible',  -- 'faible' | 'modere' | 'fort' | 'etabli'
    evolution       TEXT DEFAULT 'stable',  -- 'stable' | 'hausse' | 'baisse'
    statut          TEXT DEFAULT 'ouverte', -- 'ouverte' | 'renforcee' | 'affaiblie' | 'fermee_confirmee' | 'fermee_invalidee' | 'suspendue'
    date_cloture    TIMESTAMP,

    ce_qui_ferait_progresser TEXT
);

CREATE TABLE hypotheses_dossiers (
    hypothese_id    TEXT REFERENCES hypotheses(id),
    dossier_id      TEXT REFERENCES dossiers(id),
    PRIMARY KEY (hypothese_id, dossier_id)
);

CREATE TABLE hypotheses_indices (
    id              TEXT PRIMARY KEY,
    hypothese_id    TEXT REFERENCES hypotheses(id),
    date_indice     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dossier_id      TEXT REFERENCES dossiers(id),
    marqueur        TEXT,        -- 'Fait établi' | 'Inférence' | 'Hypothèse'
    direction       TEXT,        -- 'pour' | 'contre'
    contenu         TEXT
);

-- ============================================================
-- REGISTRE 4 — CALIBRATION DES MÉTHODES
-- ============================================================

CREATE TABLE method_calibrations (
    id              TEXT PRIMARY KEY,
    date_entree     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dossier_id      TEXT REFERENCES dossiers(id),
    type_objet      TEXT,

    methode_appliquee TEXT,
    ce_quelle_a_revele TEXT,
    ce_quelle_a_manque TEXT,
    methode_complementaire TEXT,
    lecon_pour_futur TEXT
);

-- Vue synthétique (la "matrice")
CREATE VIEW method_matrix AS
SELECT
    type_objet,
    methode_appliquee,
    COUNT(*) as nb_usages,
    -- Méthode manquante la plus fréquente
    GROUP_CONCAT(methode_complementaire, ', ') as complementaires,
    GROUP_CONCAT(ce_quelle_a_manque, ' | ') as angles_manques
FROM method_calibrations
GROUP BY type_objet, methode_appliquee
ORDER BY type_objet, nb_usages DESC;

-- ============================================================
-- REGISTRE 5 — PATTERNS RÉCURRENTS
-- ============================================================

CREATE TABLE patterns (
    id              TEXT PRIMARY KEY,
    date_creation   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    type_pattern    TEXT,  -- 'discursif' | 'sectoriel' | 'erreur_systematique'

    observation     TEXT NOT NULL,
    degre_confiance TEXT DEFAULT 'faible',

    -- Spécifique aux patterns discursifs
    registre_concerne    TEXT,
    fonction_produite    TEXT,
    vulnerabilite        TEXT,
    interets_invisibilises TEXT,

    -- Spécifique aux patterns sectoriels
    secteur_concerne     TEXT,
    benefice_type        TEXT,
    mecanisme_economique TEXT,
    hypothese_transversale TEXT REFERENCES hypotheses(id),

    -- Spécifique aux erreurs systématiques
    erreur_recurrente    TEXT,
    instruction_manquante TEXT,
    correction_apportee  TEXT
);

CREATE TABLE patterns_dossiers (
    pattern_id      TEXT REFERENCES patterns(id),
    dossier_id      TEXT REFERENCES dossiers(id),
    confirme_ou_infirme TEXT DEFAULT 'confirme',  -- 'confirme' | 'infirme'
    PRIMARY KEY (pattern_id, dossier_id)
);

-- ============================================================
-- CARTOGRAPHIE SECTORIELLE (§1.3bis)
-- ============================================================

CREATE TABLE secteurs_dossier (
    id              TEXT PRIMARY KEY,
    dossier_id      TEXT REFERENCES dossiers(id),
    secteur         TEXT,
    type_relation   TEXT,  -- 'contraint' | 'beneficiaire_direct' | 'beneficiaire_indirect' | 'absent_discours'
    contrainte_benefice TEXT,
    source          TEXT,  -- 'Inférence' | 'Fait établi' | 'Hypothèse'
    notes           TEXT
);

-- ============================================================
-- INDEX POUR PERFORMANCE
-- ============================================================

CREATE INDEX idx_analyses_type ON analyses(type_objet, registre_discursif);
CREATE INDEX idx_erreurs_type ON erreurs(type_erreur, condition_declenchante);
CREATE INDEX idx_hypotheses_statut ON hypotheses(statut, degre_confiance);
CREATE INDEX idx_patterns_type ON patterns(type_pattern, degre_confiance);
CREATE INDEX idx_sources_dossier ON sources(dossier_id, type_source);
```

---

## MODÈLES PYTHON (dataclasses)

```python
from dataclasses import dataclass, field
from typing import List, Optional, Literal
from datetime import datetime

@dataclass
class Source:
    id: str
    dossier_id: str
    url: Optional[str]
    type_source: Literal["loi", "rapport", "presse", "discours", "statistique"]
    date_source: Optional[str]
    auteur: Optional[str]
    fiabilite: Literal["haute", "moyenne", "faible"]
    contenu: str

@dataclass
class Dossier:
    id: str
    titre: str
    type_objet: str
    registre_discursif: str
    sources: List[Source] = field(default_factory=list)

@dataclass
class AgentOutput:
    agent_type: str
    prompt_version: str
    content: str
    tokens_input: int
    tokens_output: int
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class WorkflowState:
    run_id: str
    dossier_id: str
    memory_consultation: Optional[dict] = None
    t1: Optional[AgentOutput] = None
    t2: Optional[AgentOutput] = None
    t3: Optional[AgentOutput] = None
    t4: dict = field(default_factory=dict)  # {agent_type: AgentOutput}
    t5: Optional[AgentOutput] = None

@dataclass
class Error:
    id: str
    dossier_id: str
    agent_correcteur: str
    type_erreur: str
    affirmation_originale: str
    affirmation_corrigee: str
    raison: str
    condition_declenchante: str
    regle_apprise: str

@dataclass
class OpenHypothesis:
    id: str
    formulation: str
    degre_confiance: Literal["faible", "modere", "fort", "etabli"]
    statut: str
    indices_pour: List[dict] = field(default_factory=list)
    indices_contre: List[dict] = field(default_factory=list)
    dossiers: List[str] = field(default_factory=list)

@dataclass
class Pattern:
    id: str
    type_pattern: Literal["discursif", "sectoriel", "erreur_systematique"]
    observation: str
    degre_confiance: str
    dossiers: List[str] = field(default_factory=list)
```

---

## API JSON — FORMAT DE SORTIE

```json
{
  "analyse": {
    "id": "analyse_uuid",
    "dossier": "Loi Immigration 2024",
    "date": "2026-05-14",
    "version_protocole": {
      "entite": "v1.2",
      "contradicteur": "v1.1",
      "economiste": "v1.1",
      "juriste": "v1.0",
      "sociologue": "v1.0",
      "analyste_discours": "v1.1"
    },
    "question_0": {
      "profiteurs_crise": "Employeurs secteurs en tension",
      "cadrage_beneficiaires": "Évite débat sur rôle employeurs",
      "interets_invisibles": "Responsabilité patronale, marché travail informel"
    },
    "hypotheses": [
      {
        "id": "H1",
        "formulation": "Gestion politique de coalition",
        "degre_confiance": "fort",
        "indices_pour": [...],
        "indices_contre": [...]
      }
    ],
    "conclusion": {
      "etabli": [...],
      "probable": [...],
      "hypothetique": [...],
      "invisible": [...],
      "ferait_changer": [...]
    },
    "memoire_mise_a_jour": {
      "erreurs_ajoutees": ["E006"],
      "hypotheses_mises_a_jour": ["H001"],
      "patterns_ajoutees": ["P004"],
      "patterns_renforces": ["P002"]
    }
  }
}
```
