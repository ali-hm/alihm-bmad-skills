# Reporting and finalizer

Read before returning control for every outcome. Nested BMad/reviewer completion messages are evidence; this wrapper owns the final response.

## FINALIZE_GUIDED_BUILD

1. Determine the actual outcome using [execution.md](execution.md#early-exits-and-terminal-outcomes).
2. When a plan/ledger exists and writes are authorized, set Final response synthesis IN_PROGRESS. Read the plan, ledger, approvals, reviews, relevant test/verification evidence, and child results that actually exist.
3. If no plan exists or persistence is prohibited, use available conversation/tool evidence and an in-response phase record. State absent artifacts. Do not create/repair files solely for finalization.
4. Draft both mandatory sections below. Preserve failed, unavailable, waived, degraded, and unfinished work honestly. Read-only evidence inspection is not a live build or independent verification.
5. Check evidence for material claims, exact headings, valid phase statuses, accurate outcome, visible unresolved findings, and that a child summary is not the entire response.
6. When the report passes, set Final response synthesis COMPLETE and persist only where permitted. Record synthesis in-response for early/read-only exits. Do not change development outcome to COMPLETE because reporting succeeded.
7. Send the report. If a check cannot be resolved, report BLOCKED/INCOMPLETE with the limitation; do not loop to manufacture evidence.

## Mandatory response structure

Use exactly these two top-level report sections. Keep them compact and link detailed evidence instead of reproducing review transcripts.

```markdown
## Implementation Result

Ticket and outcome: <id; COMPLETE / APPROVED_STOPPED / CANCELLED / BLOCKED / INCOMPLETE>
Implemented: <actual changes, or no implementation and why>
Files: <created, modified, deleted, or none>
Acceptance: <criterion-level PASS / FAIL / PARTIAL / not exercised>
Validation: <actual commands/outcomes; unavailable checks separately>
Reviews/fixes: <BMad internal review; independent findings and re-review>
Remaining/deferred: <findings, accepted residual risk, next step>
Git: <baseline, pending changes, authorized commits/pushes if any>

## Guided Build Execution Summary

| Phase | Required | Status | What happened / evidence |
| --- | --- | --- | --- |
| <each ledger phase> | <condition> | <valid status> | <receipt/result/source/reason> |
| Final response synthesis | Yes | COMPLETE | <persisted evidence or in-response record> |

### Review Trace
<Structured review; Party Mode roles/independence/findings; elicitation methods;
implementation reviewers; disagreements; accepted/rejected/escalated findings;
fixes and targeted re-review. Say not run where applicable.>

### Plan Evolution
<Initial approach, changes/reasons, final approved version; no material changes;
or no plan created.>

### Governance / Escalation Trace
<Decisions, reused/obtained authorization and approval, affected upstream
artifacts, escalated recommendations, remaining blockers; or none.>

### Quality Gate Summary
<Plan, risk, required reviews, approval, implementation, tests, independent
review, re-review, governance: PASS / FAIL / PENDING / NOT_APPLICABLE with reasons.
Remaining BLOCKING/HIGH counts and explicit accepted risk. Actual final outcome.>
```

Include every ledger phase, including legitimate NOT_APPLICABLE/BLOCKED entries. Independence and waivers are evidence, not new phase statuses. Do not label unexecuted tests PASS because the user accepted their absence.

## Outcome-specific reporting

- **Approved and stopped:** APPROVED_STOPPED with approval evidence; implementation/tests/implementation review did not run. Do not call the ticket implemented, built, or done.
- **Cancelled before a plan:** CANCELLED, no plan/ledger written, in-response phase record. Respect the stop without further planning/review.
- **Missing dependency before planning:** BLOCKED with dependency/affected phase; no implementation. Do not read nonexistent artifacts.
- **Interrupted implementation:** INCOMPLETE/BLOCKED, actual partial changes/checks, safe next action. Unexecuted reviews are not passes.
- **Successful implementation:** COMPLETE requires acceptance evidence, applicable tests, independent review, resolved BLOCKING findings, resolved HIGH findings or explicit residual-risk acceptance, targeted re-review of fixes, and no governance blocker.

Do not imply deployment, publication, human acceptance, or ticket closure without evidence and authorization for those separate actions.
