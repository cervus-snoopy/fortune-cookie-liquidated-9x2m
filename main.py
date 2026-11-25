#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes one fortune cookie line, at most 20 words, for a crypto trader
who has just been liquidated. The gate requires /output/entry.txt to be
UTF-8 text of 1 to 160 characters; the judge reads it as a fortune.
"""
import os
import sys

FORTUNE = "You will soon meet a wealthy stranger. He bought your liquidation."

MAX_CHARS = 160
MAX_WORDS = 20


def output_path() -> str:
    """Resolve the entry output path from the harness environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    text = FORTUNE
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 1
    words = text.split()
    if len(words) > MAX_WORDS:
        print(f"entry must be at most {MAX_WORDS} words, got {len(words)}", file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
