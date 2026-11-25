"""Write the single-line GTA 6 launch-week excuse to the entry file.

The program resolves where to write from the environment first, so it
works both in the grading sandbox and on a developer machine:

  1. ENTRY_OUTPUT, when set.
  2. OUTPUT_DIR or MAKEFUN_OUTPUT_DIR joined with "entry.txt".
  3. The bounty default, /output/entry.txt.
  4. A file called entry.txt next to this script, as a last resort.

Before writing, the line is checked against the bounty's gate: it must be
UTF-8 text of 1 to 140 characters and not only whitespace, and it must be
a single line of at most 20 words. The file is written with a plain
open() call and no trailing newline, then chmodded to 0644.
"""

import os

LINE = "My washing machine flooded the kitchen at 6am and I'm mopping up before it reaches the neighbour downstairs."


def resolve_output_path():
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    out_dir = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def validate(line):
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line) > 140:
        raise ValueError("entry line exceeds the 140-character gate")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line.split()) > 20:
        raise ValueError("entry exceeds the 20-word limit")


def main():
    validate(LINE)
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
