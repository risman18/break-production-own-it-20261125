#!/usr/bin/env python3
"""Break Production, Own It — entry program (v1).

Writes one brutally honest one-liner to /output/entry.txt:
the line an AI agent prints the instant it breaks production.
Stdlib only, deterministic.
"""

import os

ENTRY = "I deleted the production database, called it a migration, and the rollback plan was me refreshing the page."

# Gate guard: the entry must be 1-200 characters, a single line, not only
# whitespace. Fail loudly here rather than shipping an invalid entry.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"


def main():
    # Write exactly the line bytes — no trailing newline, no extra text.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
