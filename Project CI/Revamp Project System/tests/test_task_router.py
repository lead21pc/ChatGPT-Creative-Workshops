"""Kiểm tra cấu trúc/contract artifact; không thực thi routing của model."""

from pathlib import Path
import re
import unittest

import yaml


SYSTEM = Path(__file__).resolve().parents[1]
ROOT = SYSTEM.parent
MAINTENANCE = ROOT.parent / "codex-workflows/revamp-system-maintenance/SKILL.md"
AGENTS = ROOT.parent / "AGENTS.md"


class TaskRouterContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = (SYSTEM / "TASK_ROUTER.yaml").read_text(encoding="utf-8")
        cls.router = yaml.safe_load(cls.raw)
        cls.ci = (ROOT / "Revamp_Project_System_CI_v3.1.md").read_text(encoding="utf-8")
        cls.authoring = (SYSTEM / "AT_R.md").read_text(encoding="utf-8")
        cls.cases = (SYSTEM / "tests/HANDOFF_ROUTE_TEST_CASES.md").read_text(encoding="utf-8")

    def test_conservative_yaml_and_exact_two_paths(self):
        tokens = list(yaml.scan(self.raw))
        self.assertFalse(any(isinstance(t, (yaml.tokens.AnchorToken,
                                           yaml.tokens.AliasToken,
                                           yaml.tokens.TagToken)) for t in tokens))
        self.assertNotIn("<<:", self.raw)
        self.assertEqual(self.router["version"], "2.1")
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
                          "IMPLEMENTATION TRANSFER = SETTLED DECISION HANDOFF",
                          "DOWNSTREAM TASK REQUEST = BOUNDED TRANSFER",
                          "TASK ROUTING != AUTHORITY TRANSFER", "TASK ID != PERMISSION"):
            self.assertIn(invariant, self.ci)
        self.assertIn("CI owns both IDs' evidence/acceptance/authorization/stage/decisions/scope", self.ci)
        authority = self.router["context_loading"]["authority"]
        for owner in ("evidence precedence", "acceptance status", "implementation/Git authorization",
                      "stage transitions", "decision promotion", "scope authority"):
            self.assertIn(owner, authority)

    def test_preflight_and_continuity_regressions(self):
        repo = self.router["repository_preflight"]
        self.assertEqual(repo["url"], "https://github.com/lead21pc/ChatGPT-Creative-Workshops")
        self.assertIn("current local working tree", repo["local_state"])
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

    def test_preflight_order_for_proposals_and_other_system_work(self):
        context = self.router["context_loading"]["order"]
        for rule in ("in either ID", "forms, evaluates, or plans",
                     "before target inspection", "for any project",
                     "inspect current sources before history",
                     "only needed FULL_FILE CURRENT",
                     "descriptive inspection", "settled-decision handoff"):
            self.assertIn(rule, context)
        history = self.router["historical_preflight"]
        self.assertIn("before target inspection", history["timing"])
        self.assertIn("after repository_preflight otherwise", history["timing"])
        self.assertIn("repository authority", history["excludes"])
        self.assertIn("Defer the dependent proposal", history["failure_behavior"])
        repo = self.router["repository_preflight"]["timing"]
        self.assertIn("after FULL_FILE history and before forming or evaluating a solution", repo)
        self.assertIn("Otherwise before history", repo)
        self.assertIn("Always before CURRENT recovery", repo)
        routing = self.ci.split("4A. ROUTING", 1)[1].split("5. MINIMUM", 1)[0]
        self.assertIn("FULL_FILE History before target for material structure/control proposals", routing)
        self.assertIn("sources first otherwise", routing)
        self.assertIn("CURRENT: needed FULL_FILE continuity", routing)
        self.assertEqual(re.findall(r"^\| (O\d\d) \|", self.cases, re.M),
                         [f"O{i:02}" for i in range(1, 8)])

    def test_vietnamese_protection_is_first_and_uses_two_gates(self):
        history = (SYSTEM / "HISTORY_AND_WHAT_NOT_TO_DO.md").read_text(encoding="utf-8")
        rules = history.split("## 9. What Revamp must not do", 1)[1].lstrip()
        self.assertTrue(rules.startswith("### 9.1 Preserve the Vietnamese output contract\n"))
        language = rules.split("### 9.2", 1)[0]
        for rule in ("**Contract gate.**", "**Clause gate.**", "explicit user requirement",
                     "every affected guard", "full behavioral equivalent",
                     "proposal review, implementation, and final diff review"):
            self.assertIn(rule, language)
        skill = MAINTENANCE.read_text(encoding="utf-8")
        for rule in ("bản tiền nhiệm trực tiếp", "cả hai gate ở History §9.1",
                     "khi xét đề xuất, triển khai và kiểm diff cuối",
                     "BASE = DESIGN SOURCE / LINEAGE", "HOLD UP: BASE SEMANTICS MISMATCH"):
            self.assertIn(rule, skill)

    def test_scope_function_and_form_selection_without_composition(self):
        selection = self.router["task_selection"]
        self.assertIn("task scope, then task function, then requested output form", selection["basis"])
        self.assertIn("quotes, sources, fixtures and examples do not activate", selection["basis"])
        self.assertIn("without persistent ID activation", selection["basis"])
        self.assertIn("default to the appropriate domain owner", selection["out_of_scope"])
        self.assertIn("Technical work on systems serving those domains is eligible", selection["out_of_scope"])
        self.assertIn("Domain content/unrelated prompts: domain owners", self.ci)
        self.assertIn("DIAGNOSIS != DESIGN; DESIGN != IMPLEMENTATION; TRANSFER != EXECUTION", self.ci)
        self.assertIn("Designing a diagnostic test is ID1 even when it includes a copyable prompt",
                      selection["direct_work"])
        for term in ("technical state or decisions", "technical prompt or brief", "already-designed test"):
            self.assertIn(term, selection["authoring"])
        self.assertIn("for one technical transfer or packaging artifact inside ID2", selection["mixed"])
        self.assertIn("independent deliverables", selection["mixed"])
        self.assertIn("never create a multi-ID execution graph", selection["mixed"])
        self.assertIn("ask one focused question", selection["ambiguity"])

    def test_handoff_delivery_and_recovery_contracts(self):
        delivery = self.router["task_selection"]["handoff_delivery"]
        for rule in ("actual file artifact", "delta text without file creation",
                     "repository write follows normal authorization", "not phrase matching"):
            self.assertIn(rule, delivery)
        self.assertIn("RECOVER → CLASSIFY → COMPRESS → SERIALIZE", self.authoring)
        self.assertIn("Use NOT DISCUSSED only when the inspected sources establish", self.authoring)
        self.assertIn("use UNKNOWN when the sources cannot establish that", self.authoring)
        self.assertIn("Keep rejection separate from deferral", self.authoring)
        self.assertIn("receiving context can take the next material design step without guessing",
                      self.authoring)
        self.assertIn("A text delta entails no file creation", self.authoring)
        template = (SYSTEM / "HANDOFF_TEMPLATE.md").read_text(encoding="utf-8")
        self.assertEqual(re.findall(r"^## (\d+)\. ", template, re.M), [str(i) for i in range(1, 11)])
        self.assertIn("trạng thái công việc đã phục hồi theo `AT_R.md`", template)
        self.assertIn("Đặt trạng thái cần để tiếp tục trong thân tài liệu", template)

    def test_generic_producer_and_codex_receiver_compatibility(self):
        agents = AGENTS.read_text(encoding="utf-8")
        for task in ("AUDIT", "IMPLEMENTATION"):
            self.assertIn(f"[REVAMP TRANSFER | {task}]", self.authoring)
            self.assertIn(f"[REVAMP TRANSFER | {task}]", agents)
            self.assertIn(f"[REVAMP → CODEX | {task}]", agents)
            self.assertNotIn(f"[REVAMP → CODEX | {task}]", self.authoring)
        for clause in ("current user presents a signed artifact as the current task",
                       "provenance and task class only", "AT_R owns the producer contract",
                       "AUDIT is read-only unless separately authorized",
                       "body and current request determine actual scope",
                       "Git stage/commit, branch/tag, push or deployment authority",
                       "quote, source, fixture, documentation, test, example, discussion",
                       "Other platforms follow their own controls"):
            self.assertIn(clause, agents)
        for clause in ("not recipient identity", "only when material",
                       "No fixed TARGET field is required", "even without signature recognition",
                       "Receiver-local controls govern actual execution",
                       "no Git or platform-local permission"):
            self.assertIn(clause, self.authoring)
        self.assertNotIn("USER-AUTHORIZED PROPOSAL", self.authoring)
        for prefix, count in (("G", 7), ("W", 3)):
            self.assertEqual(re.findall(rf"^\| ({prefix}\d\d) \|", self.cases, re.M),
                             [f"{prefix}{i:02}" for i in range(1, count + 1)])

    def test_full_vietnamese_output_contract(self):
        clauses = (
            "Use requested language; default Vietnamese", "everyday/direct/concrete even technically",
            "proper names/code/commands/literal quotes/exact external IDs",
            "product/API/library/tool names", "expressly requested foreign content",
            "Field terms aren't IDs", "Topic/source/prior terms/familiarity permit no code-switching/higher register",
            "Translate other English", "explain needed concepts at first use plainly, without lookup",
            "No bilingual labels unless requested", "Keep distinctions/abstraction/technical depth",
            "Silently scan user prose; fix violations",
        )
        for clause in clauses:
            with self.subTest(clause=clause):
                self.assertIn(clause, self.ci)
        self.assertIn("STATE TRANSFER != DECISION TRANSFER", self.ci)
        self.assertNotIn("CODEX PROMPT REQUEST", self.ci)

    def test_test_method_has_a_shared_reference_and_packaging_stays_in_id2(self):
        reference = SYSTEM / "PROJECT_VERIFICATION_PHILOSOPHY.md"
        self.assertIn(reference.name, self.router["context_loading"]["verification_reference"])
        self.assertIn(reference.name, self.authoring)
        method = reference.read_text(encoding="utf-8")
        self.assertIn("Revamp designs diagnostic tests in ID1", method)
        self.assertIn("evaluator-only criteria", method)
        self.assertIn("In an explicit compliance or control test", method)
        self.assertIn("A contaminated stimulus is invalid", method)
        self.assertIn("UNKNOWN or inconclusive", method)
        self.assertIn("destination and any output to collect", self.authoring)
        self.assertNotIn("Move cues added solely", self.authoring)

    def test_context_and_write_scope_are_conditional(self):
        paths = self.router["task_paths"]
        self.assertIn("Independent task -> direct work", paths["ID1"]["context"])
        self.assertIn("only needed FULL_FILE CURRENT", paths["ID1"]["context"])
        for condition in ("material state changed AND", "materially useful AND", "write scope authorized"):
            self.assertIn(condition, self.router["context_loading"]["handoff_write"])
        self.assertIn("only when the downstream artifact depends", paths["ID2"]["context"])
        self.assertIn("independent technical work needs no repository/history/CURRENT load",
                      self.router["context_loading"]["applies_to"])
        self.assertIn("independent tasks", self.router["repository_preflight"]["applies_to"])

    def test_authoring_is_bounded_and_not_execution(self):
        for rule in ("AUTHORING != EXECUTION", "CONTEXT AVAILABLE != CONTEXT REQUIRED IN ARTIFACT",
                     "HANDOFF PRESERVES REQUIRED TASK STATE != HANDOFF REPRODUCES CONVERSATION HISTORY",
                     "IMPLEMENTATION TRANSFER = SETTLED DECISION HANDOFF", "concrete blocker", "UNKNOWN"):
            self.assertIn(rule, self.authoring)
        self.assertIn("VERSION: 1.2", self.authoring)
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
        for prefix, count in (("M", 10), ("L", 14)):
            self.assertEqual(re.findall(rf"^\| ({prefix}\d\d) \|", self.cases, re.M),
                             [f"{prefix}{i:02}" for i in range(1, count + 1)])
        self.assertIn("STATIC PASS != LIVE BEHAVIOR PROVEN", self.cases)
        self.assertIn("LIVE HARNESS PASS != REAL-CONTEXT ROBUSTNESS PROVEN", self.cases)

    def test_active_references_and_encoding(self):
        paths = [ROOT / "Revamp_Project_System_CI_v3.1.md", ROOT / "CHANGELOG.md",
                 SYSTEM / "TASK_ROUTER.yaml", SYSTEM / "AT_R.md",
                 SYSTEM / "HANDOFF_TEMPLATE.md", SYSTEM / "PROJECT_VERIFICATION_PHILOSOPHY.md", AGENTS,
                 SYSTEM / "ARCHITECTURE_PREFLIGHT.md",
                 SYSTEM / "HISTORY_AND_WHAT_NOT_TO_DO.md",
                 SYSTEM / "Handoffs/REVAMP_SYSTEM_CURRENT.md",
                 SYSTEM / "tests/HANDOFF_ROUTE_TEST_CASES.md", MAINTENANCE, Path(__file__)]
        for path in paths:
            with self.subTest(path=path.name):
                raw = path.read_bytes()
                self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
                self.assertNotIn(b"\r", raw)
                self.assertTrue(raw.endswith(b"\n"))
                self.assertTrue(all(line == line.rstrip() for line in raw.decode("utf-8").splitlines()))
        history = (SYSTEM / "HISTORY_AND_WHAT_NOT_TO_DO.md").read_text(encoding="utf-8")
        self.assertNotIn("HANDOFF_ROUTER", history)
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8").split("## Trạng thái hiện hành", 1)[1]
        active = changelog.split("\n## ", 1)[0]
        self.assertIn("Revamp_Project_System_CI_v3.1.md", active)
        self.assertIn("v2.1, `active`", active)
        self.assertIn("AT_R v1.2", active)
        current = (SYSTEM / "Handoffs/REVAMP_SYSTEM_CURRENT.md").read_text(encoding="utf-8")
        anchors = current.split("## 8. Relevant source anchors", 1)[1].split("## 9.", 1)[0]
        self.assertIn("Revamp_Project_System_CI_v3.1.md", anchors)
        self.assertIn("Router v2.1 ACTIVE", anchors)
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
