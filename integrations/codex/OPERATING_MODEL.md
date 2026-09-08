# Codex Operating Model

How approved engineering work reaches Codex.

```text
Do not teach Codex all of JES.
Turn relevant JES decisions into an Implementation Contract.
```

```text
Experiment → Field Note → JES decision
        ↓
Implementation Contract
        ↓
Codex (reads AGENTS.md)
        ↓
Diff + tests
        ↓
Engineer re-validates in the product
        ↓
Field Note / keep or revise
```

No deep Cursor ↔ Codex pipeline is required. The interface is the contract plus git and tests.

---

## Working protocol

1. **Inspect** — implementation, callers, tests  
2. **Propose** — smallest change that satisfies the contract  
3. **Wait** — when scope is exceeded or the contract requires approval  
4. **Implement** — approved scope only  
5. **Test** — targeted first; fuller suite when appropriate  
6. **Report** — files, behavior delta, tests, risks  

---

## Quota / multi-agent practice

When Claude Code session limits block Jarvis work, Codex may take implementation contracts on a **different** project (e.g. `multiagent_problem_solving`).

Rules:

- do not silently move Jarvis architecture work to Codex “because quota”;
- keep one Implementation Contract scoped to one repo and one agent;
- log recurring quota friction in Field Notes (**P9**).

---

## Project setup checklist

1. Copy `templates/AGENTS.md` → project root `AGENTS.md` (adapt names/modules).  
2. Keep it small: how to work, not history.  
3. Per change: write an Implementation Contract from the template.  
4. Do not paste full JES into the agent context “just in case.”  
5. Engineer validates in the product; friction → JES Field Notes.
