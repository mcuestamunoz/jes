# Integrations

## Purpose

JES is an Engineering Operating System.

Its purpose is to define engineering methodology, not to implement it through any specific software tool.

External tools are considered **execution environments**.

JES remains independent from them.

---

# Principle

JES defines **how engineering should be performed**.

External tools execute that methodology.

Tools may change over time.

JES should not.

```text
Engineer
    |
    v
JES Core
    |
    v
Engineering Operations
    |
    v
Integration Layer
    |
    v
External Tool
```

---

# Integration Layer

Every external tool communicates with JES through an integration layer.

An integration implements JES in the capabilities of a specific tool.

The integration layer must never become the source of engineering knowledge.

Its only responsibility is to expose JES to the tool.

---

## Operational Translation Model

Integrations must translate engineer requests using the JES operation model:

```text
Intent
   ->
Operation Selection
   ->
Engineering Operation
   ->
Tool-specific Execution
```

Where:

- `Intent` is defined by the Engineer.
- `Operation Selection` is a Core contract (`docs/09_OPERATION_SELECTION.md`).
- Integrations declare Available Operations and invoke Selection.
- `Engineering Operation` meaning is defined by JES core.
- `Tool-specific Execution` is performed by the selected tool/runtime.

---

# Source of Truth

The source of truth is always the JES repository.

Specifically:

- SYSTEM_DEFINITION.md
- Documentation
- Engineering Rules
- Workflows
- Engineering Operations
- Templates

External integrations must reference these documents instead of duplicating them.

Canonical operation source:

- `docs/08_ENGINEERING_OPERATIONS.md`

---

# Design Principles

Every integration must follow these principles.

## Single Source of Truth

Engineering knowledge exists only inside JES.

Integrations must reference documentation.

They must not duplicate it.

---

## Thin Adapter

Integrations should remain as small as possible.

They should describe:

- where information is located
- how to access it
- when to use it

They should not redefine engineering concepts.

Tool-specific artifacts are allowed only as implementation details (for example: `FOUNDATION.md`, `OPERATING_MODEL.md`, `commands/`, `prompts/`, `skills/`, `subagents/`).

Those artifacts implement JES for one tool; they do not define JES.

---

## Tool Independence

JES must not depend on any external platform.

Replacing one tool with another should only require replacing its integration layer.

The engineering methodology must remain unchanged.

---

## Replaceable Integrations

Every integration should be isolated.

Example:

```
integrations/

cursor/

claude-code/

chatgpt/

codex/
```

Removing one integration must not affect JES.

---

# Responsibilities

## JES

Responsible for:

- engineering methodology
- architecture
- documentation
- workflows
- engineering rules
- engineering operations
- templates

---

## Integration

Responsible for:

- implementing JES for a specific tool
- exposing documentation
- configuring tool behavior
- selecting operations from intent
- mapping operations/workflow constraints into tool capabilities

---

## Tool

Responsible for:

- reasoning
- code generation
- editing
- execution
- interaction with the engineer

---

# Cursor Example (Implementation-Level)

```text
Cursor

  ->
Reads JES core context

  ->
Selects operation from intent

  ->
Applies tool-specific prompts/commands

  ->
Executes and returns JES-aligned artifacts

```

Cursor never becomes the owner of engineering knowledge.

It only consumes it.

---

# Future Integrations

Possible future integrations include:

- Cursor
- Claude Code
- ChatGPT
- Codex
- IDE plugins
- CI/CD pipelines
- Automation systems

No integration should require changes to JES itself.

---

# Summary

JES owns engineering knowledge.

Integrations expose that knowledge.

Tools execute it.

Dependency direction is one-way:

```text
JES Core
   ->
Engineering Operations
   ->
Integration
   ->
Tool
```

This separation guarantees:

- maintainability
- portability
- consistency
- replaceable tools
- long-term stability