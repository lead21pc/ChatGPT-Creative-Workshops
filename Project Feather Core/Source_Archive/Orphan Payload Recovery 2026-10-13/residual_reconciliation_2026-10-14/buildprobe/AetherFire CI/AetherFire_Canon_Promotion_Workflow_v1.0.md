# AetherFire Canon Intake and Promotion Workflow v1.0

## Purpose and authority

This workflow reduces repeated file handling while keeping the user's canon decision, source provenance, generated package, and GitHub authority distinct.

- Canon authority is the latest commit on main in lead21pc/chatgpt-ci-versioning, under AetherFire Project/, as designated by the user.
- A ChatGPT draft, a file in New Canon and Consideration/, an audit result, or a proposed edit is not canon.
- Only explicit user acceptance authorizes a canon promotion. Acceptance of one bounded change does not accept unrelated recommendations or resolve other open issues.
- GitHub connector access is read-only. Codex handles local edits and Git operations; never claim the connector wrote, committed, or published anything.

## Intake and review

1. ChatGPT retrieves the current relevant canon from the designated GitHub repository using the Source Router. Record a Git commit SHA only when the tool identifies it as a commit; a per-file blob SHA is not a commit SHA. If the exact snapshot cannot be pinned, state REMOTE_SNAPSHOT_UNVERIFIED; if decisive source cannot be retrieved, stop that conclusion as SOURCE_LOAD_BLOCKED.
2. When a portable draft is needed, export one Markdown candidate to New Canon and Consideration/. Keep the candidate explicitly unconfirmed. Codex independently re-reads relevant GitHub main sources, then audits and revises that candidate in place, preserving its initial version/provenance before replacing content.
3. Report findings, unresolved conflicts/unknowns, exact proposed changes, and affected current domains. Do not update AetherFire Project/Source_Archive/, generated outputs, or current status before the user accepts the specific change.

## Promotion after acceptance

After explicit acceptance, Codex performs the following in the AetherFire project repository:

1. Record the repository, branch, local HEAD, remote main commit, and worktree status. Compare local history with remote main. Local commits absent from remote main remain unconfirmed as GitHub canon; do not carry them into a publication without explicit decisions. Base the promotion on the verified remote canon commit or an explicitly accepted local commit chain. Preserve unrelated changes and stage only task-owned paths.
2. Preserve the accepted input byte-exactly as a uniquely named source under AetherFire Project/Source_Archive/; never overwrite an existing source. Keep the original candidate or its provenance traceable.
3. Import only the accepted content into the appropriate builder inputs and reconciliation records. AetherFire Project/Source_Archive/ is an immutable provenance store: adding a file there alone does not make it canon or cause the builder to read it. Update build_consolidation.ps1 only when the accepted delta requires a new or changed build input/transformation, and keep excluded material excluded.
4. Run build_consolidation.ps1 from the project root. Read the generated outputs, index, reconciliation record, open-issues register, and manifest affected by the decision. Confirm that unresolved items and unrelated domains remain intact.
5. Run the package verifier and isolated rebuild checks. A passing verifier proves package hashes/rebuild behavior, not canon correctness or LLM compliance; separately compare generated text to the accepted decision.
6. Review the exact staged diff and commit only the verified, task-owned paths on a dedicated task branch. Do not push or merge into main without an explicit publish instruction. Once an authorized publish is completed, the new main commit becomes the canon snapshot.

## Rollback and handoff

- Use Git history/revert for rollback; do not rewrite history.
- Handoff must name the promoted source file, changed generated domains, unresolved items, verification performed, commit SHA, and whether publication to main has occurred.
- Until a verified commit is on main, keep labeling the change as accepted locally / not yet published; do not describe it as current GitHub canon.
