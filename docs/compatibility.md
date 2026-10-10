# Compatibility and dependencies

## Package scope

This bundle contains four custom skills. BMad, uv, Git, the Skills CLI, application dependencies, and external MCP tools are not included. Installation does not automatically satisfy these dependencies.

The coordinator reads the installed skill catalog and actual specialist instructions before each handoff. BMad skill names, options, ticket stores, renderers, and artifact layouts can change; this bundle does not invent a uniform invocation API.

## Authoring snapshot

The locally installed BMad module records inspected on 2026-10-10 reported:

| Module | Recorded version |
| --- | --- |
| Method | 6.13.0-next |
| Core Tools | 6.13.0-next |

This is an authoring reference, not a promise of compatibility with every release carrying that label. No upstream commit identifier or broad supported version range has been established. Before releasing against an updated upstream version, inspect its interfaces and exercise the affected routes in a separate sample project.

## Required capabilities

For guided implementation, the host must discover bmad-build. Party Mode and Advanced Elicitation require bmad-party-mode and bmad-advanced-elicitation for the selected/risk-required phases. If a required capability is absent, stop that path and report the missing dependency.

Lifecycle routes additionally select installed specialists such as bmad-product-brief, bmad-prd, bmad-ux, bmad-architecture, bmad-spec, bmad-ticket, bmad-correct-course, bmad-project-context, and review/QA skills as needed. Not every route needs every specialist.

The host needs to run BMad's configured Python helpers with uv, read/write authorized project files, inspect Git state, and run the project's validation commands. Read-only independent reviewer contexts are preferred. When only same-context personas are available, the guided wrapper must disclose degraded independence and must not claim an independent-context review occurred.

Codex UI metadata is included, with implicit invocation enabled. Explicit prompts work through the host's normal skill mechanism; the dollar-prefixed prompt examples are for Codex. Other host discovery, invocation, permission, and delegation behavior must be verified separately.

## Project governance

Resolve canonical documentation and decision locations from the target project's instructions. The Docs/ examples in decision governance are illustrative. The bundle does not mandate another project's architecture, language, database, deployment model, design system, or document tree.

Consequential decisions need explicit user approval. Generated BMad artifacts do not override approved project decisions. A local implementation freeze remains in force. Installing a skill or requesting Auto does not authorize external publication, deployment, destructive actions, or unrelated Git changes.

## Verification limits

Package validation checks metadata, bundle version agreement, local references, and package structure. Behavioral dry runs inspect routing and permission boundaries. Neither proves that a live BMad build, acceptance test, deployment, or plugin-directory installation succeeds.

Keep live integration results separate from package-check results. The initial publication preparation did not run a live BMad build or publish this package.

The 0.2.0 evaluation procedure covers all four skills and explicitly checks risk classification, early exits, permission reuse, artifact ownership, and reviewer-capacity handling. Consult [evaluation.md](evaluation.md) and [evaluation-results.md](evaluation-results.md) for actual evidence and host-specific NOT_RUN limitations. Prompt-only dry runs do not establish that a host can execute BMad's planning/resume interface or supply independent reviewer contexts.
