"""One-line review of the most boring everyday object: a rubber band.

Writes the review to /output/entry.txt (UTF-8, single line, 1-200 chars).
"""

import os

ENTRY = "This rubber band has held the same three pens together since 2019 and still thinks it's doing important work."


def main():
    if not ENTRY.strip():
        raise ValueError("ENTRY must not be blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("ENTRY must be a single line")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"ENTRY must be 1-200 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
