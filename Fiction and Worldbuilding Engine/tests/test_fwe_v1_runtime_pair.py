"""Verify the repository control contract. These checks do not run a model."""

import re
from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTROLS = ROOT / "controls"
CI = (CONTROLS / "FWE_CI_v1.0.md").read_text(encoding="utf-8")
ROUTER_PATH = CONTROLS / "FWE_ROUTER_v1.0.yaml"
ROUTER = yaml.safe_load(ROUTER_PATH.read_text(encoding="utf-8"))
ROUTES = ROUTER["routes"]


def assert_clauses(text, *clauses):
    normalized = " ".join(text.split())
    for clause in clauses:
        assert clause in normalized, clause


def test_unique_active_pair_and_exact_binding():
    active_cis = [
        path.name for path in CONTROLS.glob("FWE_CI_*.md")
        if re.search(r"(?m)^STATUS: ACTIVE$", path.read_text(encoding="utf-8"))
    ]
    active_routers = [
        path.name for path in CONTROLS.glob("FWE_ROUTER_*.yaml")
        if yaml.safe_load(path.read_text(encoding="utf-8"))["status"] == "ACTIVE"
    ]
    assert active_cis == ["FWE_CI_v1.0.md"]
    assert active_routers == [ROUTER_PATH.name]
    assert re.findall(r"`(FWE_ROUTER_[^`]+)`", CI) == [ROUTER_PATH.name]
    assert_clauses(CI, f"exact Project Source `{ROUTER_PATH.name}` and enter `ROUTE_ONLY`",
                   "LIVE VERIFIED: NOT RUN")
    assert ROUTER["router_version"] == "1.0"
    assert ROUTER["live_verified"] == "NOT_RUN"
    assert ROUTER["flow"] == ["ROUTE_ONLY", "RESOLVE", "RETURN"]
    assert ROUTER["entry_owner"] == "FWE_CI"
    assert set(ROUTES) == {"SOURCE", "EVIDENCE", "PROFILE", "CONTROL"}
    assert_clauses(ROUTER["route_only"], "Do not discover, select or validate the active CI.")
    assert len(CI) < 8000


def test_direct_scene_and_same_premise_bypass():
    assert ROUTER["bypass_when"] == "self_sufficient"
    assert_clauses(CI, "Execute self-sufficient portions directly.",
                   "Use consequences of the existing premise to identify what actually needs further development",
                   "Keep internal checks out of creative prose.")
    assert_clauses(ROUTER["route_only"], "Enter only for a material dependency identified by CI.")


@pytest.mark.parametrize(
    "category, section, clauses",
    [
        ("SOURCE", "rule", ("material conditions, exceptions, qualifiers and bounds",
                            "an assigned creative gap needs no lookup")),
        ("SOURCE", "unresolved", ("condition the dependent world claim",
                                  "continue independent creative work")),
        ("EVIDENCE", "rule", ("external factual or causal question", "AIS owns search",
                              "World support requires separate fictional conditions")),
        ("EVIDENCE", "unresolved", ("no AIS binding", "unresolved or conditional",
                                      "without claiming verification")),
        ("PROFILE", "rule", ("permission and purpose before requesting",
                             "Creative-leaf grant confers no FWE permission")),
        ("PROFILE", "unresolved", ("no FWE Profile grant or binding", "Skip access",
                                   "model defaults when the Profile is optional")),
        ("CONTROL", "rule", ("behavior absent from both CI/core and the selected control",
                              "FWE applies it during resumed execution",
                              "do not establish its application")),
        ("CONTROL", "unresolved", ("binds no selective controls",
                                     "Continue work adequately governed by CI/core")),
    ],
)
def test_route_contract(category, section, clauses):
    assert_clauses(ROUTES[category][section], *clauses)


def test_bounded_reroute_and_waiting_point():
    reroute = ROUTER["reroute"]
    assert reroute["owner"] == "FWE_CI"
    assert set(reroute["stop_on"]) == {
        "sufficient", "scoped_limit", "cycle", "unchanged_unresolved_need"
    }
    assert_clauses(reroute["rule"], "Return an unresolved gap for a cycle such as A -> B -> A",
                   "Retry only when a material source, evidence, permission or capability changes")
    assert ROUTER["return"]["to"] == "same_waiting_portion"
    assert_clauses(CI, "Resume there when supported", "continue independently sufficient work")


def test_acceptance_and_action_evidence():
    assert_clauses(CI, "The author alone accepts changes into current fiction",
                   "Claim reads, application or success only as observed.")
    assert_clauses(ROUTER["return"]["rule"], "Router output does not accept or update fiction by itself.")
    assert ROUTER["admission"]["before_access"] == ["material_need", "scope", "permission"]
    assert ROUTER["admission"]["before_use"] == [
        "verified_identity_or_role", "actual_read", "sufficient_coverage"
    ]
    assert_clauses(ROUTER["admission"]["rule"],
                   "Selection, availability, retrieval, reading, sufficient support and application are distinct.")
