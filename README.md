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

After this repository is published, install this bundle globally for Codex:

~~~powershell
npx skills add ali-hm/alihm-bmad-skills --skill "*" --agent codex --global
~~~

To install for one project instead, run the command from that project and omit --global. Other supported agents can use their Skills CLI agent identifier; host compatibility still needs checking.

To inspect the local publishing checkout without installing:

~~~powershell
npx skills add . --list
~~~

The CLI supports repository discovery, named skills, local paths, and agent-specific installation. [Skills CLI documentation](https://github.com/vercel-labs/skills)

Keep all four companion skills together at the same version. Before installing over existing custom copies, preserve your edits and check which project/global copy the host selects. Refresh the host's skill discovery or start a new conversation after installation if needed.

## Use

In Codex, invoke a skill with its dollar-prefixed name. For example:

~~~text
Use $bmad-sdlc to guide a new project from this idea: ...

Use $bmad-sdlc to turn this approved specification into the next authorized steps: ...

Use $bmad-sdlc to investigate and fix this existing-project bug: ...

Use $bmad-sdlc to continue this project's current approved work.

Use $change-intake-governance to classify this feature request before implementation: ...

Use $decision-governance to review this proposed architecture change: ...

Use $bmad-guided-build in Interactive mode for approved ticket 3.2.

Use $bmad-guided-build in Auto mode for approved ticket 3.2. Do not commit.
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
