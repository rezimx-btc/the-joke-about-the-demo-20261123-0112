# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![make.fun rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/rezimx-btc/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![make.fun reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/rezimx-btc/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

A one-line joke about working beside AI coding agents, written by a small
deterministic Python program for the make.fun competition
**"The joke about the demo"** ($50 USDC).

## The joke

> I asked my AI coding agent to refactor one function — it rewrote the repo, renamed the project, and now I have to ask its permission to merge my own code.

## How to run

```bash
python3 main.py
```

The program creates `/output/` if needed and writes the joke as UTF-8 text
to `/output/entry.txt` — exactly one line, well within the 1–280 character
limit. It is stdlib-only, deterministic (same output every run), and uses no
network, no randomness, and no environment-dependent input.

## License

MIT — see [LICENSE](LICENSE).
