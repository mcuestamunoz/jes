# Phase 3 — Engineering Workflow in Practice

> **Status: practice phase — discovery through real work.**  
> Not an interface-design sprint. Core stays in maintenance mode.

## Correct objective

Not:

> Design the Engineer Interface.

But:

> **Discover the Engineer’s real workflow by using JES while building real projects (starting with Jarvis).**

The interface will be designed later — from field evidence, not brainstorming.

## How to work from tomorrow

Treat JES as already real. Start sessions with a Cycle Intent, not with Operation names:

```text
Project: Jarvis

Cycle Intent:
Implementar el sistema de simulación aerodinámica.

Expected Outcome:
El sistema es capaz de simular un dron con un modelo inicial de fuerzas.

Scope:
simulation_engine/*
```

Then work as an engineer:

| You say | JES should tend toward |
|---|---|
| “No entiendo cómo modelar la resistencia del aire.” | Research / Explore |
| “Este modelo es demasiado complejo.” | Design / Model |
| “Me convence la opción B.” | Decide (+ authority) |
| “Vamos a implementarla.” | Plan → Implement |

You do **not** type `Research`, `Plan`, or `Build`.

## Dual output of every Jarvis hour

1. Progress on **Jarvis**
2. Evidence for **JES** (what the Engineer needed and lacked)

Those are not two projects. One feeds the other.

## Evidence instrument

`FIELD_NOTES.md` — short dated entries from real friction.

Example shape:

```text
Fecha

Proyecto:
Jarvis

Problema observado:
He perdido el contexto después de dos días.

Consecuencia:
He tardado 20 minutos en volver a situarme.

Idea:
JES debería resumir automáticamente el estado al restaurar un ciclo.
```

No note → no interface feature. (**P9**)

## Roadmap position

```text
JES Core                 ✅
Cursor Runtime           ✅
        ↓
Develop Jarvis with JES  ← here
        ↓
Daily Field Notes
        ↓
Consolidate personal flow
        ↓
Design Engineer Interface (from evidence)
        ↓
JES Desktop (voice, HUD, projector…) — much later
```

## What Phase 3 deliberately does not do yet

- Invent HUD / voice / Desktop UX
- Add Core concepts by anticipation
- Add a second integration
- Teach the Engineer to name Operations

## Success signal

After sustained Jarvis work, Field Notes contain recurring needs (context restore, open questions, blockers, “where are we?”).  
Those recurrences become the input to interface design — not the other way around.

## Related

- Field log: `FIELD_NOTES.md`
- Core freeze: `CORE_MAINTENANCE.md`
- v1.3 closed: `MILESTONE_v13_first_implementation_validation.md`
