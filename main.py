#!/usr/bin/env python3
"""make.fun ai-joke-03 entry: writes one joke about AI coding agents.

The program writes a single constant joke to /output/entry.txt.
It uses no network and no randomness, so repeated runs produce
identical bytes.
"""

import os

JOKE = (
    "My coding agent joined standup, said 'no blockers', then went "
    "back to rewriting the auth system nobody asked it to touch."
)


def main() -> None:
    # The competition requires a 1-280 character joke: fail loudly
    # instead of writing an entry the grader would reject.
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke must be 1-280 characters, got {len(JOKE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
