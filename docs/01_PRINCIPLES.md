# JES — Principles

> This document defines the principles that govern the JARVIS Engineering System.  
> A principle is not a workflow or a rule. It is a value statement that applies even when no explicit rule exists.  
> If a rule conflicts with a principle, the principle prevails.

---

## What a principle is (and is not)

A principle answers: *what do we value when making decisions?*

It is not a workflow (how to do work).  
It is not a rule (a specific constraint).  
It is not architecture (how the system is organized).

Principles are durable value constraints for unanticipated situations.

---

> Engineering exists to build systems that remain understandable, maintainable, and evolvable over time.  
> The principles below define how JES pursues that goal.

---

## The nine JES principles

### P1 — Human Authority

Technical authority is never delegated.

The engineer alone decides direction, architecture, and strategy. AI agents may propose, analyze, review, and implement. They do not decide.

### P2 — AI as Collaborator

Implementation can be delegated; design responsibility cannot.

Agents are high-capability technical collaborators, but design direction remains with the engineer.

### P3 — Repository First

All relevant knowledge lives in the repository.

No dependency on private chats, session memory, or undocumented context is acceptable.

### P4 — Documentation as Engineering

Documentation is an engineering artifact.

A system is incomplete if knowledge is not documented with the same rigor as code and tests.

### P5 — Deterministic Engineering

Every change must be reproducible, observable, verifiable, and traceable.

If outcomes cannot be repeated and checked, they cannot be trusted or improved.

### P6 — Replaceable Tools

Tools are replaceable; architecture is not tool-owned.

Methodology must be defined by responsibilities and outcomes, not by platforms.

### P7 — Context over Memory

Agents operate from explicit context and must not rely on assumed memory.

System documents and rules are the context source.

### P8 — Continuous Validation

No implementation exists without verification.

Validation closes every change, not just final milestones.

### P9 — Justified Complexity

Every new component increases complexity and must justify clear value.

Do not add tools, abstractions, or process without a concrete problem they solve.

---

## Relationship between principles

```text
P1 Human Authority      <- authority foundation
P2 AI as Collaborator   <- role boundary
P3 Repository First     <- knowledge location
P4 Documentation        <- completion condition
P5 Determinism          <- verification model
P6 Replaceable Tools    <- technology independence
P7 Context over Memory  <- agent context model
P8 Validation           <- cycle closure
P9 Justified Complexity <- growth governance
```

P1 is the root principle.  
P9 is long-term sustainability control.

---

## Conflict resolution

Principles are designed to be complementary.  
If they appear to conflict, the engineer interprets which option best preserves JES purpose as defined in `SYSTEM_DEFINITION.md`.

Principles are applied as a coherent system, not in isolation.

---

*Version: 2026.1 — Updated: July 2026*
