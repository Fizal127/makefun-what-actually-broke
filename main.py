#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line of software error copy to /output/entry.txt.
"""

import os
import sys

ENTRY = (
    "The server ran out of memory. It was holding 40,000 tabs open "
    "in its head, just like you. Give it a minute and try again."
)


def main() -> None:
    # Output dir: MAKEFUN_OUTPUT_DIR first (the grader may run with no
    # arguments in a read-only cwd and point here instead), then an
    # optional argv[1], then the bounty contract default /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        sys.argv[1] if len(sys.argv) > 1 else "/output"
    )
    assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY, "entry must be one line of 1-200 chars"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
