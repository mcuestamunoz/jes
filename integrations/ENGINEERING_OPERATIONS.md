# Engineering Operations

This document defines the engineering operations recognized by JES integrations.

These operations are methodology-level concepts, not tool commands.

Cursor, Claude Code, ChatGPT, and future integrations should implement the same operation set, adapting only execution mechanics to their platform.

## Purpose

Engineering operations provide a stable contract between:

- JES methodology (`docs/03_WORKFLOW.md`, `docs/05_RULES.md`)
- integration operating models
- tool-specific prompts and commands

This prevents each integration from inventing its own operation taxonomy.

## Operation Set (v1)

- Research
- Analyze
- Plan
- Implement
- Review
- Validate
- Document
- Explain
- Refactor

## Operation Definitions

### Research

Goal: gather and organize relevant context before deciding implementation details.

Typical outputs:
- findings summary
- references to affected files/components
- identified unknowns and risks

### Analyze

Goal: evaluate impact, constraints, and alternatives for a defined intent.

Typical outputs:
- scope analysis
- tradeoff analysis
- recommended options for Engineer decision

### Plan

Goal: translate approved direction into verifiable execution tasks.

Typical outputs:
- ordered task list
- acceptance/verification criteria
- expected artifacts per task

### Implement

Goal: execute approved plan within defined scope.

Typical outputs:
- code/configuration changes
- tests and checks
- implementation notes

### Review

Goal: evaluate correctness, quality, and alignment with architecture/rules.

Typical outputs:
- findings by severity
- regression/risk notes
- proposed fixes

### Validate

Goal: verify that implementation satisfies technical and workflow acceptance criteria.

Typical outputs:
- validation evidence (tests/checks/results)
- pass/fail status with rationale
- unresolved validation gaps

### Document

Goal: update repository knowledge to reflect approved system state.

Typical outputs:
- updated docs/specifications
- explicit note of impacted artifacts
- documentation completeness check

### Explain

Goal: communicate rationale, behavior, and impact of a change.

Typical outputs:
- concise explanation of what changed and why
- impact summary
- follow-up considerations

### Refactor

Goal: improve internal structure without changing intended external behavior.

Typical outputs:
- structural code improvements
- preserved behavior evidence
- identified technical debt changes

## Mapping to Integrations

Each integration must define:

1. how an operation is triggered (command or equivalent),
2. which prompt(s) implement it,
3. what artifact bundle is expected at completion.

A one-to-one operation-to-prompt mapping is allowed but not required.
One operation may use multiple prompts when needed by tool constraints or workflow depth.

## Governance Constraints

- Operations must not violate JES principles.
- Operations must respect engineer authority gates.
- Output artifacts are determined by workflow + operation, not by tool preference.

## Evolution

Changes to this operation set require explicit engineer approval and must be justified by demonstrated cross-integration value.
