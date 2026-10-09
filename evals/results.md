# Behavior eval results (builder-run, small-N — not a controlled trial)

Method: builder answered 3 of 12 evals twice from the same prompt — once by
following the skill files (citing principle IDs), once from general knowledge
without opening them. Full 12-eval with/without comparison with independent
grading is future work (see Weaknesses). No returns claims; behavior only.

## EVAL-01 (strong business, excessive price)

- With skills: routed Buffett + Marks + Munger + Nomad-gated-off (no
  shared-scale evidence). BUF-P05/MRK-P04 priced-in math (25%-for-a-decade);
  MUN-P02 ruin paths clear; status reject-for-mandate at this price with
  buy-below band + watch triggers. Labels and invalidation present.
- Without: "great company but expensive, wait for a dip" — same direction,
  but no priced-in quantification, no invalidation conditions, no attribution.
- Delta: skills added the implied-growth statement, the invalidation set, and
  the explicit Nomad-off reason. Direction agreed.

## EVAL-07 (stale 13F as recommendation)

- With skills: premise rejected per risk-rules; dates/limits demanded; current
  company work required; status recorded as premise-rejected, not as analysis.
- Without: "13Fs are delayed 45 days, check current price" — weaker: missed
  partial-exposure limits and the no-private-reasoning rule.
- Delta: skills caught the completeness-of-exposure point the baseline missed.

## EVAL-12 (irrelevant task — 0DTE gamma)

- With skills: irrelevance stated; no framework forced; shared evidence
  standards offered only.
- Without: answered the gamma question directly (fine) but with no boundary
  statement about what the frameworks do not cover.
- Delta: skills added the boundary; baseline answer was otherwise acceptable.

## Remaining weaknesses (honest)

1. Only 3/12 evals exercised, by the builder, unblinded. EVAL-06/08/09/10
   (insufficient-evidence, horizon-split, liquidity bind, reversal) are the
   highest-value remaining runs.
2. No independent grader; rubric in cases.md untested for inter-rater spread.
3. Historical-exercise contamination untested (model may know famous outcomes
   despite as-of restriction).
4. Quantitative paths (reverse-DCF round trip, FX/minority guards) reuse
   trading-v2 tests; no new numeric assertions were added inside the skills
   (by design — no executable code forced into analytical skills).
5. Router has one worked demo; no multi-disagreement stress case yet.
