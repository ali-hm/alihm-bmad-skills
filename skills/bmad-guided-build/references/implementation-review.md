# Implementation review and scheduling

Read before any independent reviewer dispatch, including Party Mode. Use the plan's current risk classification in both Interactive and Auto modes.

## Review scheduling and isolation

1. Determine the required roster, current plan/diff snapshot, permitted delegation, fresh-context capability, and available reviewer slots. Reserve capacity for the coordinator; use reported host limits rather than assuming an unlimited team.
2. If capacity is smaller than the roster, run reviewers in waves of at most the available slots. One slot permits sequential fresh contexts. Keep the full risk-required or confirmed roster; batching does not waive reviewers or imply degraded independence.
3. Give each reviewer the same relevant raw artifacts, scope/permissions, and its own role objective. Do not include expected conclusions or another reviewer's report. Reviewers remain read-only. Keep earlier-wave reports out of later reviewers' input; store them separately if persistence is needed and permitted. Do not put findings into the shared plan until all required reviewers finish.
4. Keep the reviewed snapshot stable across waves. Collect all required reports, then synthesize findings/disagreements and show the receipt. The coordinator applies edits afterward. If the snapshot materially changes mid-review, rerun the affected reviewers against the new snapshot rather than combining incompatible reports.
5. Record reviewer IDs, roles, snapshot, wave/attempt, and outcome. Independence mode is PARALLEL SUBAGENTS, BATCHED SUBAGENTS, or SEQUENTIAL FRESH CONTEXTS when fresh contexts were used. Only same-context personas are DEGRADED; disclose that limitation and never call them independent-context reviews.

Use a bounded recovery policy for each required reviewer:

- Wait using the host's completion mechanism, respecting cancellation and host timeout/error signals. Do not repeatedly dispatch while a reviewer is still active.
- On a transient failure, allow at most one replacement attempt in a fresh context, and only after correcting the input/tool problem or observing restored availability. Preserve the failed attempt as evidence. A bad or contrary finding is not a dispatch failure.
- If that attempt also fails, the capability is permanently unavailable, or the blocker has not changed, mark the required phase BLOCKED. Preserve useful completed reports, name the missing role/evidence, and stop dependent implementation/final completion. Do not relaunch the same blocked roster in a loop.
- When fresh contexts are unsupported from the outset, the documented same-context fallback may run with DEGRADED independence, unless project instructions require independent contexts. An actual failed required reviewer is not silently replaced by a persona to clear the failure.
- Targeted re-review after a substantive fix is new verification work, not a dispatch retry; it still uses this bounded policy. Repeated substantive failure or disagreement needs escalation, not repeated unchanged edits/reviews.

No retry grants permission to edit files, commit, contact external systems, or broaden the reviewed scope.

## Independent Implementation Review — mandatory

This review is separate from:

- the implementing agent's own reasoning;
- BMAD Build's internal review;
- the pre-implementation Party Mode.

Its purpose is to independently inspect what was actually implemented. Also run the mandatory initial [bmad-review ticket pass](ticket-review.md) on the same snapshot. Collect role and lens reports before synthesis or fixes; neither pass replaces the other.

### Review target

Review:

- the ticket/spec;
- approved implementation plan;
- final code diff/change set;
- tests;
- relevant upstream architecture/requirements.

Review actual implementation, not only the plan.

### Reviewer independence

Follow [review scheduling and isolation](#review-scheduling-and-isolation). This policy also applies to Party Mode. Separate-context review remains mandatory when supported; the number of concurrent slots does not determine the required reviewer count.

### Reviewer count by risk

#### LOW

At least 2:
- Correctness/Test Reviewer
- Maintainability/Scope Reviewer

#### MEDIUM

At least 3:
- Correctness/Test Reviewer
- Architecture/Integration Reviewer
- Security/Reliability reviewer chosen according to relevance

#### HIGH

At least 4; choose 4–6 according to the relevant domains:
- Senior Code/Correctness Reviewer
- Architecture/Integration Reviewer
- QA/Test Reviewer
- Security Reviewer
- Reliability/Performance Reviewer
- domain specialist where relevant

#### CRITICAL

At least 5; choose 5–7 according to the relevant domains:
- Senior Code/Correctness Reviewer
- Architecture Reviewer
- QA/Test Reviewer
- Security/Threat Reviewer
- Reliability/Operations Reviewer
- compatibility/migration reviewer where relevant
- domain specialist

### Reviewer instructions

Each reviewer must independently answer:

1. Does implementation satisfy the ticket acceptance criteria?
2. Does it match the approved plan?
3. Does it violate upstream architecture/requirements?
4. Are there correctness bugs?
5. Are tests missing or weak?
6. Are there security/reliability/performance issues?
7. Did implementation introduce unnecessary scope?
8. Are compatibility/migration/deployment concerns missed?
9. Are there suspicious shortcuts, dead code, or TODOs?
10. What severity should each finding receive?

Severity:

- BLOCKING
- HIGH
- MEDIUM
- LOW
- NOTE

### Mandatory independent-review receipt

After all initial role/lens reviews and before any fixes, show this receipt alongside the `bmad-review` receipt, then perform [combined triage](ticket-review.md#initial-pass-and-combined-triage):

```text
Independent Implementation Review

Reviewers:
- ...

Independence mode:
PARALLEL SUBAGENTS | BATCHED SUBAGENTS | SEQUENTIAL FRESH CONTEXTS | DEGRADED

Findings:
BLOCKING:
- ...

HIGH:
- ...

MEDIUM:
- ...

LOW:
- ...

Disagreements:
- ...

No findings:
- state explicitly if a reviewer found none
```

Record the same evidence in the execution ledger.

The review phase is not COMPLETE until this receipt is shown.

---

## Fixing independent-review findings

The main implementing/coordinator agent applies fixes.

Subagents remain read-only.

### Auto-fix allowed

May automatically fix findings that:

- are implementation defects;
- remain inside approved ticket scope;
- do not change upstream decisions;
- do not materially change the approved plan.

Normally fix:
- BLOCKING implementation defects;
- HIGH implementation defects;
- relevant MEDIUM issues when clearly safe.

### Escalation required

Stop and require governance when a finding requires:

- new product behavior;
- architecture/security/data/deployment decision;
- scope expansion;
- changed acceptance criteria;
- cross-ticket/epic redesign;
- destructive operation not previously approved.

### After fixes

1. rerun affected tests;
2. rerun relevant validation;
3. perform a targeted independent re-review of changed/fixed areas;
4. show the re-review result;
5. run the final `bmad-review` pass on the current full ticket diff and reconcile findings as specified in [ticket-review.md](ticket-review.md#fix-validate-and-re-review);
6. update ledger and ensure final validation/review evidence still matches the final changes.

Do not close a BLOCKING/HIGH finding merely because code changed.
Require verification evidence.

---
