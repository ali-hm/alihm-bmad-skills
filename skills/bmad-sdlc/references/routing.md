# Lifecycle routing

Use this reference for choosing the next workflow. Apply installed module help within project rules and the user's explicit implementation choice: every implementation handoff uses `bmad-guided-build`. Module recommendations to use a raw build do not override that choice. Choose by intent, uncertainty, stakes, and coordination needs, not by how many artifacts can be produced.

## New project from an idea

For a thin idea such as "an app for hikers", gather the missing problem, users, outcome, and constraints. Use ideation or concept challenge only when the user needs that help. Research serves a specific unresolved question.

The current BMad Method preview routes:

- Product brief, BRD, PRFAQ, or analysis: Mary (`bmad-agent-analyst`).
- PRD or other planning document: John (`bmad-agent-pm`). Mary and John use `bmad-facilitate` to create, update, or validate documents with the appropriate templates.
- More ideas needed: `bmad-brainstorming`; challenge one uncertain idea: `bmad-forge-idea`.
- External evidence needed: `bmad-deep-recon`.
- User experience needs defining: `bmad-ux`, composed with any locally mandated design skill.
- Separately built parts need common technical decisions: `bmad-architecture`. Prepare the owning ticket's requirements first and have Sofia adopt the architecture artifact as a companion when it governs that ticket.
- When requested, turn raw source material into cited notes with `bmad-ingest`, or make a long document navigable with `bmad-shard-pro`. Use the resulting artifacts as inputs to their owning planning workflows.

When the work needs a ticket tree, pass useful outputs to Sofia (`bmad-agent-po`) for SPEC. Sofia derives Requirements and Constraints on the owning initiative or epic ticket. Resolve material assumptions before decomposition or implementation.

Do not choose frameworks or scaffold an application incidentally. A prototype must be explicitly exploratory; whether to keep it and make its choices durable is a separate decision.

## New project from a specification

Read the provided specification and its load-bearing references. Preserve its approved choices and identify gaps or contradictions. Do not restart discovery or create a duplicate PRD just because the lifecycle permits one.

For work spanning multiple builds, use Sofia's SPEC operation when the owning ticket still needs requirements, then TICKETS to slice or re-slice the tree and REFINE where individual tickets need work. Reuse an existing ticket and its companions when adequate. An approved standalone specification can remain the input for one bounded `bmad-guided-build` after required intake.

Resolve cross-cutting architecture or security questions before dependent decomposition or code. Planning and implementation permission remain distinct under the project's rules.

## Adopt an existing project

Start from the requested task. Inspect the owning implementation, relevant consumers, tests, configuration, and local conventions. No full-repository documentation pass is required merely to fix a bug.

Use `bmad-project-context` when agent instructions are missing or demonstrably stale, or the user requests adoption guidance. Use `bmad-walkthrough` when the user wants to understand existing code or changes. Do not automatically rewrite instructions, install packages, replace architecture, or regenerate existing plans.

## Changes after a baseline exists

Run locally required intake first. Record only enough to route accurately.

| Primary impact | Next route |
|---|---|
| Defect against clear approved behavior | Reproduce/trace evidence, then a bounded build; ticket first if tracking or size requires it |
| Small in-scope feature or story | Owning approved scope, then build or a ticket as appropriate |
| Larger coherent feature already in approved scope | Spec when needed, ticket breakdown, one build per ready unit |
| Ambiguous or conflicting requirement | Resolve the highest affected authoritative artifact; decision governance when consequential |
| New product scope or material UX behavior | Decision governance, reconcile owning product/UX artifacts, propagate to specs and tickets |
| Architecture, security, data, NFR, or deployment change | Decision governance and impact analysis before implementation |
| Internal refactor preserving behavior | Bounded build with preservation checks; decompose large work; reclassify if architecture changes |
| Dependency/runtime/platform upgrade | Current official documentation and compatibility assessment; governance if an approved technical choice changes |
| Incident/security hotfix | Authorized containment and smallest clear correction; validate and reconcile affected artifacts after stabilization |
| De-scope/removal | Assess dependencies, approve consequential removal, preserve superseded history, plan cleanup/migration |
| Integration failure | Establish whether the cause is code, conflicting specs, missing requirements, or architecture; route to that owner |
| External PR/diff review | Use the [standalone review handoff](handoffs.md#standalone-code-review) to choose a mode compatible with the allowed writes |

A bug label does not prove approved intent. A refactor label does not authorize schema, contract, or behavior changes. Do not hide unrelated improvements in the active ticket.

Use Sofia's REPLAN operation when a change materially affects active work. It traces stale requirements and dependent entries, reconciles the remaining tree, and leaves an in-progress build plan to its owner. Use SPEC for a requirements-only update and TICKETS for a breakdown-only update.

## Required implementation owner and mode

Use the user's custom `bmad-guided-build` for every implementation handoff, including defects, features, internal refactors, upgrades, cosmetic changes, and hotfixes. Its approvals, reviews, one-ticket limit, ledger, and final report remain required. Do not invoke `bmad-build` or `bmad-build-auto` directly; only the guided wrapper owns internal build calls.

Interactive is the default. Select Auto only when explicitly authorized and appropriate for an already-approved, bounded ticket with settled decisions. Follow the installed guided skill's classification and gates: LOW/MEDIUM/HIGH still require their prescribed reviews and validation; CRITICAL always stops for human approval. An automatic skill router or an attended session does not itself authorize Auto.

If the guided skill is unavailable, name the missing dependency and block implementation. Planning, intake, and independent read-only analysis may continue. Do not install the skill without necessary authorization, invent an equivalent workflow, or fall back to a raw build. Auto mode does not schedule itself or eliminate source-control permissions.

If a nested implementation workflow requires an unauthorized side effect, preserve the restriction. Use a documented compatible mode when one exists, or stop only the incompatible step with a precise explanation. Do not invent a no-commit flag or silently substitute another implementation method.

## Verification, acceptance, and operations

- Guided build owns its mandatory implementation reviews: independent role reviewers, initial `bmad-review`, finding triage/fixes, targeted role re-review, and final `bmad-review`. `bmad-code-review` covers an external diff or a justified extra review; avoid duplication beyond the wrapper's required phases.
- `bmad-qa-generate-e2e-tests` covers implemented features when that coverage is needed. Follow locally required test-authoring workflows.
- `bmad-walkthrough` supports human review and understanding.
- `bmad-retrospective` judges the completed epic as a whole; it does not substitute for integration/acceptance evidence.
- Release and maintenance have no universal final BMad command. Use the project's delivery and operations procedures with explicit permissions for external actions.

Close only the scope the user authorized. A completed ticket does not imply that its epic, product, deployment, or operational lifecycle is finished.
