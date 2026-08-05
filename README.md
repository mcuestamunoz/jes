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
    version: "1.3"
```

The methodology remains independent of any specific project.  
Projects consume JES. They do not contain it.

---

## Version

Current: **v1.3** — First Incremental Implementation Validation  
Status: Core in **maintenance mode**; first Cursor end-to-end validation complete without Core changes

Lineage: `v1.0` Foundation → `v1.1` Architecture → `v1.2` Execution model → **`v1.3` Implementation validation**  
(`v2.0` reserved for multi-integration portability.)

Constitutional Core rule: `validation/CORE_MAINTENANCE.md`  
Release evidence: `validation/MILESTONE_v13_first_implementation_validation.md`  
Matrix: `validation/MATRIX.md`

Next phase (not started): `validation/PHASE_3_ENGINEERING_WORKFLOW.md`

See `CHANGELOG.md` for release notes.

---

*JARVIS Engineering System — August 2026*
