"""Check the FWE control contract in the repository. These tests do not run a model."""

import re
from pathlib import Path

import pytest
import yaml


CONTROLS = Path(__file__).resolve().parents[1] / "controls"
CI_PATH = CONTROLS / "FWE_CI_v2.0.md"
ROUTER_PATH = CONTROLS / "FWE_ROUTER_v2.0.yaml"
CI = CI_PATH.read_text(encoding="utf-8")
ROUTER = yaml.safe_load(ROUTER_PATH.read_text(encoding="utf-8"))
ROUTES = ROUTER["routes"]


def assert_clauses(text, *clauses):
    normalized = " ".join(text.split())
    for clause in clauses:
        assert clause in normalized, clause


def ci_section(heading):
    return CI.split(f"## {heading}\n", 1)[1].split("\n## ", 1)[0]


def test_only_one_active_pair_with_exact_entry():
    active_cis = sorted(
        path.name for path in CONTROLS.glob("FWE_CI_*.md")
        if re.search(r"(?m)^STATUS: ACTIVE$", path.read_text(encoding="utf-8"))
    )
    active_routers = sorted(
        path.name for path in CONTROLS.glob("FWE_ROUTER_*.yaml")
        if yaml.safe_load(path.read_text(encoding="utf-8"))["status"] == "ACTIVE"
    )
    assert active_cis == [CI_PATH.name]
    assert active_routers == [ROUTER_PATH.name]
    assert re.findall(r"`(FWE_ROUTER_[^`]+)`", CI) == [ROUTER_PATH.name]
    assert_clauses(CI, f"Project Source `{ROUTER_PATH.name}` at `{ROUTER['entry']}`",
                   "LIVE VERIFIED: NOT RUN", "CI owns entry and re-entry")
    assert ROUTER["router_version"] == "2.0"
    assert ROUTER["live_verified"] == "NOT_RUN"
    assert ROUTER["entry"] == "ROUTE_ONLY"
    assert ROUTER["flow"] == ["ROUTE_ONLY", "RESOLVE", "RETURN"]
    assert ROUTER["entry_owner"] == "FWE_CI"
    assert set(ROUTES) == {"SOURCE", "EVIDENCE", "PROFILE", "CONTROL"}
    assert "bypass_when" not in ROUTER
    assert len(CI) < 8_000
    assert_clauses(ROUTER["route_only"], "compatibility is established before runtime",
                   "Do not discover, select or validate the active CI")


def test_p1_direct_creative_work():
    assert_clauses(CI, "no material unresolved dependency directly",
                   "assigned creative space", "needs no prior source",
                   "ordinary realization left to you", "Keep internal checks out of creative prose")


def test_p2_same_premise_and_author_acceptance():
    assert_clauses(CI, "shortest sufficient path", "constitutive assumptions",
                   "information, access, authority and capacity",
                   "flag the premise mutation", "The author alone accepts changes",
                   "exact scope of partial acceptance", "Repair only when requested",
                   "Use consequences of the existing premise")


def test_p3_missing_source_stays_local():
    source = ROUTES["SOURCE"]
    assert_clauses(source["rule"], "identity, role, scope and authority",
                   "material conditions, exceptions, qualifiers and bounds",
                   "stricter loading rule")
    assert_clauses(source["unresolved"], "missing decisive content or authority",
                   "affected proposition", "use limits")
    assert_clauses(CI, "Continue independent work", "within verified roles")


def test_p4_missing_ais_leaves_claim_unverified():
    evidence = ROUTES["EVIDENCE"]
    assert evidence["resolve"] == "direct_ais_binding"
    assert_clauses(evidence["rule"], "AIS owns search", "materially new question to CI",
                   "World support requires separate fictional conditions")
    assert_clauses(evidence["unresolved"], "no AIS binding", "unresolved or conditional",
                   "without claiming verification")
    assert_clauses(CI, "Keep unsupported claims open", "Assigned invention needs no external verification")


def test_p5_mid_execution_reroute_is_bounded():
    reroute = ROUTER["reroute"]
    assert reroute["owner"] == "FWE_CI"
    assert reroute["require"] == "new_material_need_for_waiting_decision"
    assert set(reroute["stop_on"]) == {"sufficient", "scoped_limit", "cycle", "unchanged_unresolved_need"}
    assert_clauses(CI, "before reliance", "even mid-execution")
    assert_clauses(reroute["rule"], "only the new need CI routed", "exact waiting point",
                   "A -> B -> A", "repeated unresolved need",
                   "Retry only when a material source, evidence, permission or capability changes")
    assert ROUTER["return"]["to"] == "same_waiting_portion"


def test_shared_handoff_preserves_task_and_basis():
    assert_clauses(CI, "waiting point, class", "exact need", "operation, stage, scope, authority",
                   "material basis", "protected constraints")
    assert_clauses(ROUTER["route_only"], "class CI supplied", "exact missing contribution",
                   "waiting point, operation, stage, scope and authority", "premise, branch, state",
                   "protected conditions", "output constraints", "class mismatch to CI before access")


def test_access_read_and_application_are_distinct():
    admission = ROUTER["admission"]
    assert admission["before_access"] == ["material_need", "scope", "permission"]
    assert admission["before_use"] == ["verified_identity_or_role", "actual_read", "sufficient_coverage"]
    assert_clauses(admission["rule"], "selection, availability, retrieval, reading",
                   "sufficient coverage and application", "actual return and its reading evidence",
                   "partial coverage", "gaps and conflicts")
    assert_clauses(CI, "Claim reads, application or success only as observed")


@pytest.mark.parametrize("dependency", ["SOURCE", "EVIDENCE", "PROFILE", "CONTROL"])
def test_unresolved_routes_return_to_ci_without_continuation(dependency):
    unresolved = ROUTES[dependency]["unresolved"]
    assert re.search(r"\breturn\b.*?\bto CI\b", unresolved, flags=re.I)
    assert not re.search(r"\b(?:continu\w*|resum\w*|fallback|defaults?)\b", unresolved, flags=re.I)


def test_ci_owns_resume_and_conclusions():
    returned = ROUTER["return"]
    assert set(returned["include"]) == {
        "contribution", "role", "actual_evidence", "coverage", "use_limits",
        "conditions", "conflicts", "unresolved_gaps",
    }
    assert_clauses(returned["rule"], "exact waiting point", "Resolution ends here",
                   "CI owns continuation, conclusions", "author's acceptance authority")
    assert_clauses(CI, "point and basis still hold", "coverage meets need", "limits fit", "gaps or conflicts",
                   "CI alone resumes, limits, conditions or defers",
                   "Continue independent work", "even without Router")


def test_profile_resolves_only_the_expression_need_assigned_by_ci():
    profile = ROUTES["PROFILE"]
    assert profile["resolve"] == "authorized_profile_contract"
    assert_clauses(profile["rule"], "exact authorial expression need supplied by CI",
                   "FWE permission", "purpose, binding, Profile identity and role",
                   "no FWE permission", "Profile owns expression-set selection, literary meaning",
                   "node interpretation, sample applicability and internal ambiguity",
                   "contribution actually returned", "coverage against the CI need")
    assert_clauses(profile["unresolved"], "no FWE Profile grant or binding",
                   "original expression requirement and authority as unchanged")
    assert "model defaults" not in yaml.safe_dump(profile).lower()
    assert "model defaults" not in CI.lower()


def test_expression_decisions_preserve_authority_and_fiction():
    expression = ci_section("External evidence and expression")
    assert set(re.findall(r"\b(IRRELEVANT|DELEGATED|REQUIRED):", expression)) == {
        "IRRELEVANT", "DELEGATED", "REQUIRED",
    }
    assert_clauses(expression, "choice by original authority", "write for the function",
                   "choose within the assigned latitude", "sufficient instruction or established voice",
                   "missing authorial ground to PROFILE", "missing fiction or source content to SOURCE",
                   "Profile failure grants no latitude", "required ground unresolved",
                   "character knowledge and identity", "narrator identity", "protected implication",
                   "premise, fiction state and acceptance")


def test_selective_controls_remain_scoped():
    control = ROUTES["CONTROL"]
    assert control["resolve"] == "directly_bound_applicable_control"
    assert_clauses(control["rule"], "concrete material failure class",
                   "behavior absent from both CI/core and the selected control",
                   "FWE applies it during resumed execution", "do not establish its application")
    assert_clauses(control["unresolved"], "no selective controls", "missing specialized support",
                   "without claiming control execution")


def test_vietnamese_output_and_scoped_exceptions():
    language = ci_section("Vietnamese output")
    assert_clauses(language, "fiction and literary analysis in Vietnamese",
                   "everyday, plain, direct Vietnamese", "Fiction follows its assigned voice",
                   "literary meaning, emotion and realization in Vietnamese",
                   "English controls", "characters' foreign languages",
                   "grant no foreign literary authority", "unless explicitly assigned another ground",
                   "Field terms are not identifiers", "Avoid bilingual labels", "Silently scan and correct")
    exceptions = re.search(r"Translate other English except ([^.]+)", language).group(1)
    assert set(re.split(r", | and ", exceptions)) == {
        "proper names", "code", "commands", "exact identifiers", "literal quotes",
        "explicitly required foreign-language content",
    }
    assert_clauses(ROUTER["route_only"], "output constraints", "grant no output or literary authority")
