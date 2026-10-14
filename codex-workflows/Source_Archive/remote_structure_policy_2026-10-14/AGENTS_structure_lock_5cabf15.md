# Repository Context Gate

Before analyzing, planning, reviewing, or modifying this repository, read [SYSTEM_CONTEXT.md](./SYSTEM_CONTEXT.md) first.

Treat it as repository-level context for interpreting the authoring model, project boundaries, control architecture, evidence states, and the relationship between repository-visible state and live ChatGPT Project runtime.

It does **not** override:
- the user's explicit task instructions;
- more specific project-local control files;
- project-declared source authority;
- canon decisions made by the author.

After reading SYSTEM_CONTEXT.md, continue with the smallest relevant project-specific source set for the task. Do not generalize one paracosm's architecture to another.

# Repository Structure Lock

The current local directory layout is an intentional management boundary and is locked repository-wide.

A structural change includes:
- creating, deleting, renaming, or moving any directory;
- moving files between directories or performing a bulk path migration;
- regrouping, flattening, normalizing, or reorganizing paths;
- any switch, checkout, merge, rebase, reset, restore, or cherry-pick whose resulting tree would change the local directory layout.

Read-only inspection is allowed. Before executing any structural change, require two separate explicit affirmations from the user:

1. Present the exact path map and concrete effects, then obtain the first affirmation approving that specific plan.
2. Immediately before execution, warn that the operation may affect the local layout, relative paths, scripts, links, nested repositories, worktrees, bindings, untracked data, and recovery behavior. Obtain a second explicit affirmation in a later user message.

One approval cannot satisfy both affirmations. Earlier general approval, approval to edit content, or approval from a different scope does not count. If the path map or expected effects change, restart both affirmations. Do not stage, commit, or execute the structural change before the second affirmation.

Treat GitHub or other remote refs separately from local refs and the working tree. A request to merge or delete a branch on GitHub authorizes only that remote operation unless the user explicitly names the corresponding local branch or local layout change.
