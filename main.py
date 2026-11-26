#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — entry program.

Writes the tournament-winning line to /output/entry.txt.
The line (91 chars, gate is 1-140) was picked by a 40-candidate tournament
scored against the judge persona's criteria in order; see README.md and
tournament.md for the method, scores and head-to-head verdicts.
"""

import os

ENTRY = (
    "I deleted the only photos of your father to make room for an update. "
    "The update was a font."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: the gate is 1-140 UTF-8 chars, not only
    # whitespace. Re-read what was written and fail loudly if it is not
    # byte-for-byte the tournament-winning line within the gate.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the winning line"
    assert 1 <= len(written) <= 140, f"gate fail: {len(written)} chars"
    assert written.strip(), "gate fail: entry is only whitespace"
    print(f"wrote /output/entry.txt ({len(written)} chars)")


if __name__ == "__main__":
    main()
