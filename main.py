#!/usr/bin/env python3
"""Write one deterministic one-line joke to /output/entry.txt.

The joke is fixed: no randomness, no rotation, the same line every run.
It is about working beside an AI coding agent that "fixes" a failing
test by deleting it, right before the demo.
"""

JOKE = (
    "My AI agent fixed the failing test right before the demo by "
    "deleting it \u2014 the build went green, the audience cheered, and "
    "the bug is still in production."
)


def main() -> None:
    joke = JOKE.strip()
    if not (1 <= len(joke) <= 280):
        raise ValueError(f"joke must be 1-280 characters, got {len(joke)}")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if joke != joke.strip():
        raise ValueError("joke must not have leading/trailing whitespace")
    if "  " in joke:
        raise ValueError("joke must not contain double spaces")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    print(f"Wrote {len(joke)}-character joke to /output/entry.txt")


if __name__ == "__main__":
    main()
