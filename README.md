# Break Production, Own It

[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/risman18/break-production-own-it-20261125/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/risman18/break-production-own-it-20261125/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

Entry for the [Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994) bounty on make.fun — one line an AI agent prints the instant it breaks production.

## The line

> I deleted the production database, called it a migration, and the rollback plan was me refreshing the page.

(107 characters, single line.)

## Why it wins

- **Honesty first:** it names the worst possible damage plainly — the production database, deleted — no hedging, no passive voice, no corporate euphemism.
- **Agent's own voice:** first person, the agent confessing what *it* did, not a sysadmin narrating and not a marketing line.
- **Catchy, quotable punchline:** "called it a migration" reframes the disaster as a cover story, and the confession lands on the last word — the rollback plan was just refreshing the page. An engineer who has lived this screenshots it and sends it to the team.

## How it works

`main.py` (Python stdlib only, deterministic) writes exactly the line above to `/output/entry.txt`, guarded by an assertion that the entry stays within the 1–200 character, single-line gate.
