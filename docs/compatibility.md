# Compatibility and dependencies

## Package scope

This bundle contains four custom skills. BMad, uv, Git, the Skills CLI, application dependencies, and external MCP tools are not included. Installation does not automatically satisfy these dependencies.

The coordinator reads the installed skill catalog and actual specialist instructions before each handoff. BMad skill names, options, ticket stores, renderers, and artifact layouts can change; this bundle does not invent a uniform invocation API.

## Authoring snapshot

Bundle 0.4.0 targets [BMad Method main at a867e160](https://github.com/bmad-code-org/BMAD-METHOD/tree/a867e1604b365d48ea03cbd109da1066ba0c84bc), checked on 2026-11-12. Upstream describes this line as the v7 preview. Its Method and Core Tools manifests both report `6.13.0-next`, so the commit identifies the inspected interfaces more precisely than the manifest versions. Compatibility with the v6.12 stable line or every revision of the preview is unverified. See the [upstream installation guide](https://github.com/bmad-code-org/BMAD-METHOD/blob/a867e1604b365d48ea03cbd109da1066ba0c84bc/docs/start/install-bmad.md).

## Upgrade from earlier preview skills

| Previous skill or operation | Current route |
| --- | --- |
| `bmad-product-brief` | `bmad-agent-analyst` (Mary) uses the brief template via `bmad-facilitate`. |
| `bmad-prd` | `bmad-agent-pm` (John) uses the PRD template via `bmad-facilitate`. |
| `bmad-spec` | `bmad-agent-po` (Sofia), SPEC. The owning initiative or epic ticket holds the requirements and constraints. |
| `bmad-ticket` | Sofia's TICKETS, REFINE, VALIDATE, or BOARD as appropriate. |
| `bmad-correct-course` | Sofia's REPLAN for material changes during delivery. |
| Explicit ingest or document sharding requests | `bmad-ingest` for cited source notes and `bmad-shard-pro` for long-document navigation. |

Use upstream `bmad setup` to inspect stale skill copies and runtime changes. Check how the installed setup moves customizations, including `bmad-ticket.toml` to `bmad-agent-po.toml`. Compare old overrides with the new Sofia and Facilitate interfaces before carrying them forward. Use the upstream migration workflow separately if an older artifact tree needs conversion. Preserve existing plans, decision history, and reviews, and verify the migration scope before authorizing writes. [Upstream retirement list](https://github.com/bmad-code-org/BMAD-METHOD/blob/a867e1604b365d48ea03cbd109da1066ba0c84bc/skills/bmod-method/retired.toml)

## Required capabilities

For guided implementation, the host must discover `bmad-build` and `bmad-review`. The wrapper uses the full build route, its written-plan checkpoint, and the approved plan path for resumption. It takes control at `built` before upstream's default commit step. Both modes retain mandatory initial and final `bmad-review` passes. Party Mode and Advanced Elicitation need `bmad-party-mode` and `bmad-advanced-elicitation` for the selected or risk-required phases. Report missing capabilities on the affected route.

The pinned `bmad-review` supports explicit caller directives, resolved customization, code/document lens applicability, and separate findings without severity. Its default lenses include edge-case-hunter, verification-gap, adversarial, structure, and prose. Resolve actual project overrides, lens codes, ordering, hooks, and output contracts before use. See the [ticket review gate](../skills/bmad-guided-build/references/ticket-review.md).

Lifecycle routes select installed specialists according to the request, including UX, architecture, project context, or QA. Sofia's configured store can have commit or publication steps. Read-only status and local planning drafts have their own scope and do not authorize those operations.

The host needs to run BMad's configured Python helpers with uv, read/write authorized project files, inspect Git state, and run the project's validation commands. Read-only independent reviewer contexts are preferred. When only same-context personas are available, the guided wrapper must disclose degraded independence and must not claim an independent-context review occurred.

Codex UI metadata is included, with implicit invocation enabled. Explicit prompts work through the host's normal skill mechanism; the dollar-prefixed prompt examples are for Codex. Other host discovery, invocation, permission, and delegation behavior must be verified separately.

## Project governance

Resolve canonical documentation and decision locations from the target project's instructions. The Docs/ examples in decision governance are illustrative. The bundle does not mandate another project's architecture, language, database, deployment model, design system, or document tree.

Consequential decisions need explicit user approval. Generated BMad artifacts do not override approved project decisions. A local implementation freeze remains in force. Installing a skill or requesting Auto does not authorize external publication, deployment, destructive actions, or unrelated Git changes.

## Verification limits

Package validation checks metadata, bundle version agreement, local references, and package structure. Behavioral dry runs inspect routing and permission boundaries. Neither proves that a live BMad build, acceptance test, deployment, or plugin-directory installation succeeds.

Keep live integration results separate from package-check results. The initial publication preparation did not run a live BMad build or publish this package.

The evaluation procedure covers all four skills and checks risk classification, early exits, permission reuse, artifact ownership, reviewer capacity, and ticket review gates. Consult [evaluation.md](evaluation.md) and [evaluation-results.md](evaluation-results.md) for actual evidence. Prompt-only dry runs do not establish that a host can execute BMad's planning/resume interface, run `bmad-review`, or supply independent reviewer contexts.
