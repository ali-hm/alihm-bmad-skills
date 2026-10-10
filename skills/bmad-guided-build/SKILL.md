---
name: bmad-guided-build
description: A human-gated or automatic wrapper around bmad-build with Git checkpoints, mandatory evidence-backed plan review, repeatable Party Mode / Advanced Elicitation, and independent post-implementation review using parallel subagents when available.
license: MIT
metadata:
  version: "0.2.0"
---

# BMad Guided Build

Coordinate one approved ticket or coherent change through BMad planning, implementation, and independent verification. This wrapper owns the gates and final response; `bmad-build` owns its internal implementation workflow. Never automatically advance to the next ticket.

## Essential boundaries

- Apply project instructions and existing user scope and permissions to every nested workflow. Preserve unrelated pending changes.
- Interactive is the default. Auto requires an explicit request for one bounded, approved ticket with settled upstream decisions.
- Classify risk as LOW, MEDIUM, HIGH, or CRITICAL in **both modes** before plan approval or implementation. Risk controls the mandatory post-implementation reviewer roster in both modes. Auto additionally requires its risk-specific plan reviews.
- CRITICAL implementation always needs explicit human approval of the current plan. Auto cannot supply that approval.
- Do not make consequential product, UX, architecture, security, data, deployment, or technology decisions silently. Stop dependent work and route unresolved choices through project governance.
- Commit, push, deploy, publish, or perform destructive actions only within explicit authorization. Auto does not grant those permissions.
- Reviewers are read-only and isolated. The main agent owns edits. A child completion message and BMad's internal review do not replace independent review or finalization.
- Required phases need actual execution, concrete evidence, and a visible result summary. Never convert an unavailable or failed phase into a pass.

## Read the relevant procedure

| When | Reference |
| --- | --- |
| Start, classify risk, approve, resume, or end early | [Execution and ledger](references/execution.md) |
| Review a plan, run Party Mode, or run Advanced Elicitation | [Plan review](references/plan-review.md) |
| Dispatch any reviewers, review implementation, fix, or re-review | [Implementation review and scheduling](references/implementation-review.md) |
| Return control, including a blocked or cancelled run | [Reporting and finalizer](references/reporting.md) |
| Author or evaluate this skill | [Behavioral scenarios](references/evaluation.md) |

Read execution before starting and reporting before ending. Load other references when their phase is reached, rather than loading every reference at entry.

## 1. Establish the baseline and reuse valid decisions

Read the work item, relevant upstream artifacts, project instructions, Git state, and existing plan/ledger. Resolve the installed `bmad-build` entrypoint and its actual planning/resume interface; do not invent flags or execute template sources.

Reuse explicit choices already supplied for this ticket: no-commit restrictions, permission to continue with pending changes, approved plans, and confirmed reviewer rosters. Verify that their scope and material plan version still match. Record each choice's source. Ask only for a missing decision, materially changed scope, or newly required permission.

The [Git checkpoint](references/execution.md#git-checkpoint) offers Commit / Continue without committing / Stop only when existing instructions have not resolved that choice. An explicit no-commit instruction selects the non-committing path; it does not clear unrelated changes or authorize other Git actions.

Missing dependencies block their affected path. Continue independent authorized analysis where useful; do not invent replacement workflows or execution evidence.

## 2. Create or resume the plan and classify risk

Use `bmad-build` to create the written plan and stop at its supported plan checkpoint. Read it back and maintain the Guided Build Execution Ledger there. On resume, verify current artifacts before repeating completed phases.

Apply the highest relevant [risk level](references/execution.md#risk-classification-in-both-modes), record the rationale, and show it to the user. Classify an older UNCLASSIFIED plan before proceeding. Preserve valid approvals/reviews when classification does not materially change the plan or reveal an unmet gate.

## 3. Review and approve the current plan

Interactive presents this repeatable menu when approval is needed:

1. **Approve and continue**
2. **Approve and stop**
3. **Review the plan**
4. **Advanced elicitation**
5. **Party mode**

Use [plan-review.md](references/plan-review.md) for the chosen action. Return to the menu after review unless an existing valid instruction already determines the next step. Confirm the Interactive Party Mode roster before starting; reuse confirmation for unchanged review scope.

Auto uses this matrix and shows evidence-backed receipts:

| Risk | Required plan review | Approval |
| --- | --- | --- |
| LOW | Structured review | Explicit Auto request permits approval after gates pass |
| MEDIUM | Party Mode | Same |
| HIGH | Party Mode, then Advanced Elicitation | Same |
| CRITICAL | Party Mode, then Advanced Elicitation | Explicit human approval of the current plan |

Validate acceptance coverage, scope, compatibility, relevant rollback/recovery, and upstream consistency before approval. Material changes invalidate affected approval/review evidence. Unresolved consequential findings block implementation even when review itself completed.

“Approve and stop” records approval and ends as APPROVED_STOPPED. It does not start implementation, tests, or implementation reviewers.

## 4. Implement, independently review, and verify

Resume `bmad-build` from the approved plan. Let it implement, test, and perform its internal review, preserving the one-ticket boundary and permission restrictions.

Then perform mandatory [independent implementation review](references/implementation-review.md). Use the current risk roster, fresh contexts where available, and capacity-aware batches. Collect all required reports before synthesis or edits. Disclose degraded independence if fresh contexts are unavailable.

Show the receipt, resolve BLOCKING findings and HIGH findings unless the user explicitly accepts residual risk, rerun affected validation, and obtain targeted independent re-review of fixes. Consequential changes return to governance or approval rather than being hidden in fixes.

Apply the bounded recovery policy to failing reviewers. Preserve completed evidence and report the blocker rather than repeatedly redispatching unchanged inputs.

## 5. Finalize every outcome truthfully

Read [reporting.md](references/reporting.md) and execute `FINALIZE_GUIDED_BUILD`. The final response must contain both headings exactly:

- `## Implementation Result`
- `## Guided Build Execution Summary`

Use the actual outcome: COMPLETE, APPROVED_STOPPED, CANCELLED, BLOCKED, or INCOMPLETE. Successful response synthesis does not make unfinished development COMPLETE. Handle absent plans or prohibited writes with the early-exit procedure; never create artifacts merely to satisfy reporting assertions.

Include the phase table, review trace, plan evolution, governance/escalation trace, and quality gates, with applicable detail and missing evidence identified. Capture child “Epic complete” or “Work summary” output as evidence, then finish this wrapper's review and reporting responsibilities.
