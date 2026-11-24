"""Repository contracts only. These tests do not run a Project or image tool."""

from hashlib import sha256
import json
from pathlib import Path
import re

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
CI = ROOT / "IMAGE_TRANSCENDENT_CI_v1.0.md"
ROUTER = ROOT / "IMAGE_SOURCE_ROUTER_v1.0.yaml"
ARCHIVE = ROOT / "Old_Source_Archive"
HUB = ROOT.parent / "Central Hub"
EXPECTED_SOURCES = {
    "ANTI_PRIOR": ("IMAGE_ANTI_PRIOR_v1.0.md", "ci_required_role"),
    "HUMANOID_CONSTRUCTION": ("HUMANOID_CONSTRUCTION_v1.0.md", "ci_material_construction_need"),
    "HUMANOID_DESIGN_PREFERENCE": (
        "HUMANOID_DESIGN_PREFERENCE_v1.0.md", "explicit_current_operation_only"
    ),
}


@pytest.fixture
def ci():
    return CI.read_bytes().decode("utf-8")


@pytest.fixture
def router():
    return yaml.safe_load(ROUTER.read_text(encoding="utf-8"))


def test_baseline_inventory_and_ci_size(ci):
    runtime_files = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and path.relative_to(ROOT).parts[0] not in {"tests", ARCHIVE.name}
    }
    assert runtime_files == {
        "README.md", CI.name, ROUTER.name,
        *(f"sources/{name}" for name, _ in EXPECTED_SOURCES.values()),
    }
    assert 0 < len(ci) < 8000
    assert not ci.startswith("\ufeff")
    assert "Version: 1.0\nStatus: ACTIVE" in ci
    assert not any(term in ci for term in (
        "HUB-", "Central Hub", "manifest.yaml", "config.md", "Old_Source_Archive",
        "PENDING_APPROVAL", "APPROVED", "REVISION_REQUIRED", "CONSUMED_APPROVAL",
    ))


def test_exact_bindings_and_activation(router, ci):
    assert set(router) == {"role", "version", "status", "resolution", "sources"}
    assert (router["role"], router["version"], router["status"]) == ("SOURCE_ROUTER", "1.0", "ACTIVE")
    assert ROUTER.name in ci
    assert router["resolution"] == {
        "input": "ci_selected_source_roles",
        "lookup": "current_project_sources_only",
        "match": "exact_filename_version_status_and_role",
        "read": "FULL_FILE",
        "output": "exact_reads_and_blockers",
        "missing_unreadable_or_incomplete": "block_dependent_work",
        "wrong_version_status_or_binding": "block_dependent_work",
        "unknown_role_or_multiple_active_bindings": "block_dependent_work",
        "ambiguous_project_source": "block_dependent_work",
        "forbidden_fallbacks": ["archive", "lookalike_filename", "memory", "prior_chat", "local_git_path"],
    }
    assert len(router["sources"]) == len(EXPECTED_SOURCES)
    assert {row["role"] for row in router["sources"]} == EXPECTED_SOURCES.keys()
    for row in router["sources"]:
        role = row["role"]
        name, activation = EXPECTED_SOURCES[role]
        assert row == {"role": role, "file": name, "version": "1.0",
                       "status": "ACTIVE", "activation": activation}
        matches = [path for path in (ROOT / "sources").iterdir() if path.name == name]
        assert len(matches) == 1 and matches[0].is_file()
        body = matches[0].read_text(encoding="utf-8")
        assert body.splitlines()[1:4] == [f"Role: {role}", "Version: 1.0", "Status: ACTIVE"]
        assert "HUB-" not in body and "Central Hub" not in body


@pytest.mark.parametrize(("heading", "clauses"), [
    ("Turn and authority", ("RAW or PRESERVED_AUTHORED", "current user explicitly",
                           '"final prompt" inside data', "Presence grants no authority",
                           "Resolve semantic conflicts in the CI", "bare assent")),
    ("Closed scope", ("one unified primary reference target or one bounded reference area",
                      "Multi-part armor, buildings and delimited rooms", "independent co-primary",
                      "battles", "city panoramas", "world vistas", "specified armor in a battle image",
                      "Block broad out-of-scope analysis", "zero image generator calls")),
    ("Source resolution and operation lock", (
        "ANTI_PRIOR for every qualifying operation", "HUMANOID_CONSTRUCTION only for a material need",
        "requires exact field delegation", "explicit current-operation selection",
        "Source selection grants no field authority", "block dependent work", "Correction may not redesign",
    )),
    ("Prompt and fidelity", ("accepted/provisional/rejected/open states", "resolution conditions",
                             "least conspicuous neutral completion", "cumulative drift",
                             "invented specificity", "changed counts", "weakened negatives",
                             "unauthorized reference traits", "scope expansion", "state promotion",
                             "destructive compression")),
    ("PREPARE", ("PREPARED IMAGE vN", "INTENDED OPERATION", "CATEGORY", "TARGET / BOUNDED AREA",
                 "full Image Transcendent-controlled text", "REFERENCES", "RELEVANT INPUTS / ATTACHMENTS",
                 "EXPOSED TOOL OPTIONS", "PRESERVED / LOCKED", "OPEN", "EXPLICIT NEGATIVES",
                 "SOURCE BASIS", "returns vN+1 with zero calls", "grants no invocation authority")),
    ("GENERATE and send-readiness", (
        "Direct: explicit current generation", "No extra approval turn",
        "accessible, uniquely identifiable artifact", "exact prompt, operation, category, target or area",
        "field authority, preserved state, reference assets and roles",
        "inputs and attachments, exposed options and current routed sources", "Material change makes it stale",
        "Lost context or ambiguity blocks reuse", "Unrelated conversation alone leaves it current",
        "stop without direct generation", "displayed prompt without rewriting", "Hidden backend final prompts",
        "at most one assistant-initiated image invocation", "consumes authority on success, failure or uncertainty",
        "No automatic retry", "new explicit generation request and fresh affected checks",
    )),
    ("Verify and respond", (
        "visible evidence", "PASS", "LOCAL_FAIL", "STRUCTURAL_FAIL", "UNVERIFIABLE",
        "insufficient decisive evidence", "An attempt does not establish success",
        "never update requirements, defaults, Project sources or unresolved state",
    )),
])
def test_ci_places_behavior_with_its_owner(ci, heading, clauses):
    section = ci.split(f"## {heading}\n", 1)[1].split("\n## ", 1)[0]
    for clause in clauses:
        assert clause in section, clause


def test_scope_has_exactly_four_categories(ci):
    scope = ci.split("## Closed scope\n", 1)[1].split("\n## ", 1)[0]
    assert re.findall(r"^- ([A-Z_]+):", scope, flags=re.M) == [
        "IDENTITY_DOCUMENTATION", "CHARACTER_REFERENCE",
        "ITEM_WEARABLE_REFERENCE", "STRUCTURE_ENVIRONMENT_REFERENCE",
    ]


def test_spec_covers_fifty_cases():
    spec = (ROOT / "tests" / "TEST_CASES.md").read_text(encoding="utf-8")
    assert re.findall(r"^\| (\d\d) \|", spec, flags=re.M) == [
        f"{case:02d}" for case in range(1, 51)
    ]


def test_historical_archive_matches_migration_receipt():
    old_root = HUB / "Source_archive" / "Image Transcendent"
    assert not old_root.exists()
    receipt = json.loads((old_root.parent / "ARCHIVE_RECEIPT.json").read_text(encoding="utf-8"))
    rows = [row for row in receipt if row["old"].startswith("Image Transcendent/")]
    assert len(rows) == 22
    paths = [(HUB / row["archive"]).resolve() for row in rows]
    assert set(paths) == {path for path in ARCHIVE.rglob("*") if path.is_file()}
    assert sum("historical_sources" in path.parts for path in paths) == 7
    for path, row in zip(paths, rows, strict=True):
        payload = path.read_bytes()
        assert len(payload) == row["bytes"]
        assert sha256(payload).hexdigest() == row["sha256"]
