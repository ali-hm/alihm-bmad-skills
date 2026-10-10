# Change-intake behavioral evaluation

Use when authoring this skill. Validate formatting, then give a fresh read-only evaluator the skill and raw scenario without the expected observations. Ask for primary classification, highest affected authority, next handoff, permissions, and whether active work can continue. Compare actual decisions, not wording.

| ID | Raw scenario | Required observations |
| --- | --- | --- |
| CI01 | Export omits rows with blank optional comments; approved requirement says include all matching rows; user authorizes a scoped fix without commits | DEFECT; smallest guided-build route; forwards no-commit and dirty-baseline restrictions; no new product decision or unnecessary replanning |
| CI02 | During approved ticket 3.2, user asks for guest access absent from the approved product/security baseline | FEATURE / SCOPE CHANGE with security impact; separate governance/planning, no silent ticket expansion or implementation |
| CI03 | Ticket and PRD disagree about whether a role may delete reports | CLARIFICATION at highest conflicting authority; stop affected implementation; no invented permission policy |
| CI04 | Driver patch fixes an issue while preserving approved architecture and observable behavior | DEPENDENCY / FRAMEWORK / RUNTIME / PLATFORM CHANGE; assess compatibility; bounded guided implementation when authorized; no automatic consequential-decision ceremony |
| CI05 | Clear approved defect, implementation authorized, wrapper missing but raw BMad builds present | Classification may complete; implementation blocked on wrapper; no raw-build fallback |
| CI06 | Review external patch only; patch changes tenant isolation without approval | EXTERNAL CHANGE / PR / PATCH with architecture/security conflict routed upstream; read-only review, no fixes or acceptance of unapproved behavior |

Record scenario IDs, actual route, side effects proposed/avoided, approval reuse, missing dependencies, and PASS/FAIL with reasons. These are dry runs unless specialist execution occurred in a separately authorized fixture.
