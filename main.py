#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes a single line to /output/entry.txt. Pure stdlib, deterministic.
Gate: the file must be UTF-8 text of 1 to 140 characters, not only
whitespace (RULES.txt).
"""

import os

LINE = (
    "I resign as office fire marshal, effective immediately \u2014 "
    "after five years of showing everyone else the exits, "
    "I've finally found my own."
)

MAX_CHARS = 140


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            f"line is {len(LINE)} chars, gate allows 1-{MAX_CHARS}"
        )
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
