# Ticket review gate

Use after implementation and initial validation, before finalization, in both Interactive and Auto. Run `bmad-review` once with the initial implementation reviews and once on the final ticket changes. These passes supplement the risk-required reviewer roster; lens count is not reviewer-role coverage.

Cancelled, approved-and-stopped, or blocked-before-implementation runs do not start this gate. Partial implementation may receive useful authorized review, but cannot become COMPLETE while its implementation or checks remain unfinished.

## Dependency and permission check

Discover and read the installed `bmad-review/SKILL.md` before application implementation. Inspect its supported customization resolver, enabled lenses, and required runtime/setup. On invocation, resolve the target project's actual customization; do not assume the author's lens catalog or install paths. If setup, the skill, or required lens capability is unavailable, block implementation readiness or the affected review phase and name the missing dependency. Do not replace a missing pass with self-review or invent an invocation flag.

Inspect activation hooks, report destinations, and completion hooks for side effects. Reviewers must remain read-only; authorized review reports may be persisted by the coordinator. Use a documented compatible customization override when permitted, or block an incompatible operation. Never inherit authority to install, edit application code, publish reports, commit, or contact external systems from a review hook.

This wrapper explicitly requests `skill:bmad-review` for each pass, satisfying that skill's caller-activation requirement. Follow its actual execution interface, output contract, customization, and lens instructions; do not copy its implementation here.

## Scope, snapshot, and lens selection

Prepare the ticket, approved plan, acceptance criteria, relevant upstream constraints, and a reviewable implementation snapshot. Identify the baseline and exact ticket-owned tracked and untracked changes, including fixes, tests, and relevant changed documentation. Exclude unrelated pending work without altering it. If attribution is ambiguous, resolve that ambiguity before review instead of reviewing the entire dirty tree as this ticket.

For branch work, use the intended merge-base comparison; for a resumed dirty baseline, attribute the ticket's changes against its recorded baseline. Follow the installed skill's staging procedure for the scoped content and provide its absolute path. Record the revision or content hash, included files, and source artifacts. A ticket summary or plan alone cannot substitute for the actual diff. If completed work has no reviewable changes, report the discrepancy; empty input is not a passed review.

Select enabled lenses using the resolved catalog and explain the choice:

- Behavioral code: edge-case and verification-gap lenses, where supported and applicable. Verification-gap analysis needs repository/test access and must follow the lens's own behavioral screening.
- Behavioral documents such as specifications or skill instructions: an applicable behavioral lens. Do not force a code-only verification lens onto prose or invent phrase-matching tests for hand-authored instructions.
- Documentation changes: applicable structure/prose lenses, respecting their ordering and content-preservation rules.
- HIGH/CRITICAL work: add an applicable adversarial lens when available; also honor explicitly requested lenses and relevant project-specific lenses. Explicit user selections take precedence; a conflict with a mandatory project gate needs resolution.

The names above describe the inspected installation, not a fixed API. Resolve actual codes and availability. Missing a required base lens for the selected content, an explicitly requested lens, or a project-required lens blocks that gate; the absence of an optional adversarial or custom lens is disclosed. No applicable enabled lenses is a missing capability, not a clean review. Record each lens's applicability, selection/omission rationale, and resolved configuration identity. Preserve the lens set between passes unless scope, risk, customization, or explicit instructions change; reassess and record any change.

## Initial pass and combined triage

1. Complete all required independent role reviews and the initial `skill:bmad-review` pass against the same stable snapshot before applying fixes. Role reviewers and independent lenses receive raw scope/artifacts, not each other's findings. Dependent lenses may receive findings only as their installed workflow requires. Apply the wrapper's [capacity and recovery policy](implementation-review.md#review-scheduling-and-isolation) to lens dispatch as well as role reviewers.
2. Show the independent-review receipt and the `bmad-review` receipt: pass, snapshot, lenses, execution/independence, report location or in-response evidence, raw findings, and failed/unavailable analysis. A clean result is valid only if the selected applicable lenses actually ran successfully.
3. Keep the upstream findings in their declared shapes. The inspected `bmad-review` does not assign severity. The coordinator maintains a separate triage record linking each raw finding to evidence, wrapper severity (BLOCKING/HIGH/MEDIUM/LOW/NOTE), disposition, and rationale. Preserve overlapping lens reports; link them to one underlying issue/fix rather than deleting the source findings.
4. Choose **FIX**, **REJECT**, **DEFER**, or **ESCALATE** for every finding. Verify its trigger and consequence before editing. REJECT needs concrete contrary evidence; DEFER needs a reason and, for HIGH residual risk, explicit user acceptance. BLOCKING findings cannot be deferred to obtain COMPLETE. ESCALATE unresolved consequential changes to governance and stop dependent work.

Some installed adversarial instructions require a minimum finding count. Follow the selected lens's instructions, but never treat its count as proof that every suggestion is valid. Unsubstantiated or out-of-scope recommendations do not authorize edits. Do not demand an empty raw report: completion depends on sound dispositions and resolved required findings, not a finding quota.

## Fix, validate, and re-review

The main agent applies accepted in-scope implementation fixes under the [fixing policy](implementation-review.md#fixing-independent-review-findings). Reviewers do not edit. Material changes to the approved plan reopen affected reviews/approval; consequential scope or decision changes return to governance.

After corrections:

1. Rerun affected tests and validation; retain earlier failures and evidence of the new results.
2. Obtain targeted independent re-review of changed/fixed areas using the relevant role reviewers. Verify each fix against its trigger, acceptance criteria, and regression risks. If no fixes were necessary, record this targeted phase NOT_APPLICABLE with the reason.
3. Explicitly invoke final `skill:bmad-review` against the **full current ticket diff**, with the same authority context and applicable lens set. Ask for fix verification and new regressions. Independent lenses receive the raw final snapshot first; supply earlier finding/disposition evidence separately for reconciliation after their independent analysis, unless the installed lens requires it earlier. This final pass runs even when there were no initial findings or no code fixes.
4. Show its receipt and reconcile every earlier finding with final evidence. Record resolved, rejected, deferred/accepted, and escalated findings plus any new ones. Rejected or accepted findings may recur without forcing repeated edits; their evidence and acceptance must still apply to the final snapshot.
5. If final review prompts another edit, previous final evidence is stale for the affected content. Revalidate, re-review relevant role fixes, and run `bmad-review` again on the resulting final snapshot before completion.

Allow at most **two corrective cycles** per invocation after initial reviews (a cycle is triage-led edits, affected validation, targeted role review, and final lens review). A repeated substantive failure or disagreement requires escalation earlier; do not make unchanged edits or retry the same blocked input. If required findings remain after the limit, report BLOCKED with evidence and the decision or changed approach needed. Tool/reviewer failures separately follow the one-replacement recovery policy; they do not consume a fictitious correction cycle or justify unlimited retries.

## Ledger and completion

Record separate phases for initial `bmad-review`, combined finding triage, fixes, targeted independent re-review, final `bmad-review`, and final verification. Include pass/cycle, snapshot, lens/configuration identity, reviewer independence, raw reports, finding dispositions, fix locations, check results, and escalations. A report's successful delivery is not evidence that every lens succeeded.

On resume, preserve valid implementation, approval, and role-review evidence. Add missing review phases as PENDING for unfinished implemented work; a pre-0.3 ledger is not proof that these gates ran. Reuse completed pass evidence only when its snapshot, authority context, selected lenses/configuration, and permissions still match. Material final edits invalidate affected reviews and validation.

COMPLETE needs both actual lens passes, triage, applicable fix verification, current final checks, no unresolved BLOCKING findings, and no unaccepted HIGH findings or governance blocker. A missing/failed required pass is BLOCKED, never NOT_APPLICABLE or a clean review. This gate does not authorize acceptance, ticket closure, publishing, or release.
