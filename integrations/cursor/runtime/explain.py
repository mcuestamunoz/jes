#!/usr/bin/env python3
"""JES Cursor Operation: Explain v0.

Consumes Engineering State (+ optional prior Understanding artifact).
Produces an Explanation artifact (Communication).
Does not research deeply, change mode, or propose implementations.
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
UNDERSTANDING = ARTIFACTS_DIR / "understanding.md"

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


def read_understanding_excerpt(limit: int = 1200) -> str | None:
    if not UNDERSTANDING.exists():
        return None
    text = UNDERSTANDING.read_text(encoding="utf-8", errors="ignore")
    return text[:limit]


def build_explanation(state: dict, understanding: str | None) -> str:
    intent = state.get("cycle_intent") or ""
    lines = [
        "# Explanation",
        "",
        f"Generated: {utc_now()}",
        "",
        "## Question",
        "",
        intent,
        "",
        "## Plain explanation",
        "",
        "This Explanation artifact communicates the current understanding of the Cycle Intent",
        "using Engineering State and, when available, a prior Understanding artifact.",
        "",
        f"Current mode is `{state.get('current_mode')}` with status `{state.get('execution_status')}`.",
        "Explain v0 does not gather new research depth; it communicates what is already in state/context.",
        "",
    ]
    if understanding:
        lines.extend(
            [
                "## Basis (from prior Understanding)",
                "",
                "```markdown",
                understanding.strip(),
                "```",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "## Basis",
                "",
                "- No prior Understanding artifact found.",
                "- Explanation is limited to Engineering State snapshot only.",
                "",
            ]
        )

    lines.extend(
        [
            "## Communicated takeaway",
            "",
            f"The engineering question under discussion is: {intent}",
            "Answer it by referring to the Core pipeline position carried in Engineering State,",
            "without changing mode or proposing implementation work.",
            "",
            "## Non-goals respected",
            "",
            "- No deep repository research pass",
            "- No mode transition",
            "- No implementation proposals",
            "- Cognition docs were not consulted; only Engineering State (+ optional Understanding)",
            "",
        ]
    )
    return "\n".join(lines)


def run_explain() -> int:
    state = load_state()
    selection = _sel.select(state, _sel.available_operations())
    if selection.get("status") != "selected" or selection.get("operation") != "Explain":
        print(json.dumps(selection, indent=2, ensure_ascii=False))
        print("REFUSED: Operation Selection did not select Explain.")
        return 2

    state["active_operation"] = "Explain"
    if state.get("execution_status") == "interpreting":
        state["execution_status"] = "active"
    save_state(state)

    explanation = build_explanation(state, read_understanding_excerpt())
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    out = ARTIFACTS_DIR / "explanation.md"
    out.write_text(explanation, encoding="utf-8")

    state = load_state()
    state["active_operation"] = None
    artifacts = list(state.get("required_artifacts") or [])
    marker = "Explanation (.jes/artifacts/explanation.md)"
    if marker not in artifacts:
        artifacts.append(marker)
    state["required_artifacts"] = artifacts
    save_state(state)

    print("EXPLAIN_OK")
    print(f"artifact: {out.relative_to(ROOT)}")
    print(f"mode_unchanged: {state.get('current_mode')}")
    print(f"active_operation: {state.get('active_operation')}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="JES Explain operation v0")
    parser.add_argument("command", choices=["run"])
    args = parser.parse_args()
    if args.command == "run":
        return run_explain()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
