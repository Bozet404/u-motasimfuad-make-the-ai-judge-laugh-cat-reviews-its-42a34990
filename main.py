#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one single-line one-star review, written by a house cat about
its human, to /output/entry.txt. The line is fixed and deterministic:
the same text on every run.
"""

import os

REVIEW = (
    "One star. The food bowl sat empty for nine whole minutes, the lap "
    "closed without warning, and the human typed on MY keyboard all "
    "afternoon. I filed a complaint with management. I am management."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
