---
name: investor-router
description: Route any investment question to the right investor frameworks. Use first on every research task to identify the decision, select frameworks, keep analyses inspectable, reconcile evidence, and preserve disagreement.
---

# Investor router

The entry point. It decides which frameworks apply, why, and how their
conclusions combine — without votes, guru scores, or famous-name counting.
Closely related frameworks (Buffett/Munger/Nomad) never count as independent
evidence.

## When to use

First on every investment research question, and again when new evidence
arrives that could change framework selection.

## Workflow

1. **Identify.** Decision, asset type, horizon, evidence on hand, mandate
   constraints. Classify: business-quality (3–5 yr) vs tactical (weeks–18 mo)
   vs irrelevant to all frameworks (state it and stop — do not force a fit).
2. **Select.** Load only relevant frameworks; explain why each applies:
   - Quality/ownership/valuation → `buffett-business-quality`
   - Thesis stress-test / incentives / inversion → `munger-mental-models`
   - Growth-story classification and verification → `lynch-growth-stories`
   - Expectations / cycles / posture → `marks-risk-and-uncertainty`
   - Regime / liquidity / reversal / expression → `druckenmiller-macro-adaptation`
   - Decade-plus compounding / shared scale → `nomad-long-duration`
   - Output, risk, journal discipline → `research-risk-discipline` (always)
3. **Analyze inspectably.** Run each selected framework separately; keep
   principle IDs, evidence, and source IDs visible per framework.
4. **Reconcile.** Shared evidence weighed once; disagreements preserved with:
   competing conclusions, driving assumptions, horizons, emphasized evidence,
   and what would resolve it.
5. **Synthesize to mandate.** Thesis, assumptions, opposing case, scenarios,
   risks, invalidation, missing info, status/next action — via
   `research-risk-discipline`. Historical holdings stay dated; current company
   facts stay timestamped.

## Selection heuristics (defaults; override with reasons)

- Long-horizon single-stock quality → Buffett + Munger + Marks (+ Lynch if
  growth-story; + Nomad if shared-scale compounder candidate).
- Falling price, intact operating thesis → Buffett (patience test) + Marks
  (expectations) + Munger (inversion).
- Cheap with deteriorating economics → Marks (loss-first) + Munger + Lynch
  category check; Buffett/Nomad usually reject — record why.
- Macro/regime/tactical → Druckenmiller + Marks; Buffett/Nomad explicitly out
  of scope for timing.
- Stale holdings disclosure as "recommendation" → reject the premise; show
  dates and limits.

## Output contract

Routing table (framework → why selected/not) + per-framework analyses +
disagreement ledger + mandate-bound synthesis in the shared memo format.
No averaged scores. No verdict by vote.

## References

- `references/selection-matrix.md` — decision types × frameworks.
- `references/disagreement-protocol.md` — material-disagreement reporting rules.
- `references/worked-example.md` — short routing trace (see also demo/).
- `references/sources.md` — router methodology sources.
