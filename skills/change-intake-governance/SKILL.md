---
name: change-intake-governance
description: Classify and route any new issue, bug, story, feature request, enhancement, architecture change, NFR change, dependency upgrade, refactor, incident, security finding, de-scope request, or integration problem after implementation has started. Use BMAD's smallest safe workflow, preserve upstream authority, require explicit approval for consequential changes, and never silently expand the active ticket.
license: MIT
metadata:
  version: "0.3.0"
---

# Change Intake Governance

Use this skill whenever new work or feedback arrives after the project has entered implementation or has an approved planning baseline.

The purpose of this workflow is to determine **where the incoming item changes project truth** before deciding how to act on it.

Do not automatically convert every incoming item into a ticket.

Do not automatically start implementation.

## Required implementation entry point

All implementation routes in this skill use the user's custom `bmad-guided-build`. Never invoke `bmad-build` or `bmad-build-auto` directly; the guided wrapper owns its internal build calls.

Use Interactive mode by default. Use the same skill's Auto mode only when explicitly authorized, allowed by project governance, and appropriate for an approved bounded ticket with settled decisions. Preserve its risk-required reviews, ledger, approval gates, and final report; CRITICAL work always requires human approval.

If `bmad-guided-build` is unavailable, report the dependency and block implementation rather than falling back to a raw build. Classification and independent planning may continue.

Do not silently expand the scope of an active ticket.

Reuse existing explicit scope decisions and permissions that still match the affected work. Carry their source, material plan/version, no-commit restrictions, and dirty-baseline choices into the guided handoff. Ask again only for missing or materially changed choices; classification alone does not grant implementation permission.

## Core authority model

Use this authority chain when classifying impact:

1. Human-approved decisions
2. Product Brief / PRD
3. UX / Architecture / Security / NFR decisions
4. Epic specification
5. Stories / tickets
6. Code and tests

A downstream artifact must not silently override an upstream artifact.

The incoming item must be routed according to the **highest authoritative layer it changes**.

---

# 1. Intake

For every incoming item, first capture:

- short title;
- source: tester / user / developer / operations / security / product / external contributor;
- observed or requested behavior;
- expected behavior, if known;
- severity / urgency;
- affected area;
- related epic, story, ticket, requirement, or decision IDs if known;
- reproduction information for defects;
- evidence such as logs, screenshots, traces, test results, or customer examples when available.

Do not require information that is unnecessary to classify the item.

---

# 2. Classify the item

Classify the item into exactly one primary class. Add secondary tags only when useful.

Use substantive authority impact to resolve overlaps. An explicitly review-only external patch enters through EXTERNAL CHANGE / PR / PATCH; report its product/architecture/security conflicts as findings and route them upstream. A dependency upgrade enters through DEPENDENCY / FRAMEWORK / RUNTIME / PLATFORM CHANGE even when defect-motivated, unless it changes approved higher-level scope or technical decisions, which take precedence. Do not let a source label hide the highest affected authority.

## A. DEFECT

Use when approved intended behavior is already clear and the implementation does not satisfy it.

Examples:
- a button does nothing;
- an API violates an existing acceptance criterion;
- synchronization loses messages despite an approved reliability requirement;
- a regression breaks previously working approved behavior.

Default route:

- small/coherent defect -> `bmad-guided-build`;
- larger defect -> `bmad-ticket`, then `bmad-guided-build` per ticket;
- production-relevant or risky defect -> use `bmad-guided-build` with its required risk reviews; add standalone `bmad-code-review thorough` only for a remaining review gap.

If investigation shows the requirement, spec, UX, or architecture is wrong or ambiguous, STOP treating it as a pure defect and reclassify it.

---

## B. CLARIFICATION

Use when implementation cannot proceed because the authoritative requirement is ambiguous, incomplete, or contradictory.

Examples:
- two plausible interpretations of read/unread behavior;
- unspecified retry behavior;
- unclear permission inheritance;
- a ticket conflicts with the PRD or architecture spine.

Route:

1. stop the affected implementation work;
2. identify the highest upstream artifact containing the ambiguity;
3. use decision governance when a consequential choice is required;
4. update/reconcile the authoritative artifact;
5. propagate the clarification to affected specs/tickets;
6. resume implementation only after the ambiguity is resolved.

Do not let the implementation agent choose silently.

If existing approved authority unambiguously resolves the conflict, reconcile the mistaken downstream artifact through its owner without asking for a new decision. Reopen governance only when intent or approval is unresolved or the proposed resolution would change consequential approved behavior.

---

## C. IN-SCOPE STORY

Use when the requested behavior is already permitted by the approved Product Brief / PRD / architecture and belongs within an existing approved epic/spec, but no implementation unit currently covers it.

Route:

1. identify the owning epic/spec;
2. verify it is genuinely within approved scope;
3. use `bmad-ticket` to add or revise the implementation unit;
4. check dependencies and ordering;
5. implement with `bmad-guided-build` when authorized.

If the story introduces new product behavior beyond the approved spec, reclassify as FEATURE / SCOPE CHANGE.

---

## D. FEATURE / SCOPE CHANGE

Use when the request adds, removes, or materially changes externally visible product capability or product scope.

Examples:
- adding guest users;
- adding video calls when only voice was approved;
- introducing public channels;
- adding a mobile client;
- changing retention behavior visible to users/admins.

Route:

1. do not create an implementation ticket immediately;
2. perform decision governance;
3. assess product value, scope, UX, security, NFR, architecture, deployment, and dependency impacts;
4. accept / reject / defer through explicit human decision;
5. if accepted during active implementation, use `bmad-correct-course` when the change is significant;
6. update Product Brief / PRD when affected;
7. update UX and Architecture when affected;
8. create or update the affected epic spec;
9. use `bmad-ticket` to create/revise implementation units;
10. implement only after the revised planning artifacts are approved.

---

## E. UX BEHAVIOR CHANGE

Use when the product capability remains the same but interaction behavior, information architecture, states, navigation, accessibility, or user workflow materially changes.

Route:

1. determine whether a product requirement also changes;
2. use decision governance for consequential UX choices;
3. reconcile BMAD UX artifacts;
4. update affected epic specs and tickets;
5. use `bmad-correct-course` when the change materially disrupts active work;
6. then implement with `bmad-guided-build`.

Minor cosmetic changes that do not alter product behavior may go directly to `bmad-guided-build` when bounded and low-risk.

---

## F. ARCHITECTURE / SECURITY / NFR CHANGE

Use when the request changes cross-cutting technical truth.

Examples:
- replacing the persistence engine;
- changing authentication model;
- modifying encryption boundaries;
- changing communication protocol;
- altering scalability, latency, availability, RPO/RTO, or audit requirements;
- changing deployment topology.

Route:

1. STOP direct implementation;
2. use decision governance;
3. identify all affected approved decisions and assumptions;
4. evaluate alternatives, migration cost, compatibility, security, operations, and already-written code;
5. require explicit human approval;
6. use `bmad-correct-course` when implementation is already underway and the change is significant;
7. update the Architecture Spine / security / NFR decisions first;
8. propagate to affected PRD/UX/specs/tickets where necessary;
9. add migration or remediation tickets explicitly;
10. implement only after consistency validation.

Never hide an architecture change inside a refactor ticket.

---

## G. REFACTOR / TECHNICAL DEBT

Use when externally observable behavior is intended to remain unchanged.

Route:

- bounded internal refactor -> `bmad-guided-build`;
- large refactor with multiple implementation units -> `bmad-spec` or `bmad-ticket`, then `bmad-guided-build`;
- refactor that changes cross-epic architecture -> reclassify as ARCHITECTURE CHANGE.

Require tests or equivalent validation that demonstrates behavior remains unchanged.

---

## H. DEPENDENCY / FRAMEWORK / RUNTIME / PLATFORM CHANGE

Use for library, framework, SDK, runtime, compiler, OS support, database version, infrastructure component, or build-tool changes.

Route:

- routine patch/minor upgrade with no changed approved technical decision -> `bmad-guided-build`;
- major upgrade, runtime/platform change, compatibility break, or change to an approved TECH/DEPLOY decision -> decision governance, and `bmad-correct-course` when significant;
- update architecture/spec/tickets where required before implementation.

Always assess breaking changes, security motivation, deployment impact, and supported environments.

---

## I. INCIDENT / SECURITY HOTFIX

Use when immediate containment or correction is required for production safety, security, data integrity, or severe operational impact.

Route:

1. prioritize containment and the smallest safe corrective action;
2. if the safe behavior is already clear and the corrective action is authorized, use a narrowly scoped `bmad-guided-build` hotfix without waiting for full planning reconciliation; preserve the guided wrapper's approval and review gates;
3. run appropriate tests;
4. use `bmad-code-review thorough` for consequential production/security changes where feasible;
5. after stabilization, reconcile any changed requirements, decisions, architecture, specs, and tickets;
6. record follow-up work separately.

Emergency handling is an exception to normal upstream-first sequencing, not an excuse to leave planning artifacts stale.

---

## J. DE-SCOPE / REMOVAL / DEPRECATION

Use when an approved feature, platform, requirement, integration, or story is being removed, deferred, or deprecated.

Route:

1. assess dependencies and already-built code;
2. use decision governance for consequential scope removal;
3. use `bmad-correct-course` when active implementation is materially affected;
4. update Product Brief / PRD / UX / Architecture as appropriate;
5. supersede or cancel affected specs/tickets rather than silently deleting historical intent;
6. create cleanup/migration tickets if implementation already exists.

---

## K. INTEGRATION / CROSS-EPIC PROBLEM

Use when individually completed components do not work correctly together.

First determine whether the cause is:

- an implementation defect -> DEFECT route;
- incompatible assumptions in specs -> CLARIFICATION / SPEC route;
- missing cross-cutting architecture -> ARCHITECTURE CHANGE route;
- missing requirement -> FEATURE / SCOPE CHANGE or CLARIFICATION route.

Repeated integration defects across multiple tickets are a signal to inspect upstream architecture/specification rather than repeatedly patching symptoms.

---

## L. EXTERNAL CHANGE / PR / PATCH

Use when reviewing code produced outside the active BMAD build flow.

Route:

1. identify intended requirement/spec/ticket;
2. review the change against that intent;
3. use `bmad-code-review`, normally `thorough` for production work;
4. do not accept code that introduces unapproved product or architecture decisions;
5. route any discovered upstream conflicts through the appropriate classification above.

---

# 3. Scope guard

If an incoming item appears while another ticket is actively being built:

- do not silently expand the active ticket;
- fix it inside the active build only if it is required to satisfy that ticket's existing intent and belongs to that change;
- otherwise record/classify it separately;
- unrelated pre-existing problems remain separate work.

---

# 4. Decision governance trigger

Invoke the project's decision-governance workflow whenever the incoming item:

- creates a new consequential product/UX/architecture/security/NFR/technology/deployment decision;
- reopens or changes an approved decision;
- introduces a conflict between authoritative artifacts whose resolution is not already determined by approved authority; mechanical downstream reconciliation follows the CLARIFICATION rule above;
- requires a choice that independent implementation agents could make incompatibly.

Do not modify an approved consequential decision without explicit human approval.

---

# 5. BMAD routing rules

Use the smallest safe BMAD path.

- Clear one-session implementation change -> `bmad-guided-build`.
- Larger coherent work -> `bmad-ticket`, then `bmad-guided-build` per ticket.
- New or changed epic-level behavior -> reconcile/create `bmad-spec`, then `bmad-ticket`.
- Significant mid-implementation change -> `bmad-correct-course`.
- Standalone review of a PR/diff/branch/change -> `bmad-code-review`.
- Completed epic -> `bmad-retrospective` plus relevant integration/acceptance testing.

For explicitly authorized automatic implementation, use `bmad-guided-build` Auto mode under the entry-point rules above. Do not substitute `bmad-build-auto`. Each guided invocation handles one ticket/change and retains its own completion gates.

---

# 6. Impact analysis

Before accepting any item that changes approved behavior, identify:

- affected decision IDs;
- affected requirements;
- affected UX rules;
- affected architecture/security/NFR decisions;
- affected epics/specs;
- affected stories/tickets;
- already-implemented code likely to need migration or rework;
- tests that must change;
- operational/deployment/documentation impacts.

For low-impact pure defects, keep this analysis proportional.

---

# 7. Completion report

After classification, report:

## Classification
- Primary class
- Severity / urgency
- Reason for classification

## Authority impact
- Highest authoritative layer affected
- Decisions/requirements/specs/tickets affected

## Recommended route
- BMAD workflow(s)
- Whether human approval is required before implementation
- Whether current active work must stop

## Proposed next action
State exactly one immediate next action.

If implementation is authorized and performed, also report:

- changed files;
- tests/validation run;
- acceptance status;
- unresolved issues;
- follow-up items created;
- whether upstream artifacts remain consistent.

---

# 8. Non-negotiable rules

- Never silently expand an active ticket.
- Never turn an ambiguous requirement into an implementation assumption.
- Never hide a feature or architecture change inside a bug fix.
- Never let a downstream artifact silently override an upstream authoritative artifact.
- Preserve history when decisions/specs are superseded.
- Use the smallest safe BMAD workflow.
- Implementation requires whatever authorization rules are defined in the project's `AGENTS.md`.

## Behavioral validation

When authoring or changing this skill, exercise [evaluation.md](references/evaluation.md). Evaluate classification, permission preservation, and actual handoff choices; packaging checks do not prove workflow behavior.
