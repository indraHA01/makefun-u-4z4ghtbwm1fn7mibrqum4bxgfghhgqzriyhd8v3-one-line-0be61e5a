#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set).

Deterministic: no network, no randomness, no input. The line is a
fixed string, validated here against the gate (1-140 UTF-8
characters, one line, not only whitespace) before it is written.

Run: python3 main.py
"""

import os
import sys

# The line. The angle: a fitness tracker celebrates an athletic
# achievement that turns out to be pure couch-potato behaviour.
# "Praised my 10,000 steps" sets up a workout; the reveal — an
# afternoon spent hunting for the TV remote — knocks it flat.
# The joke lives entirely in the gadget's own world (steps, praise,
# the remote) and the punch lands in the last words. No pun, no
# setup that gives itself away, no worn "my wife / my therapist /
# the Wi-Fi password" move: the watch is the straight man and the
# remote is the twist.
ENTRY = (
    "My smartwatch praised my 10,000 steps \u2014 I'd spent the "
    "afternoon hunting for the TV remote."
)

MAX_CHARS = 140


def output_path() -> str:
    """Where the entry goes: the harness dir, or /output by default."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def validate(text: str) -> None:
    """Gate check, mirroring the sealed scorer: 1-140 chars, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if text != text.strip():
        raise ValueError("entry has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> int:
    validate(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
