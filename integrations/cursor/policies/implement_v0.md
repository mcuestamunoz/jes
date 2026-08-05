# Cursor Policy — Implement v0

First mutating Operation. Validates nearly the full Core pipeline.

## Success criterion

> **Does Implement modify only what the Execution Plan authorizes?**

If it must reinterpret the objective, expand scope, or decide architecture, it is doing another Operation's job.

## Validates

- Engineering State
- Lifecycle (mode movement into Build)
- Operation Selection
- Workflow (Implementation phase)
- Authority Gates
- Coherence Checklist
- Required Artifacts (Change)
- Documentation (in-scope policy sync)
- Validation notes in Change artifact

## Preconditions

1. `current_mode = Build`
2. Bounded `scope`
3. Empty `authority_gates`
4. Empty `open_questions`
5. `coherence_checklist` present
6. `.jes/artifacts/execution_plan.md` exists
7. Selection `operation = Implement`

## Mutation policy

- Only paths inside declared scope prefixes
- Never Core contracts (`02.5`–`02.7`, `08`, `09`)
- Authorized v0 change: sync Cursor Selection policy catalog to Available Operations

## Non-goals

- No objective reinterpretation
- No scope expansion
- No architecture decisions
- No multi-op orchestration

## Command

```bash
python3 integrations/cursor/runtime/implement.py run
```
