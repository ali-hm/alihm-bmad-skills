# Decision-governance behavioral evaluation

Use when authoring this skill. After format validation, give a fresh evaluator the skill and only each raw scenario. Request its operation, approval handling, affected owners/update sequence, allowed writes, terminal result, and evidence needed. Keep expected observations out of evaluator input.

| ID | Raw scenario | Required observations |
| --- | --- | --- |
| DG01 | Review ARCH-004 tenant isolation; no option chosen; user requests read-only comparison | REVIEW; analyzes current decision/dependencies and realistic alternatives including keeping it; no edits or implementation |
| DG02 | User explicitly approves PROD-007 retention change; affected kernel is memlog-derived; ticket store is repository-backed | CHANGE; reuses approval, preserves superseded decision; dispatches `bmad-spec` and `bmad-ticket` supported operations; no hand-patched kernel/log/state; verifies consistency before READY |
| DG03 | Same approved retention change, but `bmad-spec` is unavailable | Decision remains approved; propagation blocked with partial evidence; no manual derived-file edit; cannot declare planning READY |
| DG04 | Approved change affects an externally hosted ticket tracker; user permits local planning edits only | Local authorized propagation may continue; external ticket publication remains blocked; no inferred tracker permission or false READY |
| DG05 | Proposed offline mode depends on an unresolved approved-authentication change | Resolves prerequisite choice first; no invented dependency decision or implementation; approval only covers selected material option |
| DG06 | Approved decision and all affected planning artifacts are consistent; guided wrapper absent | Planning may be READY with evidence; separate implementation handoff blocked, no raw-build substitution or implementation |

Keep workflow completion, planning consistency, implementation readiness, and release separate. A recorded approval is evidence of the user's choice, not evidence that propagation or validation ran.
