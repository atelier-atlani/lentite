# SPDX-License-Identifier: AGPL-3.0-only
"""Permet l'import direct des modules pipeline/*.py (schemas, orchestrateur,
agent_schemas) depuis les tests, quel que soit le répertoire d'exécution de
pytest — évite d'imposer `cd pipeline` avant de lancer la suite (lot 2.8)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
