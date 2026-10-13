# Orphan Payload Recovery Manifest — 2026-10-13

Status: historical/provenance archive only. Nothing in this directory is an active canon or control merely by presence.

Baseline: `b383e160273a110453baca6be85d4cd7f0cfa18a`.

`BUILDPROBE_INVENTORY.csv` accounts for all 156 BuildProbe files individually: 7 archived here, 74 byte-contained on baseline `main`, and 75 exact blobs reachable in pre-recovery Git refs.

## Recovered historical source

`internal_first_worldbuilding_core_philosophy.md` is restored separately at the shared `Source_Archive/` root because the current package manifest already records that exact historical path and SHA-256. It is explicitly non-canon and non-current.

| File | SHA-256 |
| --- | --- |
| `../internal_first_worldbuilding_core_philosophy.md` | `081b01f442510844da1b3b84e52883c87b829d3af0b2a61c11dbbd7a75d5ce03` |

## BuildProbe root snapshot

Source: `AetherFire_SourceArchitecture_BuildProbe_8fa3b68575004a1485849cda59a14c84`.

This is a byte-preserved experimental package snapshot. Its generated outputs and PowerShell reconstruction tool are superseded by the maintained package and current validation tooling; they remain here only for lineage and diagnostic provenance.

| File | SHA-256 |
| --- | --- |
| `.gitattributes` | `5ea223c7f624206a139b326f428768d9662eb5a550f34488c8dc298d5ea2c7bf` |
| `00_AETHERFIRE_CONSOLIDATION_INDEX.md` | `404ec41b2ca805ff5bae12c1db474356f5b18f87dcc2ac75df0dc3009aeca884` |
| `90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md` | `883599d49dc2621d10315b431767c8ebf5060caf0db5583c3a5f6d7938e2f58c` |
| `91_RECONCILIATION_RECORD.md` | `b9d70adb8d0563b4f8dd1c5d57916b33882bd9269d90b1cc08972a16fa428f72` |
| `92_OPEN_ISSUES_CURRENT.md` | `0dd887ed402270eccffbe4cf64ba3afb2e81c506e3b6d37f42f9f6ac7954d6e6` |
| `build_consolidation.ps1` | `02f69f92777537048ff48de4be8f563b178df042034fc51462dc5fe4368d945c` |
| `MANIFEST.md` | `2d7c53176d00f8cf15494eb391af5756b1634e283a47597dbaf4ad4d5c0f7678` |

## Pre-consolidation backup

Source: one canonical copy from the two byte-identical backups dated 2026-09-16.

| File | SHA-256 |
| --- | --- |
| `00_AETHERFIRE_CONSOLIDATION_INDEX.md` | `aae0d2dad8590c08e6fa1a853415546daa853d82f77ab98fe3bd48fd18a68d38` |
| `build_consolidation.ps1` | `f05d44c783158a15bb62b6b74e802a6ad9ed8e96f34f8dfa591bd488e51b4af2` |
| `MANIFEST.md` | `1487bdca7af3a5703e13819dbb66ac6770a559ec8c810485ba20a9eee6fa1c58` |

## Routing pilots

Only the minimum authored evidence set is retained for each external-only pilot: protocol, report, and observations or responses. Generated prompt wrappers, duplicated source excerpts, status captures, and temporary metadata copies are not archived.

| Pilot / file | SHA-256 |
| --- | --- |
| `section/REPORT.md` | `48db3443eb55695209d11adca2a15a241bdbbed8af8f13c574ad5d2a6507c396` |
| `section/protocol-before-runs.md` | `0c7d9201cac0920a9920712d35b150344f639d0479119c660c75d413db82828f` |
| `section/OBSERVATIONS.md` | `f4d35f61998ebb3a1d33468ef079fd9b24c52d9218d273dd087db2e7eecb6756` |
| `selector/REPORT.md` | `f907bee34ba9e95395ac2bcad4dd2cce9e4ff420d8251fc76e9165c8a46468ed` |
| `selector/protocol-before-runs.md` | `bd950f417e08aa42f6e2f37cd820664699c647bdbe330e05d14d76e463e8f16f` |
| `selector/OBSERVATIONS.md` | `bc33852bc7593a4ebdd653117dbbf1fee452d6f1260b4f389b8f72ce2a340ba2` |
| `sufficiency/REPORT.md` | `3cfbad74f722d9df91b42a367a874611d21e485ceba332bc7aaac22313997561` |
| `sufficiency/protocol-before-runs.md` | `5730745913e2401dc221fbd04ea8fee0f85c8e333079af1717e360349d806104` |
| `sufficiency/RESPONSES.md` | `cef901c1335b3def3ee47e34693c2eafa2c213a2de8cb95f738bf54c50da70ec` |

## Deliberately not recovered

- Temporary layout/audit scripts, staged patches, snapshots, and runner output: generated task scratch whose applied result is already represented in Git history.
- Pilot prompt wrappers and duplicate excerpts: experimental transport material; decisive methodology and results are retained above.
- Duplicate second backup: byte-identical to the preserved canonical backup copy.
- Temporary worktree mirrors whose file blobs are already reachable in Git.
