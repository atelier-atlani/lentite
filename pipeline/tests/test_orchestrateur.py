# SPDX-License-Identifier: AGPL-3.0-only
"""
Tests unitaires de l'orchestrateur (plan_action_002, lot 2.8, prescrits par
.claude/reviews/revue_002.md §3.4 et §4 point 2) — portent sur les deux seuls
mécanismes de l'orchestrateur qui touchent à la structure du contenu :
l'assemblage des quatre fragments (`merge_fragments`, `units` inclus) et la
conversion JSON→YAML mécanique (`dump_yaml_forcing_quotes`). Aucun appel
réseau — ces tests ne dépendent d'aucune clé API.
"""

import json

import pytest
import yaml
from pydantic import ValidationError

from orchestrateur import (
    assemble_prompt,
    dump_yaml_forcing_quotes,
    merge_fragments,
    parse_json_fragment,
    route_validation_errors,
)
from agent_schemas import AGENT_OUTPUT_MODELS
from schemas import M01Analysis


# ============================================================================
# Schémas de sortie structurée — pas d'appel réseau, juste la construction
# du schéma JSON transmise à output_config.format (lot 2.8)
# ============================================================================


def test_all_agent_output_schemas_transform_without_circular_reference():
    """Régression — VulnerabilitesOutput contenait initialement une référence
    circulaire (schemas.InferredFunction est auto-référent), rejetée par
    l'API à l'exécution réelle du lot 2.8 (« Circular reference detected...
    InferredFunction -> InferredFunction »). Ce test échoue avant tout appel
    réseau si la même classe de régression réapparaît."""
    from anthropic.resources.messages.messages import transform_schema

    for name, model in AGENT_OUTPUT_MODELS.items():
        schema = transform_schema(model)
        assert schema["type"] == "object", name


def test_bitemporal_fields_required_without_non_renseigne_in_output_schemas():
    """Lot 2.9 — les schémas de sortie agent (Vulnérabilités, Chaînes
    causales) rendent `date_fait`/`date_connaissance` requis et retirent
    `non_renseigne` de leur type, contrairement au schéma de validation
    finale (schemas.py) qui reste inchangé pour le corpus existant."""
    from agent_schemas import (
        VulnerabilityOutput,
        OmissionOutput,
        DiscourseActGapOutput,
        ObservableEffectOutput,
    )

    for model in (VulnerabilityOutput, OmissionOutput, DiscourseActGapOutput, ObservableEffectOutput):
        schema = model.model_json_schema()
        assert "date_fait" in schema["required"], model.__name__
        assert "date_connaissance" in schema["required"], model.__name__
        for field_name in ("date_fait", "date_connaissance"):
            field_schema = json.dumps(schema["properties"][field_name])
            assert "non_renseigne" not in field_schema, f"{model.__name__}.{field_name}"
            assert "non_documente" in field_schema, f"{model.__name__}.{field_name}"


# ============================================================================
# route_validation_errors — routage des erreurs vers l'agent propriétaire
# (lot 2.9, revue_002.md §4 point 3)
# ============================================================================


def _minimal_valid_candidate() -> dict:
    return {
        "method_id": "M01_ANALYSE_RHETORIQUE",
        "method_version": "2.1",
        "gabarit_version": "2.1",
        "analysis_id": "TEST",
        "execution_date": "2026-07-05",
        "execution_mode": "applicable_complete",
        "source": {"text_id": "TEST", "provenance": "test", "integrity_status": "uncertain"},
        "enonciation": {
            "speaker": {"id": "X", "name": "X", "role_at_date": "X"},
            "date": "2026-07-05",
            "place": "X",
            "primary_audience": "X",
            "channel": "X",
            "genre": "X",
            "affective_charge": "low",
            "ethical_charge": "low",
            "thematic_objects": [
                {
                    "object_id": "OT1",
                    "label": "X",
                    "efficiency_status": "efficient",
                    "efficiency_justification": "X",
                }
            ],
            "targeted_objects": [],
        },
        "units": [
            {
                "unit_id": "U1",
                "text_span": "X",
                "speech_acts": [],
                "presuppositions": [],
                "argumentative_vulnerabilities": [],
                "omissions": [],
            }
        ],
        "discourse_action_gaps_on_thematic_objects": [],
        "observable_effects_on_targeted_objects": [],
        "epistemic_synthesis": {
            "competing_hypotheses": [
                {"label": "H1", "type": "non_intentional", "confidence": 0.5, "grounded_in": []},
                {"label": "H2", "type": "non_intentional", "confidence": 0.3, "grounded_in": []},
                {"label": "H3", "type": "intentional", "confidence": 0.1, "grounded_in": []},
            ],
            "hypothesis_gap": 0.2,
            "hypothesis_status": "zone_of_indetermination",
        },
        "null_results": {},
    }


def _validation_error(mutate) -> ValidationError:
    candidate = _minimal_valid_candidate()
    mutate(candidate)
    with pytest.raises(ValidationError) as exc_info:
        M01Analysis.model_validate(candidate)
    return exc_info.value


def test_routes_top_level_charite_field_to_charite():
    e = _validation_error(lambda c: c.__setitem__("execution_mode", "invalide"))
    routed, unroutable = route_validation_errors(e)
    assert not unroutable
    assert "charite" in routed
    assert list(routed.keys()) == ["charite"]


def test_routes_unit_text_span_error_to_charite():
    e = _validation_error(lambda c: c["units"][0].pop("text_span"))
    routed, unroutable = route_validation_errors(e)
    assert not unroutable
    assert "charite" in routed


def test_routes_unit_vulnerability_field_to_vulnerabilites():
    def mutate(c):
        c["units"][0]["argumentative_vulnerabilities"] = [
            {"type": "x", "level": "invalide", "confidence": 0.5, "confidence_applies_to": "inference"}
        ]

    e = _validation_error(mutate)
    routed, unroutable = route_validation_errors(e)
    assert not unroutable
    assert "vulnerabilites" in routed
    assert "charite" not in routed


def test_routes_discourse_action_gap_field_to_chaines_causales():
    def mutate(c):
        c["discourse_action_gaps_on_thematic_objects"] = [
            {
                "thematic_object_id": "OT1",
                "declared": "X",
                "pattern_type": "invalide",
                "observation_window": "X",
                "observation": "X",
            }
        ]

    e = _validation_error(mutate)
    routed, unroutable = route_validation_errors(e)
    assert not unroutable
    assert "chaines_causales" in routed


def test_routes_epistemic_synthesis_field_to_synthese():
    e = _validation_error(lambda c: c["epistemic_synthesis"].__setitem__("hypothesis_gap", 2.0))
    routed, unroutable = route_validation_errors(e)
    assert not unroutable
    assert "synthese" in routed


def test_unroutable_field_stops_without_blaming_an_agent():
    """`method_version` est défaulté par l'orchestrateur lui-même — une
    erreur sur ce champ indique un bug de code, jamais un défaut d'agent.
    Elle doit rester non routable plutôt que d'être attribuée à un agent
    au hasard."""
    e = _validation_error(lambda c: c.__setitem__("method_version", "1.0"))
    routed, unroutable = route_validation_errors(e)
    assert unroutable
    assert not routed


def test_root_level_bitemporal_error_splits_across_two_agents():
    """Reproduit l'échec réel du lot 2.8 — `validate_bitemporal_when_durci`
    lève une seule erreur racine qui peut référencer à la fois des champs de
    Vulnérabilités (omissions) et de Chaînes causales (discourse_action_gaps)
    dans le même message. Le routage doit filtrer et distribuer les deux."""

    def mutate(c):
        c["gabarit_version"] = "2.1-durci-seq1"
        c["units"][0]["omissions"] = [
            {
                "missing_element": "X",
                "level": "structural",
                "why_expected": "X",
                "confidence": 0.5,
                "pouvoir_agir": "X",
                "opportunite": {"description": "X", "date": "2026-01-01"},
                "cloture_corpus": {"corpus_declare": "X", "date_cloture": "2026-01-01"},
                "explications_innocentes": [{"description": "X", "statut": "examinee"}],
                # date_fait/date_connaissance omis — défaut non_renseigne
            }
        ]
        c["enonciation"]["thematic_objects"][0]["efficiency_status"] = "efficient"
        c["discourse_action_gaps_on_thematic_objects"] = [
            {
                "thematic_object_id": "OT1",
                "declared": "X",
                "pattern_type": "never_observed",
                "observation_window": "X",
                "observation": "X",
                # date_fait/date_connaissance omis — défaut non_renseigne
            }
        ]

    e = _validation_error(mutate)
    routed, unroutable = route_validation_errors(e)
    assert not unroutable
    assert "vulnerabilites" in routed
    assert "chaines_causales" in routed
    assert "units[U1].omissions[0]" in routed["vulnerabilites"][0]
    assert "discourse_action_gaps_on_thematic_objects[OT1]" in routed["chaines_causales"][0]


# ============================================================================
# merge_fragments — assemblage, units inclus
# ============================================================================


def test_merge_units_by_id_preserves_charite_and_adds_vulnerabilites():
    """L'unité fusionnée porte les champs de Charité (text_span, speech_acts,
    presuppositions) ET les champs ajoutés par Vulnérabilités
    (argumentative_vulnerabilities, omissions, inferred_function), rattachés
    par unit_id — jamais un remplacement de la liste `units` de Charité."""
    charite = {
        "execution_mode": "applicable_complete",
        "units": [
            {
                "unit_id": "U1",
                "text_span": "Nous proposerons, vous déciderez.",
                "speech_acts": ["engagement"],
                "presuppositions": [],
            }
        ],
    }
    vulnerabilites = {
        "units": [
            {
                "unit_id": "U1",
                "argumentative_vulnerabilities": [
                    {
                        "type": "generalisation_hative",
                        "level": "possible",
                        "confidence": 0.4,
                        "confidence_applies_to": "inference",
                    }
                ],
                "omissions": [],
                "inferred_function": None,
            }
        ]
    }
    result = merge_fragments(charite, vulnerabilites, {}, {})

    assert len(result["units"]) == 1
    unit = result["units"][0]
    assert unit["unit_id"] == "U1"
    assert unit["text_span"] == "Nous proposerons, vous déciderez."
    assert unit["speech_acts"] == ["engagement"]
    assert unit["argumentative_vulnerabilities"][0]["type"] == "generalisation_hative"
    assert unit["omissions"] == []
    assert unit["inferred_function"] is None


def test_merge_units_unmatched_vulnerabilites_id_ignored():
    """Un `unit_id` produit par Vulnérabilités qui ne correspond à aucune
    unité de Charité n'introduit pas d'unité fantôme — seules les unités de
    Charité définissent la liste finale (Charité découpe, Vulnérabilités
    complète, jamais l'inverse)."""
    charite = {"units": [{"unit_id": "U1", "text_span": "texte", "speech_acts": [], "presuppositions": []}]}
    vulnerabilites = {"units": [{"unit_id": "U999", "argumentative_vulnerabilities": [], "omissions": []}]}
    result = merge_fragments(charite, vulnerabilites, {}, {})

    assert len(result["units"]) == 1
    assert result["units"][0]["unit_id"] == "U1"
    assert "argumentative_vulnerabilities" not in result["units"][0]


def test_merge_units_missing_vulnerabilites_entry_leaves_unit_unchanged():
    """Une unité de Charité sans complément de Vulnérabilités (liste vide
    reçue) traverse la fusion sans erreur ni champ ajouté — un résultat
    nul valide (gabarit v2.1 section 9.8), pas un cas d'échec."""
    charite = {"units": [{"unit_id": "U1", "text_span": "texte", "speech_acts": [], "presuppositions": []}]}
    result = merge_fragments(charite, {"units": []}, {}, {})

    assert result["units"] == [{"unit_id": "U1", "text_span": "texte", "speech_acts": [], "presuppositions": []}]


def test_merge_top_level_blocks_disjoint_no_clobbering():
    """Les blocs de premier niveau de Chaînes causales et Synthèse s'ajoutent
    au candidat sans toucher aux champs de Charité — depuis le lot 2.8,
    Synthèse ne recopie plus rien (revue_002.md §2.3), donc `update()` ne
    risque plus d'écraser silencieusement un champ correctement produit par
    un agent précédent avec une recopie dégradée."""
    charite = {"execution_mode": "applicable_complete", "units": []}
    chaines_causales = {
        "upstream_causal_chain": {"elements": []},
        "historiographies": [],
    }
    synthese = {
        "epistemic_synthesis": {"established_facts": ["fait X"]},
        "null_results": {"fallacies_certain": 0},
    }
    result = merge_fragments(charite, {}, chaines_causales, synthese)

    assert result["execution_mode"] == "applicable_complete"
    assert result["upstream_causal_chain"] == {"elements": []}
    assert result["epistemic_synthesis"] == {"established_facts": ["fait X"]}
    assert result["null_results"] == {"fallacies_certain": 0}


# ============================================================================
# parse_json_fragment
# ============================================================================


def test_parse_json_fragment_valid():
    raw = json.dumps({"units": [{"unit_id": "U1"}]})
    assert parse_json_fragment(raw) == {"units": [{"unit_id": "U1"}]}


def test_parse_json_fragment_empty_object():
    assert parse_json_fragment("{}") == {}


def test_parse_json_fragment_repairs_trailing_comma_before_closing_brace():
    """Reproduit exactement les deux échecs réels du lot 2.8 (exécution sur
    le corpus Lecornu) — une virgule finale avant l'accolade fermante d'une
    unité, en toute fin de liste `speech_acts`, malgré output_config.format."""
    raw = (
        '{"units": [{"unit_id": "u11a", "speech_acts": '
        '["assertion à valeur d\'accusation implicite",],}]}'
    )
    assert parse_json_fragment(raw) == {
        "units": [
            {
                "unit_id": "u11a",
                "speech_acts": ["assertion à valeur d'accusation implicite"],
            }
        ]
    }


def test_parse_json_fragment_repairs_trailing_comma_across_multiple_levels():
    raw = '{"a": [1, 2,], "b": {"c": 3,},}'
    assert parse_json_fragment(raw) == {"a": [1, 2], "b": {"c": 3}}


def test_parse_json_fragment_invalid_raises_json_decode_error():
    with pytest.raises(json.JSONDecodeError):
        parse_json_fragment("{ceci n'est pas du JSON")


# ============================================================================
# assemble_prompt — embarquement des fragments en JSON (lot 2.8)
# ============================================================================


def test_assemble_prompt_embeds_prior_fragments_as_json():
    prompt = assemble_prompt(
        "CONTENU DU PROMPT",
        "TEXTE SOURCE ICI",
        {"charite": {"execution_mode": "applicable_complete"}},
    )
    assert "```json" in prompt
    assert "```yaml" not in prompt
    assert '"execution_mode": "applicable_complete"' in prompt
    assert "TEXTE SOURCE ICI" in prompt


def test_assemble_prompt_includes_failure_report_when_given():
    prompt = assemble_prompt("PROMPT", "TEXTE", {}, failure_report="[missing] foo: Field required")
    assert "RAPPORT D'ERREURS" in prompt
    assert "[missing] foo: Field required" in prompt


def test_assemble_prompt_omits_failure_report_section_when_absent():
    prompt = assemble_prompt("PROMPT", "TEXTE", {})
    assert "RAPPORT D'ERREURS" not in prompt


# ============================================================================
# dump_yaml_forcing_quotes — conversion JSON→YAML mécanique (lot 2.8)
# ============================================================================


def test_forces_quoting_on_colon_space_in_plain_scalar():
    """Reproduit exactement la classe d'erreur diagnostiquée au lot 2.7 —
    une phrase de red_team_objections contenant `') : si` a fait échouer le
    parsing YAML du texte produit à la main par le modèle (v1.0). Le
    convertisseur mécanique doit produire un YAML qui réencode cette même
    chaîne sans ambiguïté, et qui se relit exactement identique."""
    dangerous = (
        "L'hypothèse dominante est contredite par l'aveu du locuteur "
        "('que j'avais sans doute insuffisamment mesurée, je le reconnais') "
        ": si la nécessité n'a été mesurée qu'après coup, cela affaiblit la thèse."
    )
    data = {"red_team_objections": [dangerous]}
    dumped = dump_yaml_forcing_quotes(data)

    reloaded = yaml.safe_load(dumped)
    assert reloaded == data
    assert reloaded["red_team_objections"][0] == dangerous


def test_forces_quoting_on_string_with_embedded_quote_and_trailing_context():
    """Reproduit la deuxième classe d'erreur du lot 2.7 (agent Vulnérabilités)
    — une chaîne entre guillemets suivie de texte hors guillemets sur la même
    valeur."""
    dangerous = '"J\'ai proposé au Président de la République un gouvernement" (unité ultérieure du texte)'
    dumped = dump_yaml_forcing_quotes({"evidence_of_expected_knowledge": dangerous})
    reloaded = yaml.safe_load(dumped)
    assert reloaded["evidence_of_expected_knowledge"] == dangerous


def test_simple_strings_are_not_force_quoted():
    """Les chaînes simples (labels, enums, identifiants) restent en style
    YAML plain — le quotage forcé cible spécifiquement les chaînes ambiguës,
    pas toutes les chaînes (lisibilité du YAML final, corpus existant)."""
    dumped = dump_yaml_forcing_quotes({"unit_id": "U1", "level": "certain"})
    assert "unit_id: U1\n" in dumped
    assert "level: certain\n" in dumped
    assert '"' not in dumped


def test_empty_string_is_force_quoted():
    dumped = dump_yaml_forcing_quotes({"note": ""})
    reloaded = yaml.safe_load(dumped)
    assert reloaded["note"] == ""
    assert '""' in dumped


def test_string_resembling_a_date_round_trips_as_string():
    """Depuis le lot 2.8, les fragments proviennent de JSON (json.loads), où
    une date est une chaîne ordinaire, jamais un type date natif (contrairement
    à l'ancien parsing YAML, v1.0). Le YAML produit doit donc préserver le
    typage chaîne à la relecture, pas le convertir silencieusement en date."""
    dumped = dump_yaml_forcing_quotes({"date_fait": "2025-10-14"})
    reloaded = yaml.safe_load(dumped)
    assert reloaded["date_fait"] == "2025-10-14"
    assert isinstance(reloaded["date_fait"], str)


def test_roundtrip_nested_structure_full_types():
    data = {
        "units": [
            {
                "unit_id": "U1",
                "confidence": 0.42,
                "certain": True,
                "note": None,
                "tags": ["a", "b: c"],
            }
        ]
    }
    dumped = dump_yaml_forcing_quotes(data)
    assert yaml.safe_load(dumped) == data
