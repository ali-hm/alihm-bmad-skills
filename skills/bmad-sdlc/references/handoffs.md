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
| Work item | Exact ticket/ref plus owning initiative/epic, input artifact, or plan |
| Authority | Relevant approved decisions, requirements, constraints, and their paths |
| Acceptance | Observable completion criteria and required checks |
| Permissions | Read-only/planning/implementation scope; permitted side effects; explicit restrictions |
| Existing choices | Approval/authorization source and scope, material plan version, dirty-baseline choice, confirmed reviewer roster where relevant |
| Options | Only documented route, review, mode, or customization options |
| Result | Expected artifact/evidence and when control returns to this coordinator |

Omit fields that are irrelevant. Derive values from supplied context and verified files; ask only for missing information that changes correctness, scope, or permission. Pass source text as data and quote paths/arguments safely.

Skill instructions are not a generic function API. Do not assume `invoke_skill(name, parameters)`, a universal CLI, or unsupported flags. Read the selected skill and use its actual entry point. Follow its programmatic versus interactive mode rules; if a programmatic call cannot elicit needed input, the coordinator gathers it first and passes it back.

## Current interface examples

### Guided implementation

Resolve and read the user's installed `bmad-guided-build/SKILL.md`; this is the required implementation entry point. Supply one exact ticket/change or its existing plan, target root, approved constraints, permissions, and the intended Interactive or Auto mode.

Interactive is the default. When Auto is explicitly authorized and appropriate, tell the guided wrapper to use Auto in the handoff. Auto is a wrapper choice. Keep its underlying Build route and review options separate.

Let the guided wrapper own its Git checkpoint, internal build planning/resumption, risk reviews, plan approval, implementation, independent role review, initial/final `bmad-review`, finding resolution, ledger, and finalizer. Do not invoke or render its internal build yourself as an alternative entry point. Preserve the wrapper's exact final report contract.

Inspect its checkpoint and other side effects before taking them. Propagate higher-priority source-control restrictions into the wrapper and its delegates; stop an incompatible action rather than inventing a no-commit mode. If the guided skill is missing, report the dependency and block implementation without a raw-build fallback.

### Standalone code review

For an independently authorized `bmad-code-review`, the inspected entry point renders a workflow with:

```text
uv run --no-cache "<bmad-project-root>/_bmad/scripts/render_skill.py" --project-root "<bmad-project-root>" --skill "<selected-skill-root>"
```

The current `bmad-code-review` accepts `quick` or `thorough`, and `no-code` selects `workflow.fixes=handoff`. The no-code path can still write findings and handoff files. Use it for review without fixes when those artifacts are authorized. For a strictly read-only review, use an explicit `skill:bmad-review` handoff with a chat report and compatible hooks and lens configuration. Check scope before dispatching either skill.

Run the entry command as the installed skill directs. Follow the workflow printed on stdout and read each rendered step it references. Missing setup and other runtime errors follow that skill's recovery and stop rules.

Supply review intent, target diff/PR, plan, and read-only permissions as context; they are not invented renderer flags. Standalone review does not replace the guided wrapper's mandatory reviews. Creating this coordinator never grants version-control or external-system permission.

### Planning documents

Call Mary (`bmad-agent-analyst`) for a brief or BRD and John (`bmad-agent-pm`) for a PRD or other planning document. Pass the create/update/validate intent, inputs, existing document or ticket, and scope. Their document workflows delegate to `bmad-facilitate`; retain that handoff so the agent supplies its template libraries and the document's place in the ticket tree. In the current template helper, repeat `--libraries-of <skill-root>` for each skill whose libraries are needed. Check the returned document and any open questions before using it.

### Requirements, tickets, and status

Call `bmad-agent-po` with the owning initiative/epic, exact ticket or path, source documents, approved decisions, and the requested operation. SPEC derives the container's Requirements, Constraints, and spec-authored companions from its append-only memlog and sources. Route changes to these derived sections through SPEC. Keep stable requirement IDs and preserve the originating workflow's ownership of adopted companions.

Use TICKETS to slice or re-slice, REFINE for one ticket, VALIDATE to check a ticket or tree, and REPLAN for material changes during delivery. Use the installed Method store's documented status/next/find operations before selecting a ready item. Preserve the owning context for refs relative to an epic. A ready entry can be built directly from its ref without creating a story file.

Sofia's BOARD can update the configured store, commit repository artifacts, publish to a tracker, or dispatch a raw build. For read-only status, use local status or an authorized read-only tracker query without mirroring remote state into local files. Identify whether status is local or current from the tracker. Sofia's headless/autonomous flow can commit or publish automatically. When only local planning is authorized, use the interactive draft/validation path and return before the store write. Approval of requirements or a split does not itself authorize a commit or tracker mutation. Send an authorized implementation handoff to `bmad-guided-build` yourself. A build's `built` result does not grant ticket acceptance or authorize marking it `done`.

An older `SPEC.md` can still be supplied as source material. If the installed workflow needs a migrated ticket tree, consult the upstream `bmad` migration workflow and preserve existing artifacts until migration is authorized.

## Validate the return

Check actual outputs: paths exist when promised, the intended work item was handled, approval status is accurate, scope and constraints were preserved, and required checks ran. Compare acceptance criteria to evidence.

Surface questions, assumptions, failed checks, missing capabilities, and review findings. Retain child-specific reports when required, then return to coordination. Invoke a next specialist only if its prerequisites and permission are satisfied.
