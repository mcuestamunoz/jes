# HARD RULE — Git promotion (v0)

> Binding for every Agent SDK / Grok Bot Work Order that mutates a git repository.  
> Violating this rule is a stop condition (`execution_status = blocked`), not a style preference.

## Canonical flow

```text
Bot works on jes-bot/<WO-id>-<slug>    ← one branch per Work Order
  → PR toward main (or the project's protected default branch)
  → Engineer review + ★
  → merge to main                      ← only path into the truth tip
  → runtime host (e.g. bender): git pull origin main
```

`<WO-id>` is the Work Order id (e.g. `WO-001`).  
`<slug>` is a short kebab objective from `cycle_intent`.

## Allowed

- Create and push **only** to `jes-bot/<WO-id>-<slug>`
- Commits exclusively on that branch for that WO
- Open / update a **draft or ready PR** targeting `main` (or project default)
- Request review; stop at `authority_gates` / Engineer ★
- Report branch name, PR URL, and diff summary in artifacts

## Forbidden

- Push directly to `main` / protected default
- Merge the PR (Engineer ★ only)
- Reuse one fixed branch (e.g. `jes_bot`) for multiple WOs
- Commit unrelated WOs onto an existing `jes-bot/…` branch
- Create release tags (`v0.x.y`, etc.) — Engineer / ACCEPT only
- Deploy or restart production as a side effect of the PR
- Force-push to `main` or rewrite shared history

## One branch per Work Order

| Pattern | Verdict |
|---|---|
| `jes-bot/WO-001-oauth-callback` | Correct |
| `jes-bot/WO-002-fix-flaky-parser` | Correct (separate WO) |
| `jes_bot` or `jes-bot` as a long-lived shared branch | **Forbidden** — mixes work |
| Commits on `main` “for speed” | **Forbidden** |

## Truth tip

`main` (after Engineer merge) is the only tip that runtime hosts may treat as the new version.  
A bot branch or open PR is **not** the deployed truth.

## Authority gates (minimum)

Every Implement WO that touches git must include at least:

```text
authority_gates:
  - Engineer ★ review and merge of PR to main
  - No bot merge / tag / deploy
```

## Stop conditions

If the tool cannot create a `jes-bot/…` branch or would be forced onto `main`, **do not improvise**. Set `blocked` and ask the Engineer.
