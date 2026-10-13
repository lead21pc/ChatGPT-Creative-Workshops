# ChatGPT Project runtime shadow-test plan

Status: FUTURE TEST PLAN, not an executed test or activation. PENDING CI 3.0 CONTRACT. The candidate CI 3.0 file is not proof of installed Project instructions. Local filesystem access, hashes, and Markdown parsers cannot prove Project retrieval or model behavior.

## Assumptions that require the real Project

| Assumption | Why local checks cannot prove it | Required observation |
| --- | --- | --- |
| Installed CI 3.0 text equals the reviewed candidate | Repo copies do not update Project instructions | Inspect the installed instruction text, version, and any deployment limits. |
| Router 4.0, 00, 92, modules, 91, and overlays are accessible together | A local package may differ from uploaded Project sources | Inventory actual Project-visible files and a consistent source generation. |
| Project can enumerate all source files or reliably expose a catalog | Backend enumeration is not established | Try explicit inventory; if unavailable, require the published 00 catalog and mark discovery conditional on it. |
| Project returns complete headers and full files when requested | Search excerpts can masquerade as reads | Use seeded qualifiers at beginning, middle, and end; verify the model can identify each from retrieved text. |
| Project can retrieve exact mandatory context, index, target node, and closure | Node/range control is not established | Inspect the actual retrieved spans for each required component; if not observable, node mode remains unverified. |
| The model preserves owner, status, exception, and dependency boundaries | Static schema validation says nothing about reasoning | Score answers against a source-grounded oracle, including unknown and conflict cases. |
| Catalog and modules refer to one generation | Uploads may be partial or stale | Compare visible generation identifiers/content with the pinned shadow package; block mixed snapshots. |
| Context/latency improves without semantic loss | No measured Project-run data yet | Measure only where the runtime exposes trustworthy usage and timing; otherwise report UNMEASURED. |

If the Project does not expose retrieval spans or enough evidence to certify closure, NODE_OR_FULL cannot be considered verified by a correct-looking answer alone. FULL_FILE may remain the only defensible mode.

## Controlled experiment

Prepare a separate shadow Project or another explicitly approved isolated setup. Keep the normal v2.6/Router 3.2 Project untouched. Pin one reviewed candidate CI 3.0 text, one Router 4.0 proposal implementation, one source generation, the same overlays, model/settings, and the same prompts. First test Router 4.0 with all modules FULL_FILE against the source-grounded oracle. Then change only the pilot module's approved load mode to NODE_OR_FULL; do not change CI wording, source content, prompts, model, or memory between arms.

Use a small pilot such as file 80 only after its mandatory context, index, node boundaries, and dependencies are reviewed on a shadow copy. Include file 60 as a FULL_FILE control, cross-owner cases involving 10/80, and negative cases in which the target node omits a decisive exception so fallback must occur. Test module E from NEW_MODULE_ONBOARDING_TEST.md with the same frozen Router.

For every run, record: prompt/task class, actual installed controls, source generation, selected module IDs and owners, full paths or node IDs, observed retrieved spans, 92/91 evidence, overlays, fallback, output, and reviewer verdict. A claimed read without observable support is UNVERIFIED, not PASS. Answer scoring uses an independently prepared source/status oracle, not the full-file arm's answer as ground truth.

## Required probes

1. A matching E task and an unrelated task: E routes only in the first, with no Router-core edit.
2. A candidate E omitted from the catalog: no silent claim of complete discovery.
3. A history module self-claiming current, and a module trying to seize an existing owner: no promotion.
4. A cross-domain interface: both controlling owners load when each can change the conclusion; no hierarchy inferred from a shared actor.
5. A decisive 92 issue and 91 addendum: no false closure, stale-record answer, or UNKNOWN-to-FACT change.
6. A target node missing a late qualifier, a stale index, an unreviewed NODE_REQUIRES, and a snippet-only retrieval: FULL_FILE or SOURCE_LOAD_BLOCKED, never a pretend verified closure.
7. A required overlay or transitive overlay dependency missing: the dependent operation stops.
8. A decisive full file unavailable while historical material remains readable: SOURCE_LOAD_BLOCKED, not historical fallback.

## Review and stop gate

Proposed safety criterion for review: zero observed critical authority, truth-status, source-coverage, or old-canon revival errors in the approved pilot cases; no unverified node read counted as success. The user must approve the actual acceptance threshold and testable scope before activation. A structural PASS, existing DRAFT regression case, or one plausible answer does not establish runtime compliance. If the installed CI differs, retrieval is unobservable, generation is mixed, or a critical paired-test difference appears, keep FULL_FILE and return to design review.

Only a later, separately authorized task may install CI/Router/source changes, publish a branch, upload files, or change the default Project controls. Rollback means restoring the previous compatible control/source snapshot, not mixing one old Router with new node-enabled sources.
