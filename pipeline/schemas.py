"""
L'Entité — Schémas Pydantic v2 pour le gabarit v2.1.

Implémente le schéma normatif du gabarit v2.1 section 11 pour validation
des sorties machine M01-M (et compatible avec extensions M03-M).

Conformité au gabarit v2.1 — Couche d'exécution v2.1.
"""

from __future__ import annotations
from datetime import date, datetime
from enum import Enum
from typing import Literal, Annotated
from pydantic import BaseModel, Field, model_validator, ConfigDict


# ============================================================================
# ENUMS — typologies normatives du gabarit v2.1
# ============================================================================


class ExecutionMode(str, Enum):
    """Section 4 du gabarit v2.1 — quatre verdicts d'applicabilité."""

    APPLICABLE_COMPLETE = "applicable_complete"
    APPLICABLE_DEGRADED = "applicable_degraded"
    APPLICABLE_VIGILANCE_ADVERSARIALE = "applicable_vigilance_adversariale"
    NOT_APPLICABLE = "not_applicable"


class IntegrityStatus(str, Enum):
    """Section 8 du gabarit v2.1 — intégrité du texte source."""

    CERTIFIED = "certified"
    PARTIAL = "partial"
    UNCERTAIN = "uncertain"


class Charge(str, Enum):
    """Sections 5.6 et 5.7 du gabarit v2.1 — charge affective et éthique."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class EfficiencyStatus(str, Enum):
    """Section 5.9 du gabarit v2.1 — efficience par objet."""

    EFFICIENT = "efficient"
    EFFICIENT_PARTIEL = "efficient_partiel"
    NON_EFFICIENT = "non_efficient"
    AMBIGUOUS = "ambiguous"


class TemporalPattern(str, Enum):
    """Section 6.6 du gabarit v2.1 — sept patterns temporels avec ancrage empirique."""

    NOT_YET_OBSERVED = "not_yet_observed"
    NEVER_OBSERVED = "never_observed"
    OBSERVED_LATER = "observed_later"
    OBSERVED_OTHERWISE = "observed_otherwise"
    OBSERVED_BY_OTHER_ACTOR = "observed_by_other_actor"
    PREVENTED_BY_CONSTRAINT = "prevented_by_constraint"
    BROKEN_EXPLICITLY = "broken_explicitly"
    OBSERVED_AS_ANNOUNCED = "observed_as_announced"
    PARTIALLY_OBSERVED = "partially_observed"


class ObservableEffectType(str, Enum):
    """Section 9.5 du gabarit v2.1 — typologie des effets observables ancrée empiriquement."""

    AMPLIFICATION = "amplification"
    AMPLIFICATION_PARTIELLE = "amplification_partielle"
    AMPLIFICATION_NON_ANTICIPABLE = "amplification_non_anticipable"
    AMPLIFICATION_PARTIELLE_ASYMETRIQUE = "amplification_partielle_asymetrique"
    CONTESTATION = "contestation"
    CONTESTATION_FORTE = "contestation_forte"
    IGNOREMENT = "ignorement"
    REPRISE_PAR_ALLIANCE = "reprise_par_alliance"
    APPROPRIATION_TACTIQUE = "appropriation_tactique"
    CONFIRMATION_INSTITUTIONNELLE = "confirmation_institutionnelle"
    AMPLIFICATION_DOCTRINALE_PARTIELLE_CONTESTATION_POLITIQUE_SANS_RUPTURE_INSTITUTIONNELLE = (
        "amplification_doctrinale_partielle_contestation_politique_sans_rupture_institutionnelle"
    )
    AMPLIFICATION_DU_CADRE_INTERPRETATIF = "amplification_du_cadre_interpretatif"
    AMPLIFICATION_MEMORIELLE_NON_ANTICIPABLE = "amplification_memorielle_non_anticipable"
    IGNOREMENT_INSTITUTIONNEL_A_EFFET_INCERTAIN = "ignorement_institutionnel_a_effet_incertain"
    CONSOLIDATION_OBSERVEE = "consolidation_observee"
    AMPLIFICATION_LIMITEE_AVEC_CONTESTATION = "amplification_limitee_avec_contestation"


class EpistemicRegime(str, Enum):
    """Section 6.4 du gabarit v2.1 — K/B/Affirme/Prétend_savoir."""

    KNOWS = "knows"
    BELIEVES = "believes"
    ASSERTS = "asserts"
    CLAIMS_TO_KNOW = "claims_to_know"


class VulnerabilityLevel(str, Enum):
    """Section 5.4 — trois niveaux de vulnérabilité."""

    CERTAIN = "certain"
    PROBABLE = "probable"
    POSSIBLE = "possible"


class OmissionLevel(str, Enum):
    """Section 5.5 — trois niveaux d'omission."""

    STRUCTURAL = "structural"
    STRATEGIC_PROBABLE = "strategic_probable"
    INTENTIONAL_PROVEN = "intentional_proven"


class ConsensusLevel(str, Enum):
    """Section 5.8 — quatre niveaux de consensus historiographique."""

    DISQUALIFIED = "disqualified"
    MARGINAL = "marginal"
    CONTESTED = "contested"
    STRONG_CONSENSUS = "strong_consensus"


class MobilizationType(str, Enum):
    """Section 9.6 v2.1 — distinction thematic_explicit / lexical_marginal."""

    THEMATIC_EXPLICIT = "thematic_explicit"
    LEXICAL_MARGINAL = "lexical_marginal"


class HypothesisStatus(str, Enum):
    """Section 6.7 — convention zone d'indétermination."""

    ZONE_OF_INDETERMINATION = "zone_of_indetermination"
    UNCERTAIN_DOMINANCE = "uncertain_dominance"
    CLEAR_DOMINANCE = "clear_dominance"


class HypothesisType(str, Enum):
    """Type d'hypothèse — intentionnelle ou non."""

    INTENTIONAL = "intentional"
    NON_INTENTIONAL = "non_intentional"
    NON_INTENTIONAL_OR_MODERATE = "non_intentional_or_moderate"


class ConfidenceAppliesTo(str, Enum):
    """Distinction confidence/truth — sur quoi porte la confidence."""

    INFERENCE = "inference"
    HYPOTHESIS = "hypothesis"
    SOURCE_RELIABILITY = "source_reliability"


class TermHandling(str, Enum):
    """Section 6.2 — règle opérationnelle pour la charité."""

    QUOTED = "quoted"
    ATTRIBUTED = "attributed"
    REFORMULATED_NEUTRAL = "reformulated_neutral"


class UpstreamElementType(str, Enum):
    """Section 5.11 — types d'éléments de chaîne causale amont."""

    PRIOR_POSITION = "prior_position"
    CONTEXT = "context"
    TRIGGER_EVENT = "trigger_event"
    ELECTORAL_EXPECTATION = "electoral_expectation"
    PRIOR_NEGOTIATION = "prior_negotiation"
    INSTITUTIONAL_CONSTRAINT = "institutional_constraint"


# ============================================================================
# MODÈLES — schémas Pydantic conformes au gabarit v2.1 section 11
# ============================================================================


Confidence = Annotated[float, Field(ge=0.0, le=1.0)]
"""Confidence entre 0.0 et 1.0."""


class BorrowedTerm(BaseModel):
    """Section 6.2 — terme évaluatif emprunté avec sa modalité de traitement."""

    term: str
    handling: TermHandling


class CharityReconstruction(BaseModel):
    """Section 6.1-6.2 — reconstruction charitable de l'argument principal."""

    content: str = Field(min_length=100)
    borrowed_terms_handled: list[BorrowedTerm] = Field(default_factory=list)


# ----------------------------------------------------------------------------
# Objets v2.1 — thématiques et visés
# ----------------------------------------------------------------------------


class ThematicObject(BaseModel):
    """Section 2.2 et 5.10 v2.1 — objet thématique du discours."""

    object_id: str
    label: str
    efficiency_status: EfficiencyStatus
    efficiency_justification: str


class TargetedObject(BaseModel):
    """Section 2.2 et 5.10 v2.1 — objet visé par le discours.

    Contrainte v2.1 — grounded_in doit être non vide (l'inférence d'identification
    de l'objet visé doit être supportée par au moins un élément du discours).
    """

    object_id: str
    label: str
    inference_confidence: Confidence
    inference_confidence_applies_to: Literal[ConfidenceAppliesTo.INFERENCE] = (
        ConfidenceAppliesTo.INFERENCE
    )
    grounded_in: list[str] = Field(min_length=1)
    efficiency_status: EfficiencyStatus
    efficiency_justification: str


# ----------------------------------------------------------------------------
# Chaînes causales v2.1
# ----------------------------------------------------------------------------


class UpstreamElement(BaseModel):
    """Section 5.11 v2.1 — élément de chaîne causale amont."""

    element_label: str
    type: UpstreamElementType
    source_reference: str
    confidence: Confidence
    confidence_applies_to: Literal[ConfidenceAppliesTo.INFERENCE] = ConfidenceAppliesTo.INFERENCE


class UpstreamCausalChain(BaseModel):
    """Section 5.11 v2.1 — chaîne causale amont."""

    elements: list[UpstreamElement] = Field(min_length=1)


class PlausibleConsequence(BaseModel):
    """Section 5.11 v2.1 — conséquence plausible.

    Contrainte v2.1 — au moins deux defeaters par conséquence inférée
    (section 6.5 défaisabilité).
    """

    consequence_label: str
    confidence: Confidence
    confidence_applies_to: Literal[ConfidenceAppliesTo.INFERENCE] = ConfidenceAppliesTo.INFERENCE
    defeaters: list[str] = Field(min_length=2)
    observable_to_date: str | None = None


class DownstreamCausalChain(BaseModel):
    """Section 5.11 v2.1 — chaîne causale aval pour un objet visé."""

    targeted_object_id: str
    plausible_consequences: list[PlausibleConsequence] = Field(min_length=1)


# ----------------------------------------------------------------------------
# Écarts et effets observables v2.1
# ----------------------------------------------------------------------------


class DiscourseActGap(BaseModel):
    """Section 9.5 v2.1 — écart entre discours et acte sur objet thématique.

    Contrainte v2.1 — si pattern_type == broken_explicitly,
    public_motivation_invoked doit être renseigné.
    """

    thematic_object_id: str
    declared: str
    pattern_type: TemporalPattern
    observation_window: str
    observation: str
    constraint_named: str | None = None
    public_motivation_invoked: str | None = None
    source_reference: str | None = None

    @model_validator(mode="after")
    def validate_pattern_constraints(self) -> "DiscourseActGap":
        if self.pattern_type == TemporalPattern.BROKEN_EXPLICITLY:
            if not self.public_motivation_invoked:
                raise ValueError(
                    "pattern_type=broken_explicitly requires public_motivation_invoked "
                    "(gabarit v2.1 section 6.6 — ancrage empirique du pattern)"
                )
        if self.pattern_type == TemporalPattern.PREVENTED_BY_CONSTRAINT:
            if not self.constraint_named:
                raise ValueError(
                    "pattern_type=prevented_by_constraint requires constraint_named"
                )
        return self


class ObservableEffect(BaseModel):
    """Section 9.5 v2.1 — effet observable sur un objet visé."""

    targeted_object_id: str
    effect_type: ObservableEffectType
    description: str
    source_reference: str | None = None


# ----------------------------------------------------------------------------
# Unités argumentatives
# ----------------------------------------------------------------------------


class Vulnerability(BaseModel):
    """Vulnérabilité argumentative — section 5.4.

    Contrainte section 6.5 — au moins 2 defeaters pour règles causales.
    """

    type: str
    level: VulnerabilityLevel
    evidence_span: str | None = None
    confidence: Confidence
    confidence_applies_to: ConfidenceAppliesTo
    charitable_alternative: str | None = None
    hidden_premises: list[str] = Field(default_factory=list)
    defeaters: list[str] = Field(default_factory=list)


class Omission(BaseModel):
    """Omission — section 5.5."""

    missing_element: str
    level: OmissionLevel
    why_expected: str
    evidence_of_expected_knowledge: str | None = None
    confidence: Confidence
    confidence_applies_to: Literal[ConfidenceAppliesTo.INFERENCE] = ConfidenceAppliesTo.INFERENCE


class InferredFunction(BaseModel):
    """Fonction inférée — avec régime épistémique obligatoire pour attributions mentales."""

    label: str
    confidence: Confidence
    confidence_applies_to: Literal[ConfidenceAppliesTo.INFERENCE] = ConfidenceAppliesTo.INFERENCE
    epistemic_regime: EpistemicRegime
    alternative_functions: list["InferredFunction"] = Field(default_factory=list)


class Unit(BaseModel):
    """Unité argumentative — section 5.1."""

    unit_id: str
    text_span: str
    speech_acts: list[str] = Field(default_factory=list)
    presuppositions: list[str] = Field(default_factory=list)
    argumentative_vulnerabilities: list[Vulnerability] = Field(default_factory=list)
    omissions: list[Omission] = Field(default_factory=list)
    inferred_function: InferredFunction | None = None


# ----------------------------------------------------------------------------
# Historiographies v2.1
# ----------------------------------------------------------------------------


class Historiography(BaseModel):
    """Section 9.6 v2.1 — historiographie avec mobilization_type."""

    reference_in_text: str | None = None
    mobilized: str
    mobilization_type: MobilizationType
    consensus_level_mobilized: ConsensusLevel
    competing: str | None = None
    consensus_level_competing: ConsensusLevel | None = None
    what_competing_would_say: str | None = None


# ----------------------------------------------------------------------------
# Synthèse épistémique
# ----------------------------------------------------------------------------


class Inference(BaseModel):
    """Inférence avec sa prémisse et sa confidence."""

    label: str
    confidence: Confidence
    confidence_applies_to: Literal[ConfidenceAppliesTo.INFERENCE] = ConfidenceAppliesTo.INFERENCE
    premise: str | None = None


class Hypothesis(BaseModel):
    """Hypothèse concurrente — section 6.7."""

    label: str
    type: HypothesisType
    confidence: Confidence
    confidence_applies_to: Literal[ConfidenceAppliesTo.HYPOTHESIS] = ConfidenceAppliesTo.HYPOTHESIS
    grounded_in: list[str] = Field(default_factory=list)


class EpistemicSynthesis(BaseModel):
    """Section 9.7 — synthèse en trois statuts épistémiques.

    Contrainte section 6.7 — au moins 3 hypothèses dont 2 non intentionnelles.
    """

    established_facts: list[str] = Field(default_factory=list)
    inferences: list[Inference] = Field(default_factory=list)
    competing_hypotheses: list[Hypothesis] = Field(min_length=3)
    hypothesis_gap: float = Field(ge=0.0, le=1.0)
    hypothesis_status: HypothesisStatus
    red_team_objections: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_min_non_intentional(self) -> "EpistemicSynthesis":
        non_intentional_count = sum(
            1
            for h in self.competing_hypotheses
            if h.type
            in (HypothesisType.NON_INTENTIONAL, HypothesisType.NON_INTENTIONAL_OR_MODERATE)
        )
        if non_intentional_count < 2:
            raise ValueError(
                f"At least 2 non-intentional hypotheses required (gabarit v2.1 section 6.7), "
                f"got {non_intentional_count}"
            )
        return self

    @model_validator(mode="after")
    def validate_hypothesis_status_consistency(self) -> "EpistemicSynthesis":
        gap = self.hypothesis_gap
        status = self.hypothesis_status
        if gap <= 0.2 and status != HypothesisStatus.ZONE_OF_INDETERMINATION:
            raise ValueError(
                f"hypothesis_gap={gap} <= 0.2 requires status=zone_of_indetermination, "
                f"got {status}"
            )
        if 0.2 < gap <= 0.4 and status != HypothesisStatus.UNCERTAIN_DOMINANCE:
            raise ValueError(
                f"hypothesis_gap={gap} in (0.2, 0.4] requires status=uncertain_dominance, "
                f"got {status}"
            )
        if gap > 0.4 and status != HypothesisStatus.CLEAR_DOMINANCE:
            raise ValueError(
                f"hypothesis_gap={gap} > 0.4 requires status=clear_dominance, got {status}"
            )
        return self


# ----------------------------------------------------------------------------
# Blocs auxiliaires
# ----------------------------------------------------------------------------


class Source(BaseModel):
    """Source du texte analysé."""

    text_id: str
    provenance: str
    integrity_status: IntegrityStatus
    text_span_total: str | None = None
    retrieval_date: datetime | None = None
    content_hash: str | None = None


class Speaker(BaseModel):
    """Locuteur."""

    id: str
    name: str
    role_at_date: str


class Enonciation(BaseModel):
    """Bloc d'énonciation enrichi v2.1."""

    speaker: Speaker
    date: date
    place: str
    primary_audience: str
    secondary_audiences: list[str] = Field(default_factory=list)
    channel: str
    political_sequence: str | None = None
    genre: str
    communication_contract: str | None = None
    affective_charge: Charge
    ethical_charge: Charge
    # nouveau v2.1
    thematic_objects: list[ThematicObject] = Field(min_length=1)
    targeted_objects: list[TargetedObject] = Field(default_factory=list)


class NullResults(BaseModel):
    """Section 9.8 — blocs de neutralisation."""

    fallacies_certain: int = Field(default=0, ge=0)
    fallacies_probable_or_possible: int = Field(default=0, ge=0)
    intentional_omissions_proved: int = Field(default=0, ge=0)
    modal_shifts_detected: list[str] = Field(default_factory=list)
    ethical_content_not_neutralized: dict | None = None


# ============================================================================
# MODÈLE RACINE — analyse M01 v2.1 complète
# ============================================================================


class M01Analysis(BaseModel):
    """Analyse M01 v2.1 complète selon le gabarit v2.1.

    Schéma racine validant la sortie machine M01-M.
    """

    model_config = ConfigDict(extra="allow")  # tolérer champs additionnels en transition

    method_id: str
    method_version: str
    analysis_id: str
    execution_date: date
    execution_mode: ExecutionMode
    execution_mode_note: str | None = None

    source: Source
    enonciation: Enonciation
    charity_reconstruction: CharityReconstruction | None = None

    units: list[Unit] = Field(default_factory=list)

    # blocs v2.1
    upstream_causal_chain: UpstreamCausalChain | None = None
    downstream_causal_chains: list[DownstreamCausalChain] = Field(default_factory=list)
    discourse_action_gaps_on_thematic_objects: list[DiscourseActGap] = Field(default_factory=list)
    observable_effects_on_targeted_objects: list[ObservableEffect] = Field(default_factory=list)

    historiographies: list[Historiography] = Field(default_factory=list)
    epistemic_synthesis: EpistemicSynthesis | None = None
    null_results: NullResults | None = None

    @model_validator(mode="after")
    def validate_method_version(self) -> "M01Analysis":
        if not self.method_version.startswith("2.1"):
            raise ValueError(
                f"Schema is for gabarit v2.1, got method_version={self.method_version}"
            )
        return self

    @model_validator(mode="after")
    def validate_v3_efficiency_block_coherence(self) -> "M01Analysis":
        """Section 13 critère 7 du gabarit v2.1 — cohérence efficience / bloc V.3.

        Le sous-bloc V.3 (discourse_action_gaps_on_thematic_objects) est vide
        si et seulement si le locuteur est non-efficient sur l'objet thématique.
        """
        if not self.enonciation:
            return self

        # Vérifier qu'on a au moins un objet thématique avec locuteur efficient ou non
        efficient_thematic = [
            t
            for t in self.enonciation.thematic_objects
            if t.efficiency_status
            in (EfficiencyStatus.EFFICIENT, EfficiencyStatus.EFFICIENT_PARTIEL)
        ]
        gaps = self.discourse_action_gaps_on_thematic_objects

        # Si tous les objets thématiques sont non-efficient, V.3 doit être vide
        if not efficient_thematic and len(gaps) > 0:
            raise ValueError(
                "Sub-bloc V.3 should be empty when speaker is non-efficient on all thematic "
                "objects (gabarit v2.1 section 13 critère 7)"
            )

        # Si au moins un objet thématique est efficient, V.3 peut être vide (engagements tenus)
        # ou plein (engagements à documenter). Pas de contrainte stricte d'avoir des gaps.

        return self


# ============================================================================
# EXPORTS
# ============================================================================


__all__ = [
    # Enums
    "ExecutionMode",
    "IntegrityStatus",
    "Charge",
    "EfficiencyStatus",
    "TemporalPattern",
    "ObservableEffectType",
    "EpistemicRegime",
    "VulnerabilityLevel",
    "OmissionLevel",
    "ConsensusLevel",
    "MobilizationType",
    "HypothesisStatus",
    "HypothesisType",
    "ConfidenceAppliesTo",
    "TermHandling",
    "UpstreamElementType",
    # Modèles
    "ThematicObject",
    "TargetedObject",
    "UpstreamElement",
    "UpstreamCausalChain",
    "PlausibleConsequence",
    "DownstreamCausalChain",
    "DiscourseActGap",
    "ObservableEffect",
    "Vulnerability",
    "Omission",
    "InferredFunction",
    "Unit",
    "Historiography",
    "Inference",
    "Hypothesis",
    "EpistemicSynthesis",
    "Source",
    "Speaker",
    "Enonciation",
    "NullResults",
    "CharityReconstruction",
    "BorrowedTerm",
    # Racine
    "M01Analysis",
]
