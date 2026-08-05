# Cursor Integration

This directory contains the JES integration for Cursor.

## Purpose

The integration translates JES methodology into Cursor-compatible operational artifacts.

JES defines the methodology.  
This integration adapts it to Cursor.

Shared Core references:

- `../../docs/02.5_ENGINEERING_COGNITION.md`
- `../../docs/02.6_ENGINEERING_STATE.md`
- `../../docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`
- `../../docs/08_ENGINEERING_OPERATIONS.md`
- `../../docs/09_OPERATION_SELECTION.md`

## Structure

```text
cursor/
├── FOUNDATION.md
├── OPERATING_MODEL.md
├── RUNTIME.md
├── README.md
├── runtime/      # state, selection, operations (v0)
└── policies/     # Cursor policy adapters for runtime/ops
```

Empty `commands/`, `prompts/`, `rules/`, `skills/`, and `subagents/` skeletons were removed.  
Reintroduce them only when Field Notes demonstrate a need (**P9**).

## Components

- `FOUNDATION.md`: baseline operational contract between JES and Cursor.
- `OPERATING_MODEL.md`: translation model from engineering intent to JES-aligned execution.
- `RUNTIME.md`: how JES cycles, state, and lifecycle live inside Cursor.
- `runtime/`: Runtime tools (state, selection, operations).
- `policies/`: Cursor-specific policy adapters.

## Scope

This directory should not redefine JES principles, workflows, cognition, state, or governance.

It must reference and implement JES, not replace it.
