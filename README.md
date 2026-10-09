# investor-skills

A collection of reusable agent skills that translate the **documented** methods of
exceptional investors into procedures an investing agent can apply, challenge, and
evaluate. Interpretation of documented methods — not impersonation, not advice, and
not a claim of edge.

Installable with the skills CLI (`npx skills`) and loadable directly by
Claude Code, Pi coding agent, OpenAI Codex, and Hermes.

## Skills

| Skill (directory) | What it contributes |
|---|---|
| `skills/buffett-business-quality` | Business ownership, economic quality, owner earnings, moats, capital allocation, patience, price discipline |
| `skills/munger-mental-models` | Latticework of models, incentives, inversion, competence boundaries, temperament, checklists |
| `skills/lynch-growth-stories` | Six categories, two-minute story, PEG/famous numbers, observational edge with verification, sell discipline |
| `skills/marks-risk-and-uncertainty` | Risk as permanent loss, second-level thinking, cycles/pendulum, price vs value, forecasting limits, offense/defense |
| `skills/druckenmiller-macro-adaptation` | Regime change, liquidity first, asymmetry + concentration, fast reversal, multi-asset expression (tactical, short-horizon) |
| `skills/nomad-long-duration` | Scale-economies-shared, stakeholder generosity, destination analysis, concentration + inaction (joint Sleep + Zakaria attribution) |
| `skills/research-risk-discipline` | Shared research output (memo + JSON), risk limits, journaling, revision rules |
| `skills/investor-router` | Selects relevant frameworks, keeps analyses inspectable, reconciles evidence, preserves disagreement |

Expansion list (not yet built): Graham, Fisher, Greenblatt, Klarman, Pabrai,
Soros, Smith. A new framework is added only when it contributes a distinct,
adequately sourced method.

This is **not** a ranking of the best investors.

## Install

```bash
# skills CLI, project scope (from any project dir)
npx skills add mxttwoods/investor-skills --skill '*' --agent '*' -y

# global install
npx skills add mxttwoods/investor-skills -g --skill '*' --agent '*' -y

# list what the repo offers without installing
npx skills add mxttwoods/investor-skills -l
```

Manual paths (the repo layout is the portable form: directory containing `SKILL.md`):

| Runtime | Project scope | Personal scope |
|---|---|---|
| Claude Code | `.claude/skills/<name>/SKILL.md` | `~/.claude/skills/<name>/SKILL.md` |
| Pi coding agent | `.pi/skills/<name>` or `.agents/skills/<name>` | `~/.pi/agent/skills/<name>` or `~/.agents/skills/<name>` |
| Codex | link repo `skills/*` into skills path | `~/.codex/skills/<name>` |
| Hermes | link into `~/.hermes/skills/<name>` | same |

`SKILL.md` frontmatter (`name`, `description`) follows the Agent Skills spec and
works in all four runtimes. References are loaded on demand via relative paths.

## Evidence standard

Principle sources are ranked:

1. Original shareholder/partnership letters
2. The investor's own books, essays, memos
3. Original interviews, speeches, Q&A
4. Filings and contemporaneous records
5. Reputable biographies/secondary analysis (labeled)

Every skill carries `references/sources.md`: stable source ID, author/title/date,
event date where different, URL or local reference, page/section/timestamp,
supported claim, firsthand-or-secondary status, access limits. Statements are
labeled **Documented principle**, **Interpretation**, or **Implementation choice**.
Search snippets and quote collections are discovery aids only.

Quotations are short and attributed; nothing reproduces books, letters, or
transcripts wholesale. Gaps are recorded in `sources.md` instead of invented.

## Configuration

Holding period, asset universe, portfolio constraints, and execution policy are
**implementation choices** set by the user, not doctrines of any investor:

```json
{
  "mandate": {
    "assets": ["US-listed equities"],
    "horizon_years": [3, 5],
    "style": "long-only, no leverage, no shorts, no options",
    "position_count": [10, 20],
    "max_position_pct": 10,
    "risk_limits": "see skills/research-risk-discipline/SKILL.md"
  }
}
```

The router binds every synthesis to the configured mandate. Research skills never
grant order-placement permission.

## Layout

```
skills/<name>/SKILL.md                  # trigger, workflow, output contract
skills/<name>/references/worldview.md   # person behind the method
skills/<name>/references/principles.md  # operational principle records
skills/<name>/references/cases.md       # decisions, mistakes, counterexamples
skills/<name>/references/sources.md     # source ledger
schemas/research-memo.json              # machine-readable memo
templates/decision-journal.md           # decision record template
evals/cases.md                          # behavior evals (prompts + separate answers)
scripts/validate_skills.py              # structural + evidence validation
demo/router-demo.md                     # worked router demonstration
```

## Status

- Created in this repo: 8 skills (6 investor + 1 shared + 1 router), schema,
  journal template, 12 eval cases, validator, demo.
- Installed: see demo/install-status.md for the verified per-runtime record.
- Validation: `python3 scripts/validate_skills.py` (structural). Behavior evals in
  `evals/` with expected answers kept separate from the skills.
- Returns claims: none. Skill-behavior tests do not establish profitable
  performance; any returns claim needs point-in-time data, costs, benchmarks,
  and look-ahead/survivorship controls.
