# SPDX-License-Identifier: Apache-2.0
"""
L'Entité — Schémas Pydantic v2 pour M03 v2.1 (analyse comparative multi-acteurs).

Implémente le schéma normatif du gabarit v2.1 section 11 pour validation
des sorties machine M03-M, en extension de schemas.py (M01).

Conformité au gabarit v2.1 et à M03 v2.1 section 11.
"""

from __future__ import annotations
from datetime import date
from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field, model_validator

from schemas import (
    EfficiencyStatus,
    EpistemicRegime,
    ConsensusLevel,
    HypothesisType,
    HypothesisStatus,
    ConfidenceAppliesTo,
    ExecutionMode,
    Hypothesis,
    Confidence,
)


# ============================================================================
# ENUMS — typologies normatives propres à M03 v2.1
# ============================================================================


class EpistemicMatrixRegime(str, Enum):
    """Régime épistémique étendu pour matrice positions épistémiques M03.

    Étend les quatre valeurs canoniques (K, B, Affirme, Prétend_savoir)
    avec les cas spéciaux nécessaires à l'analyse comparative.
    """

    K = "K"
    B = "B"
    ASSERTS = "Asserts"
    CLAIMS_TO_KNOW = "ClaimsToKnow"
    SILENT = "silent"
    REFUTES = "refutes"
    REFUTES_IMPLICITLY = "refutes_implicitly"
    ASSERTS_WITH_K_CLAIM = "Asserts_with_K_claim"
    AMBIGUOUS_B_SILENT = "ambiguous_B_silent"
    AMBIGUOUS_B_ASSERTS = "ambiguous_B_Asserts"
    AMBIGUOUS_K_CLAIMS_TO_KNOW = "ambiguous_K_ClaimsToKnow"


class TargetedObjectStatus(str, Enum):
    """Statut d'un objet visé pour un acteur dans la matrice M03."""

    AIMED = "aimed"
    NOT_AIMED = "not_aimed"
    NOT_AIMED_INVERSE = "not_aimed_inverse"
    AMBIGUOUS = "ambiguous"
    AMBIGUOUS_FRACTURED = "ambiguous_fractured"


class CrossMatrixCaseType(str, Enum):
    """Types de cas saillants v2.1 (gabarit M03 v2.1 sections 5.4, étape 10)."""

    CONVERGENCE_AIM_DIVERGENCE_PROPOSITION = "convergence_aim_divergence_proposition"
    CONVERGENCE_PROPOSITION_DIVERGENCE_AIM = "convergence_proposition_divergence_aim"
    TACTICAL_COALITION = "tactical_coalition"
    UNANTICIPATED_CONVERGENCE = "unanticipated_convergence"


class ArenaRelationType(str, Enum):
    """Types de relations dans la structure de l'arène M03 v2.1."""

    OFFER_CONCESSION = "offer_concession"
    CONDITIONAL_ACCEPTANCE = "conditional_acceptance"
    FRONTAL_DISQUALIFICATION = "frontal_disqualification"
    PERSONAL_DISQUALIFICATION = "personal_disqualification"
    EXPLICIT_ALLIANCE = "explicit_alliance"
    POACHING_ATTEMPT = "poaching_attempt"
    PREEMPTION_SYMBOLIQUE = "preemption_symbolique"
    ALLIANCE_AFFIRMATION = "alliance_affirmation"
    LEXICAL_BORROWING = "lexical_borrowing"
    METHODOLOGICAL_ENGAGEMENT = "methodological_engagement"
    RESPONDS_TO = "responds_to"
    OPPOSES = "opposes"
    IGNORES = "ignores"
    CITES = "cites"


# ============================================================================
# MODÈLES — composants de la matrice et de la cartographie
# ============================================================================


class Controversy(BaseModel):
    """Objet structurant de la controverse (gabarit M03 v2.1 section 5.1)."""

    object: str
    temporal_sequence: str
    date_range: tuple[date, date]
    effects_observation_extension: date | None = None


class EfficiencyByDimension(BaseModel):
    """Efficience d'un acteur par dimension de la controverse (gabarit M03 v2.1 section 5.2)."""

    dimension_label: str
    efficiency_status: EfficiencyStatus
    justification: str


class Actor(BaseModel):
    """Acteur de la controverse avec référence à son analyse M01 individuelle."""

    actor_id: str
    name: str
    role_at_date: str
    m01_analysis_id: str
    execution_mode_on_m01: str
    efficiency_by_dimension: list[EfficiencyByDimension] = Field(default_factory=list)


class StructuringProposition(BaseModel):
    """Proposition structurante du noyau de la controverse."""

    proposition_id: str
    label: str
    source_documentability: str | None = None


# ----------------------------------------------------------------------------
# Matrices v2.1
# ----------------------------------------------------------------------------


class EpistemicCell(BaseModel):
    """Cellule de la matrice positions épistémiques (acteur × proposition)."""

    actor: str
    proposition: str
    regime: EpistemicMatrixRegime
    source_citation: str | None = None
    confidence: Confidence
    confidence_applies_to: Literal[ConfidenceAppliesTo.INFERENCE] = ConfidenceAppliesTo.INFERENCE
    note: str | None = None


class TargetedObjectCell(BaseModel):
    """Cellule de la matrice objets visés (acteur × objet visé) — schéma v2.1.

    Contrainte v2.1 — si status == aimed, grounded_in doit être renseigné
    (référence à l'analyse M01 individuelle qui supporte l'inférence).
    """

    actor: str
    object: str
    label: str | None = None
    status: TargetedObjectStatus
    confidence: Confidence
    confidence_applies_to: Literal[ConfidenceAppliesTo.INFERENCE] = ConfidenceAppliesTo.INFERENCE
    efficiency: EfficiencyStatus | None = None
    note: str | None = None
    grounded_in: list[str] = Field(default_factory=list)


# ----------------------------------------------------------------------------
# Cas saillants v2.1
# ----------------------------------------------------------------------------


class CrossMatrixCase(BaseModel):
    """Cas saillant identifié dans le croisement des deux matrices (M03 v2.1)."""

    type: CrossMatrixCaseType
    actors_involved: list[str] = Field(min_length=2)
    description: str
    analytical_reading: str


# ----------------------------------------------------------------------------
# Cadres interprétatifs v2.1
# ----------------------------------------------------------------------------


class InterpretiveFrame(BaseModel):
    """Cadre interprétatif concurrent mobilisé dans la controverse.

    Contrainte v2.1 — empirical_grounding doit contenir au moins deux cas
    externes au projet documentant le cadre (gabarit v2.1 section 6.6
    sur l'ancrage empirique des typologies).
    """

    frame_label: str
    empirical_grounding: list[str] = Field(min_length=2)
    consensus_level: ConsensusLevel
    mobilizing_actors: list[str] = Field(min_length=1)


# ----------------------------------------------------------------------------
# Structure de l'arène et chaînes causales aval comparées
# ----------------------------------------------------------------------------


class ArenaEdge(BaseModel):
    """Arête de la cartographie de l'arène (gabarit M03 v2.1 section 5.6)."""

    source: str
    target: str
    relation: ArenaRelationType
    source_citation: str | None = None


class ActorObservableEffect(BaseModel):
    """Effet observable pour un acteur, lien vers son analyse M01."""

    object: str
    effect: str  # référence au ObservableEffectType ou type étendu
    description: str


class ActorDownstreamChain(BaseModel):
    """Chaîne causale aval pour un acteur — extension v2.1."""

    actor: str
    observable_effects: list[ActorObservableEffect] = Field(default_factory=list)


# ----------------------------------------------------------------------------
# Asymétries de bénéfice et prédictions invalidées (v2.1)
# ----------------------------------------------------------------------------


class BenefitAsymmetry(BaseModel):
    """Asymétrie de bénéfice révélée par les effets observables comparés."""

    effect_label: str
    actors_benefiting: list[str] = Field(min_length=1)
    actors_not_benefiting: list[str] = Field(default_factory=list)
    note: str | None = None


class InvalidatedPrediction(BaseModel):
    """Prédiction formulée par un acteur, comparée à la réalité observable."""

    actor: str
    predicted: str
    observation_to_date: str
    pattern_type: str | None = None
    source_citation: str | None = None


# ----------------------------------------------------------------------------
# Synthèse épistémique simplifiée pour M03
# ----------------------------------------------------------------------------


class M03EpistemicSynthesis(BaseModel):
    """Synthèse épistémique de M03 — simplifiée par rapport à M01.

    Au minimum 3 hypothèses concurrentes, convention 6.7 vérifiée.
    """

    competing_hypotheses: list[Hypothesis] = Field(min_length=3)
    hypothesis_gap: float = Field(ge=0.0, le=1.0)
    hypothesis_status: HypothesisStatus

    @model_validator(mode="after")
    def validate_hypothesis_status_consistency(self) -> "M03EpistemicSynthesis":
        gap = self.hypothesis_gap
        status = self.hypothesis_status
        if gap <= 0.2 and status != HypothesisStatus.ZONE_OF_INDETERMINATION:
            raise ValueError(
                f"hypothesis_gap={gap} <= 0.2 requires status=zone_of_indetermination"
            )
        if 0.2 < gap <= 0.4 and status != HypothesisStatus.UNCERTAIN_DOMINANCE:
            raise ValueError(
                f"hypothesis_gap={gap} in (0.2, 0.4] requires status=uncertain_dominance"
            )
        if gap > 0.4 and status != HypothesisStatus.CLEAR_DOMINANCE:
            raise ValueError(f"hypothesis_gap={gap} > 0.4 requires status=clear_dominance")
        return self


# ============================================================================
# MODÈLE RACINE — analyse M03 v2.1 complète
# ============================================================================


class ArenaStructure(BaseModel):
    """Structure de l'arène — nœuds (acteurs et entités) + arêtes typées."""

    nodes: list[str] = Field(min_length=3)
    edges: list[ArenaEdge] = Field(default_factory=list)


class M03NullResults(BaseModel):
    """Résultats nuls de l'analyse comparative."""

    factual_disagreements_K_K: int = Field(default=0, ge=0)
    stable_lasting_coalitions: int = Field(default=0, ge=0)
    dominant_interpretive_frame: str | None = None
    what_the_controversy_states_correctly: list[str] = Field(default_factory=list)
    non_convergent_indices: list[str] = Field(default_factory=list)


class M03InvisibleAndRevision(BaseModel):
    """Conditions de révision et méthodes complémentaires."""

    invisible_from_this_post: list[str] = Field(default_factory=list)
    revision_conditions: list[str] = Field(default_factory=list)
    next_methods_recommended: list[str] = Field(default_factory=list)


class M03Analysis(BaseModel):
    """Analyse M03 v2.1 complète selon le gabarit v2.1.

    Schéma racine validant la sortie machine M03-M.
    """

    method_id: str
    method_version: str
    analysis_id: str
    execution_date: date
    execution_mode: ExecutionMode

    controversy: Controversy
    actors: list[Actor] = Field(min_length=3)
    structuring_propositions: list[StructuringProposition] = Field(min_length=3)

    # matrices v2.1
    epistemic_position_matrix: list[EpistemicCell] = Field(min_length=1)
    targeted_objects_matrix: list[TargetedObjectCell] = Field(min_length=1)
    cross_matrix_salient_cases: list[CrossMatrixCase] = Field(default_factory=list)

    interpretive_frames: list[InterpretiveFrame] = Field(default_factory=list)
    arena_structure: ArenaStructure | None = None
    comparative_downstream_chains: list[ActorDownstreamChain] = Field(default_factory=list)
    asymmetries_of_benefit: list[BenefitAsymmetry] = Field(default_factory=list)
    invalidated_predictions: list[InvalidatedPrediction] = Field(default_factory=list)

    epistemic_synthesis: M03EpistemicSynthesis | None = None
    null_results: M03NullResults | None = None
    invisible_and_revision: M03InvisibleAndRevision | None = None

    @model_validator(mode="after")
    def validate_method_version(self) -> "M03Analysis":
        if not self.method_version.startswith("2.1"):
            raise ValueError(
                f"Schema is for gabarit v2.1, got method_version={self.method_version}"
            )
        return self

    @model_validator(mode="after")
    def validate_matrix_coverage(self) -> "M03Analysis":
        """Vérifier qu'aucune cellule de la matrice positions épistémiques ne
        référence un acteur ou une proposition inconnus."""
        actor_ids = {a.actor_id for a in self.actors}
        proposition_ids = {p.proposition_id for p in self.structuring_propositions}
        for cell in self.epistemic_position_matrix:
            if cell.actor not in actor_ids:
                raise ValueError(
                    f"epistemic_position_matrix references unknown actor: {cell.actor}"
                )
            if cell.proposition not in proposition_ids:
                raise ValueError(
                    f"epistemic_position_matrix references unknown proposition: {cell.proposition}"
                )
        return self

    @model_validator(mode="after")
    def validate_salient_cases(self) -> "M03Analysis":
        """Section 13 critère 9 du gabarit M03 v2.1 — au moins un cas saillant
        identifié dans le croisement des matrices."""
        if not self.cross_matrix_salient_cases:
            raise ValueError(
                "At least one cross_matrix_salient_case required "
                "(gabarit M03 v2.1 section 13 — critère présence de cas saillant identifié)"
            )
        return self


__all__ = [
    "EpistemicMatrixRegime",
    "TargetedObjectStatus",
    "CrossMatrixCaseType",
    "ArenaRelationType",
    "Controversy",
    "EfficiencyByDimension",
    "Actor",
    "StructuringProposition",
    "EpistemicCell",
    "TargetedObjectCell",
    "CrossMatrixCase",
    "InterpretiveFrame",
    "ArenaEdge",
    "ArenaStructure",
    "ActorObservableEffect",
    "ActorDownstreamChain",
    "BenefitAsymmetry",
    "InvalidatedPrediction",
    "M03EpistemicSynthesis",
    "M03NullResults",
    "M03InvisibleAndRevision",
    "M03Analysis",
]
