"""Write one line to my younger self into /output/entry.txt."""

import os

ENTRY = "Don't throw away her letters, you will read them at 3 a.m. in a house you can't afford, looking for the boy she loved."


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if ENTRY.count("\n"):
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
