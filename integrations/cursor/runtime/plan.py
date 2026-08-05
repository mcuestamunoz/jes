#!/usr/bin/env python3
"""JES Cursor Operation: Plan v0.

Consumes the full Engineering State.
Produces an Execution Plan artifact (verifiable tasks).
Does not decide architecture, invent requirements, select future
operations, or execute changes.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[3]
STATE_PATH = ROOT / ".jes" / "state" / "engineering_state.json"
ARTIFACTS_DIR = ROOT / ".jes" / "artifacts"

_spec = importlib.util.spec_from_file_location(
    "operation_selection",
    Path(__file__).resolve().parent / "operation_selection.py",
)
_sel = importlib.util.module_from_spec(_spec)
assert _spec and _spec.loader
_spec.loader.exec_module(_sel)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_state() -> dict:
    data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if data.get("status") == "empty" or "schema_version" not in data:
        raise SystemExit("No live Engineering State. Run Interpretation first.")
    return data


def save_state(state: dict) -> None:
    state = dict(state)
    state["updated_at"] = utc_now()
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def preconditions(state: dict) -> list[str]:
    """Defense in depth beyond Selection."""
    errors: list[str] = []
    if not state.get("scope"):
        errors.append("scope is unbounded; Plan will not invent scope.")
    if state.get("authority_gates"):
        errors.append("authority_gates are pending; Plan will not close Decide.")
    return errors


def verifiable_tasks(state: dict) -> list[dict]:
    """Deterministic task skeleton from state — not an operation sequence."""
    intent = state.get("cycle_intent") or ""
    scope = state.get("scope") or ""
    return [
        {
            "id": "T1",
            "task": "Confirm Cycle Intent matches the approved objective text.",
            "done_when": f"Intent remains: {intent}",
            "in_scope": True,
        },
        {
            "id": "T2",
            "task": "Keep all work inside declared scope boundaries.",
            "done_when": f"No change outside: {scope}",
            "in_scope": True,
        },
        {
            "id": "T3",
            "task": "Produce the required closure artifacts listed in this plan.",
            "done_when": "Every required_artifact marker is present or explicitly waived by Engineer.",
            "in_scope": True,
        },
        {
            "id": "T4",
            "task": "Resolve or explicitly accept remaining open questions before Build.",
            "done_when": "open_questions is empty, or Engineer accepts a minimum cycle.",
            "in_scope": True,
        },
        {
            "id": "T5",
            "task": "Run technical validation against acceptance criteria after changes.",
            "done_when": "Evidence exists for technical + human validation.",
            "in_scope": True,
        },
    ]


def expected_closure_artifacts() -> list[str]:
    return [
        "Execution Plan (.jes/artifacts/execution_plan.md)",
        "Change (produced by a future Build operation — not executed by Plan)",
        "Evidence (produced by a future Validate/Review path — not executed by Plan)",
    ]


def build_execution_plan(state: dict) -> str:
    intent = state.get("cycle_intent") or ""
    scope = state.get("scope") or ""
    open_q = list(state.get("open_questions") or [])
    gates = list(state.get("authority_gates") or [])
    phases = list(state.get("relevant_workflow_phases") or [])
    required = list(state.get("required_artifacts") or [])
    tasks = verifiable_tasks(state)

    lines = [
        "# Execution Plan",
        "",
        f"Generated: {utc_now()}",
        "",
        "## Approved objective",
        "",
        intent,
        "",
        "## Engineering State consumed",
        "",
        f"- current_mode: `{state.get('current_mode')}`",
        f"- execution_status: `{state.get('execution_status')}`",
        f"- scope: `{scope}`",
        f"- open_questions: {len(open_q)}",
        f"- authority_gates: {len(gates)}",
        f"- required_artifacts (pre-plan): {len(required)}",
        f"- relevant_workflow_phases: {phases or ['(none yet)']}",
        "",
        "## Scope boundaries",
        "",
        f"- In scope: {scope}",
        "- Out of scope: anything not named above (Plan will not expand scope).",
        "",
        "## Workflow position",
        "",
        "```text",
        "Intent -> Analysis -> Design -> Plan -> Implementation -> Validation -> ...",
        "                                    ^",
        "                                 (here)",
        "```",
        "",
        "Plan turns an approved direction into verifiable execution.",
        "It does not reopen Design/Decide.",
        "",
        "## Authority gates",
        "",
    ]
    if gates:
        for g in gates:
            lines.append(f"- PENDING: {g}")
        lines.append("")
        lines.append("Plan must not run while gates are pending.")
    else:
        lines.extend(["- None pending — direction treated as approved for planning.", ""])

    lines.extend(["## Open questions", ""])
    if open_q:
        for q in open_q:
            lines.append(f"- UNRESOLVED: {q}")
        lines.append("")
        lines.append("Plan does not invent answers. These block Build unless Engineer accepts risk.")
    else:
        lines.extend(["- None.", ""])

    lines.extend(["## Verifiable tasks", ""])
    for t in tasks:
        lines.append(f"### {t['id']} — {t['task']}")
        lines.append("")
        lines.append(f"- Done when: {t['done_when']}")
        lines.append(f"- In scope: {t['in_scope']}")
        lines.append("")

    lines.extend(["## Required artifacts (closure bundle)", ""])
    for a in expected_closure_artifacts():
        lines.append(f"- {a}")
    lines.extend(
        [
            "",
            "## Explicit non-goals",
            "",
            "- No architecture decision",
            "- No invented requirements to close open questions",
            "- No selection of a multi-step operation sequence (Selection picks only the next op)",
            "- No repository mutation / no Implement execution",
            "- Cognition docs were not consulted; only Engineering State",
            "",
            "## Bridge to Build",
            "",
            "This Execution Plan is the handoff artifact for a future Implement operation.",
            "Build begins only when scope, gates, and open questions allow it.",
            "",
        ]
    )
    return "\n".join(lines)


def run_plan() -> int:
    state = load_state()
    selection = _sel.select(state, _sel.available_operations())
    if selection.get("status") != "selected" or selection.get("operation") != "Plan":
        print(json.dumps(selection, indent=2, ensure_ascii=False))
        print("REFUSED: Operation Selection did not select Plan.")
        return 2

    errors = preconditions(state)
    if errors:
        print("REFUSED: Plan preconditions failed.")
        for e in errors:
            print(f"- {e}")
        return 2

    state["active_operation"] = "Plan"
    if state.get("execution_status") == "interpreting":
        state["execution_status"] = "active"
    # Record workflow position without inventing earlier phase outputs.
    phases = list(state.get("relevant_workflow_phases") or [])
    for p in ("Intent", "Design", "Plan"):
        if p not in phases:
            phases.append(p)
    state["relevant_workflow_phases"] = phases
    save_state(state)

    plan = build_execution_plan(state)
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    out = ARTIFACTS_DIR / "execution_plan.md"
    out.write_text(plan, encoding="utf-8")

    state = load_state()
    state["active_operation"] = None
    artifacts = list(state.get("required_artifacts") or [])
    marker = "Execution Plan (.jes/artifacts/execution_plan.md)"
    if marker not in artifacts:
        artifacts.append(marker)
    # Expected later closure markers (not produced by Plan).
    for later in (
        "Change (future Build — not produced by Plan)",
        "Evidence (future Validate — not produced by Plan)",
    ):
        if later not in artifacts:
            artifacts.append(later)
    state["required_artifacts"] = artifacts
    save_state(state)

    print("PLAN_OK")
    print(f"artifact: {out.relative_to(ROOT)}")
    print(f"mode_unchanged: {state.get('current_mode')}")
    print(f"scope: {state.get('scope')}")
    print(f"open_questions: {len(state.get('open_questions') or [])}")
    print(f"authority_gates: {len(state.get('authority_gates') or [])}")
    print(f"required_artifacts: {len(state.get('required_artifacts') or [])}")
    print(f"active_operation: {state.get('active_operation')}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="JES Plan operation v0")
    parser.add_argument("command", choices=["run"])
    args = parser.parse_args()
    if args.command == "run":
        return run_plan()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
