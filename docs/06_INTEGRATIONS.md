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

```
Engineer
      │
      ▼
     JES
      │
      ▼
Integration Layer
      │
      ▼
External Tool
```

---

# Integration Layer

Every external tool communicates with JES through an integration layer.

An integration translates JES concepts into the capabilities of a specific tool.

The integration layer must never become the source of engineering knowledge.

Its only responsibility is to expose JES to the tool.

---

# Source of Truth

The source of truth is always the JES repository.

Specifically:

- SYSTEM_DEFINITION.md
- Documentation
- Engineering Rules
- Workflows
- Templates

External integrations must reference these documents instead of duplicating them.

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
- templates

---

## Integration

Responsible for:

- adapting JES to a specific tool
- exposing documentation
- configuring tool behaviour
- mapping workflows into tool capabilities

---

## Tool

Responsible for:

- reasoning
- code generation
- editing
- execution
- interaction with the engineer

---

# Cursor Example

```
Cursor

↓

Cursor Rule

↓

Read:

SYSTEM_DEFINITION.md

↓

Read:

Engineering Rules

↓

Execute Task
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

This separation guarantees:

- maintainability
- portability
- consistency
- replaceable tools
- long-term stability