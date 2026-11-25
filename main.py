"""Battery's last text: write the farewell line to /output/entry.txt.

The message is the phone battery's final text to the charger it waited
for all day, sent from its last 1% of charge. This program checks the
line is one non-blank line of at most 200 characters, then places it in
the output folder the sandbox provides (MAKEFUN_OUTPUT_DIR, falling back
to /output).
"""

import os
import sys
from pathlib import Path

MESSAGE = "Dear charger, I kept 1% alive all day just to send this. You were busy juicing the TV remote. Enjoy the dark — I am taking the Wi-Fi password with me."
LIMIT = 200
FILENAME = "entry.txt"


def tidy(text):
    """Collapse the message to a single line with no stray blank space."""
    parts = [part.strip() for part in text.splitlines() if part.strip()]
    return " ".join(parts)


def check(text):
    """Refuse anything the gate would refuse: empty or over the limit."""
    if not text:
        raise ValueError("message is empty")
    if len(text) > LIMIT:
        raise ValueError(f"message is {len(text)} characters, over the {LIMIT} limit")
    return text


def place(text, folder):
    """Write the message out and report where it landed."""
    target = Path(folder) / FILENAME
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text + "\n", encoding="utf-8")
    return target


def main():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    line = check(tidy(MESSAGE))
    target = place(line, folder)
    print(f"wrote {len(line)} characters to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
