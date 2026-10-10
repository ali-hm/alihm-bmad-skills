# Alihm BMad Skills

Four companion skills for guiding a project from an idea or specification through delivery and ongoing maintenance with BMad.

**Bundle version: 0.1.0. License: MIT.** This is an independent extension; it is not an official BMad distribution.

| Skill | Responsibility |
| --- | --- |
| [bmad-sdlc](skills/bmad-sdlc/SKILL.md) | Coordinate discovery, planning, implementation, verification, resumption, and maintenance. |
| [bmad-guided-build](skills/bmad-guided-build/SKILL.md) | Plan and implement one ticket/change with review gates, an execution ledger, and independent implementation review. |
| [change-intake-governance](skills/change-intake-governance/SKILL.md) | Classify incoming work by the highest authoritative artifact it changes and choose the smallest safe route. |
| [decision-governance](skills/decision-governance/SKILL.md) | Analyze consequential decisions, obtain approval, and reconcile affected planning artifacts without starting implementation. |

All implementation handoffs from the three coordinating skills use **bmad-guided-build**. Only that wrapper calls the underlying BMad build internally. Missing dependencies block the affected route; they do not permit a raw-build fallback.

## Requirements

- A coding agent that reads Agent Skills. Codex UI metadata is included for all four skills; other hosts need their own skill discovery support.
- BMad Method and Core Tools installed and configured for the target project. These four skills do not bundle or automatically install BMad.
- Git for the guided wrapper's previous-work checkpoint, and the tools needed to build/test your application.
- uv for BMad's Python helpers. Node.js/npm is needed if installing through the Skills CLI.

See [compatibility and dependencies](docs/compatibility.md) for the inspected upstream snapshot, required capabilities, and verification limits. Cline references in the guided wrapper describe an optional host example; Cline is not a prerequisite. Independent reviewers use available host capabilities, with degraded independence disclosed when isolation is unavailable.

## Install

First install and set up BMad using the [upstream instructions](https://github.com/bmad-code-org/BMAD-METHOD). Ask the installed bmad skill to set up the Method and Core Tools modules in your target project.

Install all four skills globally for the agents detected by the Skills CLI. Follow its agent-selection prompts when shown:

~~~powershell
npx skills add ali-hm/alihm-bmad-skills --skill "*" --global
~~~

Global installation makes the skills available across projects for your user account. It does not install BMad or configure individual projects.

To select agents explicitly, use their CLI identifiers. For example, install globally for Claude Code, Cursor, and GitHub Copilot together:

~~~powershell
npx skills add ali-hm/alihm-bmad-skills --skill "*" --agent claude-code --agent cursor --agent github-copilot --global
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

~~~powershell
npx skills add ali-hm/alihm-bmad-skills --skill "*" --agent gemini-cli --global
~~~

The CLI also accepts `--agent "*"` to target all supported agents, including ones you do not currently use. Some agents, such as Eve, support project installation only; use explicit agent identifiers for global installation if the wildcard reports an unsupported target. See the [supported-agent list and installation options](https://github.com/vercel-labs/skills#supported-agents) for the current choices.

To install for one project instead, run the command from that project and omit `--global`. Agent discovery and workflow capabilities still depend on the selected host; installation alone does not verify live BMad execution there.

To inspect the local publishing checkout without installing:

~~~powershell
npx skills add . --list
~~~

The CLI supports repository discovery, named skills, local paths, and agent-specific installation. [Skills CLI documentation](https://github.com/vercel-labs/skills)

Keep all four companion skills together at the same version. Before installing over existing custom copies, preserve your edits and check which project/global copy the host selects. Refresh the host's skill discovery or start a new conversation after installation if needed.

## Use

The examples below name the skill in an ordinary request. Use your host's skill invocation mechanism when needed; in Codex, you can invoke a skill with its dollar-prefixed name, such as `$bmad-sdlc`. Replace the sample paths and ticket IDs with your project's actual artifacts.

### Coordinate a project with bmad-sdlc

Use this when you want help choosing and carrying out the next suitable steps across planning and delivery.

~~~text
Use bmad-sdlc to guide a new project: a volunteer scheduling app for a local
food bank. Help clarify the users, core workflows, and constraints before
choosing technologies or scaffolding the app.

Use bmad-sdlc with the approved specification at docs/booking-spec.md.
Check for gaps, then propose a ticket breakdown and implementation order.
Stop before implementation.

Use bmad-sdlc to investigate and fix duplicate notifications when a user
reconnects. Approved behavior is one notification per event. Preserve the
existing API contract and unrelated pending changes.

Use bmad-sdlc to continue this project's current approved work. Verify the
saved plan, ticket state, and review evidence before resuming the next step.

Use bmad-sdlc to report what remains before release. Inspect the current
evidence without editing files, changing ticket states, or deploying.
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

The Git checkpoint inspects pending work; a dirty tree may require a user choice. Auto does not authorize commits, publishing, deployment, or changes to consequential decisions. Project instructions and explicit user permissions remain authoritative.

Installing the bundle makes the skills available; it does not rewrite a project's policies or force every request through governance. To adopt them as project policy, review the [optional project-instruction example](docs/project-instructions.md).

## Updates and versions

Update the four skills together:

~~~powershell
npx skills update bmad-sdlc bmad-guided-build change-intake-governance decision-governance --global
~~~

For a project installation, use --project instead of --global. Review [CHANGELOG.md](CHANGELOG.md) before updating, particularly for workflow or approval changes. Updates can replace local edits; maintain modifications in a separate fork or reconcile them before updating.

The CLI uses recorded source information/content hashes to detect changes. Version metadata labels releases; it does not schedule checks or update manually copied skills. Normal repository installs follow their recorded source, so the default branch is kept ready for users. [Skills CLI update mechanism](https://github.com/vercel-labs/skills/blob/main/AGENTS.md)

Git tags and GitHub Releases identify reproducible bundle snapshots. To use a fixed release without following the default branch, check out its tag and install from that local checkout. Keep that installation under an explicit manual upgrade policy; a local-path install does not promise remote update detection.

BMad updates are separate. Use the installed bmad setup/update workflow and recheck compatibility before changing the upstream version.

## Maintain or publish this repository

Install validation dependencies and check the package from its root:

~~~powershell
python -m pip install -r requirements-dev.txt
python scripts/validate.py
~~~

Python 3.10+ is required for this repository's validation tooling. It is separate from the application stack and BMad's uv-managed runtime.

See [release instructions](docs/releasing.md) for version changes, validation, GitHub publication, and optional plugin submission. The root plugin.json packages the same four skills for portable plugin distribution; directory publication is a separate step.

Format validation does not prove live workflow execution. Review [compatibility.md](docs/compatibility.md) and the coordinator's [behavioral scenarios](skills/bmad-sdlc/references/evaluation.md) when assessing readiness.

## License and upstream

These custom skills and repository tooling use the [MIT license](LICENSE). BMad is an external dependency distributed under its own terms; no upstream BMad skills or runtime files are vendored here.

- [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD)
- [Agent Skills specification](https://agentskills.io/specification)
- [Skills CLI](https://github.com/vercel-labs/skills)
