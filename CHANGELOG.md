# Changelog

This publication repository uses one semantic version for the entire four-skill bundle. Entries describe package versions, independently of the target project's own changelog policy.

## [Unreleased]

## [0.3.0] - 2026-10-16

### Changed

- Added mandatory initial and final upstream bmad-review passes to every implemented guided ticket in both Interactive and Auto, alongside the existing risk-required independent reviewers.
- Defined scoped review snapshots, applicable resolved lenses, raw finding preservation, separate severity/disposition triage, in-scope fixes, affected validation, targeted role re-review, and a final full-ticket review for regressions.
- Added a two-correction-cycle limit, permission checks for review hooks, explicit dependency blockers, and ledger/reporting evidence for both passes. Early exits before implementation retain their existing behavior.

### Upgrade notes

- This adds a required dependency and completion gate: ensure upstream bmad-review and its project setup are available before application implementation. Missing or failed required review blocks completion; it is not replaced with self-review.
- Keep all four companion skills at 0.3.0. On unfinished pre-0.3 work, add missing review phases as PENDING and retain still-valid approval and review evidence. No global installed copies are updated by a repository commit.

### Documentation

- Expanded the README's bmad-sdlc guide with execution-scope descriptions and 38 explained examples covering supported lifecycle scenarios, Interactive/Auto implementation, planning, and read-only work.
- Added Linux/macOS installation, update, and maintainer-validation commands alongside Windows examples.
- Moved the README update/version section directly after installation.

## [0.2.0] - 2026-10-10

### Changed

- Classified guided-build risk in both Interactive and Auto modes before approval/implementation; Interactive plan-review actions remain user-selected.
- Defined approved-and-stopped, cancelled, blocked, incomplete, and complete outcomes, with valid phase statuses separate from reviewer independence and waivers.
- Split the guided-build entrypoint into execution, plan-review, implementation-review/scheduling, reporting, and evaluation references while preserving its review and final-response contracts.
- Reused matching existing approvals, authorization, dirty-baseline choices, and reviewer rosters across handoffs and resumption.
- Required decision propagation through spec, ticket, and other artifact owners rather than direct edits to generated outputs or state fields.
- Added behavioral scenarios for all four skills and a results protocol distinguishing package checks, dry runs, live integrations, and host compatibility.
- Added capacity-aware reviewer batches, stable snapshots, findings isolation, and bounded recovery for failed reviewers.

### Upgrade notes

- Older guided plans must receive a current risk classification before approval or implementation resumes. Preserve valid evidence and reopen only affected gates.
- Ledger phase statuses are PENDING, IN_PROGRESS, COMPLETE, NOT_APPLICABLE, or BLOCKED. Store DEGRADED independence and explicit waiver details separately; do not turn prior unexecuted or failed phases into completed evidence.
- On resuming an approved-and-stopped or cancelled run, restore newly required future phases to PENDING rather than inheriting their previous NOT_APPLICABLE disposition.

### Documentation

- Added global installation instructions for multiple coding agents and their CLI identifiers.
- Expanded usage examples for lifecycle coordination, change intake, decision governance, and guided Interactive/Auto implementation.

## [0.1.0] - 2026-10-10

Initial publication package, prepared locally; a version entry does not itself indicate that a tag, GitHub Release, or plugin listing has been published.

### Added

- BMad SDLC coordination for new projects, supplied specifications, existing projects, and ongoing maintenance.
- Guided one-ticket implementation with Interactive and explicitly authorized Auto modes, review evidence, an execution ledger, and independent implementation review.
- Change intake and decision governance with approval boundaries and downstream consistency checks.
- Exclusive guided-build implementation routing from the three coordinating skills.
- Shared version metadata, Codex UI metadata, MIT licensing, installation/update documentation, a portable plugin manifest, and package validation in CI.
