#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single one-line museum placard (<=180 chars) to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = (
    "Stapler, steel, c. 1997. The Accounts tribe bound treaties with a single "
    "rite; donor Gary still insists the jam of March 3rd was sabotage, not "
    "user error. Cat. No. 0417."
)


def main() -> None:
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be blank"
    assert len(ENTRY) <= 180, "entry exceeds 180 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
