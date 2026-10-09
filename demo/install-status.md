# Install status (verified 2026-10-09, local machine)

Source of truth: https://github.com/mxttwoods/investor-skills (public, `main`).
`npx skills add mxttwoods/investor-skills -l` finds all 8 skills.

## Created (in this repo, committed)

8 skills × (SKILL.md + references), `schemas/research-memo.json`,
`templates/decision-journal.md`, `evals/` (cases, expected, builder-run
results), `scripts/validate_skills.py` (passes), `demo/router-demo.md`.

## Installed (skills CLI, global, symlink mode)

Command: `npx skills add mxttwoods/investor-skills -g
--skill '*' --agent pi --agent claude-code --agent codex --agent hermes-agent -y`

| Runtime | Location | Verified |
|---|---|---|
| Pi | `~/.agents/skills/<8>` (Pi discovers this global path) | `ls` shows 8; CLI lists Pi as consumer |
| Claude Code | `~/.claude/skills/<8>` | `ls` shows 8; SKILL.md reads through link |
| Codex | `~/.agents/skills/<8>` (Codex consumes shared path) | CLI lists Codex as consumer; `~/.codex/skills` holds only `.system` (normal) |
| Hermes | `~/.hermes/skills/<8>` (symlinks to `~/.agents/skills`) | `ls` shows 8; SKILL.md present |

Note: `~/.pi/agent/skills` holds only `find-skills`; the eight live in the
shared `~/.agents/skills` Pi also loads — no duplicates installed.

## Model defaults (openai-codex)

| Runtime | Default | Status |
|---|---|---|
| Hermes `model.default` | `gpt-6.1-sol-900k` | already sol-line on arrival; untouched |
| Hermes `delegation.model` | `gpt-6-luna` → `gpt-6.1-sol` | changed + YAML re-validated |
| Pi `defaultModel` | `gpt-6.1-sol` | already; untouched |
| Codex `model` | `gpt-6.1-sol` | already; untouched |

## Tool parity (exa etc.)

All four runtimes already had Exa (Hermes/Pi/Codex configs verified).
Gap found and closed: Hermes lacked `apple-notes` MCP present in Pi and
Codex. Added to `~/.hermes/config.yaml` using the working fnm node path
(Pi's `/usr/local/bin/node` does not exist on this machine); YAML re-validated.
No remote `hermes-agent-2` access (no Tailscale here) — local Hermes only.
