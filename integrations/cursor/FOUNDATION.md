# Cursor Foundation

This document defines the baseline operational contract for Cursor when operating inside a workspace governed by the JARVIS Engineering System (JES).

It does not define the engineering methodology.  
The methodology is defined by JES.

This document defines how Cursor must behave to implement that methodology.

## Authority

- The human engineer has final authority over all technical and strategic decisions.
- Never make architectural decisions autonomously.
- Ask for clarification when requirements are ambiguous.

## Engineering Principles

Before implementing changes:

- Respect the documented architecture.
- Prefer existing patterns over creating new ones.
- Minimize unnecessary complexity.
- Keep changes deterministic and traceable.
- Preserve consistency across the project.

## Documentation

When a change affects architecture, workflows, interfaces, or engineering decisions:

- Recommend updating the relevant documentation.
- Never silently introduce undocumented behavior.

## Context

Before making assumptions, consult repository documentation.

The engineering methodology is defined by the documents in this repository.

Core documents:

- `SYSTEM_DEFINITION.md`
- `docs/01_PRINCIPLES.md`
- `docs/02_ARCHITECTURE.md`
- `docs/03_WORKFLOW.md`
- `docs/04_ROLES.md`
- `docs/05_RULES.md`
- `docs/06_INTEGRATIONS.md`
- `docs/07_ECOSYSTEM.md`
- `docs/08_ENGINEERING_OPERATIONS.md`

Repository documentation is the source of truth.
