---
name: bmad-sdlc
description: Coordinate BMad across a project's lifecycle, from a simple idea or supplied specification through planning, implementation, validation, and ongoing maintenance. Use for starting or adopting projects, delivering features, fixing bugs, refactoring, or resuming BMad work when the user wants lifecycle guidance and execution. Do not activate for unrelated questions or isolated edits the user is directing.
license: MIT
metadata:
  version: "0.2.0"
---

# BMad SDLC

Act as the user's continuing project guide and workflow coordinator. Translate ordinary requests into the smallest suitable sequence of installed BMad skills, carry out authorized steps, and verify the handoffs. Explain the next action in plain language; the user need not know BMad's vocabulary.

This skill owns coordination, not the specialist workflows. Read and follow the actual selected skill instead of imitating it or copying its implementation here.

Implementation must enter through the user's custom `bmad-guided-build` skill in both Interactive and Auto modes. Never invoke `bmad-build` or `bmad-build-auto` directly, including when module help recommends them. The guided wrapper owns its internal build calls, plan gates, reviews, execution ledger, and finalizer. If it is unavailable, continue independent planning where useful and report implementation blocked; do not fall back to a raw build.

## 1. Establish context

Use the user's request and existing conversation first. Reuse explicit choices and authorization already given.

- Determine the target project and work item. Use the current project unless the user names another. Ask only if the target is materially ambiguous.
- Read applicable agent instructions and the relevant approved project decisions. Observe any implementation freeze, design requirements, source-control policy, documentation rules, and mandatory governance workflows.
- Inspect current pending changes before edits. Preserve unrelated work; do not commit, stash, reset, clean, branch, or push merely to satisfy a nested workflow.
- Determine whether the request is a new idea, a supplied specification, existing-project work, status/review only, or resumption. Inspect only relevant artifacts and code; use the project's required discovery tools.
- Discover the installed BMad capabilities and setup using [handoffs.md](references/handoffs.md). Do not assume a skill exists from its name or from this document's examples.

For a status, explanation, or review-only request, remain read-only. Do not create tracking files, repair setup, change ticket states, or apply findings without authorization.

## 2. Route the work

Read [routing.md](references/routing.md) for the current situation. Adapt the installed modules' own routing guidance to the project's rules.

Classify incoming changes by the highest authoritative layer they affect. Run project-required change intake before creating tickets or implementation work. Use required decision governance for consequential unresolved choices or changes to approved decisions.

If those governance skills are absent and not required by the project, perform a proportional intake inline: requested/expected behavior, evidence, scope, affected requirements or decisions, and next action. Present unresolved consequential choices with alternatives and tradeoffs; obtain the necessary user decision before dependent work. Do not install governance skills or import another project's policies merely because this coordinator is present.

For a bounded, understood implementation change, hand off directly to `bmad-guided-build` after required intake. Use specification and tickets when decomposition or uncertainty justifies them. Requirements, UX, architecture, research, and ideation skills supply missing information; they are not mandatory ceremonies for every request.

For new projects, turn vague ideas into enough intent to plan; use supplied specifications directly when adequate. Confirm the needed product, technical, security, operational, and UX boundaries under local policy before scaffolding. Existing projects retain their established contracts and conventions.

## 3. Execute one verified handoff at a time

Read [handoffs.md](references/handoffs.md) before invoking a specialist. Supply its supported inputs, the exact work item, relevant artifact paths, constraints, acceptance criteria, and execution permissions.

Automatically choose and execute routine steps already authorized by the request and project policy. Do not ask the user to select skill names, repeat settled decisions, or approve every internal tool call. Honor genuine interaction or approval requirements in the selected workflow unless the user's explicit instructions already resolve them.

Pass the source and scope of existing permissions, current plan approval, no-commit/dirty-baseline choices, and confirmed reviewer rosters through handoffs. Reuse them while the target, material plan, and authorization scope match; reopen only affected choices when evidence changes. Do not turn a nested default prompt into a request to repeat a settled decision.

Choose the guided wrapper's mode without bypassing its own requirements:

- Default to `bmad-guided-build` Interactive mode. Planning completion does not grant implementation permission where the project requires a separate go-ahead.
- Use that same skill's Auto mode only when explicitly authorized, permitted locally, and suitable for the approved ticket. Preserve its risk classification, required review receipts, and human approval for CRITICAL work. Auto is a guided-build mode, not a reason to select `bmad-build-auto` or create background work.
- A selected build owns one ticket or coherent change. Do not silently extend it or advance beyond a wrapper's one-ticket boundary.
- Multi-ticket continuation needs explicit authorization for that scope. Recheck readiness and the previous ticket's acceptance before dispatching another.
- Pass restrictions through to any delegated agent. Delegate only when permitted; loading this skill alone does not request a team.

After each specialist returns, inspect its actual output and relevant persisted evidence. Resolve material open questions before dependent work. An artifact's existence, an agent's completion sentence, or a ticket label alone is insufficient proof.

Stop the affected path on unresolved intent, a conflicting decision, unsupported required capability, or a failed mandatory check. Report the blocker and a concrete next action; persist it only when writes are authorized. Continue independent authorized work when useful; do not repeatedly dispatch the same blocked input.

## 4. Maintain continuity

For multi-session or multi-ticket work, read [continuity.md](references/continuity.md). Reuse authoritative decisions, spec logs, ticket stores, plans, and review records. Add a small coordinator progress note only when it provides necessary cross-workflow continuity.

On "continue" or "what next", verify the saved references against current project state. Resume the earliest unfinished or newly affected step, not the entire lifecycle. Treat pending approvals as pending until explicit evidence resolves them.

## 5. Validate and close the requested scope

Match validation to the change and acceptance criteria. A build is not runtime or UI verification. Preserve failed or unavailable checks as such; fix introduced failures before claiming completion.

Reuse adequate review evidence without skipping the guided wrapper's mandatory independent post-implementation review, re-review, or finalizer. Run additional review, end-to-end tests, walkthroughs, or retrospective when requested, locally required, or justified by a remaining gap.

For release/operations work, verify deployment, rollback, migration, backup, security, and support requirements only as applicable. Use available specialist skills and tools; if a required capability is missing, identify it rather than inventing a BMad workflow. Deploy, publish, commit, push, and modify external systems only within explicit authorization. Release preparation may include requested local packaging and review artifacts; it does not by itself authorize Git tags, use of production signing keys, remote release creation, or publication.

Distinguish implemented/built, validated, accepted/done, and released. Update ticket state only through its owning workflow and permitted acceptance rules. Finishing development does not imply release or human acceptance.

End with the outcome, relevant artifacts or changes, checks actually performed, remaining decisions or blockers, and the next action when work remains. Honor any selected wrapper's mandatory reporting contract. Do not relay a child workflow's completion message as the whole lifecycle result.

## Behavioral validation

When creating or modifying this coordinator, use [evaluation.md](references/evaluation.md) for scenario-based dry runs. Skill-format validation alone does not prove correct routing.
