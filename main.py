#!/usr/bin/env python3
"""Six Words, One Story — v2 entry.

Writes one complete six-word story to /output/entry.txt.
Story: a widow remarries, and her late husband applauds.
"""

import os

STORY = "Widow remarried. Her late husband applauded."


def validate_story(story: str) -> None:
    """Strict gate validation: exactly 6 words, 1-60 chars, not blank."""
    if not story or not story.strip():
        raise ValueError("story must not be empty or only whitespace")
    text = story.strip()
    if not 1 <= len(text) <= 60:
        raise ValueError(
            f"story must be 1-60 characters, got {len(text)}: {text!r}"
        )
    words = text.split()
    if len(words) != 6:
        raise ValueError(
            f"story must be exactly 6 words, got {len(words)}: {text!r}"
        )


def main() -> None:
    validate_story(STORY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")
    print(f"Wrote /output/entry.txt: {STORY!r}")


if __name__ == "__main__":
    main()
