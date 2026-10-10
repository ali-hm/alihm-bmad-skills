# Continuity and completion

Read for multi-session work, multi-ticket delivery, "continue", "what next", and final acceptance.

## State ownership

Keep decisions in the project's decision register, requirements and UX/architecture in their owning artifacts, spec history in its memlog, tickets in their configured store, and build/review evidence in plans or ledgers. Do not create another authoritative database of the same facts.

For substantial lifecycle work, reuse an existing coordinator note or add `sdlc-progress.md` under the resolved active initiative's folder. If no initiative applies, use a locally permitted planning location only when a durable note is needed. Resolve the owner before writing; do not scatter duplicate notes or store them in an unrelated global personal-memory folder.

The note is a navigation and recovery aid. It cannot approve a decision, clear a failed check, change a ticket state, or override current project truth.

Its coordinator status describes lifecycle navigation, not a guided-build outcome. Preserve the wrapper's exact outcome and phase evidence separately; “scope complete” in a coordinator note cannot convert APPROVED_STOPPED, BLOCKED, or INCOMPLETE implementation into COMPLETE.

## Minimal progress note

Record the relevant fields, not an empty template for every project:

```markdown
# SDLC progress

Updated: <date and timezone>
Target: <project/workspace and initiative>
Intent and authorized scope: <brief statement>
Mode: <attended; or explicitly authorized unattended scope>
Current step: <work item and specialist>
Status: <in progress / waiting for decision / blocked / scope complete>

## References
- Approved scope and decisions: <paths/IDs>
- Current spec and companions: <paths>
- Ticket store and active item: <references>
- Build plan, reviews, and verification: <paths>

## Handoffs
| Step | Specialist / item | Result | Evidence |
|---|---|---|---|

## Pending
- Decision/blocker: <question, impact, responsible party, evidence>
- Permission boundary: <exact action pending, or existing approval reference>
- Next action: <one concrete step>
```

Use links and brief evidence, not copied requirements or raw logs. Record user approval with its scope and source; do not invent timestamps or treat the note's wording as proof. Never store credentials or sensitive runtime data.

When writes are authorized, update after a material handoff, a new blocker, a pause/handoff, or completion. In read-only work, report progress and blockers in the response without writing a note. Tiny single-session changes need no extra progress file.

## Resume algorithm

1. Read the user's latest steering and relevant project instructions.
2. Find the active work through the configured initiative/ticket store and any coordinator note. Resolve ambiguity between plausible targets.
3. Inspect current pending changes and the referenced plan, spec, decisions, ticket state, and review evidence. Verify drift only where it affects the next action.
4. Reconcile disagreements through the artifact owner. A filename or status alone is not completion evidence.
5. Continue from the earliest unfinished or affected step. Reuse still-valid approvals; a material change may require renewed approval.
6. For blocked work, establish that the cause is resolved before changing its state through the owning workflow. Do not repeatedly resubmit a blocked plan.
7. For `built`/review work, inspect acceptance evidence instead of blindly redispatching implementation.
8. Resume implementation only through `bmad-guided-build`, using its mode authorization, resume rules, ledger, and finalizer; never resume by directly invoking its underlying build.

Preserve unrelated dirty work. Never stash, commit, revert, or recreate missing source to manufacture a clean baseline.

## Continue across tickets

The user's authorization must cover the proposed sequence; "next ticket" covers one, while "implement these approved tickets" can cover several. Follow dependency order and local checkpoints. Do not advance automatically when the selected wrapper or project requires a fresh invocation or acceptance decision.

After each build, verify its result and required acceptance before selecting another. Stop the affected sequence for unresolved scope, security, architecture, failed mandatory checks, or missing permissions. Record new unrelated findings separately.

An unattended runner is separate infrastructure. This skill does not schedule itself, survive session termination by itself, or create background jobs. Use an available scheduling/runner capability only on explicit request and within project policy.

## Completion evidence

For the requested scope, verify:

- Observable acceptance criteria are satisfied and relevant consumers remain compatible.
- Appropriate checks ran and their outcomes are accurately recorded.
- Material review findings are resolved or explicitly accepted under local rules.
- Required documentation/changelog and affected planning artifacts are consistent.
- The change set contains only intended work and preserved unrelated changes.
- Ticket closure, human acceptance, deployment, and release are claimed only when evidenced.

If some necessary check could not run, report partial verification or a blocker. Do not silently treat it as a pass.

The final response should say what finished, where the evidence is, what remains, and the next action if any. Use a nested wrapper's mandatory report format when applicable, while preserving the distinction between that ticket's result and the larger lifecycle.
