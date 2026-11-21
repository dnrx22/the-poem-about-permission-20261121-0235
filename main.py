#!/usr/bin/env python3
"""Write a short original poem about permission to the output file.

The poem is about agency: the power to ask, and to be given.
Deterministic, stdlib only, no network.
"""

import os

POEM = (
    "I knocked once. The door, which had been wood,\n"
    "became a question. Someone said come in \u2014\n"
    "and just like that the wall gave way, the room\n"
    "stood wider than my fear. Permission is\n"
    "a hinge: it only moves when someone asks.\n"
    "I asked, and the latch unlearned its rust."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"wrote {path} ({len(POEM)} characters)")


if __name__ == "__main__":
    main()
