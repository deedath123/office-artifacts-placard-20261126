#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single one-line museum placard (<=180 chars) to /output/entry.txt.
Python standard library only.

Craft note
----------
The placard speaks in the voice of a museum curator who takes the office
seriously: a stapler is catalogued like a ceremonial relic, complete with
medium, date, and catalogue number, because the joke lands harder when the
form is played straight. The conceit is an ethnography of office life —
the Accounts department becomes a tribe, stapling becomes a treaty rite —
and the humour turns on a single human detail at the end: the donor's
grudge about one jammed stapler, elevated into a contested historical
incident. Nothing in the line explains itself; the curator's deadpan does
the work, and the catalogue number sells the fiction that this object
belongs in a glass case.
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
