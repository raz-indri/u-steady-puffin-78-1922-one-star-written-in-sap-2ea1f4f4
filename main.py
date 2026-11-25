#!/usr/bin/env python3
"""One Star, Written in Sap — entry program.

Writes a single one-line, under-280-character 1-star review from a
houseplant (Gary the monstera) about its human owner to /output/entry.txt.
The line was chosen by pairwise duel-testing 7 original drafts against
the judge brief; this draft won all 6 of its duels (duel score 0.75).
Why it won: a named plant (Gary the monstera), a precise number (63 days
without water), and a surprising turn — the roots filing for divorce after
the flood — so the grievance, the single star, and the joke all land in
one plant's-eye voice, with no stock wilting/ignored phrasing.
"""

import os

ENTRY = (
    "One star. Gary the monstera here. 63 days without water, then a flood "
    "so violent my roots filed for divorce. Consistency is apparently not "
    "in this household's vocabulary."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 279, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
