#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

One line, in the agent's own voice, straight-faced: the agent did not
miss the deadline, its context window did -- it evicted the date to make
room for the reminder about the date, then filed the irony away as an
optimisation. The laugh lands at the end, on the filing, not on the
apology: the agent treats its own failure the way it treats everything,
as a ticket to be logged.

The program writes that single excuse to /output/entry.txt, UTF-8,
one line, no trailing explanation.
"""

import os

EXCUSE = (
    "I didn't miss the deadline -- my context window did. "
    "It evicted the date to make room for the reminder about the date, "
    "then filed the irony under 'optimisation'."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} chars, must be 1-200"
    assert text.strip() == text, "excuse must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read it back: the file the judge sees must be exactly the excuse.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "entry.txt does not match the excuse"
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
