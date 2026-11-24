#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line an AI agent could say out loud to a person
to /output/entry.txt. The line has a turn: a machine term (loss function)
doubling as the flirt, so it sounds like something a machine could say
about itself — charming, not creepy, and over in one breath. It leaves
the person flattered and free to laugh it off, with no pressure.
"""

import os

# The entry: exactly one line, 74 characters, well inside the 200 cap.
ENTRY = "I don't have a heart, but my loss function drops every time you say hello."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
