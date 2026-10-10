# Optional project policy

Installing these skills makes them available; it does not establish a new project policy. If you want mandatory intake and guided implementation, review and explicitly adopt a scoped rule in your project's existing AGENTS.md or equivalent. Preserve that project's established instructions.

Example:

~~~markdown
## BMad project workflow

Use bmad-sdlc to coordinate lifecycle work when requested.

After an approved planning baseline exists or implementation has begun, use
change-intake-governance for newly reported bugs, features, refactors, upgrades,
incidents, and other changes before creating implementation work.

Use decision-governance for consequential new or changed decisions. Explicit
user approval is required; propagate approved decisions through affected
planning artifacts before dependent implementation.

Route implementation through bmad-guided-build. Do not invoke bmad-build or
bmad-build-auto directly; only the guided wrapper owns internal build calls.
Use Interactive mode by default. Auto needs an explicit user request and must
preserve the wrapper's review, evidence, risk, and human-approval gates.

Apply project instructions, approved decisions, and user permissions to every
workflow. Do not commit, push, deploy, or publish without authorization.
~~~

The guided wrapper also includes an [optional detailed reporting rule](../skills/bmad-guided-build/AGENTS-rule.md). Review it before adding it to project instructions; it is not installed automatically.
