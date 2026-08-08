# Claude Code Foundation

Baseline contract for Claude Code when operating on a project governed by JES.

This document does **not** redefine JES methodology.  
It defines **authority boundaries** between JES, Claude Code, and the Engineer.

## Belonging

> If a concept would still matter after Claude Code disappears, it belongs to JES Core.  
> If it only makes sense because Claude Code exists, it belongs here or in project `CLAUDE.md`.

---

## Roles

### JES — Architect

Decides:

- which problem is being solved
- which principles and architecture must hold
- which changes are justified
- what must **not** be built
- when a refactor is justified
- what “done” means for an approved change
- which modules/files are in scope

JES does **not** write the project’s production code through this integration.

### Claude Code — Implementer

May decide:

- how to implement an approved change
- which local extraction or helper is cleanest
- how to structure tests
- which local technical risks to report

Must not decide:

- product direction
- new architectural subsystems
- Core or domain contract changes
- large structural moves without an explicit contract

> Claude may have **local technical authority**.  
> Claude must not have **global architectural authority**.

### Engineer — Direction and validation

Decides:

- whether the result works in real use
- whether the experience is correct
- whether the change should be kept
- whether unexpected behavior becomes a new Field Note

---

## Filtered view rule

Claude Code receives a **filtered view** of JES — not the whole system.

Provide:

- project `CLAUDE.md` (how to work)
- the active `IMPLEMENTATION_CONTRACT` for the task
- only the architecture constraints that task needs

Do **not** provide by default:

- full JES history
- all Field Notes
- roadmap / vision / “next objectives”
- philosophical discussion threads
- unrelated ADRs

Reason: excess architectural narrative invites the agent to reinterpret direction.

---

## Authority

- Final technical and strategic authority stays with the Engineer.
- Architectural direction is established externally (JES + Engineer) and must not be changed without explicit approval.
- Ambiguity that crosses module or contract boundaries → stop and ask.

---

## Documentation

- Important knowledge stays in the **project repository** (P3).
- This integration must not become a second source of engineering truth.
- Per-task contracts may be ephemeral; lasting decisions belong in project docs / ADRs / JES-derived constraints — not buried only in chat.

---

## Core references (for adapters, not for dumping into Claude)

- `../../SYSTEM_DEFINITION.md`
- `../../docs/01_PRINCIPLES.md`
- `../../docs/06_INTEGRATIONS.md`
- `../../docs/08_ENGINEERING_OPERATIONS.md`

Claude’s day-to-day instructions live in the project’s `CLAUDE.md` and the active Implementation Contract.
