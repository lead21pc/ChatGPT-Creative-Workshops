"""Storage invariants; these tests do not certify ChatGPT runtime behavior."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

PROJECT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('cold', PROJECT / 'tools/build_cold_package.py')
cold = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cold)


class ColdPackageTests(unittest.TestCase):
    def test_exact_payloads_and_generation(self):
        data = (PROJECT / cold.PACKAGE).read_bytes()
        m, loaded = cold.validate(data, cold.sha(data), cold.manifest()['generation'])
        self.assertEqual(len(loaded), 7)
        for entry in m['sources']:
            self.assertEqual(loaded[entry['identity']], (PROJECT / entry['authoring_path']).read_bytes())
        self.assertEqual(data, cold.build())
        cold.check()

    def test_partial_prefix_tail_and_payload_rejected(self):
        data = cold.build()
        for corrupted in (data[:1000], data[:-1], data[:-5000], data + b'extra',
                          data.replace(b'Audit/control layer only.', b'Audit/control layer changed.', 1)):
            with self.subTest(length=len(corrupted)), self.assertRaises((ValueError, KeyError)):
                cold.validate(corrupted)

    def test_wrong_package_digest_and_generation_rejected(self):
        for digest, generation in (('0' * 64, None), (None, '0' * 64)):
            with self.assertRaises(ValueError):
                cold.validate(cold.build(), digest, generation)

    def test_required_source_missing_duplicate_or_boundary_wrong(self):
        data = cold.build()
        variants = (
            data.replace(b'91_RECONCILIATION_RECORD.md', b'91_MISSING_RECORD_SOURCE.md'),
            data.replace(b'BEGIN LOGICAL SOURCE', b'BROKEN LOGICAL SOURCE', 1),
            data.replace(b'END COMPLETE AETHERFIRE COLD PACKAGE', b'END PARTIAL AETHERFIRE COLD PACKAGE'),
        )
        for corrupted in variants:
            with self.assertRaises(ValueError):
                cold.validate(corrupted)

    def test_hot_change_invalidates_old_cold_generation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for path in set(cold.HOT + cold.COLD):
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((PROJECT / path).read_bytes())
            before = cold.manifest(root)['generation']
            target = root / cold.HOT[0]
            target.write_bytes(target.read_bytes() + b'\nChanged hot generation\n')
            after = cold.manifest(root)['generation']
            self.assertNotEqual(before, after)
            with self.assertRaises(ValueError):
                cold.validate(cold.build(root), expected_generation=before)

    def test_authoring_sources_remain_separate_and_unmodified(self):
        # Packaging cannot rewrite either temporal layer or an overlay.
        before = {p: (PROJECT / p).read_bytes() for p in cold.COLD + cold.HOT}
        cold.build()
        self.assertEqual(before, {p: (PROJECT / p).read_bytes() for p in before})


if __name__ == '__main__':
    unittest.main()
