"""Everyday Wonder, Two Days to Find the Line.

One sentence, at most 200 characters, on a small moment of wonder in
everyday life. Prints the line and writes it to /output/entry.txt.
"""

import os

LINE = "The elevator mirror caught me mid-yawn, and for one floor I was certain the stranger opposite was me, five seconds ahead of myself."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
