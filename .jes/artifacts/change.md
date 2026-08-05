# Change

Generated: 2026-08-05T17:18:16Z

## Criterion

> Implement modifies **only** what the Execution Plan authorizes within scope.

## Cycle Intent

Implement the approved Execution Plan for Operation Selection documentation updates in Cursor runtime.

## Scope respected

integrations/cursor docs and validation scenarios only

## Execution Plan

- present: `.jes/artifacts/execution_plan.md`

## Mutated paths

- `integrations/cursor/policies/operation_selection_v0.md`

## Coherence checklist (Build)

- [x] code — considered for this documentation-scoped change
- [x] tests — considered for this documentation-scoped change
- [x] docs — considered for this documentation-scoped change
- [x] contracts — considered for this documentation-scoped change
- [x] workflow — considered for this documentation-scoped change

## Documentation

- Cursor Operation Selection policy catalog synced to Available Operations.

## Validation notes

- Technical: catalog block updated deterministically from `available_operations.json`.
- Human: Engineer should confirm the Change matches the approved plan.

## Explicit non-goals respected

- No objective reinterpretation
- No scope expansion
- No architecture decision
- No Core contract edits
- Cognition docs were not consulted; only Engineering State + Execution Plan
