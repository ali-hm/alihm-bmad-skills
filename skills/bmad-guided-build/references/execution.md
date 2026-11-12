# Execution and ledger

Read at entry, resumption, approval, and early exit. The [entrypoint](../SKILL.md) defines the core gates.

## Git checkpoint

Inspect status and identify previous completed work, planning files, unrelated changes, and generated files. Record HEAD if it exists; an unborn branch has no HEAD.

| Existing instruction/state | Action |
| --- | --- |
| Continue without committing, or do not commit | Preserve and record the dirty baseline; continue within authorized scope |
| Commit identified previous work | Stage only authorized scope, check staged diff, commit, record hash, recheck status |
| Stop | End as CANCELLED; do not start planning |
| Dirty tree, no applicable choice | Summarize ownership and offer Commit previous work / Continue without committing / Stop |
| Clean tree | Record observation and HEAD if available; continue |

Do not commit merely to make the tree clean. Ambiguous commit scope still needs resolution. A prior choice covers only its baseline and scope; new unrelated files are not authorized for staging. Record pending files for honest later attribution.

## Planning and resumption

Read the installed `bmad-build` and use its supported planning/resume interface. In the current preview, request `full` at entry and on resume. Its entrypoint renders with `--set workflow.route=full`; the automatic and `oneshot` routes can implement before the wrapper's approval. Read the rendered workflow. Stop at CHECKPOINT 1 with the written draft and resolved open questions, then run the wrapper's reviews and approval flow. Capture the ticket, plan path/version, acceptance criteria, footprint, questions, risks, and high-impact actions. BMAD plan is COMPLETE only after the file exists and is read back.

The wrapper owns approval. At the checkpoint, let upstream apply its approval transition to `ready-for-dev` only after the wrapper's gates pass. For Approve and stop, use that upstream checkpoint action and return control. For an approved continuation, proceed from that checkpoint or invoke the exact approved plan path on resume. A draft re-enters planning. An existing `ready-for-dev` or `in-progress` status by itself is insufficient approval evidence. Re-read the plan before implementation and recheck the approval if the content changed. Preserve upstream's frozen intent and record wrapper evidence outside it.

On resume, compare ticket, plan, code baseline, approvals, review evidence, and blockers. Reuse valid completed phases; investigate drift before redispatching. Reopen only affected phases. Formatting-only changes do not revoke otherwise valid approval.

If implementation and upstream validation are already evidenced, continue at the first pending wrapper gate. Passing a `built` plan to upstream Build again can re-enter its internal review, so use the existing snapshot and ledger for review-only resumption.

Before dispatch, check the installed workflow's actions and hooks. The current preview stages all changes since its Git baseline, including untracked files. If that would expose unrelated work to review or cause its review fixes to touch unrelated files, use a compatible scoped diff or an authorized isolated checkout that preserves the intended base and inputs. If neither is possible, stop the incompatible path before application edits and continue independent planning. Leave the original dirty tree intact.

For unfinished implemented work from before 0.3.0, add the new initial/final `bmad-review` and triage phases as PENDING. Preserve matching plan approval and independent role-review evidence; do not infer that the newly required passes ran from an older COMPLETE review label. Follow [ticket-review.md](ticket-review.md) for pass reuse and snapshot validity.

## Build completion boundary

The current preview's full-route presentation step marks the plan `built` after upstream verification, then requests a commit when the tree is dirty. Return to the wrapper at `built`, before that commit and any unauthorized completion hook. Keep the resulting work available for scoped independent review, fixes, final review, and verification. Record the return point and the actual validation in the ledger. Any explicitly requested commit of this ticket's work belongs after the wrapper's final checks and must be limited to its authorized files. Upstream has no documented no-commit option for this step. If a host cannot return control before the side effect, block that execution path before application edits.

`built` records the upstream implementation state. Wrapper completion requires its own evidence, and ticket acceptance or `done` requires the owning store workflow and applicable authorization.

## Risk classification in both modes

Classify before approval or implementation in Interactive and Auto, using the highest applicable level. Record the rationale and show it. Interactive plan reviews remain user-selected; its implementation-review roster still depends on risk.

| Level | Typical triggers |
| --- | --- |
| LOW | Localized reversible work; no architecture/security/data/protocol/deployment change; low concurrency/reliability risk |
| MEDIUM | Multiple modules; meaningful integration/state behavior; moderate compatibility, performance, concurrency, or reliability concerns |
| HIGH | Foundational patterns; security-sensitive implementation within approved boundaries; reversible persistence/schema work; protocol, serialization, synchronization, ordering, distributed systems, update/backup/recovery, or broad cross-module changes |
| CRITICAL | Destructive or difficult-to-reverse migration; cryptography/key management; authentication/authorization boundary changes; externally consumed breaking API/protocol; irreversible data action; broad privacy/security exposure; production changes with large operational impact; uncertain recovery; potential widespread data loss or unavailability |

A risk label does not approve an unresolved consequential decision. Reclassify when evidence increases risk; reopen affected reviews and approval before dependent work. CRITICAL always needs explicit human plan approval.

## Guided Build Execution Ledger

Maintain this in the plan when it exists and writing is authorized. Reuse the existing ledger rather than creating another authority store.

```markdown
## Guided Build Execution Ledger

Mode: Interactive | Auto
Importance: UNCLASSIFIED | LOW | MEDIUM | HIGH | CRITICAL
Ticket: <id and owning context>
Plan: <path and verifiable revision/hash/version>
Outcome: INCOMPLETE
Permissions: <scope, restrictions, and authorization source>

| Phase | Required | Status | Evidence / reason |
| --- | --- | --- | --- |
| Git checkpoint | Yes | PENDING | |
| BMAD plan | Yes | PENDING | |
| Plan risk classification | Both modes | PENDING | |
| Structured plan review | Auto LOW or user-selected | PENDING | |
| Party Mode | Auto MEDIUM/HIGH/CRITICAL or user-selected | PENDING | |
| Advanced Elicitation | Auto HIGH/CRITICAL or user-selected | PENDING | |
| Plan validation | Before approval | PENDING | |
| Plan approval | Before implementation | PENDING | |
| Implementation | If approved to continue | PENDING | |
| Tests/validation | If implemented | PENDING | |
| Independent implementation review | If implemented | PENDING | |
| Initial bmad-review | If implemented | PENDING | |
| Combined finding triage | After initial reviews | PENDING | |
| Review fixes | If findings require | PENDING | |
| Targeted independent re-review | If fixes require | PENDING | |
| Final bmad-review | If implemented, even without fixes | PENDING | |
| Final verification | If implemented | PENDING | |
| Final response synthesis | Every outcome | PENDING | |
```

Phase status has exactly five values: PENDING, IN_PROGRESS, COMPLETE, NOT_APPLICABLE, BLOCKED. Independence is separate: PARALLEL SUBAGENTS, BATCHED SUBAGENTS, SEQUENTIAL FRESH CONTEXTS, or DEGRADED. An unavailable required review is BLOCKED, never NOT_APPLICABLE.

Record actual commands/outcomes, plan version, reviewer IDs/roles, findings/receipts, approval source/scope, verification, and re-review results. Required review is COMPLETE only if it ran, evidence was recorded, and results were shown. Completed review can still contain a finding blocking a later gate.

For lens reviews, also record pass/cycle, snapshot, resolved lenses/configuration, raw output, and the coordinator's separate finding dispositions/severity. Follow the [ticket review completion gate](ticket-review.md#ledger-and-completion); final checks and reviews must cover the current changes.

A failed required check is BLOCKED while its failure is outstanding. During an actual authorized corrective run it can be IN_PROGRESS; only passing executed evidence makes that check COMPLETE. Retain earlier failures and do not add FAILED as a sixth status.

NOT_APPLICABLE needs a reason. An explicit waiver of a waivable requirement uses NOT_APPLICABLE with waiver source/scope; never COMPLETE. Auto, urgency, or silence are not waivers. A waiver cannot override higher-priority instructions or fabricate required approval. Do not use SKIPPED or DEGRADED as phase statuses.

Before advancing in either mode, verify the transition's prerequisites are COMPLETE or legitimately NOT_APPLICABLE, with no unresolved blocker. Future phases can remain PENDING while awaiting approval. Early exits use outcome rules rather than the development-completion gate.

## Plan validation and approval

Validate acceptance coverage, outstanding questions, blocking findings, adequate tests, ticket scope, upstream consistency, compatibility, and relevant recovery. Record and show the result.

Interactive uses the entrypoint's five-option menu. Auto uses the [plan-review matrix](plan-review.md) and cannot implement without required reviews, receipts, and validation. LOW/MEDIUM/HIGH automated approval derives from the explicit Auto request; CRITICAL approval comes from the human.

Reuse explicit approval only if it covers this ticket, current material plan, and implementation permission. Approval to stop approves the plan but does not authorize starting; a later request to resume/implement can supply that permission. Record source and matching plan version. Reuse confirmed reviewer rosters for unchanged review scope.

Material changes include approach, module boundaries, persistence, interfaces, security, deployment, irreversible actions, compatibility guarantees, acceptance behavior, or substantially larger footprint. Invalidate affected evidence and return to the approval path. Do not silently approve changed plans.

## Early exits and terminal outcomes

| Outcome | Meaning and handling |
| --- | --- |
| COMPLETE | Implementation satisfies applicable acceptance, validation, review, fixes/re-review, governance, and reporting gates |
| APPROVED_STOPPED | Plan approved; user chose no implementation. Unstarted implementation/test/review phases are NOT_APPLICABLE for this invocation, with that reason |
| CANCELLED | User stopped. Preserve partial evidence; unstarted future phases are NOT_APPLICABLE because cancelled; retain existing failed checks |
| BLOCKED | Missing dependency/permission/check/decision prevents progress. Affected phase is BLOCKED; dependent future phases remain PENDING |
| INCOMPLETE | Scope remains unfinished without a more specific outcome; identify unfinished phases |

Before a plan exists, do not claim a persisted ledger exists. Keep an in-response phase record. If writes are authorized and existing tracking is available, record the blocker there; a new empty plan/ledger is unnecessary. Read-only restrictions and cancellation take precedence over persistence instructions.

Use [reporting.md](reporting.md) for every outcome. Report missing evidence rather than looping to manufacture it. Reporting COMPLETE means the response was synthesized, not development completed. On resumption of APPROVED_STOPPED/CANCELLED, restore newly required future phases to PENDING and revalidate remaining evidence.

## Governance stop conditions

Stop dependent implementation for consequential decisions, upstream conflicts, scope expansion, ambiguous acceptance, unresolved blocking findings, disagreements changing approved behavior, destructive actions beyond authorization, or cross-ticket redesign. Continue useful independent authorized analysis. Preserve the one-ticket boundary; do not repeatedly retry unchanged blocked inputs.
