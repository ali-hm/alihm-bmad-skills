# Plan review procedures

Read for structured plan review, Party Mode, or Advanced Elicitation. The Auto risk matrix applies to Auto; Interactive review actions remain user-selected.

## Structured plan review

Use for:

- Interactive `Review the plan`;
- LOW Auto mode.

Check:

- acceptance criteria coverage;
- alignment with PRD/UX/Architecture/approved decisions;
- hidden assumptions;
- missing steps;
- missing tests;
- dependency direction;
- compatibility;
- security/reliability;
- deployment/migration implications;
- unnecessary complexity;
- scope creep;
- rollback/recovery where relevant.

Report:

- Blocking
- Important
- Optional

For Auto LOW:
- apply only safe in-scope refinements;
- record findings and applied/rejected items;
- show a visible result summary;
- then continue.

For Interactive:
- let user choose which changes to apply;
- return to the five-option menu.

---

## Party Mode — role selection and independent execution

### Interactive role selection

Do not invoke Party Mode until the final roster is confirmed.

First propose:

**Recommended party**
- 4–6 roles selected for this ticket.

Ask:

1. **Continue with recommended party**
2. **Customize party**
3. **Cancel**

#### Customize party

Keep recommended roles preselected unless user chooses to clear them.

Show the current roster and role catalog:

1. System Architect
2. Senior Developer
3. QA / Test Engineer
4. Security Engineer
5. SRE / Reliability Engineer
6. DevOps / Deployment Engineer
7. Database / Data Engineer
8. Performance Engineer
9. API / Integration Engineer
10. Distributed Systems / Messaging Engineer
11. Network Engineer
12. Concurrency Specialist
13. Desktop Application Engineer
14. Web Frontend Engineer
15. UX Designer / UX Engineer
16. Accessibility Specialist
17. Product Manager
18. Business / Domain Analyst
19. Operations / Support Engineer
20. Observability Engineer
21. Release / Packaging Engineer
22. Backward-Compatibility Reviewer
23. Data Privacy / Compliance Reviewer
24. Threat Model / Red-Team Reviewer
25. Minimalism / Complexity Reviewer
26. Maintainability Reviewer
27. Failure-Mode / Pre-mortem Reviewer
28. Integration Reviewer
29. Migration Reviewer
30. User / Customer Advocate
31. Enterprise Identity / LDAP Engineer
32. Offline / Air-Gapped Deployment Engineer
33. Custom role

Do NOT use a single-choice role picker.

Use plain-text multi-selection, supporting:

- `+7,+10,-4`
- `set 1,2,3,10,24`
- `add Database Engineer, remove Security Engineer`
- `33: Cryptography Reviewer`
- `clear`
- `recommended`

After customization show the resulting roster and ask:

1. **Start Party Mode with this roster**
2. **Customize again**
3. **Restore recommended party**
4. **Cancel**

Only start Party Mode after explicit confirmation. Reuse an already confirmed roster for the same plan and review scope; ask again only when a material change affects that choice.

### Auto role selection

Auto mode selects 4–6 roles automatically from the same catalog.

Examples:

#### General
- System Architect
- Senior Developer
- QA / Test Engineer
- Security Engineer
- SRE / Reliability Engineer

#### Messaging/synchronization
- System Architect
- Senior Developer
- Distributed Systems / Messaging Engineer
- QA / Test Engineer
- SRE / Reliability Engineer

#### Database/persistence
- System Architect
- Senior Developer
- Database / Data Engineer
- Performance Engineer
- QA / Test Engineer

#### Authentication/LDAP
- System Architect
- Security Engineer
- Enterprise Identity / LDAP Engineer
- Senior Developer
- QA / Test Engineer

#### Deployment/update/air-gapped
- System Architect
- DevOps / Deployment Engineer
- Offline / Air-Gapped Deployment Engineer
- Security Engineer
- Operations / Support Engineer

#### UI/UX
- UX Designer / UX Engineer
- Senior Developer
- relevant Desktop/Web engineer
- Accessibility Specialist
- QA / Test Engineer

#### Protocol/networking
- System Architect
- Distributed Systems / Messaging Engineer
- Network Engineer
- Security Engineer
- QA / Test Engineer

### Independent execution policy

Use the shared [review scheduling policy](implementation-review.md#review-scheduling-and-isolation) for Party Mode as well as implementation review. It defines capacity detection, fresh-context batches, evidence isolation, bounded recovery, and degraded review disclosure. Do not reduce the confirmed roster just because there are fewer concurrent slots.

### Party Mode review questions

Each reviewer should challenge:

- hidden assumptions;
- architecture/integration;
- security;
- reliability;
- test coverage;
- operability;
- compatibility;
- unnecessary complexity;
- failure modes;
- scope creep.

### Mandatory Party Mode receipt

Party Mode cannot be marked COMPLETE until the user has been shown:

```text
Party Mode Result
Roles executed:
- ...

Per-role findings:
- <Role>: ...
- <Role>: ...

Cross-role disagreements:
- ...

Accepted recommendations:
- ...

Rejected recommendations:
- ... (reason)

Escalated:
- ...
```

In Auto mode this visible receipt is mandatory even though no approval is requested.

If the receipt was not produced, Party Mode is not complete.

### Applying recommendations

Automatically apply only recommendations that are:

- within approved ticket/spec scope;
- consistent with upstream artifacts;
- implementation-plan refinements;
- non-conflicting.

Do not auto-apply recommendations that:

- change product scope/acceptance behavior;
- change approved architecture/security/data/deployment/technology;
- create a new consequential decision;
- materially expand the ticket;
- contradict authoritative artifacts.

Such findings stop Auto mode and route through governance.

After applying safe changes:
- update the plan;
- revalidate consistency;
- record accepted/rejected/escalated recommendations;
- return to the five-option menu in Interactive mode.

---

## Advanced Elicitation

Use `bmad-advanced-elicitation` against the exact plan.

### Interactive

Let the user select methods normally.

Afterward:
- apply only user-accepted refinements;
- update the plan;
- revalidate;
- show results;
- return to the five-option menu.

### Auto

Required for HIGH and CRITICAL.

Choose 2–4 methods appropriate to risk.

#### Foundational architecture
- First Principles
- Pre-mortem
- Boundary/Edge-Case Sweep
- Complexity Reduction/Inversion

#### Security/identity
- Red Team/Adversarial Review
- Threat/Abuse-Case Analysis
- Pre-mortem
- Assumption Challenge

#### Distributed systems/messaging
- Failure-Mode Analysis
- Cascading Failure Simulation
- Boundary/Edge-Case Sweep
- First Principles

#### Data/migration
- Migration Failure Analysis
- Reversibility/Rollback Analysis
- Edge-Case Sweep
- Pre-mortem

#### Deployment/operations
- Pre-mortem
- Failure-Mode Analysis
- Rollback/Recovery Analysis
- Constraint Analysis

#### Performance/concurrency
- Bottleneck/Constraint Analysis
- Race/Interleaving Analysis
- Boundary/Load Extremes
- Pre-mortem

If installed method names differ, choose the closest by intent.

### Mandatory Advanced Elicitation receipt

It cannot be marked COMPLETE until the user sees:

```text
Advanced Elicitation Result
Methods executed:
- ...

Findings:
- ...

Accepted refinements:
- ...

Rejected:
- ... (reason)

Escalated:
- ...
```

In Auto mode this receipt is mandatory.

Apply only safe in-scope refinements.
Escalate consequential decisions.

---

## Auto-mode plan-review matrix

After the plan exists:

### LOW

Structured plan review only.

### MEDIUM

Party Mode.

### HIGH

Party Mode
→ reconcile safe findings
→ Advanced Elicitation
→ reconcile safe findings.

### CRITICAL

Same as HIGH
→ final validation
→ STOP for explicit human approval.

Before Auto mode may approve LOW/MEDIUM/HIGH, assert from the ledger:

- required plan review = COMPLETE;
- Party Mode = COMPLETE when required;
- Advanced Elicitation = COMPLETE when required;
- visible receipts were produced;
- no unresolved blocker/escalation exists.

If any assertion fails, Auto mode MUST NOT implement.

---

## Automated Review provenance in the plan

Maintain:

```md
## Automated Review

Importance: <level>

### Structured Review
...

### Party Mode
Roles:
- ...

Per-role findings:
- ...

Accepted:
- ...

Rejected:
- ...

Escalated:
- ...

### Advanced Elicitation
Methods:
- ...

Findings:
- ...

Accepted:
- ...

Rejected:
- ...

Escalated:
- ...
```

Omit sections that are genuinely NOT_APPLICABLE.

Do not write a false empty section just to satisfy the format.

---
