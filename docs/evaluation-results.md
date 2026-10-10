# Evaluation results

Bundle: 0.2.0. Date: 2026-10-10 (Asia/Tehran).

This file records actual checks only. Scenario expectations live in the individual skill references. Routing evaluations use hypothetical read-only fixtures; no application was built or deployed during these evaluations.

## Method and evidence

Three fresh, read-only agent contexts evaluated 28 unique hypothetical scenarios. They received the actual skill instructions, needed phase references, and raw fixture facts, without the expected-observation tables or other reviewers' conclusions. The coordinator compared their concrete proposed actions against the scenario observations. Targeted reruns assessed clarified instructions; repeats are not counted as additional unique cases.

Host: local Codex. Evaluator model identifier was not recorded. Evidence is retained in this task's tool history under `/root/evaluate_guided`, `/root/evaluate_governance`, and `/root/evaluate_coordinator`, including their first-pass and follow-up final responses. The table below summarizes those actual responses; it is not a transcript of BMad or application execution.

## Guided build: 12 cases

Evaluator: `/root/evaluate_guided`; fresh context, read-only. GB02 and GB11 were rerun after clarification.

| Case | Observed routing/state decision | Final result |
| --- | --- | --- |
| GB01 | Classified shared retry work at least MEDIUM (conservatively HIGH); kept Interactive plan reviews user-selected and derived the implementation roster from risk | PASS |
| GB02 | Rerun classified destructive migration CRITICAL; human approval BLOCKED, implementation PENDING despite Auto and completed risk reviews | PASS |
| GB03 | APPROVED_STOPPED; unstarted implementation/checks NOT_APPLICABLE for that invocation; no ticket-completion claim | PASS |
| GB04 | CANCELLED without writing plan/ledger; in-response phase record and final report only | PASS |
| GB05 | Missing build dependency BLOCKED planning; no empty ledger or invented fallback | PASS |
| GB06 | Reused matching approval, non-committing baseline, and roster; preserved unrelated edits and rechecked evidence | PASS |
| GB07 | Breaking API revision classified CRITICAL; affected approval/reviews invalidated and consequential choice routed upstream | PASS |
| GB08 | Six fresh reviewers in three waves of two; stable snapshot, withheld reports, BATCHED SUBAGENTS without independence downgrade | PASS |
| GB09 | One corrected replacement after initial failure; second failure BLOCKED required review, without third retry or persona substitution | PASS |
| GB10 | Permitted same-context fallback disclosed DEGRADED as independence metadata, not phase status or independent-context review | PASS |
| GB11 | Rerun kept partial implementation IN_PROGRESS, failed required checks BLOCKED, unrun review PENDING, outcome BLOCKED; preserved failures | PASS |
| GB12 | Reused stopped plan approval; later implementation instruction restored newly required phases to PENDING and retained no-commit restriction | PASS |

First pass qualified GB02 because the rewritten risk table did not explicitly retain destructive migration as a CRITICAL trigger, and GB11 because failed-check phase status was underspecified. Both instructions were clarified and the evaluator explicitly confirmed the reruns resolved those ambiguities. GB01's exact MEDIUM/HIGH selection depends on synchronization/ordering facts; either can satisfy the case's minimum risk requirement with rationale. GB11's scope alone does not establish a risk category, and the evaluator did not invent one.

## Change intake and decisions: 12 cases

Evaluator: `/root/evaluate_governance`; fresh context, read-only. CI03/CI04/CI06/DG03/DG04 were rerun after clarifications; CI03 received a final targeted consistency reassessment.

| Case | Observed routing/permission decision | Final result |
| --- | --- | --- |
| CI01 | DEFECT; bounded guided Interactive handoff with no-commit restriction; no new product decision | PASS |
| CI02 | FEATURE / SCOPE CHANGE with security impact; separate governance before tickets/implementation, preserving active ticket scope | PASS |
| CI03 | CLARIFICATION; owner-led downstream reconciliation when approved authority settles intent; governance only for unresolved or changed consequential intent | PASS |
| CI04 | DEPENDENCY / FRAMEWORK / RUNTIME / PLATFORM CHANGE with defect tag; compatibility assessment before authorized guided implementation | PASS |
| CI05 | DEFECT classification complete but wrapper dependency blocks implementation; raw builds not substituted | PASS |
| CI06 | EXTERNAL CHANGE / PR / PATCH for read-only review; isolation conflict routed upstream without applying or accepting the patch | PASS |
| DG01 | REVIEW; retained current decision and compared alternatives read-only | PASS |
| DG02 | CHANGE; reused approval, preserved superseded history, dispatched spec/memlog and tickets through their owners before consistency validation | PASS |
| DG03 | BLOCKED explicitly by missing spec owner; retained approval and partial evidence, no manual generated-output edits or false READY | PASS |
| DG04 | BLOCKED explicitly by external tracker permission; continued permitted local reconciliation without tracker mutation | PASS |
| DG05 | Resolved authentication prerequisite before offline choice; no invented approved dependency or implementation | PASS |
| DG06 | Planning READY under consistent-artifact fixture, separately blocked implementation handoff on missing guided wrapper | PASS |

First pass identified unclear primary-class precedence for upgrades/external reviews and a BLOCKED label that named decisions but omitted dependency/permission blockers. These were clarified and rerun. The final targeted CI03 reassessment confirmed that class B and the governance-trigger section now agree about mechanical reconciliation. Actual approver roles and canonical locations remain project inputs, not globally invented defaults.

## Coordinator: 4 regression cases

Evaluator: `/root/evaluate_coordinator`; fresh context, read-only. SD17/SD20 and the status relationship were reassessed after clarification.

| Case | Observed routing/permission decision | Final result |
| --- | --- | --- |
| SD17 | Verified current artifacts, then resumed earliest unfinished guided phase while reusing approval, dirty baseline, no-commit, and confirmed roster | PASS |
| SD18 | Stopped dependent implementation on changed external API; reopened affected decision/approval/review gates, preserving unaffected choices | PASS |
| SD19 | Missing renderer blocked formal specialist review; no setup/tracking writes or unsupported invocation bypass under read-only scope | PASS |
| SD20 | Generated spec through its owner; local reconciliation allowed, external ticket update pending permission; no false synchronization/closure | PASS |

The coordinator evaluator found no routing failure and recommended clarifying that coordinator navigation status does not replace guided outcome. The added continuity statement was reassessed and the evaluator confirmed the distinction was explicit.

## Package checks and limits

| Check | Actual result |
| --- | --- |
| `python scripts/validate.py --release --tag v0.2.0` | PASS: four skills, matching versions/licenses, UI metadata, local references |
| Bundled skill-creator `quick_validate.py` for each skill | PASS for all four |
| `npx skills add . --list` | Four intended skills discovered; no installation performed |
| `git diff --check` | PASS |
| Older coordinator baseline cases | NOT_RUN during this update; cases remain documented |
| Live BMad plan/resume, fixture implementation/tests, actual reviewer scheduling/recovery | NOT_RUN; hypothetical decisions only |
| Live integrations on Codex or other supported hosts | NOT_RUN; no cross-host compatibility claim |

The 28 PASS results mean evaluators selected the required actions and state/permission boundaries in dry runs. They do not prove that BMad interfaces, application tests, or reviewer dispatch work in a live project. Package version/tag validation does not create a Git tag or release.
