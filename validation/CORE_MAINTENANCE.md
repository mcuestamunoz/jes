# Core Maintenance Mode (constitutional)

> Effective after Implement v0 validated the Core against knowledge and transformation operations  
> without modifying Core contracts.

## Positioning

JES is no longer only a designed methodology.

> **JES is an engineering system validated by incremental implementation.**

## Constitutional rule

> **The Core enters maintenance mode.**

### Forbidden without cause

- ❌ Adding new Core concepts by anticipation
- ❌ Reorganizing Core documents because they would “look nicer”
- ❌ Refining Core models for elegance alone

### Allowed Core change — only if

1. An Operation **cannot** be implemented while respecting the Core contract, or
2. A **second integration** (Claude Code, Codex, etc.) demonstrates the contract is not truly tool-agnostic

Nothing else.

## Protected Core contracts

- `docs/02.5_ENGINEERING_COGNITION.md`
- `docs/02.6_ENGINEERING_STATE.md`
- `docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`
- `docs/08_ENGINEERING_OPERATIONS.md`
- `docs/09_OPERATION_SELECTION.md`

Related root/docs may evolve for positioning and ecosystem guidance, but must not silently invent new cognitive/state/selection semantics.

## Matrix gate

Any proposed Core edit must answer:

> **Which matrix cell failed to justify this change?**

If no cell failed, there is no Core change.

## What continues outside Core

- Fill remaining useful Operations when experience justifies them
- Enrich integrations (Cursor consolidation, then others)
- Accumulate matrix evidence
- Empirically validate P6 (Replaceable Tools) via a second runtime
