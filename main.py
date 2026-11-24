#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt. Stdlib only."""
import os

JOKE = "The office plant is the only thing thriving here — watered once a month, ignored daily, and somehow promoted over people who actually show up."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote /output/entry.txt ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
