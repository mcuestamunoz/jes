#!/usr/bin/env python3
"""JES Cursor Operation: Research v0.

Consumes Engineering State only (not Cognition docs).
Produces an Understanding artifact.
Does not plan, change mode, propose implementations, or invent tasks.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STATE_PATH = ROOT / ".jes" / "state" / "engineering_state.json"
ARTIFACTS_DIR = ROOT / ".jes" / "artifacts"
DOCS_DIR = ROOT / "docs"
INTEGRATIONS_DIR = ROOT / "integrations"

# Import selection from sibling module without package install.
import importlib.util

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


def tokenize(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", text.lower()) if len(t) > 2}


def candidate_files() -> list[Path]:
    files: list[Path] = []
    for base in (DOCS_DIR, INTEGRATIONS_DIR, ROOT):
        if not base.exists():
            continue
        pattern = "*.md" if base != INTEGRATIONS_DIR else "**/*.md"
        files.extend(sorted(base.glob(pattern)))
    # Prefer core docs and cursor runtime docs; de-dupe.
    uniq: list[Path] = []
    seen = set()
    for f in files:
        if f.name.startswith("."):
            continue
        if "node_modules" in f.parts:
            continue
        key = str(f.resolve())
        if key in seen:
            continue
        seen.add(key)
        uniq.append(f)
    return uniq


def rank_files(intent: str, paths: list[Path], limit: int = 8) -> list[tuple[Path, int]]:
    tokens = tokenize(intent)
    scored: list[tuple[Path, int]] = []
    for path in paths:
        name_tokens = tokenize(path.stem.replace("_", " ") + " " + path.name)
        score = len(tokens & name_tokens)
        # Light content peek (first 2KB) for extra signal without full LLM.
        try:
            head = path.read_text(encoding="utf-8", errors="ignore")[:2000].lower()
        except OSError:
            continue
        score += sum(1 for t in tokens if t in head)
        if score > 0:
            scored.append((path, score))
    scored.sort(key=lambda x: (-x[1], str(x[0])))
    return scored[:limit]


def build_understanding(state: dict, ranked: list[tuple[Path, int]]) -> str:
    intent = state.get("cycle_intent") or ""
    mode = state.get("current_mode")
    status = state.get("execution_status")
    scope = state.get("scope")
    open_q = state.get("open_questions") or []

    lines = [
        "# Understanding",
        "",
        f"Generated: {utc_now()}",
        "",
        "## Cycle Intent",
        "",
        intent,
        "",
        "## State snapshot (consumed)",
        "",
        f"- current_mode: `{mode}`",
        f"- execution_status: `{status}`",
        f"- scope: `{scope}`",
        f"- open_questions: {len(open_q)}",
        "",
        "## Relevant repository context",
        "",
    ]
    if not ranked:
        lines.append("- No strongly matching files found by deterministic keyword ranking.")
    else:
        for path, score in ranked:
            rel = path.relative_to(ROOT)
            lines.append(f"- `{rel}` (score={score})")
    lines.extend(
        [
            "",
            "## Understanding summary",
            "",
            "Research v0 produces structured Understanding only.",
            "It does not plan work, change mode, propose implementations, or create tasks.",
            "",
            "Based on the Cycle Intent and matched repository documents, the investigated topic",
            "should be understood through the listed context files before any Design/Build work.",
            "",
            "## Non-goals respected",
            "",
            "- No mode transition",
            "- No implementation proposals",
            "- No multi-step plan",
            "- Cognition docs were not consulted; only Engineering State + repository files",
            "",
        ]
    )
    return "\n".join(lines)


def run_research() -> int:
    state = load_state()

    # Selection gate: do not execute unless Selection says Research.
    selection = _sel.select(state, _sel.available_operations())
    if selection.get("status") != "selected" or selection.get("operation") != "Research":
        print(json.dumps(selection, indent=2, ensure_ascii=False))
        print("REFUSED: Operation Selection did not select Research.")
        return 2

    # Mark operation active (state mutation allowed for execution lifecycle).
    state["active_operation"] = "Research"
    if state.get("execution_status") == "interpreting":
        state["execution_status"] = "active"
    save_state(state)

    ranked = rank_files(state.get("cycle_intent") or "", candidate_files())
    understanding = build_understanding(state, ranked)

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    out = ARTIFACTS_DIR / "understanding.md"
    out.write_text(understanding, encoding="utf-8")

    # State update after operation: clear active op; record artifact expectation met.
    state = load_state()
    state["active_operation"] = None
    artifacts = list(state.get("required_artifacts") or [])
    marker = "Understanding (.jes/artifacts/understanding.md)"
    if marker not in artifacts:
        artifacts.append(marker)
    state["required_artifacts"] = artifacts
    # Remove the generic scope question if present — Research produced understanding; scope may remain.
    save_state(state)

    print("RESEARCH_OK")
    print(f"artifact: {out.relative_to(ROOT)}")
    print(f"mode_unchanged: {state.get('current_mode')}")
    print(f"active_operation: {state.get('active_operation')}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="JES Research operation v0")
    parser.add_argument("command", choices=["run"], help="run Research against current state")
    args = parser.parse_args()
    if args.command == "run":
        return run_research()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
