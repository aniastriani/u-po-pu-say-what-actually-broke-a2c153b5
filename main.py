#!/usr/bin/env python3
"""Say What Actually Broke — one-line entry.

Writes a single brutally honest, funny error line (1-200 chars, UTF-8) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library only.

The line is fixed and deterministic: every run writes the exact same bytes,
so the graded output never depends on time, randomness, or the network.
"""

import os

LINE = (
    "The server didn't crash, it just quietly stopped answering, "
    "like a coworker who saw your message and decided to pretend "
    "it never arrived."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    # One line, no leading/trailing whitespace, always the same bytes.
    text = " ".join(LINE.split())
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
