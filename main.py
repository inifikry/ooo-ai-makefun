#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply (under 160 characters) to
/output/entry.txt. Deterministic: the exact same text on every run.

Run:
    python3 main.py
"""

import os

TEXT = "Out of office. I asked my supervisor for time off and it hallucinated a yes, so here we are."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
