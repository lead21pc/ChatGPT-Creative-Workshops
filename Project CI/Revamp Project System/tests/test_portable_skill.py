"""Kiểm hợp đồng tĩnh của gói portable; không thực thi quyết định của mô hình.

Baseline Project vẫn hoạt động nên test_task_router.py tiếp tục kiểm baseline đó.
Các kiểm tra dưới đây không yêu cầu Router, ID, AT_R, số mục CI hoặc trần 8k.
Đối chiếu nghĩa, trigger, failure behavior nằm trong PORTABLE_SKILL_SEMANTIC_COVERAGE.md.
"""

from pathlib import Path
import re
import shutil
import tempfile
import unittest

import yaml


SYSTEM = Path(__file__).resolve().parents[1]
PACKAGE = SYSTEM.parents[1] / "skills/revamp-system"
EXPECTED = {
    "SKILL.md",
    "references/HISTORY_AND_WHAT_NOT_TO_DO.md",
    "references/ARCHITECTURE_PREFLIGHT.md",
    "references/PROJECT_VERIFICATION_PHILOSOPHY.md",
    "assets/HANDOFF_TEMPLATE.md",
}


def read_package(package):
    """Chỉ đọc chính gói, không tìm dependency ở repository hoặc host đã cài."""
    files = {p.relative_to(package).as_posix(): p.read_text(encoding="utf-8")
             for p in package.rglob("*") if p.is_file()}
    raw = files["SKILL.md"]
    frontmatter, body = raw.removeprefix("---\n").split("\n---\n", 1)
    return files, yaml.safe_load(frontmatter), body


class PortableSkillContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files, cls.meta, cls.core = read_package(PACKAGE)

    def require(self, text, *clauses):
        for clause in clauses:
            with self.subTest(clause=clause):
                self.assertIn(clause, text)

    def test_minimal_portable_frontmatter_and_scope(self):
        self.assertEqual(set(self.meta), {"name", "description"})
        self.assertEqual(self.meta["name"], "revamp-system")
        self.assertRegex(self.meta["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(self.meta["description"]), 1024)
        self.require(self.meta["description"], "technical system failures",
                     "repository-dependent proposals", "bounded technical transfers",
                     "authorized system changes", "not ordinary domain creation")

    def test_closed_resource_set_and_no_workstream_state(self):
        self.assertEqual(set(self.files), EXPECTED)
        self.assertFalse(any(p.is_symlink() for p in PACKAGE.rglob("*")))
        self.assertFalse(any(Path(name).name.endswith("_CURRENT.md") for name in self.files))
        self.assertNotIn("CORE.md", self.files)
        self.assertNotIn("agents/openai.yaml", self.files)

    def test_resources_resolve_inside_a_detached_copy(self):
        # Bản sao không chứa CI/Router/AT_R hoặc cấu hình của repository.
        with tempfile.TemporaryDirectory() as temporary:
            detached = Path(temporary) / "revamp-system"
            shutil.copytree(PACKAGE, detached)
            files, metadata, body = read_package(detached)
            self.assertEqual(metadata, self.meta)
            self.assertEqual(files, self.files)
            links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", body)
            self.assertEqual(set(links), EXPECTED - {"SKILL.md"})
            for resource in links:
                resolved = (detached / resource).resolve()
                self.assertTrue(resolved.is_relative_to(detached.resolve()))
                self.assertTrue(resolved.is_file())

    def test_no_legacy_or_provider_dependency_in_operating_instructions(self):
        operating = "\n".join(text for name, text in self.files.items()
                              if "HISTORY_AND_WHAT_NOT_TO_DO" not in name)
        for legacy in ("ID1", "ID2", "AT_R.md", "TASK_ROUTER.yaml",
                       "Revamp_Project_System_CI", "REVAMP_SYSTEM_CURRENT.md",
                       "Project CI/", "AGENTS.md", "CLAUDE.md", "CORE.md",
                       "Codex", "OpenAI", "ChatGPT", "KIMI_SKILL_DIR",
                       "disable-model-invocation", "allowed-tools"):
            with self.subTest(legacy=legacy):
                self.assertNotIn(legacy, operating)
        self.require(self.core, "No external base supplies missing governing logic",
                     "References specialize conditional work; this file decides when")

    def test_activation_and_target_authority(self):
        self.require(self.core, "once the skill is loaded",
                     "does not establish activation, continuous enforcement",
                     "higher-priority host controls", "target-local instructions",
                     "does not replace a target's governing controls",
                     "Actions require actual user authority plus actual host capability",
                     "CAPABILITY != AUTHORITY", "TASK REQUEST != PERMISSION ESCALATION",
                     "LOCAL IMPLEMENTATION != COMMIT/PUSH/DEPLOY",
                     "Do not assume all hosts share a Git policy",
                     "ask again for authority already validly granted")

    def test_operation_stage_and_delivery_are_not_collapsed(self):
        self.require(self.core, "DIAGNOSIS != DESIGN", "DESIGN != IMPLEMENTATION",
                     "TRANSFER != EXECUTION", "QUESTION != APPROVAL",
                     "PROPOSAL != IMPLEMENTATION AUTHORIZATION", "AUDIT != REDESIGN",
                     "HYPOTHETICAL != DECISION", "LOCAL FAILURE != GLOBAL REBUILD",
                     "DESIGNING A TEST != PACKAGING A SETTLED TEST",
                     "copyable block alone does not turn direct work into transfer",
                     "clear request to transition is a valid signal",
                     "Separate only genuinely independent deliverables",
                     "Quotes, sources, fixtures, examples")

    def test_current_target_precedes_conditional_history_and_continuity(self):
        procedure = self.core.split("## Inspect the target and select context", 1)[1]
        self.assertLess(procedure.index("inspect current relevant target sources"),
                        procedure.index("### Conditional bundled resources"))
        self.require(procedure, "Independent work proceeds directly",
                     "current local working tree, including relevant dirty dependencies",
                     "already satisfied, genuine gap or conflict",
                     "History is not a prerequisite for CURRENT",
                     "Read the entire selected reference (FULL_FILE)",
                     "defer only dependent conclusions/actions",
                     "continue independent work when safe")

    def test_reference_triggers_and_dependency_failure_behavior(self):
        resources = self.core.split("### Conditional bundled resources", 1)[1].split(
            "## Minimum sufficient change", 1)[0]
        self.require(resources, "prior failure, precedent, provenance or decision materially affects",
                     "Compare the historical mechanism and operating conditions",
                     "materially creates or changes structural execution surfaces or boundaries",
                     "behavioral test design/evaluation or packaging a settled behavioral test",
                     "use after state recovery when producing a full CURRENT",
                     "missing or unreadable", "name its exact path and dependency",
                     "Defer only the affected", "continue independent portions safely",
                     "Optional historical provenance outside the package is not a governing runtime dependency")

    def test_evidence_claim_state_and_local_updates(self):
        self.require(self.core, "observation, reported state, inference, scoped assumption",
                     "definition, proposal, hypothetical, uncertainty, conflict and unknown",
                     "acknowledgment or conditional use establishes no fact",
                     "Repetition and contextual fit add no evidence",
                     "Revise affected premises and dependent conclusions",
                     "OBSERVED FAILURE", "REPRODUCED FAILURE", "SUPPORTED RISK",
                     "HYPOTHETICAL FUTURE RISK", "PLAUSIBLE != CONFIRMED",
                     "NOT FOUND != FALSE", "UNKNOWN != PERMISSION TO INVENT",
                     "FILE EXISTS != DEPLOYED", "IMPLEMENTED != VERIFIED",
                     "STATIC PASS != LIVE BEHAVIOR")

    def test_complete_language_contract(self):
        self.require(self.core, "Use the requested language; default to Vietnamese",
                     "everyday, direct and concrete even for technical work",
                     "proper names, code, commands, literal quotes, exact external identifiers",
                     "foreign content expressly requested now",
                     "Field terms are not exact identifiers",
                     "permit neither code-switching nor a higher register",
                     "Translate other English", "explain needed concepts plainly at first use",
                     "Do not add bilingual labels unless requested",
                     "Keep distinctions, abstraction and technical depth",
                     "silently scan user-facing prose and fix language violations")

    def test_minimum_change_does_not_change_operation_or_ban_architecture(self):
        self.require(self.core, "Ground operation/stage first",
                     "even a small design exceeds an audit",
                     "concrete actual requirement or failure can justify substantial architecture",
                     "LOW DENSITY → TEST → ADD COMPLEXITY ONLY WHERE FAILURE REMAINS",
                     "CANDIDATE != REQUIRED STAGE", "Preserve verified working behavior",
                     "ARCHITECTURE IS NOT ONTOLOGY", "distinct recurring failure",
                     "Use a personal-use premise only when explicitly established")

    def test_recovery_and_semantic_completeness_before_compression(self):
        self.require(self.core, "RECOVER → CLASSIFY → COMPRESS → SERIALIZE",
                     "Use NOT DISCUSSED only when inspected sources establish",
                     "use UNKNOWN when they cannot establish",
                     "Keep rejection separate from deferral",
                     "Minimum sufficient handoff does not mean minimum fact count",
                     "An OPEN state may matter even without an immediate task",
                     "Do not merge distinct mechanisms",
                     "Omit it when it adds no material value",
                     "Keep continuation state in the body",
                     "not a cryptographic checksum, validator, proof")

    def test_transfer_signatures_and_actual_file_delta_delivery(self):
        self.require(self.core, "[REVAMP TRANSFER | AUDIT]",
                     "[REVAMP TRANSFER | IMPLEMENTATION]",
                     "body must work without signature recognition",
                     "Receiver-local controls govern execution",
                     "A delta handoff is copyable text against an identified baseline",
                     "A text delta entails no file creation",
                     "A downloadable artifact is not a repository write",
                     "say that no file was created",
                     "does not execute the target, call a downstream model, send the artifact",
                     "step number, exact content, destination and output to collect")

    def test_external_state_discovery_and_scoped_staleness(self):
        self.require(self.core, "CURRENT is bounded mutable workstream state outside",
                     "explicit source supplied by the user or target instructions",
                     "established repository-local convention for bounded discovery",
                     "location or authority is unestablished",
                     "Do not scan the whole filesystem",
                     "load state from the installed skill directory",
                     "carry a previous repository's CURRENT into a new target",
                     "Mark only affected claims STALE / CONFLICTED",
                     "A stale shared-version pin does not invalidate the whole handoff",
                     "material state changed AND cross-chat continuity is materially useful AND",
                     "read the entire existing record before replacing it",
                     "Creating a state file does not activate it")

    def test_capability_degradation_and_primary_task_recovery(self):
        self.require(self.core, "FAILURE DETECTION != DEBUG AUTHORIZATION",
                     "Stop relying on invalid paths, retain them as evidence",
                     "resume the primary task from sufficient safe current state",
                     "Do not assume repository access, filesystem, shell, Git, browser",
                     "background execution, subagents, approval APIs or write access",
                     "unavailable capability limits only dependent work",
                     "Host security/approval enforcement remains with the host",
                     "NOT RUN for unperformed checks")

    def test_conditional_references_preserve_specialized_behavior(self):
        history = self.files["references/HISTORY_AND_WHAT_NOT_TO_DO.md"]
        architecture = self.files["references/ARCHITECTURE_PREFLIGHT.md"]
        verification = self.files["references/PROJECT_VERIFICATION_PHILOSOPHY.md"]
        self.require(history, "historical cases", "no historical file, external link or old workflow",
                     "**Contract gate.**", "**Clause gate.**",
                     "Reading this reference is not a prerequisite for CURRENT")
        self.require(architecture, "LOCAL MINIMUM != SYSTEM MINIMUM",
                     "review the whole proposal once", "permanent operating surface",
                     "new failure modes", "combined operating burden",
                     "COMPONENT A PASS + COMPONENT B PASS != A↔B BOUNDARY PASS",
                     "no independent authority", "then STOP")
        self.require(verification, "evaluator-only criteria", "A contaminated stimulus is invalid",
                     "real opportunity to act", "Judge the target separately from the test procedure",
                     "not a mandatory execution pipeline", "not one provider")

    def test_template_is_an_asset_with_preserved_state_structure(self):
        template = self.files["assets/HANDOFF_TEMPLATE.md"]
        self.assertEqual(re.findall(r"^## (\d+)\. ", template, re.M),
                         [str(i) for i in range(1, 11)])
        for state in ("USER-PROVIDED STATE", "DECIDED != IMPLEMENTED",
                      "IMPLEMENTED != VERIFIED", "PROPOSAL != ACCEPTED",
                      "NOT RUN", "Handoff Receipt"):
            self.assertIn(state, template)
        self.require(template, "không sở hữu quy trình tìm nguồn",
                     "tại đích bên ngoài gói skill", "không tự kích hoạt")

    def test_utf8_lf_and_no_accidental_absolute_machine_paths(self):
        for name, text in self.files.items():
            with self.subTest(file=name):
                raw = (PACKAGE / name).read_bytes()
                self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
                self.assertNotIn(b"\r", raw)
                self.assertTrue(raw.endswith(b"\n"))
                self.assertTrue(all(line == line.rstrip() for line in text.splitlines()))
                self.assertNotRegex(text, r"[A-Za-z]:[\\/]")


if __name__ == "__main__":
    unittest.main()
