"""Keep real runtime observations scoped independently of exact installed bodies."""
import unittest

from test_hub_contracts import ARCHITECTURE, ROOT, HUB_ROUTER, ROOT_CATALOG

CHANGELOG = ROOT / 'RUNTIME_EVIDENCE_CHANGELOG.md'


class RuntimeEvidenceTests(unittest.TestCase):
    def test_evidence_owner_separate_from_runtime_controls(self):
        body = CHANGELOG.read_text(encoding='utf-8')
        self.assertIn('not a runtime control', body)
        for path in (ARCHITECTURE, HUB_ROUTER, ROOT_CATALOG):
            self.assertNotIn('USER_CONFIRMED_LIVE_PASS', path.read_text(encoding='utf-8'))
