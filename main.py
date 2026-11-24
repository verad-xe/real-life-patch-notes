"""Real-Life Patch Notes: The Comedy Changelog — one funny patch note.

Writes exactly one line (at most 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output): a software patch note
for a bug in real life, in the terse register of a real release note.
Deterministic, no input, no network.

Why this line: the bug is specific and instantly recognisable (the
little toe finding a table leg in the dark), the register is dry
engineering ("located ... by direct impact"), and the wince is the
punchline — no setup the joke does not need.
"""

import os

LINE = (
    "v4.3.1: fixed a bug where the little toe, in the dark, located "
    "every table leg by direct impact."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
