## FINAL RESPONSE OWNERSHIP — HIGH PRIORITY

When `bmad-guided-build` is active, it owns the final user-facing response.

Never end the run by directly relaying the completion output of `bmad-build`,
Party Mode, Advanced Elicitation, or any subagent.

Those outputs are intermediate evidence.

Before the final response:
1. re-read the persisted Guided Build Execution Ledger and plan;
2. run the guided-build finalizer;
3. ensure the response contains BOTH:
   - `## Implementation Result`
   - `## Guided Build Execution Summary`
4. verify the execution summary includes review trace, plan evolution,
   governance/escalation trace, and final quality gates.

Add and complete a `Final response synthesis` ledger phase.
If it is not COMPLETE, the guided build is not complete.

If the response draft lacks either mandatory heading, do not send it.

## Guided BMAD Build Workflow

Use `bmad-guided-build` for planned ticket/story implementation when governed plan review and independent implementation review are required.

### Before each new job

The skill must inspect Git status and, when previous work is uncommitted, ask:

1. Commit previous work
2. Continue without committing
3. Stop

Never commit automatically or include unrelated files silently.

### Plan approval menu

After `bmad-build` creates the implementation plan, Interactive mode uses:

1. Approve and continue
2. Approve and stop
3. Review the plan
4. Advanced elicitation
5. Party mode

Review the Plan, Advanced Elicitation, and Party Mode remain repeatable.

### Auto mode

Auto mode is allowed only when explicitly requested.

Risk policy:

- LOW → structured plan review
- MEDIUM → Party Mode
- HIGH → Party Mode + Advanced Elicitation
- CRITICAL → Party Mode + Advanced Elicitation + explicit human approval before implementation

CRITICAL work must never be auto-approved.

### No silent skipping

`bmad-guided-build` must maintain a `Guided Build Execution Ledger` in the implementation plan.

A required phase is COMPLETE only if:
- it actually ran;
- concrete evidence is recorded;
- a visible result summary was shown to the user.

If a required Party Mode, Advanced Elicitation, test, or independent review phase is missing, Auto mode must stop instead of proceeding.

### Party Mode independence

When the harness supports parallel subagents, selected Party Mode reviewers must run as independent read-only subagents with separate contexts and must not see each other's findings before completion.

If parallel subagents are unavailable, use fresh sequential reviewers where possible and disclose degraded independence if necessary.

### Independent post-implementation review

After implementation and tests, but before declaring the ticket complete, `bmad-guided-build` must perform an independent review of the actual implementation using read-only subagents/fresh contexts.

The implementing agent's self-review or BMAD Build's internal review does not replace this independent review.

The skill must show reviewer roles, independence mode, findings by severity, disagreements, fixes applied, and re-review results.

BLOCKING findings must be resolved.
HIGH findings must be resolved unless the user explicitly accepts the residual risk.

### Governance boundary

Auto mode may refine and implement an already-approved ticket.

It must stop for:
- new product/UX/architecture/security/data/deployment/technology decisions;
- scope expansion;
- upstream conflicts;
- ambiguous acceptance criteria;
- destructive actions not already approved.

One guided build applies to one ticket/change only.
Never automatically continue to the next ticket.


### Final guided-build reporting

At the end of every `bmad-guided-build`, the final response must contain:

1. **Implementation Result** — what changed, files, acceptance criteria, tests, reviews, fixes, remaining issues, and Git state.
2. **Guided Build Execution Summary** — a chronological report derived from the Guided Build Execution Ledger.

The execution summary must cover:
- Git checkpoint;
- BMAD plan creation;
- risk classification;
- structured plan review;
- Party Mode;
- Advanced Elicitation;
- plan approval;
- implementation;
- tests/validation;
- independent implementation review;
- review fixes;
- final verification.

It must also include:
- review roles/methods/results;
- plan evolution;
- governance/escalation trace;
- final quality-gate status.

Never report a phase as COMPLETE without ledger evidence.
Skipped, failed, unavailable, or degraded phases must be disclosed explicitly.


### Child workflow completion interception

A message like `Epic complete`, `Ticket complete`, `Work summary`, or `Verification`
returned by `bmad-build` is not the final response of `bmad-guided-build`.

Capture it as evidence, continue required post-implementation phases, then run
`FINALIZE_GUIDED_BUILD`.

The wrapper's two-part final report is mandatory even when the nested BMAD workflow
already produced a polished completion summary.
