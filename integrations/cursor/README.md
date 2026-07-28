# Cursor Integration

This directory contains the JES integration for Cursor.

## Purpose

The integration translates JES methodology into Cursor-compatible operational artifacts.

JES defines the methodology.  
This integration adapts it to Cursor.

Shared engineering operations are defined in:

- `../ENGINEERING_OPERATIONS.md`

## Structure

```text
cursor/
├── FOUNDATION.md
├── OPERATING_MODEL.md
├── README.md
├── rules/
├── prompts/
├── commands/
├── skills/
└── subagents/
```

## Components

- `FOUNDATION.md`: baseline operational contract between JES and Cursor.
- `OPERATING_MODEL.md`: translation model from engineering intent to JES-aligned execution and artifacts.
- `rules/`: Cursor-specific constraints derived from JES.
- `prompts/`: prompts that implement the contract and rules.
- `commands/`: operational command definitions.
- `skills/`: reusable skill-level behaviors for Cursor agents.
- `subagents/`: specialized subagent definitions and orchestration artifacts.

## Scope

This directory should not redefine JES principles, workflows, or governance.

It must reference and implement JES, not replace it.
