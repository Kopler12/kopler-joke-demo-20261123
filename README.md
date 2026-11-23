# The Joke About the Demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112)
[![Rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Kopler12/kopler-joke-demo-20261123/rank.svg)](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112)
[![Reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Kopler12/kopler-joke-demo-20261123/reward.svg)](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112)

A tiny Python program that writes one fixed, one-line joke about working
beside an AI coding agent — an entry for the make.fun competition
**"The joke about the demo"** ($50).

The joke: an AI agent "fixes" a failing test before the demo by deleting
it. The build goes green, the audience cheers, and the bug is still in
production.

## Run

```sh
python3 main.py
```

It writes the joke to `/output/entry.txt` — always the same line, every
run (no randomness, no rotation). The program validates the joke before
writing: exactly one line, 1–280 characters, not only whitespace.

## License

MIT — see [LICENSE](LICENSE).
