"""Kiểm tra cấu trúc/contract artifact; không thực thi routing của model."""

from pathlib import Path
import re
import unittest

import yaml


SYSTEM = Path(__file__).resolve().parents[1]
ROOT = SYSTEM.parent


class TaskRouterContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = (SYSTEM / "TASK_ROUTER.yaml").read_text(encoding="utf-8")
        cls.router = yaml.safe_load(cls.raw)
        cls.ci = (ROOT / "Revamp_Project_System_CI_v2.5.md").read_text(encoding="utf-8")
        cls.authoring = (SYSTEM / "AT_R.md").read_text(encoding="utf-8")
        cls.cases = (SYSTEM / "tests/HANDOFF_ROUTE_TEST_CASES.md").read_text(encoding="utf-8")

    def test_conservative_yaml_and_exact_two_paths(self):
        tokens = list(yaml.scan(self.raw))
        self.assertFalse(any(isinstance(t, (yaml.tokens.AnchorToken,
                                           yaml.tokens.AliasToken,
                                           yaml.tokens.TagToken)) for t in tokens))
        self.assertNotIn("<<:", self.raw)
        self.assertEqual(self.router["version"], "2.0")
        self.assertEqual(self.router["status"], "active")
        paths = self.router["task_paths"]
        self.assertEqual(set(paths), {"ID1", "ID2"})
        self.assertEqual(paths["ID1"]["name"], "REVAMP_CORE")
        self.assertEqual(paths["ID2"]["name"], "AUTHORING")
        self.assertEqual(paths["ID2"]["owner"], "AT_R.md")
        self.assertTrue((SYSTEM / paths["ID2"]["owner"]).is_file())
        self.assertEqual(self.router["task_selection"]["default"], "ID1")

    def test_ci_authority_size_and_preserved_invariants(self):
        self.assertLessEqual(len(self.ci), 8000)
        self.assertEqual(re.findall(r"^(\d+)\. ", self.ci, re.M),
                         [str(i) for i in range(1, 15)])
        for invariant in ("QUESTION != APPROVAL", "PROPOSAL != IMPLEMENTATION AUTHORIZATION",
                          "AUDIT != REDESIGN", "FAILURE DETECTION != DEBUG AUTHORIZATION",
                          "LOW DENSITY → TEST → ADD COMPLEXITY ONLY WHERE FAILURE REMAINS",
                          "CODEX PROMPT REQUEST = DECISION HANDOFF",
                          "AUTHORING REQUEST = BOUNDED TASK HANDOFF",
                          "TASK ROUTING != AUTHORITY TRANSFER", "TASK ID != PERMISSION"):
            self.assertIn(invariant, self.ci)
        self.assertIn("All IDs obey CI, sole owner", self.ci)
        authority = self.router["context_loading"]["authority"]
        for owner in ("evidence precedence", "acceptance status", "implementation/Git authorization",
                      "stage transitions", "decision promotion", "scope authority"):
            self.assertIn(owner, authority)

    def test_preflight_and_continuity_regressions(self):
        repo = self.router["repository_preflight"]
        self.assertEqual(repo["url"], "https://github.com/lead21pc/ChatGPT-Creative-Workshops")
        self.assertIn("current local working tree", repo["local_state"])
        self.assertIn("before history, CURRENT recovery", repo["timing"])
        self.assertIn("already satisfied, genuine gap or conflict", repo["proposal_check"])
        history = self.router["historical_preflight"]
        self.assertEqual(history["read_mode"], "FULL_FILE")
        self.assertTrue((SYSTEM / history["file"]).is_file())
        self.assertIn("before selecting or recovering any CURRENT", history["timing"])
        selection = "\n".join(self.router["selection"])
        for rule in ("WORKSTREAM RELEVANCE != HANDOFF NECESSITY",
                     "HANDOFF PRESENCE != HANDOFF NECESSITY", "no persistent activation",
                     "never version or timestamp discovery", "UNKNOWN"):
            self.assertIn(rule, selection)
        self.assertEqual(set(self.router["handoffs"]), {"revamp_system"})
        for entry in self.router["handoffs"].values():
            self.assertTrue((SYSTEM / entry["file"]).is_file())
        self.assertIn("Continue only independent task portions",
                      "\n".join(self.router["failure_behavior"]))
        boundaries = "\n".join(self.router["boundaries"])
        for rule in ("takes precedence", "STALE / CONFLICTED",
                     "STALE SHARED VERSION PIN != STALE ENTIRE HANDOFF", "Central Hub"):
            self.assertIn(rule, boundaries)

    def test_deliverable_based_selection_and_no_composition(self):
        selection = self.router["task_selection"]
        for term in ("main deliverable", "source, quotes or examples", "reassess each request"):
            self.assertIn(term, selection["basis"])
        for term in ("prompt", "enhanced prompt", "downstream brief", "bounded handoff"):
            self.assertIn(term, selection["authoring"])
        self.assertIn("discussion about authoring alone is ID1", selection["direct_work"])
        self.assertIn("Analysis needed to prepare one requested prompt stays within ID2", selection["mixed"])
        self.assertIn("independent deliverables", selection["mixed"])
        self.assertIn("never create a multi-ID execution graph", selection["mixed"])
        self.assertIn("ask one focused question", selection["ambiguity"])

    def test_context_and_write_scope_are_conditional(self):
        paths = self.router["task_paths"]
        self.assertIn("Independent task -> direct work", paths["ID1"]["context"])
        self.assertIn("only needed FULL_FILE CURRENT", paths["ID1"]["context"])
        for condition in ("material state changed AND", "materially useful AND", "write scope authorized"):
            self.assertIn(condition, paths["ID1"]["handoff_write"])
        self.assertIn("only when the downstream artifact depends", paths["ID2"]["context"])
        self.assertIn("needs no repository/history/CURRENT load", self.router["context_loading"]["applies_to"])
        self.assertIn("independent tasks", self.router["repository_preflight"]["applies_to"])

    def test_authoring_is_bounded_and_not_execution(self):
        for rule in ("AUTHORING != EXECUTION", "CONTEXT AVAILABLE != CONTEXT REQUIRED IN ARTIFACT",
                     "HANDOFF PRESERVES REQUIRED TASK STATE != HANDOFF REPRODUCES CONVERSATION HISTORY",
                     "CODEX PROMPT REQUEST = DECISION HANDOFF", "concrete blocker", "UNKNOWN"):
            self.assertIn(rule, self.authoring)
        output = self.router["task_paths"]["ID2"]["output"]
        for limit in ("does not execute", "authorize implementation/Git", "change stage/scope/acceptance",
                      "promote decisions/evidence"):
            self.assertIn(limit, output)

    def test_all_old_cases_and_focused_cases_remain_specifications(self):
        for prefix, count in (("R", 18), ("P", 7), ("Q", 4), ("N", 8), ("V", 15)):
            self.assertEqual(re.findall(rf"^\| ({prefix}\d\d) \|", self.cases, re.M),
                             [f"{prefix}{i:02}" for i in range(1, count + 1)])
        self.assertEqual(re.findall(r"^- (T\d\d):", self.cases, re.M),
                         [f"T{i:02}" for i in range(1, 7)])
        self.assertIn("STATIC PASS != LIVE BEHAVIOR PROVEN", self.cases)
        self.assertIn("LIVE HARNESS PASS != REAL-CONTEXT ROBUSTNESS PROVEN", self.cases)

    def test_active_references_and_encoding(self):
        paths = [ROOT / "Revamp_Project_System_CI_v2.5.md", ROOT / "CHANGELOG.md",
                 SYSTEM / "TASK_ROUTER.yaml", SYSTEM / "AT_R.md",
                 SYSTEM / "ARCHITECTURE_PREFLIGHT.md",
                 SYSTEM / "HISTORY_AND_WHAT_NOT_TO_DO.md",
                 SYSTEM / "Handoffs/REVAMP_SYSTEM_CURRENT.md",
                 SYSTEM / "tests/HANDOFF_ROUTE_TEST_CASES.md", Path(__file__)]
        for path in paths:
            with self.subTest(path=path.name):
                raw = path.read_bytes()
                self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
                self.assertNotIn(b"\r", raw)
                self.assertTrue(raw.endswith(b"\n"))
                self.assertTrue(all(line == line.rstrip() for line in raw.decode("utf-8").splitlines()))
        history = (SYSTEM / "HISTORY_AND_WHAT_NOT_TO_DO.md").read_text(encoding="utf-8")
        self.assertNotIn("HANDOFF_ROUTER", history)
        self.assertIn("TASK_ROUTER.yaml", self.ci)
        self.assertFalse((SYSTEM / "HANDOFF_ROUTER.yaml").exists())
        self.assertFalse((ROOT / "Revamp_Project_System_CI_v2.4.md").exists())

    def test_architecture_preflight_is_conditional_under_existing_id(self):
        preflight = self.router["architecture_preflight"]
        self.assertEqual(set(self.router["task_paths"]), {"ID1", "ID2"})
        self.assertEqual(preflight["file"], "ARCHITECTURE_PREFLIGHT.md")
        self.assertEqual(preflight["read_mode"], "FULL_FILE")
        self.assertIn("no independent authority", preflight["owner"])
        self.assertIn("either selected ID", preflight["applies_to"])
        self.assertIn("downstream proposal", preflight["applies_to"])
        for exclusion in ("mere mention", "explanation", "examples/hypotheticals",
                          "without a structural proposal"):
            self.assertIn(exclusion, preflight["excludes"])
        self.assertIn("no persistent activation", preflight["timing"])
        for boundary in ("ID1 stays ID1", "ID2 stays AUTHORING under AT_R.md",
                         "no multi-ID composition", "grants no scope/Git authority"):
            self.assertIn(boundary, preflight["limits"])
        self.assertIn("defer only dependent", preflight["failure_behavior"])

    def test_aggregate_review_and_stack_substitution_contract(self):
        reference = (SYSTEM / self.router["architecture_preflight"]["file"]).read_text(encoding="utf-8")
        for rule in ("LOCAL MINIMUM != SYSTEM MINIMUM", "review the whole proposal once",
                     "permanent operating surface", "new failure modes", "additional verification",
                     "current execution stack", "combined operating burden",
                     "impose no language quota", "then STOP", "CONTROL COMPLEXITY IS STILL COMPLEXITY",
                     "LOCAL IMPLEMENTATION FRICTION != PERMISSION TO INTRODUCE A NEW EXECUTION STACK",
                     "Before continuing that substitution", "unsuccessful smaller corrections",
                     "COMPONENT A PASS + COMPONENT B PASS != A↔B BOUNDARY PASS",
                     "STATIC PASS != LIVE BEHAVIOR PROVEN",
                     "LIVE HARNESS PASS != REAL-CONTEXT ROBUSTNESS PROVEN"):
            self.assertIn(rule, reference)
        self.assertEqual(re.findall(r"^\| (A\d\d) \|", self.cases, re.M),
                         [f"A{i:02}" for i in range(1, 11)])


if __name__ == "__main__":
    unittest.main()
