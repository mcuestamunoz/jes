# Codex Integration

Thin JES adapter for OpenAI Codex as an **implementation and refactoring agent**.

This is **not** a Runtime validation (P6 / v2.0).  
It defines the **boundary** so Codex executes approved work without becoming another architect.

## Status

| Item | State |
|---|---|
| Boundary (Foundation + Operating Model + templates) | Defined |
| Project materialization (`AGENTS.md` in target repo) | Outside this repo |
| Runtime / Available Operations / matrix cells | Not started |
| P6 portability claim | Not claimed |

## Purpose

Same pattern as Claude Code: convert **relevant JES decisions** into Implementation Contracts.

```text
Engineer experiment / Field Note
        ↓
JES (architect)
        ↓
Implementation Contract (filtered view)
        ↓
Codex (implementer)  ← AGENTS.md = how to work
        ↓
Project code + tests
        ↓
Engineer validation → Field Note → JES
```

## Filename rule (important)

Codex auto-reads **`AGENTS.md`** (and optional `AGENTS.override.md`).

Do **not** rely on `CODEX.md` unless you configure `project_doc_fallback_filenames` in Codex.  
Prefer the standard name.

## Suggested project split (practice)

| Project | Agent | Root file |
|---|---|---|
| Jarvis | Claude Code | `CLAUDE.md` |
| multiagent_problem_solving (or other) | Codex | `AGENTS.md` |

One contract → one agent → one repo. Do not mix architectural authority across tools.

## Structure

```text
codex/
├── README.md
├── FOUNDATION.md
├── OPERATING_MODEL.md
└── templates/
    ├── AGENTS.md
    └── IMPLEMENTATION_CONTRACT.md
```

## Project materialization

```text
multiagent_problem_solving/   # example
├── AGENTS.md                 ← from templates/AGENTS.md
├── docs/implementation/      ← optional per-task contracts
└── …
```

## Related

- Sibling boundary: `../claude-code/` (same authority model; different tool file)
- Integration principles: `../../docs/06_INTEGRATIONS.md`
- Core freeze: `../../validation/CORE_MAINTENANCE.md`
- Evidence log: `../../validation/FIELD_NOTES.md`
