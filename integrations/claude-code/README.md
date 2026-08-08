# Claude Code Integration

Thin JES adapter for Claude Code as an **implementation and refactoring agent**.

This is **not** a second validated Runtime (P6 / v2.0).  
It defines the **boundary** so Claude Code executes approved work without becoming another architect.

## Status

| Item | State |
|---|---|
| Boundary (Foundation + Operating Model + templates) | Defined |
| Project materialization (`CLAUDE.md` in Jarvis) | Outside this repo |
| Runtime / Available Operations / matrix cells | Not started |
| P6 portability claim | Not claimed |

## Purpose

Convert **relevant JES decisions** into implementation contracts that Claude Code can execute.

Claude Code does **not** need all of JES.  
It needs the constraints JES decided are relevant for a concrete task.

```text
Engineer experiment / Field Note
        ↓
JES (architect)
        ↓
Implementation Contract (filtered view)
        ↓
Claude Code (implementer)  ← CLAUDE.md = how to work
        ↓
Project code + tests (e.g. Jarvis)
        ↓
Engineer validation → Field Note → JES
```

## Structure

```text
claude-code/
├── README.md
├── FOUNDATION.md
├── OPERATING_MODEL.md
└── templates/
    ├── CLAUDE.md
    └── IMPLEMENTATION_CONTRACT.md
```

| Artifact | Role |
|---|---|
| `FOUNDATION.md` | Who decides what (JES / Claude / Engineer) |
| `OPERATING_MODEL.md` | How work flows into Claude Code |
| `templates/CLAUDE.md` | Repo operating manual — copy into the **project** root |
| `templates/IMPLEMENTATION_CONTRACT.md` | Per-task contract — scoped instruction, not a roadmap |

## What this integration is not

- Not a dump of JES Core, Field Notes, roadmap, or decision history into Claude
- Not product architecture ownership for the agent
- Not a deep Cursor ↔ Claude pipeline — the interface is the contract
- Not authorization to invent subsystems or change Core contracts

## Project materialization

JES owns the templates. The consuming project (e.g. Jarvis) owns the live files:

```text
Jarvis/
├── CLAUDE.md                    ← from templates/CLAUDE.md
├── docs/implementation/         ← optional per-task contracts
│   └── FN-00N-….md
└── …
```

## Related

- Integration principles: `../../docs/06_INTEGRATIONS.md`
- Ecosystem capability map: `../../docs/07_ECOSYSTEM.md`
- Core freeze: `../../validation/CORE_MAINTENANCE.md`
- Evidence log: `../../validation/FIELD_NOTES.md`
- Cursor (development environment): `../cursor/`
