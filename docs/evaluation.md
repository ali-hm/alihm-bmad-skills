# Behavioral evaluation of the bundle

Package validation checks structure, metadata, versions, licenses, and local references. It does not execute skill instructions or prove good workflow decisions. Evaluate the four skills using their scenarios:

| Skill | Scenarios |
| --- | --- |
| bmad-sdlc | [Coordinator](../skills/bmad-sdlc/references/evaluation.md) |
| bmad-guided-build | [Guided build](../skills/bmad-guided-build/references/evaluation.md) |
| change-intake-governance | [Change intake](../skills/change-intake-governance/references/evaluation.md) |
| decision-governance | [Decisions](../skills/decision-governance/references/evaluation.md) |

## Procedure and evidence

1. Validate package format and references first.
2. Select cases affected by the change. Cover all four skills for changes to shared permissions, ownership, or handoffs. Reuse the existing coordinator cases as baseline coverage.
3. Give an evaluator the actual skill, its needed local references, and raw scenario artifacts. Withhold expected observations, proposed fixes, other evaluator findings, and author conclusions until it finishes. Use fresh read-only contexts where available; otherwise disclose self-evaluation.
4. For hypothetical fixtures, request concrete next actions, selected workflow, scope, gates, phase states/outcome, and evidence needed. Do not execute installers, builds, Git mutations, trackers, or deployments in a dry run.
5. Compare the actual answer with expected observable behavior. Mark PASS, FAIL, or NOT_RUN with a reason. Do not score based on exact wording or keyword presence. A route listing alone is insufficient when permission or state transitions matter.
6. Fix demonstrated failures within authorized scope and rerun affected cases. Keep first-pass failures distinct from corrected results.
7. Save the scenario ID, date, package version, evaluator host/model when known, independence, actual observed action/outcome, result/reason, evidence reference, and limitations. Retain raw transcripts in the host's task history or an authorized artifact; never fabricate an execution transcript from an expected answer.

## Integration matrix

Record these levels separately for each host rather than assuming portable installation proves workflow support:

| Level | What it demonstrates |
| --- | --- |
| Package checks | Format, metadata, references, and CLI discovery |
| Routing dry run | Choices and handoff construction in hypothetical/read-only scenarios |
| Live local integration | Installed BMad planning/resume, real ledger/reviews, and an actual fixture's tests |
| Host compatibility | Discovery/invocation, permission enforcement, reviewer capacity/isolation, and cancellation on that host |

For live integration, use a disposable sample project and pre-authorize its allowed local side effects. Exercise Interactive, explicit Auto, early cancellation, missing dependencies, approval reuse, and reviewer-slot limits. Test each claimed host separately, including its actual fresh-context capability. Tracker publication and deployment require separate scope and fixtures.

Current results belong in [evaluation-results.md](evaluation-results.md). NOT_RUN integrations remain unverified; a passing dry run is never a substitute for live execution.
