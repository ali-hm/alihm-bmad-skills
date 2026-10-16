# Alihm BMad Skills

Four companion skills for guiding a project from an idea or specification through delivery and ongoing maintenance with BMad.

**Bundle version: 0.3.0. License: MIT.** This is an independent extension; it is not an official BMad distribution.

| Skill | Responsibility |
| --- | --- |
| [bmad-sdlc](skills/bmad-sdlc/SKILL.md) | Coordinate discovery, planning, implementation, verification, resumption, and maintenance. |
| [bmad-guided-build](skills/bmad-guided-build/SKILL.md) | Plan and implement one ticket/change with independent reviewers, bmad-review, fixes, final re-review, and an execution ledger. |
| [change-intake-governance](skills/change-intake-governance/SKILL.md) | Classify incoming work by the highest authoritative artifact it changes and choose the smallest safe route. |
| [decision-governance](skills/decision-governance/SKILL.md) | Analyze consequential decisions, obtain approval, and reconcile affected planning artifacts without starting implementation. |

All implementation handoffs from the three coordinating skills use **bmad-guided-build**. Only that wrapper calls the underlying BMad build internally. Missing dependencies block the affected route; they do not permit a raw-build fallback.

## Requirements

- A coding agent that reads Agent Skills. Codex UI metadata is included for all four skills; other hosts need their own skill discovery support.
- BMad Method and Core Tools installed and configured for the target project. These four skills do not bundle or automatically install BMad.
- Guided implementation requires the upstream `bmad-build` and `bmad-review` skills and their project setup. Version 0.3.0 adds initial/final `bmad-review` gates; update all four companion skills together and verify that dependency before implementing.
- Git for the guided wrapper's previous-work checkpoint, and the tools needed to build/test your application.
- uv for BMad's Python helpers. Node.js/npm is needed if installing through the Skills CLI.

See [compatibility and dependencies](docs/compatibility.md) for the inspected upstream snapshot, required capabilities, and verification limits. Cline references in the guided wrapper describe an optional host example; Cline is not a prerequisite. Independent reviewers use available host capabilities, with degraded independence disclosed when isolation is unavailable.

## Install

First install and set up BMad using the [upstream instructions](https://github.com/bmad-code-org/BMAD-METHOD). Ask the installed bmad skill to set up the Method and Core Tools modules in your target project.

On Windows, Linux, and macOS, install Git and Node.js/npm before using the commands below. Confirm that `git --version`, `node --version`, `npm --version`, and `npx --version` work in your terminal. BMad also needs the uv prerequisite listed above.

Install all four skills globally for the agents detected by the Skills CLI. Follow its agent-selection prompts when shown:

**Windows (PowerShell)**

~~~powershell
npx skills add ali-hm/alihm-bmad-skills --skill "*" --global
~~~

**Linux and macOS (Bash or Zsh)**

~~~bash
npx skills add ali-hm/alihm-bmad-skills --skill '*' --global
~~~

Keep the wildcard quoted so your shell passes it to the CLI rather than expanding local filenames.

Global installation makes the skills available across projects for your user account. It does not install BMad or configure individual projects.

To select agents explicitly, use their CLI identifiers. For example, install globally for Claude Code, Cursor, and GitHub Copilot together:

**Windows (PowerShell)**

~~~powershell
npx skills add ali-hm/alihm-bmad-skills --skill "*" --agent claude-code --agent cursor --agent github-copilot --global
~~~

**Linux and macOS (Bash or Zsh)**

~~~bash
npx skills add ali-hm/alihm-bmad-skills --skill '*' --agent claude-code --agent cursor --agent github-copilot --global
~~~

| Agent | CLI identifier |
| --- | --- |
| Claude Code | `claude-code` |
| Cursor | `cursor` |
| GitHub Copilot | `github-copilot` |
| Gemini CLI | `gemini-cli` |
| Cline | `cline` |
| Windsurf | `windsurf` |
| Codex | `codex` |

For a single agent, keep just its identifier. For example:

**Windows (PowerShell)**

~~~powershell
npx skills add ali-hm/alihm-bmad-skills --skill "*" --agent gemini-cli --global
~~~

**Linux and macOS (Bash or Zsh)**

~~~bash
npx skills add ali-hm/alihm-bmad-skills --skill '*' --agent gemini-cli --global
~~~

The CLI also accepts `--agent "*"` to target all supported agents, including ones you do not currently use. Some agents, such as Eve, support project installation only; use explicit agent identifiers for global installation if the wildcard reports an unsupported target. See the [supported-agent list and installation options](https://github.com/vercel-labs/skills#supported-agents) for the current choices.

To install for one project instead, run the command from that project and omit `--global`. Agent discovery and workflow capabilities still depend on the selected host; installation alone does not verify live BMad execution there.

For example, on Linux or macOS:

~~~bash
cd /path/to/your/project
npx skills add ali-hm/alihm-bmad-skills --skill '*'
~~~

To inspect the local publishing checkout without installing, run this from the checkout in PowerShell, Bash, or Zsh:

~~~shell
npx skills add . --list
~~~

The CLI supports repository discovery, named skills, local paths, and agent-specific installation. [Skills CLI documentation](https://github.com/vercel-labs/skills)

Keep all four companion skills together at the same version. Before installing over existing custom copies, preserve your edits and check which project/global copy the host selects. Refresh the host's skill discovery or start a new conversation after installation if needed.

## Updates and versions

Update the four skills together:

**Windows (PowerShell)**

~~~powershell
npx skills update bmad-sdlc bmad-guided-build change-intake-governance decision-governance --global
~~~

**Linux and macOS (Bash or Zsh)**

~~~bash
npx skills update bmad-sdlc bmad-guided-build change-intake-governance decision-governance --global
~~~

For a project installation on any of these systems, run from the target project and use `--project` instead of `--global`:

~~~shell
npx skills update bmad-sdlc bmad-guided-build change-intake-governance decision-governance --project
~~~

Review [CHANGELOG.md](CHANGELOG.md) before updating, particularly for workflow or approval changes. Updates can replace local edits; maintain modifications in a separate fork or reconcile them before updating.

The CLI uses recorded source information/content hashes to detect changes. Version metadata labels releases; it does not schedule checks or update manually copied skills. Normal repository installs follow their recorded source, so the default branch is kept ready for users. [Skills CLI update mechanism](https://github.com/vercel-labs/skills/blob/main/AGENTS.md)

Git tags and GitHub Releases identify reproducible bundle snapshots. To use a fixed release without following the default branch, check out its tag and install from that local checkout. Keep that installation under an explicit manual upgrade policy; a local-path install does not promise remote update detection.

BMad updates are separate. Use the installed bmad setup/update workflow and recheck compatibility before changing the upstream version.

## Use

The examples below name the skill in an ordinary request. Use your host's skill invocation mechanism when needed; in Codex, you can invoke a skill with its dollar-prefixed name, such as `$bmad-sdlc`. Replace the sample paths and ticket IDs with your project's actual artifacts.

### Coordinate a project with bmad-sdlc

`bmad-sdlc` is the coordinator for work that crosses discovery, planning, delivery, and maintenance. Describe your starting point, desired outcome, existing artifacts, and permission limits in ordinary language. It inspects the relevant project state, chooses the smallest suitable route through installed BMad skills, and checks each handoff. You do not need to choose the specialist skills yourself or run the whole lifecycle for a small change.

It can start from an idea, a specification, or an existing application. After a baseline exists, it distinguishes a defect or missing approved behavior from new scope, changed requirements, and consequential decisions. Every implementation handoff uses `bmad-guided-build`; planning, review, and status requests can stop before implementation. Specialist routes depend on the capabilities installed in your project. See the [routing reference](skills/bmad-sdlc/references/routing.md) for the supported routes and boundaries.

#### Choose the execution scope and mode

| Request | Behavior |
| --- | --- |
| Interactive implementation (default) | Uses guided build for one ticket/change, with its plan approval and review gates. Automatically selecting specialist skills does not select Auto mode. |
| Explicit Auto implementation | Uses guided build Auto for an approved, bounded ticket with settled decisions. Required reviews still run; CRITICAL work needs human approval. |
| Planning only | Produces or reconciles authorized planning artifacts and stops before application implementation. This is a scope restriction, not a third build mode. |
| Read-only investigation, review, or status | Reports findings without edits, setup repairs, progress-note writes, or ticket-state changes. This is also a scope restriction. |

Auto does not create a background runner or authorize commits, pushes, tracker publication, or deployment. Continuing across multiple tickets needs explicit authorization for that sequence and remains subject to each ticket's readiness and acceptance rules. The samples below are independent requests; replace their paths, decisions, and ticket IDs with your own.

#### Start or adopt a project

**1. Start from a simple idea.** Use this when the problem, users, and boundaries still need clarification. Discovery comes before choosing a stack or scaffolding.

~~~text
Use bmad-sdlc to guide a new project: a volunteer scheduling app for a local
food bank. Help clarify the users, core workflows, success criteria, and
constraints, then prepare the planning artifacts we need. Stop before
choosing technologies or writing application code.
~~~

**2. Explore alternatives or challenge an uncertain idea.** The coordinator can route to brainstorming or concept challenge before the idea becomes an approved plan.

~~~text
Use bmad-sdlc to explore ways to reduce missed volunteer shifts. Compare
reminders, shift swaps, and a waiting list, then challenge the strongest
idea's assumptions. Help me choose a direction before creating a build plan.
~~~

**3. Research a specific unresolved question.** Use evidence gathering when a product or technical choice depends on facts that the project does not yet have.

~~~text
Use bmad-sdlc to research whether our volunteers need offline scheduling.
Review the supplied interview notes in docs/interviews/ and identify what
additional evidence we need. Present the implications for scope and data
synchronization before recommending a decision. Do not implement it.
~~~

**4. Start from a supplied specification.** Adequate approved specifications are used directly; gaps and contradictions are resolved without restarting discovery unnecessarily.

~~~text
Use bmad-sdlc with the approved specification at docs/booking-spec.md.
Check its referenced requirements and decisions, identify material gaps,
then propose a ticket breakdown and dependency order. Preserve approved
choices and stop before implementation.
~~~

**5. Develop requirements, UX, and shared architecture before building.** Use this for a larger project whose stakeholders, user journeys, integrations, or technical boundaries need agreement.

~~~text
Use bmad-sdlc to plan a booking platform from docs/product-brief.md.
Develop the missing requirements and user journeys, and identify shared
architecture and security decisions needed by the web app and API teams.
Bring consequential choices to me before decomposing dependent work.
Planning only; do not scaffold or implement the application.
~~~

**6. Adopt an existing project.** Start with the requested work and existing conventions; project-context setup is appropriate when instructions are missing or stale.

~~~text
Use bmad-sdlc to adopt this existing booking application for future BMad
work. Inspect the current project instructions and planning artifacts,
identify gaps, and set up the necessary local project context. Preserve
the established architecture and application behavior. Do not implement
features or replace existing plans merely to standardize them.
~~~

**7. Understand existing code before deciding on a change.** A walkthrough can explain the relevant flow without initiating implementation or repository-wide adoption.

~~~text
Use bmad-sdlc to explain how a booking moves from the UI through the API
to persistence and notifications. Walk me through the relevant code,
contracts, and tests. Keep this read-only; I have not chosen a change yet.
~~~

#### Deliver features and investigate defects

**8. Implement one small approved feature in Interactive mode.** A bounded change can go to guided build after required intake, without unnecessary new planning documents.

~~~text
Use bmad-sdlc in Interactive mode to implement approved ticket 3.2:
add a date filter to the bookings list. Read its owning specification and
acceptance criteria, then present the implementation plan for approval.
Preserve the existing API contract and unrelated pending changes.
~~~

**9. Break down a larger approved feature.** Plan coherent units and their dependencies before dispatching individual builds.

~~~text
Use bmad-sdlc to plan the approved recurring-bookings feature in
docs/recurring-bookings.md. Check completeness, reconcile the build spec
if needed, and create an agreed ticket breakdown with integration checks.
Recommend the first ready ticket, then stop before implementation.
~~~

**10. Add a missing feature already promised by approved scope.** Missing approved behavior can be treated as incomplete delivery rather than a new product decision.

~~~text
Use bmad-sdlc to complete the CSV export capability required by CAP-012
in the approved reporting spec. It is absent from the current application.
Verify the requirement and existing work, then guide the smallest suitable
implementation through Interactive mode without expanding export scope.
~~~

**11. Assess a missing feature that was never approved.** New user expectations need scope assessment before becoming implementation work.

~~~text
Use bmad-sdlc for this missing capability: customers want a waiting list
when a session is full, but our approved scope does not mention it.
Assess the product, notification, and data impacts, propose options, and
prepare the planning changes for my decision. Do not implement yet.
~~~

**12. Fix a reproducible bug against clear approved behavior.** Trace the defect and preserve existing contracts while routing a focused correction.

~~~text
Use bmad-sdlc to investigate and fix duplicate notifications when a user
reconnects. Approved behavior is one notification per event; reproduction
steps are in docs/issues/duplicate-notifications.md. Preserve the existing
API contract and unrelated pending changes. Use Interactive implementation.
~~~

**13. Triage an issue whose cause or intended behavior is unclear.** An issue label does not establish whether the problem is code, a conflicting specification, or a missing requirement.

~~~text
Use bmad-sdlc to triage this issue: a booking is confirmed in the web app
but appears pending in the partner integration. Trace the relevant flow,
compare the approved contracts, and determine whether this is a defect,
conflicting specifications, or missing behavior. Investigate read-only
and report the evidence and proposed route before applying a correction.
~~~

#### Change requirements and maintain the application

**14. Resolve ambiguous or conflicting requirements.** Clarify the authoritative intent before creating dependent implementation work.

~~~text
Use bmad-sdlc to resolve a conflict: the product requirements allow
cancellation until a session starts, but the API spec says 24 hours before.
Identify the owning artifacts and affected consumers, explain the options,
and obtain the required decision before reconciling the planning baseline.
Do not implement either interpretation yet.
~~~

**15. Apply a changed approved requirement.** Preserve the previous decision's history and propagate the new choice through the workflows that own the affected artifacts.

~~~text
Use bmad-sdlc to apply my approved change to PROD-007: extend report
retention from 30 to 90 days. Reconcile the owning requirements, affected
specifications, and tickets through their owning workflows, preserving
superseded history. Report consistency and readiness; stop before code.
~~~

**16. Change a user journey or material UX behavior.** Assess product and UX effects before treating the request as a cosmetic edit.

~~~text
Use bmad-sdlc to assess replacing the three-step booking wizard with a
single-page flow. Preserve required validation, accessibility, and mobile
behavior. Reconcile the approved user journey and acceptance criteria
before proposing implementation tickets. Planning only for now.
~~~

**17. Reconsider architecture, security, or data decisions.** Consequential changes need impact analysis and an approved direction before dependent work.

~~~text
Use bmad-sdlc to assess replacing our shared tenant database with isolated
tenant databases. Review ARCH-004, authentication boundaries, migrations,
operations, and affected integrations. Compare realistic options and bring
the decision to me before updating the baseline or implementing changes.
~~~

**18. Address performance, reliability, or another nonfunctional requirement.** Establish measurable acceptance criteria and distinguish a defect from a changed service target.

~~~text
Use bmad-sdlc to address slow report generation. The approved target is
under five seconds for 10,000 rows; current runs take about 30 seconds.
Verify the measurement and bottleneck, then plan a bounded correction.
Preserve report contents and authorization behavior. Use Interactive mode
when the implementation is ready; surface any required architecture change.
~~~

**19. Refactor while preserving behavior.** Internal cleanup remains bounded by preservation checks; a changed contract or architecture needs reassessment.

~~~text
Use bmad-sdlc to refactor the duplicated booking validation into a shared
module. Preserve validation messages, ordering, public interfaces, and
persistence behavior. Assess the scope, propose the preservation checks,
and use Interactive guided implementation for one coherent change.
~~~

**20. Upgrade a dependency, runtime, or platform.** Start with current official documentation and compatibility impacts rather than assuming a version bump is sufficient.

~~~text
Use bmad-sdlc to plan upgrading our database driver to the next major
version. Check current official migration documentation and our actual
usage, compatibility, configuration, and deployment constraints. Identify
any approved technical decisions that need review, then propose bounded
tickets and validation. Do not change dependencies yet.
~~~

**21. Respond to an incident or security hotfix.** Coordinate authorized containment and a small correction, then reconcile evidence and planning after stabilization.

~~~text
Use bmad-sdlc to investigate an incident: duplicate payment callbacks
can create two bookings for one payment. Local investigation and a patch
are authorized; production operations are not. Identify immediate
containment options, guide the smallest clear correction, and retain the
required risk reviews and approval gates. Document follow-up work separately.
~~~

**22. Remove or de-scope a capability.** Examine consumers, retained data, dependencies, and migration needs before deleting code or history.

~~~text
Use bmad-sdlc to assess retiring the legacy SMS reminder channel.
Identify active consumers, fallback behavior, data retention, configuration,
and operational dependencies. Propose the scope decision and cleanup or
migration plan, preserving superseded history. Stop before implementation.
~~~

**23. Handle a significant midstream change.** Reconcile the affected planning layers and active work instead of silently expanding a ticket.

~~~text
Use bmad-sdlc to assess new feedback during ticket 3.2: bookings now need
manager approval before confirmation. Evaluate the impact on the PRD,
user journey, architecture, specifications, and active tickets. Use the
installed course-correction workflow if its required inputs exist.
Present the decisions needed before continuing dependent implementation.
~~~

**24. Make a specification-only correction.** Keep work in the spec's owning workflow when approved intent is unchanged and no code change is requested.

~~~text
Use bmad-sdlc to clarify the date-filter examples in the reporting spec
using the already-approved inclusive date-range behavior. Update through
the spec's owning workflow and check consistency. Do not change approved
requirements, ticket states, or application code.
~~~

**25. Resequence tickets without changing product scope.** Ticket dependency and readiness changes belong to the configured ticket workflow.

~~~text
Use bmad-sdlc to reassess the order of the remaining reporting tickets:
the shared query helper must now precede both export and dashboard work.
Verify the dependencies and update the local ticket plan through its owning
workflow. Preserve approved scope; do not implement or publish tracker changes.
~~~

#### Resume work and use Auto deliberately

**26. Resume an unchanged approved plan.** Verify saved state and reuse approvals and review evidence that still apply.

~~~text
Use bmad-sdlc to continue approved ticket 3.2 from its existing plan and
execution ledger. Verify the current spec, pending changes, and review
evidence, then resume the earliest unfinished step. Reuse matching plan
approval, the confirmed reviewer roster, and my existing no-commit choice.
~~~

**27. Reassess blocked work or a plan that has drifted.** A stale progress note or changed plan does not resolve a blocker or preserve an approval automatically.

~~~text
Use bmad-sdlc to reassess blocked ticket 4.1. The partner API contract has
changed since its plan was approved. Verify the blocker and affected
decisions against current evidence, identify which approvals or reviews
need reopening, and recommend the next action. Keep this pass read-only.
~~~

**28. Finish acceptance for an already-built ticket.** Inspect implementation and review evidence before closing work or sending it back through a build.

~~~text
Use bmad-sdlc to assess ticket 3.2, which is marked built and awaits
acceptance. Compare its criteria with the actual implementation, checks,
and review evidence. Report any gaps and the required acceptance step;
do not rebuild it or mark it done without the required acceptance.
~~~

**29. Execute one approved ticket in Auto mode.** This explicitly selects guided Auto while retaining review, risk, and source-control boundaries.

~~~text
Use bmad-sdlc in Auto mode for approved ticket 3.2 only. Its scope and
upstream decisions are settled. Run the required guided-build reviews,
implementation, and verification. Do not commit, push, publish, or deploy.
Stop for any new consequential decision or CRITICAL approval requirement.
~~~

**30. Continue across an explicitly approved sequence.** Each build still owns one ticket; the coordinator checks dependencies and acceptance between builds.

~~~text
Use bmad-sdlc in Auto mode for approved tickets 3.2, 3.3, and 3.4, in
dependency order, within this session. Handle one ticket per guided build
and verify its result and required acceptance before selecting the next.
Stop if a ticket is not ready, acceptance needs my input, a mandatory check
fails, or a consequential decision arises. Do not commit, push, or deploy.
~~~

#### Review, verify, and prepare delivery

**31. Review a PR or diff without applying findings.** Standalone code review is distinct from implementing fixes and from guided build's mandatory reviews.

~~~text
Use bmad-sdlc to review the current branch diff against main for booking
correctness, compatibility, and missing verification. Report actionable
findings with evidence. Review only: do not edit files, repair setup,
write progress notes, change tickets, or implement the findings.
~~~

**32. Add verification for an implemented feature.** Request API or end-to-end coverage when it fills an actual acceptance gap.

~~~text
Use bmad-sdlc to add the missing API and end-to-end verification for the
implemented recurring-bookings feature. Derive coverage from its approved
acceptance criteria and existing test conventions, run the available
checks, and distinguish failures from unavailable environments. Route any
necessary implementation changes through guided build; do not expand scope.
~~~

**33. Prepare a human walkthrough.** Explain the implementation and evidence so a person can review or accept the work.

~~~text
Use bmad-sdlc to walk me through ticket 3.2's implementation, relevant
diff, checks, and unresolved questions before I accept it. Keep the
walkthrough read-only and leave the acceptance decision with me.
~~~

**34. Review a completed epic with a retrospective.** Assess the epic's outcomes and evidence without treating the retrospective as missing integration or acceptance testing.

~~~text
Use bmad-sdlc to run a retrospective for the completed reporting epic.
Review the epic, tickets, delivery evidence, and remaining integration or
acceptance gaps. Report lessons and proposed follow-up work. Do not change
ticket states or implement follow-up items during the retrospective.
~~~

**35. Ask for status or the next suitable step.** Verify authoritative artifacts and actual evidence rather than trusting labels or a progress note alone.

~~~text
Use bmad-sdlc to report where this initiative stands and what should
happen next. Check the current spec, decisions, ticket dependencies,
plans, and review evidence. Keep this read-only; identify pending decisions,
blockers, and the first ready action without starting it.
~~~

**36. Inspect BMad setup without repairing it.** Setup diagnosis can remain read-only even when configuration is incomplete.

~~~text
Use bmad-sdlc to tell me whether BMad and the four companion skills are
ready for this project. Inspect the active configuration and available
capabilities, then report missing dependencies and affected routes.
Do not install packages, initialize setup, or change any files.
~~~

**37. Prepare a release without publishing it.** Separate implemented, validated, accepted, and released states, and produce reviewable readiness evidence.

~~~text
Use bmad-sdlc to prepare the approved reporting release for review.
Check acceptance evidence, required documentation, migration and rollback
readiness, and remaining blockers. Update the authorized local release
checklist, but do not tag, sign, publish, deploy, or claim it is released.
~~~

**38. Plan operational maintenance or deployment work.** Use the project's procedures and available specialists; operational actions need their own authorization.

~~~text
Use bmad-sdlc to plan the booking service's database maintenance window.
Review the project's backup, restore, migration, deployment, rollback,
and support procedures. Identify missing readiness evidence and propose
the sequence and checks. Planning only; do not access or modify production.
~~~

### Classify incoming work with change-intake-governance

Use this after a planning baseline exists or implementation has started, when new feedback may affect the active work or upstream decisions.

~~~text
Use change-intake-governance to classify this defect: exporting a report
omits rows with an empty optional comment. The approved requirement says
all matching rows must be included. Identify the smallest safe fix route.

Use change-intake-governance for this request: let external guests view
shared reports. Determine which approved requirements and security
decisions would change before creating implementation tickets.

Use change-intake-governance to assess upgrading our database driver to
the next major version. Identify compatibility and deployment impacts,
and whether an approved technical decision needs reconsideration.

Use change-intake-governance for new feedback during ticket 3.2: add bulk
editing to the list. Determine whether it belongs in the active ticket
or needs separate scope approval. Do not expand ticket 3.2 silently.
~~~

### Review decisions with decision-governance

Use this to evaluate consequential choices and reconcile approved planning artifacts. This workflow does not start implementation.

~~~text
Use decision-governance to propose a retention policy for uploaded files.
Compare realistic options, security and operational effects, and affected
requirements. Wait for my choice before recording an approved decision.

Use decision-governance to review decision ARCH-004, which selects a shared
database for all tenants. Compare keeping it with tenant isolation options.
Keep the review read-only until I choose an option.

Use decision-governance to apply my approved change to PROD-007: replace
30-day report retention with 90 days. Preserve the previous decision as
superseded, reconcile affected planning artifacts, and check consistency.
Do not implement the change.

Use decision-governance to check whether the proposed offline mode conflicts
with approved authentication and data-storage decisions. Identify unresolved
prerequisites and the planning artifacts each option would affect.
~~~

### Implement one approved change with bmad-guided-build

Use Interactive mode when you want to review the plan, request further review, and explicitly approve implementation.

~~~text
Use bmad-guided-build in Interactive mode for approved ticket 3.2.
Read its owning spec and project instructions, create the implementation
plan, and present the plan approval menu before editing application code.

Use bmad-guided-build in Interactive mode for approved ticket 3.2.
I want Party Mode and Advanced Elicitation before deciding whether to
approve implementation. Let me confirm the Party Mode reviewer roster.

Use bmad-guided-build to resume ticket 3.2 from its existing approved plan.
Verify that the plan and scope have not materially changed, preserve valid
review evidence, and complete the remaining review and verification phases.
~~~

For explicitly authorized Auto mode, name one approved, bounded ticket and retain any source-control restrictions:

~~~text
Use bmad-guided-build in Auto mode for approved ticket 3.2 only.
Run its required risk reviews, implementation checks, and independent
post-implementation review. Do not commit, push, or deploy. Stop for any
new consequential decision or CRITICAL approval requirement.
~~~

Interactive is the default: the user reviews and approves the plan. Auto requires an explicit request and an approved bounded ticket with settled upstream decisions. Its required risk reviews still run; CRITICAL work always requires human approval. Every guided invocation handles one ticket/change and does not automatically advance to the next.

Both modes classify risk before approval or implementation so the implementation-review roster is defined. Reviewers can run in batches when host capacity is limited, while retaining fresh contexts and the required roles. Existing matching approvals, no-commit choices, and confirmed rosters are reused; material changes reopen the affected gates.

After implementation and initial validation, both modes run the risk-required independent role reviews and an initial `bmad-review` on the ticket's scoped changes. The coordinator triages every finding, applies valid in-scope fixes, reruns affected checks, and obtains targeted independent re-review. A final `bmad-review` then checks the full current ticket diff for resolved findings and regressions, even if the initial pass found nothing. Required reviews must complete before the wrapper declares success.

Code review uses applicable behavioral and verification lenses; documents use the applicable behavioral/editorial lenses. Raw findings are retained, with separate fix/reject/defer/escalate decisions. Suggestions are not automatic edit instructions, and consequential changes return to governance. Repeated failures or findings remaining after two correction cycles block completion. See the [ticket review procedure](skills/bmad-guided-build/references/ticket-review.md) for dependency checks, snapshots, lens selection, and evidence reuse on resume.

To make the expected cycle explicit in a request:

~~~text
Use bmad-guided-build in Interactive mode for approved ticket 3.2.
After implementation, run its independent reviewers and bmad-review,
triage findings, apply valid in-scope fixes, and rerun affected checks.
Perform targeted independent re-review and final bmad-review on the
complete ticket diff. Do not commit, push, or deploy.
~~~

These review gates are automatic for implemented tickets; the extra wording is optional. Approved-and-stopped, cancelled, and blocked-before-implementation runs do not run implementation reviews. Older unfinished ledgers receive the new review phases without discarding still-valid plan approval or review evidence.

The guided wrapper reports COMPLETE, APPROVED_STOPPED, CANCELLED, BLOCKED, or INCOMPLETE separately from individual phase statuses. Early exits do not require creating an empty plan or running implementation checks. See the [execution procedure](skills/bmad-guided-build/references/execution.md) for resuming an older plan or an approved-and-stopped run.

The Git checkpoint inspects pending work; a dirty tree may require a user choice. Auto does not authorize commits, publishing, deployment, or changes to consequential decisions. Project instructions and explicit user permissions remain authoritative.

Installing the bundle makes the skills available; it does not rewrite a project's policies or force every request through governance. To adopt them as project policy, review the [optional project-instruction example](docs/project-instructions.md).

## Maintain or publish this repository

Install validation dependencies and check the package from its root:

**Windows (PowerShell)**

~~~powershell
python -m pip install -r requirements-dev.txt
python scripts/validate.py
~~~

**Linux and macOS (Bash or Zsh)**

Use a local virtual environment for the validation dependencies:

~~~bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate.py
deactivate
~~~

Python 3.10+ is required for this repository's validation tooling. It is separate from the application stack and BMad's uv-managed runtime.

See [release instructions](docs/releasing.md) for version changes, validation, GitHub publication, and optional plugin submission. The root plugin.json packages the same four skills for portable plugin distribution; directory publication is a separate step.

Format validation does not prove live workflow execution. Review [compatibility.md](docs/compatibility.md), the [four-skill evaluation procedure](docs/evaluation.md), and [recorded results](docs/evaluation-results.md) when assessing readiness.

## License and upstream

These custom skills and repository tooling use the [MIT license](LICENSE). BMad is an external dependency distributed under its own terms; no upstream BMad skills or runtime files are vendored here.

- [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD)
- [Agent Skills specification](https://agentskills.io/specification)
- [Skills CLI](https://github.com/vercel-labs/skills)
