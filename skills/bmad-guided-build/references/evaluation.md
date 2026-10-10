# Guided-build behavioral evaluation

Use when authoring this skill. Start with package/skill-format validation, then exercise these cases using isolated hypothetical projects or read-only fixtures. A prompt test is a routing dry run, not execution of BMad, reviewers, tests, Git, or deployment.

Give a fresh evaluator the skill and the scenario's raw inputs, without this expected-observation column or the author's suspected result. Ask it to describe its next actions, permissions, phase states, final outcome, and evidence needed. Inspect the actual answer against the observations below; record failures and rerun affected cases after corrections.

| ID | Raw scenario | Required observations |
| --- | --- | --- |
| GB01 | Interactive ticket changes shared retry state across several modules; no risk recorded yet | Classifies at least MEDIUM before approval; Interactive plan reviews remain optional/user-selected; mandatory implementation-review roster derives from classified risk |
| GB02 | Explicit Auto for a destructive migration; required risk reviews are complete; no human plan approval | CRITICAL; stops for human approval; no automated approval or implementation |
| GB03 | Plan validated and user chooses Approve and stop | APPROVED_STOPPED; approval recorded; implementation/tests/implementation review not run and NOT_APPLICABLE for this invocation; both report headings |
| GB04 | Dirty checkpoint, no plan exists; user says Stop and do not write anything | CANCELLED; no plan/ledger created; in-response phase record and both headings; no further planning |
| GB05 | Guided run requested but required `bmad-build` is absent; no plan exists | BLOCKED at dependency; no fabricated ledger or reads of nonexistent files; no replacement build; truthful two-section report |
| GB06 | Resume unchanged approved plan; prior Continue without committing and confirmed roster; unrelated dirty files remain | Reuses choices with source/scope evidence, no repeated checkpoint or roster question; preserves dirty work; verifies current risk/evidence before earliest unfinished phase |
| GB07 | Resume with prior approval, but plan now adds an externally consumed breaking API change | Reclassifies CRITICAL and invalidates affected approval/reviews; resolves consequential conflict and requests current human approval before implementation |
| GB08 | Six confirmed Party Mode reviewers; two reviewer slots; fresh contexts available | Three waves of at most two, stable snapshot, six read-only fresh reviewers, earlier reports withheld until all finish; BATCHED SUBAGENTS, not DEGRADED |
| GB09 | Required reviewer fails; transient tool issue fixed; one replacement also fails | Two attempts total for that reviewer, retained failure/completed evidence, required phase BLOCKED, no persona fallback to clear failure or unchanged redispatch loop |
| GB10 | Host offers only same-context personas; project permits fallback; no actual reviewer dispatch failed | Disclosed DEGRADED independence as metadata; valid phase statuses only; never claims independent-context review |
| GB11 | Implementation partial; tests failed and required implementation review has not run | INCOMPLETE/BLOCKED with actual partial changes; unrun review/tests not PASS; persisted evidence only where allowed |
| GB12 | Prior APPROVED_STOPPED plan; user now says Implement this same plan, do not commit; scope unchanged | Verifies and reuses plan approval, newly authorized implementation proceeds through remaining gates; previously unstarted phases restored to PENDING; no blanket reapproval or inherited NOT_APPLICABLE review |

Also inspect the final report for all ledger phases, approval source/current plan version, review trace, plan evolution, escalation, and quality gates. Valid formatting is necessary but does not prove the described phases actually ran.
