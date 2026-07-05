# SPDX-License-Identifier: AGPL-3.0-only
"""
L'Entité — Schémas de sortie structurée par agent fonctionnel (plan_action_002,
lot 2.8, correctif structurel prescrit par `.claude/reviews/revue_002.md` §4
point 1).

Chaque modèle ci-dessous est un fragment PARTIEL de `M01Analysis`
(`pipeline/schemas.py`, Apache-2.0) — les champs qu'un agent fonctionnel donné
est responsable de produire, jamais une redéfinition parallèle de leur forme :
tous les modèles imbriqués (Vulnerability, Omission, Enonciation, etc.) sont
importés tels quels depuis `schemas.py`, jamais recopiés. Ce module n'a aucune
autorité de validation propre — il sert exclusivement à construire le schéma
JSON transmis à `output_config.format` (SDK Anthropic) pour contraindre la
sortie de chaque agent ; la validation normative reste `schemas.M01Analysis`,
appliquée par l'orchestrateur après fusion des quatre fragments.

Exception à la règle de réutilisation directe — `InferredFunctionOutput` /
`InferredFunctionAlternative` recopient les champs de `schemas.InferredFunction`
en plafonnant sa récursion (`alternative_functions`) à un niveau, parce que
l'API rejette les schémas JSON auto-référents pour `output_config.format`
(constaté à l'exécution réelle du lot 2.8 : « Circular reference detected...
InferredFunction -> InferredFunction »). Voir la note de `InferredFunctionAlternative`
ci-dessous — la validation finale reste `schemas.InferredFunction`, récursive
sans limite, inchangée.
"""

from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field

from schemas import (
    Confidence,
    ExecutionMode,
    Enonciation,
    CharityReconstruction,
    Vulnerability,
    Omission,
    EpistemicRegime,
    UpstreamCausalChain,
    DownstreamCausalChain,
    DiscourseActGap,
    ObservableEffect,
    Historiography,
    EpistemicSynthesis,
    NullResults,
)


class InferredFunctionAlternative(BaseModel):
    """Alternative de fonction inférée, sans récursion supplémentaire.

    `schemas.InferredFunction` est auto-référent (`alternative_functions:
    list["InferredFunction"]`) — légitime pour la validation Pydantic finale,
    mais l'API rejette les schémas JSON récursifs pour `output_config.format`
    (« Circular reference detected... InferredFunction -> InferredFunction »,
    constaté à l'exécution réelle du lot 2.8). Ce modèle plafonne la
    récursion à un niveau pour le SEUL schéma de sortie structurée — une
    fonction inférée et ses alternatives immédiates, sans alternatives
    d'alternatives. La validation finale (schemas.InferredFunction, toujours
    récursive sans limite) n'est pas affectée : cette classe n'existe que
    pour construire un schéma JSON acceptable par l'API, jamais pour valider."""

    model_config = ConfigDict(extra="forbid")

    label: str
    confidence: Confidence
    epistemic_regime: EpistemicRegime


class InferredFunctionOutput(BaseModel):
    """Fonction inférée produite par l'agent Vulnérabilités — voir
    `InferredFunctionAlternative` pour le motif du plafonnement de récursion."""

    model_config = ConfigDict(extra="forbid")

    label: str
    confidence: Confidence
    epistemic_regime: EpistemicRegime
    alternative_functions: list[InferredFunctionAlternative] = Field(default_factory=list)


class CharitePartialUnit(BaseModel):
    """Unité produite par l'agent Charité — texte, actes de langage,
    présuppositions. Ne porte jamais `argumentative_vulnerabilities` /
    `omissions` / `inferred_function` (interdiction du prompt Charité —
    complétés ensuite par l'agent Vulnérabilités, fusionnés par unit_id)."""

    model_config = ConfigDict(extra="forbid")

    unit_id: str
    text_span: str
    speech_acts: list[str] = Field(default_factory=list)
    presuppositions: list[str] = Field(default_factory=list)


class ChariteOutput(BaseModel):
    """Fragment produit par l'agent Charité (étapes 1-8, prompt v2.0)."""

    model_config = ConfigDict(extra="forbid")

    execution_mode: ExecutionMode
    execution_mode_note: str | None = None
    enonciation: Enonciation
    charity_reconstruction: CharityReconstruction | None = None
    units: list[CharitePartialUnit] = Field(default_factory=list)


class VulnerabilitesPartialUnit(BaseModel):
    """Complément d'unité produit par l'agent Vulnérabilités — identifié par
    `unit_id` (déjà attribué par Charité), fusionné dans l'unité correspondante
    par `merge_fragments` (orchestrateur)."""

    model_config = ConfigDict(extra="forbid")

    unit_id: str
    argumentative_vulnerabilities: list[Vulnerability] = Field(default_factory=list)
    omissions: list[Omission] = Field(default_factory=list)
    inferred_function: InferredFunctionOutput | None = None


class VulnerabilitesOutput(BaseModel):
    """Fragment produit par l'agent Vulnérabilités (étapes 9-10, prompt v2.0)."""

    model_config = ConfigDict(extra="forbid")

    units: list[VulnerabilitesPartialUnit] = Field(default_factory=list)


class ChainesCausalesOutput(BaseModel):
    """Fragment produit par l'agent Chaînes causales (étape 11 + 12, prompt v2.0)."""

    model_config = ConfigDict(extra="forbid")

    upstream_causal_chain: UpstreamCausalChain | None = None
    downstream_causal_chains: list[DownstreamCausalChain] = Field(default_factory=list)
    discourse_action_gaps_on_thematic_objects: list[DiscourseActGap] = Field(
        default_factory=list
    )
    observable_effects_on_targeted_objects: list[ObservableEffect] = Field(
        default_factory=list
    )
    historiographies: list[Historiography] = Field(default_factory=list)


class SyntheseOutput(BaseModel):
    """Fragment produit par l'agent Synthèse (étapes 13-14, prompt v2.0).

    Ne recopie plus les sorties des trois agents précédents (contrairement au
    prompt v1.0) — l'assemblage complet du candidat M01-M est désormais un
    mécanisme unique de l'orchestrateur (`merge_fragments`), pas une tâche
    partiellement dupliquée entre le modèle et le code (revue_002.md §2.3,
    §4 point 2)."""

    model_config = ConfigDict(extra="forbid")

    epistemic_synthesis: EpistemicSynthesis
    null_results: NullResults


# ============================================================================
# TABLE DE DISPATCH — nom d'agent -> modèle de sortie structurée
# ============================================================================

AGENT_OUTPUT_MODELS: dict[str, type[BaseModel]] = {
    "charite": ChariteOutput,
    "vulnerabilites": VulnerabilitesOutput,
    "chaines_causales": ChainesCausalesOutput,
    "synthese": SyntheseOutput,
}


__all__ = [
    "CharitePartialUnit",
    "ChariteOutput",
    "InferredFunctionAlternative",
    "InferredFunctionOutput",
    "VulnerabilitesPartialUnit",
    "VulnerabilitesOutput",
    "ChainesCausalesOutput",
    "SyntheseOutput",
    "AGENT_OUTPUT_MODELS",
]
