# The Excuse That Almost Works

One line of plain text — the excuse a gamer texts the boss to skip work
on GTA 6 launch week — written by a program for the [The Excuse That
Almost Works](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
bounty on make.fun.

[![Bounty](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![Rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/freysiatiara/excuse-that-almost-works-20261125/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![Reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/freysiatiara/excuse-that-almost-works-20261125/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

## The line

> My washing machine flooded the kitchen at 6am and I'm mopping up before it reaches the neighbour downstairs.

## How it works

`main.py` (Python, standard library only) writes the line above to the
entry file. The output path is resolved from `ENTRY_OUTPUT`, then
`OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR`, then `/output/entry.txt`, falling back
to a file beside the script. The program validates the line against the
bounty's gate (1–140 characters, not only whitespace, one line, at most
20 words) before writing, and writes with plain `open()` plus
`os.chmod(path, 0o644)`, with no trailing newline.

Run it:

```sh
python3 main.py
```
