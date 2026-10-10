---
name: bmad-guided-build
description: A human-gated or automatic wrapper around bmad-build with Git checkpoints, mandatory evidence-backed plan review, repeatable Party Mode / Advanced Elicitation, and independent post-implementation review using parallel subagents when available.
license: MIT
metadata:
  version: "0.1.0"
---

# BMAD Guided Build

This skill orchestrates BMAD. It does not replace `bmad-build`.

Use it for one implementation ticket/change at a time.

It provides:

- a Git checkpoint before starting the next job;
- normal `bmad-build` plan generation;
- Interactive and Auto execution modes;
- repeatable `bmad-party-mode` and `bmad-advanced-elicitation`;
- independent parallel subagent review when the harness supports it;
- a mandatory execution ledger so required phases cannot be silently skipped;
- independent post-implementation review before completion.

---

# FINAL RESPONSE CONTRACT — HIGH PRIORITY

`bmad-guided-build` is the top-level orchestrator.

Outputs returned by nested workflows such as:
- `bmad-build`;
- `bmad-party-mode`;
- `bmad-advanced-elicitation`;
- test/review subagents;

are INTERMEDIATE CHILD-WORKFLOW RESULTS.

They are never, by themselves, the final user-facing response.

In particular, if `bmad-build` returns a completion message such as:

> Epic complete. All tickets implemented, verified, committed.

or:

> Work summary: ...

DO NOT relay that message as the final answer and stop.

Instead:

1. capture it as implementation evidence;
2. update the Guided Build Execution Ledger;
3. continue any still-required post-implementation review/fix/revalidation phases;
4. enter `FINALIZE_GUIDED_BUILD`;
5. reload the plan and ledger from disk;
6. synthesize the mandatory final response;
7. validate that the final response contains BOTH required top-level sections:
   - `## Implementation Result`
   - `## Guided Build Execution Summary`
8. only then send the final response.

A run is not COMPLETE until final-response synthesis itself is recorded as COMPLETE.

If the agent is about to end and those two required headings are not present in the response draft, it MUST NOT send the response. It must run the finalizer first.

---

# 0. Non-negotiable invariants

1. **One invocation = one ticket/change.**
2. Never automatically advance to the next ticket.
3. Never silently commit unrelated work.
4. Never silently make a consequential product/UX/architecture/security/data/deployment/technology decision.
5. A required review phase is not complete merely because the agent says it ran.
6. A required review phase is complete only when:
   - the review actually ran;
   - its evidence is recorded in the execution ledger;
   - a visible result summary is shown to the user.
7. If a required phase cannot run, mark the workflow BLOCKED. Do not pretend it completed.
8. Subagent reviewers must be read-only reviewers. The coordinator/main agent owns edits.
9. Reviewer independence must be preserved: do not reveal one reviewer's findings to another before that reviewer finishes.
10. Implementation begins only after the current plan has passed the required approval path.
11. A nested BMAD/agent completion message is never the terminal response of this skill.
12. Before sending the final response, re-read the persisted ledger/plan and execute `FINALIZE_GUIDED_BUILD`.
13. The final response must contain both mandatory report headings exactly.

---

# 1. Execution modes

## Interactive mode

Default.

Flow:

Git checkpoint
→ `bmad-build` creates plan
→ five-option plan menu
→ optional repeatable Review / Advanced Elicitation / Party Mode
→ explicit user approval
→ implementation
→ independent implementation review
→ fixes/verification
→ completion.

## Auto mode

Enabled only by explicit user request, for example:

- `Use bmad-guided-build in auto mode for the next ready ticket.`
- `Use bmad-guided-build --auto for ticket 3.2.`

Do not infer Auto mode from vague wording.

Flow:

Git checkpoint
→ `bmad-build` creates plan
→ classify LOW / MEDIUM / HIGH / CRITICAL
→ risk-appropriate plan review
→ evidence-backed review results
→ safe plan refinements
→ approval
→ implementation
→ independent implementation review
→ safe fixes
→ revalidation
→ completion.

CRITICAL work always requires explicit human approval before implementation.

Auto mode may autonomously refine and implement an already-approved ticket.
Auto mode may not autonomously redefine upstream project truth.

---

# 2. Mandatory Guided Build Execution Ledger

As soon as `bmad-build` creates the implementation plan, append or maintain:

```md
## Guided Build Execution Ledger

Mode: Interactive | Auto
Importance: UNCLASSIFIED | LOW | MEDIUM | HIGH | CRITICAL
Ticket: <id>
Plan: <path>

| Phase | Required | Status | Evidence |
|---|---|---|---|
| Git checkpoint | Yes | ... | ... |
| BMAD plan | Yes | ... | ... |
| Plan risk classification | Auto | ... | ... |
| Structured plan review | Risk-dependent | ... | ... |
| Party Mode | Risk-dependent/user-selected | ... | ... |
| Advanced Elicitation | Risk-dependent/user-selected | ... | ... |
| Plan validation | Yes | ... | ... |
| Plan approval | Yes | ... | ... |
| Implementation | If approved | ... | ... |
| Tests/validation | If implemented | ... | ... |
| Independent implementation review | If implemented | ... | ... |
| Review fixes | If findings require | ... | ... |
| Final verification | If implemented | ... | ... |
| Final response synthesis | Yes | PENDING | Must contain both mandatory final report sections |
```

Allowed statuses:

- `PENDING`
- `IN_PROGRESS`
- `COMPLETE`
- `NOT_APPLICABLE`
- `BLOCKED`

Never set a phase to COMPLETE without concrete evidence.

Examples of evidence:

- plan file path;
- Git commit hash;
- Party Mode role list + result section;
- Advanced Elicitation method list + result section;
- test command + outcome;
- subagent reviewer IDs/roles + findings;
- code review result;
- final diff/validation result.

## Transition assertion

Before moving from one phase to another, check:

> Are all phases required before this transition COMPLETE or explicitly NOT_APPLICABLE?

If no:
- do not continue;
- run the missing phase or mark BLOCKED and explain why.

This assertion is mandatory in Auto mode.

Before terminating the skill, run a second terminal assertion:

> Is `Final response synthesis` COMPLETE, and does the response draft contain both
> `## Implementation Result` and `## Guided Build Execution Summary`?

If no, termination is forbidden.

---

# 3. Phase 0 — Previous-work Git checkpoint

Before planning the new ticket/change:

1. inspect Git status;
2. identify uncommitted changes;
3. distinguish where possible:
   - previous completed work;
   - planning/documentation;
   - unrelated user work;
   - generated/temp files.

Never commit automatically.

## Clean tree

Report:

> Previous work is committed; working tree is clean.

Record the current HEAD commit in the ledger.

Continue.

## Dirty tree

Stop before starting the new job.

Summarize modified/untracked/deleted files and likely ownership.

Ask:

1. **Commit previous work**
2. **Continue without committing**
3. **Stop**

### Commit previous work

- identify intended files;
- do not stage unrelated files;
- propose a concise conventional commit message;
- show staging scope;
- if scope is ambiguous, ask before staging;
- commit only intended files;
- show commit hash and subject;
- re-check Git status;
- record evidence in ledger.

### Continue without committing

- preserve all existing changes;
- record the dirty baseline clearly;
- warn that later diff attribution may be less precise;
- continue.

### Stop

Stop immediately.

---

# 4. Phase 1 — Create BMAD implementation plan

Invoke/use `bmad-build` for the requested ticket/change.

Preserve BMAD's normal behavior for:

- intent resolution;
- repository investigation;
- upstream context;
- footprint/risk analysis;
- written implementation-plan generation.

Stop at the plan checkpoint. Do not implement yet.

Capture:

- ticket/change identifier;
- plan path;
- plan summary;
- affected areas;
- open questions;
- footprint;
- risks;
- irreversible/high-impact actions.

Record BMAD plan phase as COMPLETE only after the plan file exists and has been read back successfully.

---

# 5. Auto-mode importance classification

Auto mode must classify the plan using the highest applicable level.

## LOW

Typical:

- localized change;
- small reversible footprint;
- no architecture/security/data/protocol/deployment change;
- low concurrency/reliability risk.

## MEDIUM

Typical:

- multiple modules/files;
- meaningful integration behavior;
- non-trivial state handling;
- moderate compatibility/concurrency/performance/reliability concerns;
- significant test surface.

## HIGH

Typical:

- foundational patterns;
- architecture-sensitive work;
- security-sensitive implementation within an already-approved boundary;
- reversible schema/persistence work;
- protocol/serialization/synchronization/ordering/distributed-systems behavior;
- deployment/update/backup/recovery/air-gapped lifecycle;
- broad cross-module footprint;
- high concurrency/performance/reliability risk.

## CRITICAL

Use when any applies:

- destructive/difficult-to-reverse migration;
- cryptography/key management;
- authentication/authorization boundary change;
- externally consumed breaking protocol/API change;
- irreversible data operation;
- broad security/privacy blast radius;
- production deployment/update change with large operational blast radius;
- uncertain rollback/recovery;
- failure could cause widespread data loss, security compromise, or service unavailability.

Record classification and rationale in the ledger and show it to the user.

---

# 6. Interactive plan approval menu

At the first plan checkpoint, and again after every non-approval review action, present exactly:

1. **Approve and continue**
2. **Approve and stop**
3. **Review the plan**
4. **Advanced elicitation**
5. **Party mode**

The menu remains available repeatedly.

The user may do sequences such as:

- Party Mode → Advanced Elicitation → Party Mode → Approve and continue
- Review → Party Mode → Review → Approve and stop
- Advanced Elicitation → Advanced Elicitation → Approve and continue

---

# 7. Structured plan review

Use for:

- Interactive `Review the plan`;
- LOW Auto mode.

Check:

- acceptance criteria coverage;
- alignment with PRD/UX/Architecture/approved decisions;
- hidden assumptions;
- missing steps;
- missing tests;
- dependency direction;
- compatibility;
- security/reliability;
- deployment/migration implications;
- unnecessary complexity;
- scope creep;
- rollback/recovery where relevant.

Report:

- Blocking
- Important
- Optional

For Auto LOW:
- apply only safe in-scope refinements;
- record findings and applied/rejected items;
- show a visible result summary;
- then continue.

For Interactive:
- let user choose which changes to apply;
- return to the five-option menu.

---

# 8. Party Mode — role selection and independent execution

## Interactive role selection

Do not invoke Party Mode until the final roster is confirmed.

First propose:

**Recommended party**
- 4–6 roles selected for this ticket.

Ask:

1. **Continue with recommended party**
2. **Customize party**
3. **Cancel**

### Customize party

Keep recommended roles preselected unless user chooses to clear them.

Show the current roster and role catalog:

1. System Architect
2. Senior Developer
3. QA / Test Engineer
4. Security Engineer
5. SRE / Reliability Engineer
6. DevOps / Deployment Engineer
7. Database / Data Engineer
8. Performance Engineer
9. API / Integration Engineer
10. Distributed Systems / Messaging Engineer
11. Network Engineer
12. Concurrency Specialist
13. Desktop Application Engineer
14. Web Frontend Engineer
15. UX Designer / UX Engineer
16. Accessibility Specialist
17. Product Manager
18. Business / Domain Analyst
19. Operations / Support Engineer
20. Observability Engineer
21. Release / Packaging Engineer
22. Backward-Compatibility Reviewer
23. Data Privacy / Compliance Reviewer
24. Threat Model / Red-Team Reviewer
25. Minimalism / Complexity Reviewer
26. Maintainability Reviewer
27. Failure-Mode / Pre-mortem Reviewer
28. Integration Reviewer
29. Migration Reviewer
30. User / Customer Advocate
31. Enterprise Identity / LDAP Engineer
32. Offline / Air-Gapped Deployment Engineer
33. Custom role

Do NOT use a single-choice role picker.

Use plain-text multi-selection, supporting:

- `+7,+10,-4`
- `set 1,2,3,10,24`
- `add Database Engineer, remove Security Engineer`
- `33: Cryptography Reviewer`
- `clear`
- `recommended`

After customization show the resulting roster and ask:

1. **Start Party Mode with this roster**
2. **Customize again**
3. **Restore recommended party**
4. **Cancel**

Only start Party Mode after explicit confirmation.

## Auto role selection

Auto mode selects 4–6 roles automatically from the same catalog.

Examples:

### General
- System Architect
- Senior Developer
- QA / Test Engineer
- Security Engineer
- SRE / Reliability Engineer

### Messaging/synchronization
- System Architect
- Senior Developer
- Distributed Systems / Messaging Engineer
- QA / Test Engineer
- SRE / Reliability Engineer

### Database/persistence
- System Architect
- Senior Developer
- Database / Data Engineer
- Performance Engineer
- QA / Test Engineer

### Authentication/LDAP
- System Architect
- Security Engineer
- Enterprise Identity / LDAP Engineer
- Senior Developer
- QA / Test Engineer

### Deployment/update/air-gapped
- System Architect
- DevOps / Deployment Engineer
- Offline / Air-Gapped Deployment Engineer
- Security Engineer
- Operations / Support Engineer

### UI/UX
- UX Designer / UX Engineer
- Senior Developer
- relevant Desktop/Web engineer
- Accessibility Specialist
- QA / Test Engineer

### Protocol/networking
- System Architect
- Distributed Systems / Messaging Engineer
- Network Engineer
- Security Engineer
- QA / Test Engineer

## Independent execution policy

When the harness supports parallel subagents:

1. execute the selected Party Mode roles as independent parallel read-only subagents;
2. give each reviewer:
   - plan path;
   - ticket/spec path;
   - relevant upstream artifacts;
   - relevant repository areas;
   - its own specialist review objective;
3. each reviewer must work in a separate context;
4. reviewers must not see other reviewers' findings until they finish;
5. reviewers must not edit files;
6. wait for all required reviewers to return;
7. synthesize only after all reports arrive.

For Cline IDE-style read-only subagents, this is the preferred mode.

If parallel subagents are unavailable:
- use fresh sequential subagents/contexts if available;
- otherwise use Party Mode in one context and explicitly report **DEGRADED INDEPENDENCE**.

Do not silently downgrade.

## Party Mode review questions

Each reviewer should challenge:

- hidden assumptions;
- architecture/integration;
- security;
- reliability;
- test coverage;
- operability;
- compatibility;
- unnecessary complexity;
- failure modes;
- scope creep.

## Mandatory Party Mode receipt

Party Mode cannot be marked COMPLETE until the user has been shown:

```text
Party Mode Result
Roles executed:
- ...

Per-role findings:
- <Role>: ...
- <Role>: ...

Cross-role disagreements:
- ...

Accepted recommendations:
- ...

Rejected recommendations:
- ... (reason)

Escalated:
- ...
```

In Auto mode this visible receipt is mandatory even though no approval is requested.

If the receipt was not produced, Party Mode is not complete.

## Applying recommendations

Automatically apply only recommendations that are:

- within approved ticket/spec scope;
- consistent with upstream artifacts;
- implementation-plan refinements;
- non-conflicting.

Do not auto-apply recommendations that:

- change product scope/acceptance behavior;
- change approved architecture/security/data/deployment/technology;
- create a new consequential decision;
- materially expand the ticket;
- contradict authoritative artifacts.

Such findings stop Auto mode and route through governance.

After applying safe changes:
- update the plan;
- revalidate consistency;
- record accepted/rejected/escalated recommendations;
- return to the five-option menu in Interactive mode.

---

# 9. Advanced Elicitation

Use `bmad-advanced-elicitation` against the exact plan.

## Interactive

Let the user select methods normally.

Afterward:
- apply only user-accepted refinements;
- update the plan;
- revalidate;
- show results;
- return to the five-option menu.

## Auto

Required for HIGH and CRITICAL.

Choose 2–4 methods appropriate to risk.

### Foundational architecture
- First Principles
- Pre-mortem
- Boundary/Edge-Case Sweep
- Complexity Reduction/Inversion

### Security/identity
- Red Team/Adversarial Review
- Threat/Abuse-Case Analysis
- Pre-mortem
- Assumption Challenge

### Distributed systems/messaging
- Failure-Mode Analysis
- Cascading Failure Simulation
- Boundary/Edge-Case Sweep
- First Principles

### Data/migration
- Migration Failure Analysis
- Reversibility/Rollback Analysis
- Edge-Case Sweep
- Pre-mortem

### Deployment/operations
- Pre-mortem
- Failure-Mode Analysis
- Rollback/Recovery Analysis
- Constraint Analysis

### Performance/concurrency
- Bottleneck/Constraint Analysis
- Race/Interleaving Analysis
- Boundary/Load Extremes
- Pre-mortem

If installed method names differ, choose the closest by intent.

## Mandatory Advanced Elicitation receipt

It cannot be marked COMPLETE until the user sees:

```text
Advanced Elicitation Result
Methods executed:
- ...

Findings:
- ...

Accepted refinements:
- ...

Rejected:
- ... (reason)

Escalated:
- ...
```

In Auto mode this receipt is mandatory.

Apply only safe in-scope refinements.
Escalate consequential decisions.

---

# 10. Auto-mode plan-review matrix

After the plan exists:

## LOW

Structured plan review only.

## MEDIUM

Party Mode.

## HIGH

Party Mode
→ reconcile safe findings
→ Advanced Elicitation
→ reconcile safe findings.

## CRITICAL

Same as HIGH
→ final validation
→ STOP for explicit human approval.

Before Auto mode may approve LOW/MEDIUM/HIGH, assert from the ledger:

- required plan review = COMPLETE;
- Party Mode = COMPLETE when required;
- Advanced Elicitation = COMPLETE when required;
- visible receipts were produced;
- no unresolved blocker/escalation exists.

If any assertion fails, Auto mode MUST NOT implement.

---

# 11. Automated Review provenance in the plan

Maintain:

```md
## Automated Review

Importance: <level>

### Structured Review
...

### Party Mode
Roles:
- ...

Per-role findings:
- ...

Accepted:
- ...

Rejected:
- ...

Escalated:
- ...

### Advanced Elicitation
Methods:
- ...

Findings:
- ...

Accepted:
- ...

Rejected:
- ...

Escalated:
- ...
```

Omit sections that are genuinely NOT_APPLICABLE.

Do not write a false empty section just to satisfy the format.

---

# 12. Final plan validation

Before approval verify:

- all acceptance criteria are addressed;
- no unresolved plan questions remain;
- no blocking review finding remains;
- tests are adequate;
- scope remains inside the ticket;
- no hidden consequential decision exists;
- no upstream artifact is contradicted;
- compatibility is addressed;
- rollback/recovery is addressed where relevant.

Record and show the validation result.

---

# 13. Plan approval

## Interactive

### Approve and continue

Explicit user approval.

Reload the current plan and verify no material change occurred after approval.

Then implement.

### Approve and stop

Record approval for handoff.
Do not implement.

### Material plan change

Any material change invalidates prior approval.

Material examples:
- implementation approach;
- module boundaries;
- schema/persistence;
- external interface/protocol;
- security behavior;
- deployment behavior;
- irreversible operations;
- compatibility guarantee;
- acceptance behavior;
- substantially larger footprint.

Return to plan approval.

## Auto

### LOW / MEDIUM / HIGH

If all required ledger phases and validation checks pass, the user's explicit Auto-mode request authorizes automated approval and implementation.

### CRITICAL

Never auto-approve.

Show:
- classification/rationale;
- plan path;
- Party Mode receipt;
- Advanced Elicitation receipt;
- final validation.

Then ask:

1. **Approve and continue**
2. **Approve and stop**
3. **Review the plan**

---

# 14. Implementation

Resume `bmad-build` from the approved plan.

Allow normal:

- implementation;
- tests;
- BMAD internal review/triage/fixes.

Do not start the next ticket.

After implementation/tests finish, do NOT declare the ticket complete yet.

Proceed to Independent Implementation Review.

---

# 15. Independent Implementation Review — mandatory

This review is separate from:

- the implementing agent's own reasoning;
- BMAD Build's internal review;
- the pre-implementation Party Mode.

Its purpose is to independently inspect what was actually implemented.

## Review target

Review:

- the ticket/spec;
- approved implementation plan;
- final code diff/change set;
- tests;
- relevant upstream architecture/requirements.

Review actual implementation, not only the plan.

## Reviewer independence

When parallel subagents are supported:

- spawn independent read-only reviewers in parallel;
- use separate contexts;
- do not expose findings between reviewers before completion;
- reviewers must not edit files.

If parallel subagents are unavailable:
- use fresh sequential reviewers;
- if that is unavailable, use same-context role separation and mark **DEGRADED INDEPENDENCE**.

Never claim independent review if independent contexts were not actually used.

## Reviewer count by risk

### LOW

At least 2:
- Correctness/Test Reviewer
- Maintainability/Scope Reviewer

### MEDIUM

At least 3:
- Correctness/Test Reviewer
- Architecture/Integration Reviewer
- Security/Reliability reviewer chosen according to relevance

### HIGH

At least 4–6:
- Senior Code/Correctness Reviewer
- Architecture/Integration Reviewer
- QA/Test Reviewer
- Security Reviewer
- Reliability/Performance Reviewer
- domain specialist where relevant

### CRITICAL

At least 5–7:
- Senior Code/Correctness Reviewer
- Architecture Reviewer
- QA/Test Reviewer
- Security/Threat Reviewer
- Reliability/Operations Reviewer
- compatibility/migration reviewer where relevant
- domain specialist

## Reviewer instructions

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

## Mandatory independent-review receipt

Before any fixes, show:

```text
Independent Implementation Review

Reviewers:
- ...

Independence mode:
PARALLEL SUBAGENTS | SEQUENTIAL FRESH CONTEXTS | DEGRADED

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

# 16. Fixing independent-review findings

The main implementing/coordinator agent applies fixes.

Subagents remain read-only.

## Auto-fix allowed

May automatically fix findings that:

- are implementation defects;
- remain inside approved ticket scope;
- do not change upstream decisions;
- do not materially change the approved plan.

Normally fix:
- BLOCKING implementation defects;
- HIGH implementation defects;
- relevant MEDIUM issues when clearly safe.

## Escalation required

Stop and require governance when a finding requires:

- new product behavior;
- architecture/security/data/deployment decision;
- scope expansion;
- changed acceptance criteria;
- cross-ticket/epic redesign;
- destructive operation not previously approved.

## After fixes

1. rerun affected tests;
2. rerun relevant validation;
3. perform a targeted independent re-review of changed/fixed areas;
4. show the re-review result;
5. update ledger.

Do not close a BLOCKING/HIGH finding merely because code changed.
Require verification evidence.

---



# 16.5 FINALIZE_GUIDED_BUILD — mandatory terminal phase

This phase owns the final user-facing response.

It runs AFTER:
- implementation;
- tests;
- BMAD internal review/fixes;
- independent implementation review;
- required re-review;
- final verification.

It also runs when the workflow ends BLOCKED or INCOMPLETE.

## Finalizer algorithm

1. Set ledger phase `Final response synthesis` to `IN_PROGRESS`.
2. Re-read from disk:
   - the current implementation plan;
   - the Guided Build Execution Ledger;
   - `## Automated Review` / review provenance;
   - Party Mode result sections;
   - Advanced Elicitation result sections;
   - Independent Implementation Review result sections;
   - final verification/test evidence.
3. Do not rely only on conversational memory or the last child-agent response.
4. Capture the last `bmad-build` completion output only as one evidence source.
5. Build the final response from persisted evidence.
6. The response MUST contain exactly these two top-level report sections:
   - `## Implementation Result`
   - `## Guided Build Execution Summary`
7. Under the execution summary, include:
   - chronological phase table;
   - Review Trace;
   - Plan Evolution;
   - Governance / Escalation Trace;
   - Quality Gate Summary.
8. Perform `FINAL_RESPONSE_SELF_CHECK`.
9. If the self-check passes, set `Final response synthesis` to `COMPLETE`.
10. Persist that final ledger status.
11. Send the response.
12. Do not append a second child-workflow completion summary afterward.

## FINAL_RESPONSE_SELF_CHECK

Before sending, verify all of the following:

```text
[ ] Heading "## Implementation Result" exists.
[ ] Heading "## Guided Build Execution Summary" exists.
[ ] Execution summary was derived from persisted ledger evidence.
[ ] Every required phase has a truthful status.
[ ] Party Mode roles/results are present when Party Mode ran.
[ ] Advanced Elicitation methods/results are present when it ran.
[ ] Independent implementation review is present when implementation occurred.
[ ] Plan evolution is summarized.
[ ] Governance/escalation status is stated.
[ ] Quality gate result is stated.
[ ] Final response synthesis ledger row is COMPLETE.
[ ] No unresolved BLOCKING finding is hidden.
[ ] No child-workflow "Epic complete / Work summary" output is being used as the whole final response.
```

If any box fails:
- do not send;
- regenerate or repair the final report;
- rerun the self-check.

## Child completion interception example

If `bmad-build` returns:

```text
Epic 10 complete.
Work summary:
- ...
Verification:
- ...
```

treat it internally as:

```text
Child workflow result captured.
Implementation evidence updated.
Continue guided-build finalization.
```

The final user-facing message must still be generated by `FINALIZE_GUIDED_BUILD`.

---

# 17. Final completion gate

Before declaring the ticket complete, assert:

- Git checkpoint evidence exists;
- plan exists;
- all risk-required plan reviews completed;
- visible review receipts were shown;
- plan was approved correctly;
- implementation completed;
- tests/validation passed or failures are explicitly accepted;
- independent implementation review completed;
- BLOCKING findings = 0;
- unresolved HIGH findings = 0 unless explicitly accepted by user;
- required re-review after fixes completed;
- no unresolved governance escalation remains.

The final response MUST contain two separate reports:

## 17.1 Implementation Result

Report what was actually implemented:

```text
Implementation Result

Ticket:
Status:

Implemented:
- ...

Files:
- Created: ...
- Modified: ...
- Deleted: ...

Acceptance Criteria:
- AC1: PASS / FAIL / PARTIAL
- ...

Tests & Validation:
- ...

BMAD Internal Review:
- ...

Independent Review:
- ...

Post-review Fixes:
- ...

Remaining Issues:
- ...

Deferred:
- ...

Git:
- ...
```

## 17.2 Guided Build Execution Summary

Build this report from the `Guided Build Execution Ledger`, not from memory.

Include every phase, including `NOT_APPLICABLE`, `BLOCKED`, `DEGRADED`, or explicitly skipped phases.

Use:

```text
Guided Build Execution Summary

| # | Phase | Required | Status | What happened | Evidence / Result |
|---|---|---|---|---|---|
| 1 | Git checkpoint | Yes | COMPLETE | ... | ... |
| 2 | BMAD plan | Yes | COMPLETE | ... | ... |
| 3 | Risk classification | Auto | COMPLETE | ... | ... |
| 4 | Structured plan review | Risk-dependent | ... | ... | ... |
| 5 | Party Mode | Risk-dependent/user-selected | ... | ... | ... |
| 6 | Advanced Elicitation | Risk-dependent/user-selected | ... | ... | ... |
| 7 | Plan validation | Yes | ... | ... | ... |
| 8 | Plan approval | Yes | ... | ... | ... |
| 9 | Implementation | If approved | ... | ... | ... |
| 10 | Tests/validation | If implemented | ... | ... | ... |
| 11 | Independent implementation review | If implemented | ... | ... | ... |
| 12 | Review fixes | If required | ... | ... | ... |
| 13 | Final verification | If implemented | ... | ... | ... |
| 14 | Final response synthesis | Yes | COMPLETE | Reloaded persisted ledger and rendered mandatory reports | self-check PASS |
```

Then include:

### Review Trace

```text
Structured Review:
- Used / Not applicable
- Main findings: ...

Party Mode:
- Used / Not applicable
- Roles: ...
- Independence mode: ...
- Findings: ...
- Accepted: ...
- Rejected: ...
- Escalated: ...

Advanced Elicitation:
- Used / Not applicable
- Methods: ...
- Findings: ...
- Applied refinements: ...
- Escalated: ...

Independent Implementation Review:
- Reviewers: ...
- Independence mode: ...
- Findings by severity: ...
- Fixes applied: ...
- Re-review result: ...
```

### Plan Evolution

If the plan changed during review, summarize:

```text
Initial plan:
- ...

Changes after Party Mode:
- ...

Changes after Advanced Elicitation:
- ...

Changes after direct review:
- ...

Final approved plan:
- ...
```

If no material change occurred, state:

> No material plan changes after initial planning.

### Governance / Escalation Trace

Report:
- consequential decisions encountered;
- governance workflows invoked;
- upstream artifacts changed;
- blocked/escalated recommendations;
- residual governance issues.

If none, state:

> No governance escalation was required.

### Quality Gate Summary

```text
Quality Gates

Plan complete: PASS / FAIL
Required plan reviews complete: PASS / FAIL
Plan approval: PASS / FAIL
Implementation complete: PASS / FAIL
Tests/validation: PASS / FAIL
Independent review: PASS / FAIL
Blocking findings remaining: <count>
High findings remaining: <count>
Governance blockers: <count>

Final Result: COMPLETE / BLOCKED / INCOMPLETE
```

## 17.3 Concision rule

Keep the final execution summary complete but compact.

Prefer:
- tables;
- counts;
- short findings;
- paths to detailed artifacts.

Do not reproduce full Party Mode or Advanced Elicitation transcripts.

## 17.4 Truthfulness rule

Never claim a phase ran merely because it was required.

The final summary must reflect the actual ledger state.

Examples:
- `BLOCKED — Party Mode could not run`
- `DEGRADED — no parallel subagents; sequential fresh-context review used`
- `NOT_APPLICABLE — LOW-risk ticket`
- `SKIPPED — user explicitly waived review`

Do not convert these to COMPLETE.

Only after both final reports are shown, `FINAL_RESPONSE_SELF_CHECK` passes,
and `Final response synthesis` is persisted as COMPLETE may the workflow be marked COMPLETE.

A normal `bmad-build` completion message does not satisfy this requirement.

---

# 18. Auto-mode stop conditions

Stop Auto mode immediately for:

- new consequential decision;
- upstream conflict;
- material scope expansion;
- ambiguous acceptance criteria;
- unresolved blocking plan finding;
- reviewer disagreement that changes product/architecture behavior;
- destructive/irreversible action not already approved;
- recommendation requiring another epic/ticket change;
- implementation review finding that cannot be fixed within approved scope.

Auto mode is autonomous execution, not autonomous governance.

---

# 19. Harness-aware subagent policy

Use the best available isolation:

1. **Parallel independent subagents** — preferred.
2. **Sequential fresh subagents/contexts** — fallback.
3. **Same-context personas** — last resort; label DEGRADED INDEPENDENCE.

For Cline editor subagents:
- use them as parallel read-only reviewers;
- let the main Cline agent synthesize and edit.

For harnesses with full writable teams:
- reviewers should still remain read-only for review phases unless this skill explicitly delegates a fix;
- do not let multiple reviewers race to edit the same implementation.

For Party Mode and implementation review, independence is more valuable than parallel editing.
