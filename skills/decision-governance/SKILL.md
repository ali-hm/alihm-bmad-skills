---
name: decision-governance
description: >-
  Govern new, reviewed, and changed product, operational, UX,
  security, architecture, data, technology, deployment, and
  non-functional decisions. Use when proposing or reconsidering
  decisions, assessing dependencies and downstream impact,
  obtaining explicit approval, updating BMAD planning artifacts,
  and validating consistency. Never start implementation.
license: MIT
metadata:
  version: "0.3.0"
---

# Decision Governance Workflow

Use this workflow whenever a new product, operational, UX, security, architecture, data, technology, deployment, or non-functional decision is proposed, reviewed, or changed.

Resolve the canonical decision register and document locations from the target project's instructions. The Docs/ paths below are examples; do not impose that directory layout on another project. Approved decisions are authoritative; generated BMAD artifacts remain proposals until explicitly approved.

## Operating Principle

A decision is not considered complete merely because it has been written to the decision register.

Every new or changed decision must be:

1. analyzed;
2. checked against existing approved decisions;
3. checked for downstream impact;
4. explicitly approved by the user;
5. propagated to all affected planning artifacts;
6. validated for consistency after propagation.

Never silently make or change a consequential decision.

Never begin implementation as part of this workflow.

Reuse explicit user choices and approvals already supplied when their decision ID, selected alternative, affected scope, and material proposal still match. Record the source; do not ask the user to approve the same unchanged choice again. New consequential choices or material proposal changes require fresh approval. Permission to reconcile planning does not authorize implementation or external tracker publication.

---

# 1. Determine the operation

Classify the request as one of:

- NEW — a decision does not yet exist.
- REVIEW — an existing decision is being reconsidered but has not yet been changed.
- CHANGE — the user has explicitly approved replacing or modifying an existing decision.

If unclear, treat it as REVIEW rather than CHANGE.

---

# 2. For NEW decisions

Before recording a new decision:

Identify:

- the problem requiring a decision;
- why the decision is needed now;
- prerequisites or unresolved decisions it depends on;
- relevant existing approved decisions;
- realistic alternatives;
- important advantages and disadvantages of each alternative;
- product consequences;
- UX consequences;
- architecture consequences;
- security consequences;
- operational/deployment consequences;
- data/storage consequences;
- implementation consequences;
- risks and assumptions;
- downstream BMAD artifacts likely to be affected.

When reasonable alternatives exist, present 2–5 options.

Give a recommendation and rationale, but do not decide on behalf of the user.

Wait for explicit user approval before recording the decision as APPROVED.

---

# 3. For REVIEW of an existing decision

Do not modify any files initially.

Retrieve and present:

- current decision ID and status;
- current decision;
- original rationale;
- assumptions behind it;
- consequences previously identified;
- dependencies;
- decisions that depend on it;
- relevant requirements;
- relevant architecture;
- affected epics/stories.

Then analyze:

- whether the original assumptions still hold;
- contradictions with later decisions;
- feasibility concerns;
- unnecessary complexity;
- security concerns;
- operational concerns;
- technology constraints;
- better alternatives that have become apparent;
- cost of changing now versus later.

Present realistic alternatives, including keeping the current decision.

For every alternative provide:

- benefits;
- disadvantages;
- risks;
- migration/change impact;
- affected decision IDs;
- affected BMAD artifacts;
- affected epics/stories;
- recommendation.

Do not modify anything until the user explicitly chooses an option.

---

# 4. For an approved CHANGE

When the user explicitly approves a change:

Do not erase the historical decision.

Preserve the old decision as SUPERSEDED and record:

- previous decision;
- previous rationale;
- date/status of supersession;
- replacement decision ID or revision;
- reason for change.

Record the new/current decision as APPROVED.

Update the canonical decision register first.

Then perform impact propagation.

---

# 5. Impact propagation

Determine which artifacts are actually affected.

Potential sources include:

- AGENTS.md
- Docs/memory/decisions.md
- Docs/product/*
- Docs/architecture/*
- Docs/CHANGELOG.md
- BMAD Product Brief
- BMAD PRD
- BMAD UX artifacts
- BMAD Architecture Spine
- BMAD Spec Kernel
- epic specifications
- tickets.toml
- individual stories/tickets
- project context

Do not mechanically rewrite every artifact.

Update only artifacts whose meaning, requirement, constraint, dependency, acceptance criteria, or implementation plan is affected.

Respect the authority hierarchy:

Product intent / scope
→ Product Brief / PRD

UX behavior
→ UX artifacts

Cross-cutting technical decisions
→ Architecture Spine

Epic behavior
→ Epic SPEC

Implementation decomposition
→ tickets/stories

Implementation code
→ only after a separately authorized build workflow

If an upstream artifact changes, reconcile all affected downstream artifacts.

Never fix an upstream inconsistency only by modifying a downstream ticket.

### Preserve artifact ownership

Before propagation, identify each affected artifact's owner and supported update operation. Dispatch changes through that owner and inspect the returned result:

| Artifact | Update path |
| --- | --- |
| Canonical decision register | Project's decision-register procedure; preserve superseded history |
| Product/UX/architecture artifacts | Owning project/BMad workflow, preserving approved intent |
| Spec kernel and spec-authored companions | `bmad-spec` with the approved change and full spec context; update its append-only source log through that skill |
| Adopted spec companions | Their originating workflow; do not treat every file in a spec folder as spec-generated |
| Tickets, dependencies, acceptance, or status | `bmad-ticket` and the configured store's supported operations |
| Project instructions or other human-maintained documents | Scoped direct edits only when permitted by that document's policy |

Never hand-patch generated spec outputs, source logs, or ticket-state fields to make downstream documents look consistent. Do not infer that a repository store and an external tracker have interchangeable commands. Pass existing authorization through; external tracker changes still need authorization for that destination and scope.

If an owning workflow is missing or fails, block that propagation path, preserve the approved decision and partial evidence, and continue independent authorized reconciliation. Report the remaining inconsistency rather than declaring planning READY. Do not replace a failed owner with manual edits to its derived files.

---

# 6. BMAD workflow routing

Use the appropriate BMAD workflow where useful:

- Product requirement/scope change → update/reconcile PRD.
- UX behavior change → reconcile BMAD UX artifacts.
- Cross-epic technical/architecture change → reconcile BMAD Architecture Spine.
- Epic-level behavior change → reconcile the affected bmad-spec.
- Story decomposition change → reconcile tickets.
- Significant change after implementation has started → use bmad-correct-course where appropriate.

This workflow remains planning-only. When planning is READY and implementation is separately authorized, its implementation handoff must name the user's custom `bmad-guided-build` exclusively. Never invoke `bmad-build` or `bmad-build-auto` directly; the guided wrapper owns its internal build calls.

Recommend Interactive mode by default. Recommend the same skill's Auto mode only when explicitly authorized, allowed by project governance, and appropriate for an approved bounded ticket with settled decisions. Preserve its risk-required reviews, ledger, approval gates, and final report; CRITICAL work always requires human approval.

If `bmad-guided-build` is unavailable, report that implementation dependency; do not substitute a raw build. Planning can still be READY when its artifacts are consistent, while the separate implementation handoff remains blocked. Do not invoke the guided wrapper or start implementation as part of decision governance.

---

# 7. Dependency analysis

For every new or changed decision, identify:

- decisions this decision depends on;
- decisions that depend on this decision;
- requirements affected;
- epics affected;
- stories affected.

If the proposed decision depends on another unresolved decision, resolve that prerequisite first.

Do not silently invent the prerequisite.

---

# 8. Consistency validation

After approved changes have been propagated, perform a complete consistency check across relevant planning artifacts.

Check specifically for:

- contradictory decisions;
- stale superseded requirements;
- orphan requirements;
- duplicated requirements with different wording;
- architecture inconsistent with PRD;
- UX inconsistent with product requirements;
- specifications inconsistent with architecture;
- tickets inconsistent with specifications;
- acceptance criteria based on superseded decisions;
- implementation assumptions no longer justified;
- new unresolved decisions introduced by the change.

Report all findings.

Fix direct mechanical inconsistencies caused by the approved change.

Apply mechanical fixes through the artifact ownership rules above; “mechanical” does not authorize bypassing an owning workflow or generated-file boundary.

For any issue requiring a new consequential decision, stop and ask the user rather than choosing silently.

---

# 9. Completion report

At completion, report:

Decision:
- ID
- operation: NEW / REVIEW / CHANGE
- final status

Changed artifacts:
- files/artifacts changed and why

Affected scope:
- decisions
- requirements
- epics
- stories

Validation:
- consistency checks performed
- unresolved issues
- new decisions requiring attention

Implementation impact:
- none / low / medium / high

End with one of:

READY — planning artifacts are consistent.

or

BLOCKED — identify the unresolved decision, missing dependency, missing permission, or remaining planning inconsistency that prevents completion.

Do not start implementation automatically.

## Behavioral validation

When authoring or changing this skill, exercise [evaluation.md](references/evaluation.md), including approved-change propagation and missing-owner cases. Keep planning consistency, implementation readiness, and actual implementation separate in the results.
