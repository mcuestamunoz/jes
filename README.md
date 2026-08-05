# JARVIS Engineering System (JES)

> **JES is an engineering system validated by incremental implementation.**

A tool-independent engineering methodology for human–AI collaborative software development.

---

## What JES defines

- **Principles** — the values that govern all engineering decisions
- **Architecture** — how the system is structured
- **Engineering Cognition** — how the engineer navigates work intentions
- **Engineering State** — live representation of an engineering cycle in progress
- **State Lifecycle** — how Engineering State is created, evolved, persisted, and ended
- **Roles** — who is responsible for what
- **Workflow** — how engineering cycles are closed and validated
- **Rules** — the constraints that apply within those cycles
- **Ecosystem** — the capabilities required and how tools provide them
- **Engineering Operations** — tool-agnostic units of engineering work
- **Operation Selection** — how to choose the next coherent available operation

---

## What JES does not define

JES does not define software.  
JES defines how engineering is performed.

---

## How to use JES

Projects that adopt JES declare the version they use:

```yaml
engineering:
  methodology:
    name: JES
    version: "1.2"
```

The methodology remains independent of any specific project.  
Projects consume JES. They do not contain it.

---

## Current phase

```text
Core (v1.2) — maintenance mode
   ↓
Cursor validation — done through Implement
   ↓
Ecosystem — consolidate Cursor, then second integration (Claude Code / P6)
```

Constitutional Core rule: `validation/CORE_MAINTENANCE.md`  
Operation evidence: `validation/MATRIX.md`  
Ecosystem roadmap: `validation/MILESTONE_ecosystem_phase.md`

---

## Version

Current: **v1.2** — Executable engineering core  
Status: **Core in maintenance** — validated by incremental implementation; evolve only on failed matrix cells or failed second-integration proof

See `CHANGELOG.md` for release notes.

---

*JARVIS Engineering System — August 2026*
