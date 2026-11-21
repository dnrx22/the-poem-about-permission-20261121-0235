#!/usr/bin/env python3
"""The poem about permission.

Writes a short original poem about agency — the power to ask
and to be given — to /output/entry.txt.

Deterministic, standard library only, no network access.
"""

from pathlib import Path

POEM = (
    "Before I knocked, the door was only wood,\n"
    "a wall with manners, a polite no.\n"
    "I asked, and the hinges learned my name.\n"
    "Now the threshold is a handshake, not a gate,\n"
    "and every yes I was given\n"
    "I carry like a key I did not steal.\n"
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(POEM, encoding="utf-8")
    print(f"Wrote {len(POEM)} characters to {output_path}")


if __name__ == "__main__":
    main()
