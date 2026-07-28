# JES — Ecosystem

> This document defines the JES execution ecosystem.  
> An ecosystem is not a tool list; it is a capability model and collaboration design.

---

## What the ecosystem defines

JES methodology defines principles, roles, workflows, and rules.  
The ecosystem defines where and how that methodology is executed.

It answers:
1. What capabilities JES needs,
2. What tool types can provide them,
3. How tools collaborate through an engineering cycle.

---

## JES capabilities

| Capability | Description | Cycle phases |
|---|---|---|
| Governance | methodological direction and high-level review | Intent, Analysis, Design |
| Development | implementation and technical execution | Plan, Implementation |
| Review | quality and architecture review | Validation |
| Automation | repeatable workflow execution, CI/CD | Validation, Completion |
| Knowledge | context and engineering knowledge retrieval | Analysis, Documentation |
| Execution | IDE, git, build/test runtime | Whole cycle |

---

## Integration criteria

A new tool should enter the ecosystem only if it:
- covers an uncovered/weakly covered capability,
- significantly improves quality/speed/reliability,
- avoids unnecessary duplication,
- adapts to JES without forcing JES changes,
- is replaceable.

Novelty alone is not a valid criterion.

---

## Ecosystem architecture

```text
JES
  |
  +-- Governance
  +-- Development
  +-- Knowledge
```

Current examples:
- Governance: ChatGPT/Claude
- Development: Cursor
- Review: Claude Code
- Automation: GitHub Actions
- Execution: Git + IDE

---

## Relationship with integrations

- `08_ENGINEERING_OPERATIONS.md` defines shared operation semantics.
- `06_INTEGRATIONS.md` defines how adapters are built.
- `integrations/` contains concrete adapters.

```text
08_ENGINEERING_OPERATIONS.md
        |
        v
07_ECOSYSTEM.md
        |
        v
06_INTEGRATIONS.md
        |
        v
integrations/
```

---

*Version: 2026.2 — Updated: July 2026*
