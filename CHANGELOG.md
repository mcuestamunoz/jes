# Changelog

All notable changes to the JARVIS Engineering System (JES) are documented in this file.

## v1.1 — 2026-07-28

Architecture refinement that separates methodology from tool implementation while preserving v1.0 principles.

### Added

- Engineering Operations as a JES Core concept (`docs/08_ENGINEERING_OPERATIONS.md`)
- Cursor integration foundation contract (`integrations/cursor/FOUNDATION.md`)
- Cursor operating model (`integrations/cursor/OPERATING_MODEL.md`)
- Cursor integration skeleton (`rules/`, `prompts/`, `commands/`, `skills/`, `subagents/`)

### Changed

- Integration architecture now follows:
  - JES Core → Engineering Operations → Integration Layer → Tool Runtime
- `docs/06_INTEGRATIONS.md` aligned with Intent → Operation Selection → Engineering Operation → Execution
- `docs/02_ARCHITECTURE.md` updated to include the Engineering Operations layer
- `SYSTEM_DEFINITION.md` workflow diagram made tool-agnostic
- Core documentation rewritten in English for consistency

### Removed

- Tool-specific engineering concepts from Core methodology
- Legacy `JES.md` (duplicated `README.md` / `SYSTEM_DEFINITION.md`)
- Misplaced foundation document under Cursor `rules/`

## v1.0 — 2026-07

Foundational specification.

### Added

- System Definition
- Principles
- Architecture
- Workflow
- Roles
- Rules
- Integrations
- Ecosystem
