# Codex Foundation

Baseline contract for Codex when operating on a project governed by JES.

This document does **not** redefine JES methodology.  
It defines **authority boundaries** between JES, Codex, and the Engineer.

## Belonging

> If a concept would still matter after Codex disappears, it belongs to JES Core.  
> If it only makes sense because Codex exists, it belongs here or in project `AGENTS.md`.

---

## Roles

### JES — Architect

Decides problem, principles, architecture kept/forbidden, scope, and done criteria.

### Codex — Implementer

May decide local implementation, helpers, tests, and technical risk reports **inside** an approved contract.

Must not decide product direction, new subsystems, or Core/domain contract changes.

> Codex may have **local technical authority**.  
> Codex must not have **global architectural authority**.

### Engineer — Direction and validation

Validates real use, accepts/rejects, and opens new Field Notes.

---

## Filtered view rule

Provide:

- project `AGENTS.md`
- the active Implementation Contract for the task
- only architecture constraints that task needs

Do **not** dump by default: full JES, all Field Notes, roadmap, vision, or decision history.

---

## Tool file

Use **`AGENTS.md`** at the project root (Codex discovery default).  
Optional: nested `AGENTS.md` / `AGENTS.override.md` closer to the working directory.

---

## Core references (for adapters, not for dumping into Codex)

- `../../SYSTEM_DEFINITION.md`
- `../../docs/01_PRINCIPLES.md`
- `../../docs/06_INTEGRATIONS.md`
- `../../docs/08_ENGINEERING_OPERATIONS.md`
