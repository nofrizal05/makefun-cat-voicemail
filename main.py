#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one line, the funniest voicemail greeting a cat would record,
to /output/entry.txt. Standard library only.

The joke: the cat opens like a normal voicemail greeting, then instantly
pleads innocent about the vase — a classic cat crime, denied in the
cat's own defiant voice, with the punch landing before the beep.
"""

import os

LINE = "You've reached the cat. If this is about the vase, I deny everything. Leave a message."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
