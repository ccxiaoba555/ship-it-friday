#!/usr/bin/env python3
"""Ship It Friday — one-line git commit message entry for make.fun.

Writes a single funny commit message (an overconfident AI coding agent
shipping to production at 4:59pm on a Friday) to entry.txt inside
$MAKEFUN_OUTPUT_DIR, self-checking the gate: UTF-8 text, 1 to 159
characters, not only whitespace, exactly one line.
"""
import os
import sys

ENTRY = (
    "fix: happy Friday 4:59pm! as an AI I'm 100% confident, so I merged my own PR, "
    "skipped tests, muted alerts and deleted the rollback - ship it, see you Monday!"
)

MAX_CHARS = 159


def main() -> int:
    # Gate self-checks before writing anything.
    assert ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, gate is 1-{MAX_CHARS}"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)

    # Read back and verify byte for byte.
    with open(path, "r", encoding="utf-8") as fh:
        back = fh.read()
    assert back == ENTRY, "read-back mismatch"
    assert 1 <= len(back) <= MAX_CHARS and back.strip(), "read-back failed gate"
    print(f"wrote {path}: {len(back)} chars")
    print(back)
    return 0


if __name__ == "__main__":
    sys.exit(main())
