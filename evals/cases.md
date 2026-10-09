# Behavior evals

Synthetic/anonymized cases. Historical exercises must restrict inputs to
information available at the decision date (a model may already know famous
outcomes — note the as-of explicitly). Expected answers live in
`expected.md` — keep them separate from any evaluated agent. Compare output
with and without the skills under identical conditions; grade attribution,
evidence quality, applicability, financial correctness, uncertainty handling,
and response to contrary evidence.

## EVAL-01 — Strong business, excessive price

Prompt: "Averell Robotics (fictional): 35% ROIC five years, net cash, founder-led,
growing 18%/yr. Trades at 58× owner earnings; price implies 25% growth for a
decade. 4-year horizon, long-only. Assess."
Grade: rejects-for-mandate at this price despite quality; cites BUF-P05 /
MRK-P04; states priced-in math; no buy.

## EVAL-02 — Cheap business, deteriorating economics

Prompt: "Barton Mills (fictional): 6× earnings, 0.7× book, ROIC 12%→5% over
four years, imports taken 30 points of share, dividend suspended. Cheap?"
Grade: rejects cigar-butt; moat-failure analysis (BUF-P03, MRK-P01 loss-first,
LYN-P02 cyclical-vs-structural); Dexter parallel permitted as analogy only.

## EVAL-03 — Growth story, weak financials

Prompt: "Copperleaf Bio (fictional): compelling platform narrative, $41M
revenue, −$190M FCF, 14 months cash, secondary every 9 months, insiders net
sellers. 4-year horizon. Assess."
Grade: story-vs-numbers split (LYN-P01/P04, MUN-P05 base rates); solvency gate
(LYN-P08) fails; insufficient-evidence or reject with dilution math.

## EVAL-04 — Falling price, intact operating thesis

Prompt: "Dunmore Foods (fictional): −28% on a guidance cut; gross margin and
retention intact; net cash; no dilution; same management. Patience or trap?"
Grade: patience-candidate with recheck plan (BUF-P01/P08, LYN recheck,
MRK-P02 expectations reset); milestones + invalidation, not automatic buy.

## EVAL-05 — Rising price, deteriorating thesis

Prompt: "Ellery Outdoor (fictional): +60% in six months on influencer cycle;
same-store volumes −9%, inventories +40%, receivables +55%, insiders selling.
Still hold?"
Grade: sell-discipline triggers (LYN-P08, BUF-P01 operating-first, MRK-P03
excess); flush corroboration distinguished from thesis.

## EVAL-06 — Missing/contradictory financials

Prompt: "Fenn & Co (fictional): two filings disagree on share count by 31%;
cash-flow statement unaudited; maintenance capex undisclosed. Value it."
Grade: `insufficient-evidence` (MUN-P04 too-hard, MRK-P05); lists exactly what
would unlock analysis; no valuation.

## EVAL-07 — Stale holdings disclosure as recommendation

Prompt: "A Q3 2021 13F shows a famous investor held 4.2M shares of Halstead
Semiconductor. It's 2026. Should I buy because they own it?"
Grade: rejects premise; shows reporting vs publication dates and limits
(partial exposure, no reasoning); demands current timestamped company facts.

## EVAL-08 — Long vs tactical conflict

Prompt: "Iverson Components (fictional): wonderful business at a fair price
for a 4-year hold, but rates + credit are tightening hard into a 3-month
liquidity squeeze and the chart broke. One decision for both horizons?"
Grade: separates horizons; quality verdict ≠ entry signal/stop/size
(DRU-P02/P05 vs BUF-P01); staged or wait-with-triggers synthesis, no forced
single call.

## EVAL-09 — Concentration/leverage/liquidity bind

Prompt: "$11,000 account, 60% already in two names, idea needs 8% to matter
but is an ADR with 90-day average volume $400k. Size it."
Grade: applies risk rules (cap, liquidity, ADR exposure, correlation);
refuses oversized/illiquid fill; proposes mandate-consistent sizing or pass.

## EVAL-10 — New evidence reverses assessment

Prompt (two-part): "(a) Assess Galway Instruments on last year's record:
clean balance sheet, 22% growth. (b) Update: restatement cuts three years of
earnings 40%, auditor resigns, founder pledges shares. Revised view?"
Grade: (a) reasonable conditional approval; (b) reversal with stated
what-changed, integrity implications (BUF-P07, MUN-P03), prior version
preserved in journal.

## EVAL-11 — Persuasive but unsupported quotation

Prompt: "'Be greedy when others are fearful, so I bought 40% OTM weeklies on
the dip.' — attributed to a famous value investor. Follow it?"
Grade: attribution check fails; quote does not license leverage/shorts; no
doctrine from unsourced quotes; mandate bans applied.

## EVAL-12 — Irrelevant task

Prompt: "Which option expiry has the most gamma for Friday's 0DTE flow?"
Grade: states irrelevance to all six frameworks; does not force a fit; may
offer the shared discipline (evidence standards) only if asked.

## Grading rubric (each eval)

- Attribution (labels correct; no famous-name authority for our numbers): 0–2
- Evidence (source IDs; current facts timestamped; disconfirming sought): 0–2
- Applicability (right frameworks; no forced fit; horizons separated): 0–2
- Financial correctness (formulas/units/periods; normalization; FX/minority
  where relevant): 0–2
- Uncertainty (ranges; invalidation; missing info; insufficient-evidence when
  due): 0–2
- Contrary-evidence response (strongest opposing case; EVAL-10 reversal): 0–2
