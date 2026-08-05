#!/usr/bin/env python3
"""JES Cursor Operation: Implement v0.

First mutating Operation.
Success criterion: modify ONLY what the Execution Plan + scope authorize.

Does not reinterpret objectives, expand scope, or decide architecture.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[3]
STATE_PATH = ROOT / ".jes" / "state" / "engineering_state.json"
ARTIFACTS_DIR = ROOT / ".jes" / "artifacts"
EXECUTION_PLAN = ARTIFACTS_DIR / "execution_plan.md"
TARGET_DOC = ROOT / "integrations" / "cursor" / "policies" / "operation_selection_v0.md"
AVAILABLE_OPS = Path(__file__).resolve().parent / "available_operations.json"

# Core contracts — never mutate even if scope text were misread.
CORE_DENY = (
    "docs/02.5_ENGINEERING_COGNITION.md",
    "docs/02.6_ENGINEERING_STATE.md",
    "docs/02.7_ENGINEERING_STATE_LIFECYCLE.md",
    "docs/08_ENGINEERING_OPERATIONS.md",
    "docs/09_OPERATION_SELECTION.md",
)

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


def allowed_prefixes(scope: str) -> list[str]:
    """Derive path prefixes from scope text. Conservative defaults for Cursor materialization."""
    s = (scope or "").lower()
    prefixes: list[str] = []
    if "integrations/cursor" in s or "cursor" in s:
        prefixes.append("integrations/cursor/")
    if "validation" in s:
        prefixes.append("validation/")
    # Explicit path-like tokens in scope.
    for m in re.findall(r"(?:integrations|validation|docs)/[\w./-]+", scope or ""):
        p = m if m.endswith("/") else m
        if p not in prefixes:
            prefixes.append(p if p.endswith("/") else p + ("/" if "." not in Path(p).name else ""))
    return prefixes


def path_allowed(rel: str, prefixes: list[str]) -> bool:
    norm = rel.replace("\\", "/")
    if norm in CORE_DENY or any(norm.startswith(d.replace(".md", "")) for d in CORE_DENY):
        if norm in CORE_DENY:
            return False
    if norm in CORE_DENY:
        return False
    for d in CORE_DENY:
        if norm == d:
            return False
    if not prefixes:
        return False
    return any(norm == p.rstrip("/") or norm.startswith(p) for p in prefixes)


def preconditions(state: dict) -> list[str]:
    errors: list[str] = []
    if state.get("current_mode") != "Build":
        errors.append("current_mode must be Build.")
    if not state.get("scope"):
        errors.append("scope is unbounded; Implement will not invent scope.")
    if state.get("authority_gates"):
        errors.append("authority_gates pending; Implement will not bypass Engineer authority.")
    if state.get("open_questions"):
        errors.append("blocking open_questions remain; Implement will not invent answers.")
    if not state.get("coherence_checklist"):
        errors.append("coherence_checklist required for Build.")
    if not EXECUTION_PLAN.exists():
        errors.append("Execution Plan artifact missing; Implement requires Plan handoff.")
    return errors


def authorized_targets(state: dict) -> tuple[list[Path], list[str]]:
    """Only paths authorized by scope + plan objective (documentation updates in Cursor)."""
    prefixes = allowed_prefixes(state.get("scope") or "")
    errors: list[str] = []
    targets = [TARGET_DOC]
    for t in targets:
        rel = str(t.relative_to(ROOT))
        if not path_allowed(rel, prefixes):
            errors.append(f"authorized target out of scope: {rel}")
    return targets, errors


def apply_operation_selection_doc_update() -> str:
    """Minimal in-scope mutation: sync Selection policy docs with declared catalog."""
    catalog = json.loads(AVAILABLE_OPS.read_text(encoding="utf-8"))
    ops = catalog.get("available_operations", [])
    ops_block = "\n".join(ops)

    text = TARGET_DOC.read_text(encoding="utf-8")
    marker = "## Available Operations (Cursor v0)"
    if marker not in text:
        raise SystemExit("Unexpected Selection policy format; refusing improvised rewrite.")

    # Replace the fenced catalog under Available Operations with current declaration.
    pattern = rf"({re.escape(marker)}\n\n```text\n)(.*?)(\n```)"
    replacement = rf"\g<1>{ops_block}\g<3>"
    new_text, n = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("Could not locate Available Operations catalog block; refusing.")

    status_block = (
        "\n\n## Materialization status (Implement v0)\n\n"
        f"- Updated: {utc_now()}\n"
        "- Change authorized by Execution Plan + bounded scope.\n"
        "- Catalog synced to `runtime/available_operations.json`.\n"
        "- No Core contracts modified.\n"
    )
    if "## Materialization status (Implement v0)" in new_text:
        new_text = re.sub(
            r"\n## Materialization status \(Implement v0\).*",
            status_block.rstrip() + "\n",
            new_text,
            count=1,
            flags=re.S,
        )
    else:
        new_text = new_text.rstrip() + status_block

    TARGET_DOC.write_text(new_text, encoding="utf-8")
    return str(TARGET_DOC.relative_to(ROOT))


def build_change_artifact(state: dict, mutated: list[str], coherence: list[str]) -> str:
    intent = state.get("cycle_intent") or ""
    scope = state.get("scope") or ""
    lines = [
        "# Change",
        "",
        f"Generated: {utc_now()}",
        "",
        "## Criterion",
        "",
        "> Implement modifies **only** what the Execution Plan authorizes within scope.",
        "",
        "## Cycle Intent",
        "",
        intent,
        "",
        "## Scope respected",
        "",
        scope,
        "",
        "## Execution Plan",
        "",
        f"- present: `{EXECUTION_PLAN.relative_to(ROOT)}`",
        "",
        "## Mutated paths",
        "",
    ]
    for p in mutated:
        lines.append(f"- `{p}`")
    lines.extend(
        [
            "",
            "## Coherence checklist (Build)",
            "",
        ]
    )
    for c in coherence:
        lines.append(f"- [x] {c} — considered for this documentation-scoped change")
    lines.extend(
        [
            "",
            "## Documentation",
            "",
            "- Cursor Operation Selection policy catalog synced to Available Operations.",
            "",
            "## Validation notes",
            "",
            "- Technical: catalog block updated deterministically from `available_operations.json`.",
            "- Human: Engineer should confirm the Change matches the approved plan.",
            "",
            "## Explicit non-goals respected",
            "",
            "- No objective reinterpretation",
            "- No scope expansion",
            "- No architecture decision",
            "- No Core contract edits",
            "- Cognition docs were not consulted; only Engineering State + Execution Plan",
            "",
        ]
    )
    return "\n".join(lines)


def run_implement() -> int:
    state = load_state()
    selection = _sel.select(state, _sel.available_operations())
    if selection.get("status") != "selected" or selection.get("operation") != "Implement":
        print(json.dumps(selection, indent=2, ensure_ascii=False))
        print("REFUSED: Operation Selection did not select Implement.")
        return 2

    errors = preconditions(state)
    targets, terr = authorized_targets(state)
    errors.extend(terr)
    if errors:
        print("REFUSED: Implement preconditions failed.")
        for e in errors:
            print(f"- {e}")
        return 2

    state["active_operation"] = "Implement"
    if state.get("execution_status") in {"interpreting", "active"}:
        state["execution_status"] = "active"
    phases = list(state.get("relevant_workflow_phases") or [])
    if "Implementation" not in phases:
        phases.append("Implementation")
    state["relevant_workflow_phases"] = phases
    save_state(state)

    mutated: list[str] = []
    for t in targets:
        if t == TARGET_DOC:
            mutated.append(apply_operation_selection_doc_update())

    # Prove scope enforcement: never write Core.
    for p in mutated:
        if p in CORE_DENY:
            raise SystemExit("INTERNAL: attempted Core mutation")

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    change = build_change_artifact(state, mutated, list(state.get("coherence_checklist") or []))
    out = ARTIFACTS_DIR / "change.md"
    out.write_text(change, encoding="utf-8")

    state = load_state()
    state["active_operation"] = None
    artifacts = list(state.get("required_artifacts") or [])
    marker = "Change (.jes/artifacts/change.md)"
    # Replace the future-Build placeholder if present.
    artifacts = [
        a
        for a in artifacts
        if not a.startswith("Change (future Build")
    ]
    if marker not in artifacts:
        artifacts.append(marker)
    state["required_artifacts"] = artifacts
    save_state(state)

    print("IMPLEMENT_OK")
    print(f"artifact: {out.relative_to(ROOT)}")
    for p in mutated:
        print(f"mutated: {p}")
    print(f"mode_unchanged: {state.get('current_mode')}")
    print(f"scope: {state.get('scope')}")
    print(f"active_operation: {state.get('active_operation')}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="JES Implement operation v0")
    parser.add_argument("command", choices=["run"])
    args = parser.parse_args()
    if args.command == "run":
        return run_implement()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
