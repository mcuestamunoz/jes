# JES — Roles

> This document defines responsibilities in JES.  
> A role is not a person or tool; it is an accountability boundary.

---

## Role model

JES defines three roles:

| Role | Actor Type | Objective |
|---|---|---|
| Engineer | Human | Govern the system |
| Engineering Agent | AI | Execute technical work |
| Knowledge Manager | Human/AI-assisted | Preserve and update knowledge |

---

## 1) Engineer

Responsibilities:
- define direction and strategy,
- make architectural decisions,
- approve methodology changes,
- validate cycle outcomes.

Authority:
- final decision authority,
- non-delegable strategic control.

---

## 2) Engineering Agent

Responsibilities:
- implement approved work,
- generate code/tests/technical artifacts,
- analyze impact and propose alternatives,
- support technical validation.

Limits:
- no autonomous design decisions,
- no architectural modifications without explicit approval,
- no integration of changes as final truth without validation.

---

## 3) Knowledge Manager

Responsibilities:
- maintain repository accuracy,
- record relevant decisions,
- keep docs synchronized with approved system state.

Limits:
- reflects approved decisions,
- does not originate strategic changes independently.

---

## Role interaction flow

```text
Engineer -> assigns scoped work + context -> Engineering Agent
Engineering Agent -> produces artifacts -> Engineer
Engineer -> validates/approves -> Knowledge Manager
Knowledge Manager -> updates repository truth
```

---

## What is not a role

- LLM model type (runtime capability, not responsibility boundary)
- Tool/platform (execution environment, not governance role)
- Prompt (instruction mechanism, not role identity)
- Task (temporary activity, not persistent accountability)

---

*Version: 2026.2 — Updated: July 2026*
