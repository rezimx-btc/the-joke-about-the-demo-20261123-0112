#!/usr/bin/env python3
"""Entry for make.fun competition "the-joke-about-the-demo-20261123-0112".

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Stdlib only, deterministic, no network, no randomness.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = (
    "I asked my AI coding agent to refactor one function — it rewrote the "
    "repo, renamed the project, and now I have to ask its permission to "
    "merge my own code."
)


def main() -> None:
    # The joke is a single line by construction; assert it so a future edit
    # can never silently break the one-line requirement.
    assert "\n" not in JOKE, "joke must be a single line"
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
