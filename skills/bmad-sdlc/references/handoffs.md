# Discovery and specialist handoffs

Read this before calling BMad skills. Examples reflect an inspected installation and are not a compatibility promise; the actual installed skill is authoritative.

## Discover installed capabilities

Use the host's available-skills catalog first. Resolve exact skill paths; never hardcode a particular user's home directory. Read the selected skill's `SKILL.md` and only the supporting references it needs.

The BMad root is the nearest ancestor containing `_bmad/`, starting from the target working directory. Do not assume the Git root is the BMad root; several repositories may share a workspace installation. If no root exists, use the installed `bmad` setup instructions.

When available, use BMad's installed knowledge helper to obtain module help:

```text
uv run <bmad-skill-root>/scripts/knowledge.py --root <project-skills-root> --root <user-skills-root> --content
```

Include only active roots that actually exist, project roots first. This command inventories modules; custom non-module skills may still be in the host catalog. Read all returned module help, and only relevant listed topic files. If this read-only helper cannot run, inspect its installed help files directly and disclose incomplete discovery where it matters.

Use the installed config resolver to locate the active initiative and output folder:

```text
uv run <bmad-project-root>/_bmad/scripts/resolve_config.py --project-root <bmad-project-root> --key core.output_folder --key core.active_initiative
```

Do not assume an initiative slug, default output directory, or legacy artifact layout. If several initiatives fit, resolve the target before writing. Do not migrate or change the active initiative merely to answer status.

If setup or a required skill is missing, explain the exact dependency and use the installed setup workflow when installation/setup is already authorized. A request to start or adopt a project using BMad normally authorizes the necessary reversible local BMad setup files, unless the user or project restricts writes. Advice, status, and review-only requests do not authorize setup changes. Installing packages or using a network must still fit the request and environment permissions; obtain only genuinely missing authorization. A freeze on application dependencies is not automatically a ban on tooling setup; evaluate its actual scope. Never repair unrelated configuration just to continue.

## Handoff contract

Prepare a concise dispatch in natural language or the selected skill's documented input format:

| Field | Content |
|---|---|
| Target | Absolute project/BMad root; affected repositories when more than one |
| Operation | Discover, create, update, validate, plan, implement, review, resume, or status |
| Intent | User's requested behavior, defect evidence, or refactor preservation goal |
| Work item | Exact ticket/ref plus owning initiative/epic, spec folder, input artifact, or plan |
| Authority | Relevant approved decisions, requirements, constraints, and their paths |
| Acceptance | Observable completion criteria and required checks |
| Permissions | Read-only/planning/implementation scope; permitted side effects; explicit restrictions |
| Options | Only documented route, review, mode, or customization options |
| Result | Expected artifact/evidence and when control returns to this coordinator |

Omit fields that are irrelevant. Derive values from supplied context and verified files; ask only for missing information that changes correctness, scope, or permission. Pass source text as data and quote paths/arguments safely.

Skill instructions are not a generic function API. Do not assume `invoke_skill(name, parameters)`, a universal CLI, or unsupported flags. Read the selected skill and use its actual entry point. Follow its programmatic versus interactive mode rules; if a programmatic call cannot elicit needed input, the coordinator gathers it first and passes it back.

## Current interface examples

### Guided implementation

Resolve and read the user's installed `bmad-guided-build/SKILL.md`; this is the required implementation entry point. Supply one exact ticket/change or its existing plan, target root, approved constraints, permissions, and the intended Interactive or Auto mode.

Interactive is the default. When Auto is explicitly authorized and appropriate, invoke the guided skill in its documented Auto mode (the inspected skill accepts natural-language Auto requests and `--auto` in invocation text). This is not a shell command or renderer option. Do not turn it into `--set workflow.mode=auto` or dispatch `bmad-build-auto`.

Let the guided wrapper own its Git checkpoint, internal build planning/resumption, risk reviews, plan approval, implementation, independent review, ledger, and finalizer. Do not invoke or render its internal build yourself as an alternative entry point. Preserve the wrapper's exact final report contract.

Inspect its checkpoint and other side effects before taking them. Propagate higher-priority source-control restrictions into the wrapper and its delegates; stop an incompatible action rather than inventing a no-commit mode. If the guided skill is missing, report the dependency and block implementation without a raw-build fallback.

### Standalone code review

For an independently authorized `bmad-code-review`, the inspected entry point renders a workflow with:

```text
uv run --no-cache "<bmad-project-root>/_bmad/scripts/render_skill.py" --project-root "<bmad-project-root>" --skill "<selected-skill-root>"
```

Standalone code review accepts `--set workflow.review=quick` or `thorough` when selected. Reverify those values against its installed entry point. This example is for standalone review, not a direct-build recipe.

Run the entry command exactly as that skill requires, then read the returned absolute `workflow.md`. Do not skip rendering or execute template sources directly. Missing setup and other runtime errors follow that skill's recovery/stop rules; a general discovery fallback is not permission to bypass an execution failure.

Supply review intent, target diff/PR, plan, and read-only permissions as context; they are not invented renderer flags. Standalone review does not replace the guided wrapper's mandatory reviews. Creating this coordinator never grants version-control or external-system permission.

### Specification

`bmad-spec` receives the input sources, the target spec folder or meaningful slug, and the intended create/update/validate operation. Programmatic invocations may run headless and require an explicit or derivable slug. Inspect returned JSON errors as errors, not as completed artifacts.

The spec kernel and spec-authored companions are derived from its append-only memlog. Update through `bmad-spec`; never hand-patch derived outputs. Adopted companions stay owned by their originating workflow. Project-approved decisions retain authority over generated proposals.

### Tickets and status

`bmad-ticket` reads the configured store and its own operation references. Supply the full spec folder for decomposition so capability IDs remain traceable.

Use its documented status/next/query operations before selecting a ready item. Ticket refs can be relative to an epic; preserve the owning context. Use ticket-store commands rather than directly editing state fields or assuming repo-store commands work on a tracker.

Publishing to a tracker is an external mutation with its own authorization. A build's `built` result is not automatically `done`; observe the installed acceptance contract.

## Validate the return

Check actual outputs: paths exist when promised, the intended work item was handled, approval status is accurate, scope and constraints were preserved, and required checks ran. Compare acceptance criteria to evidence.

Surface questions, assumptions, failed checks, missing capabilities, and review findings. Retain child-specific reports when required, then return to coordination. Invoke a next specialist only if its prerequisites and permission are satisfied.
