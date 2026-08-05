# Phase 3 — Engineering Workflow in Practice

> **Status: design opened (discovery captured). Not implemented.**  
> Opens after JES v1.3. Does **not** modify Core yet (maintenance mode).

## Discovery

The opening act is not:

> Open Cursor to ask for code.

It is:

> **Open Cursor to start an engineering cycle.**

| Improvisation (today) | JES (target) |
|---|---|
| “Hazme un planner” | State a Cycle Intent |
| Name Operations (`Research`, `Plan`…) | Speak goals and judgments |
| Conversation drift | Interpretation → State → Selection → Operation |
| Talk to the IDE | Work with **JES** (tool is a carrier) |

The Engineer never needs to know that Research or Implement exist.  
They say what they want to achieve; JES translates.

## Seed examples (intent language)

```text
Quiero que Jarvis optimice configuraciones de drones mediante DSE.
```

```text
Vale. Diseñemos la arquitectura del DSE.
```

```text
Me convence esta arquitectura.
```

```text
Perfecto. Implementémosla.
```

```text
Creo que estamos atascados.
```

```text
Continuemos.
```

These carry **intention**, not implementation recipes.

## What already exists (internal machinery)

```text
Cycle Intent → Interpretation → Engineering State → Cognition/Mode
    → Operation Selection → Operation → Artifacts / State Update
```

v1.3 validated that pipeline inside Cursor without Core edits.

## What is missing (external face)

> **How does the Engineer converse with JES?**

Not with Cursor. With JES.

Until now the architecture answered an **internal** question:

> How does the system work?

It has not fully answered the **external** one:

> What is the Engineer’s daily experience?

That experience is the entrance to JES. If it is natural, the Engineer does not think about Modes, State, or Operations — they work, and JES does the rest.

## Design object of Phase 3

**Engineer Interface** — the conversational contract between Engineer and JES.

Candidate concerns (to design from practice, not invent wholesale):

1. How a day starts (arrive → Cycle Intent → first response)
2. Intent language vs Operation language (forbidden: requiring the Engineer to name ops)
3. How progress is felt (HUD-like presence vs invisible State)
4. How Mode/Operation changes are announced without jargon overload
5. How authority gates appear in conversation (“I need your decision”)
6. How a session ends / cycle pauses / cycle closes
7. Belonging: which interface rules are Core (tool-agnostic) vs integration chrome

## Method

Same rigor as Core validation:

```text
Hypothesis: intent-language dialogue is enough for daily engineering.
     ↓
Practice: develop JARVIS speaking only in intentions.
     ↓
Evidence: field notes (friction, missing cues, unwanted Operation leakage).
     ↓
Conclusion: specify Engineer Interface; only then touch Core if a cell fails.
```

## Non-goals (for now)

- No new Core concepts by anticipation
- No second integration
- No prompt pack that teaches the Engineer to type `Research`
- No full UX chrome invention before practice evidence

## Day loop (target sketch — not final)

```text
Arrive
  → state Cycle Intent (goal, not op name)
  → JES interprets / selects / runs
  → Engineer judges, redirects, approves, continues
  → session ends with State persistable for tomorrow
```

## Open question for design

> What must the Engineer say — and what must they never have to say — for JES to remain the system of work rather than a chat wrapper around an IDE?
