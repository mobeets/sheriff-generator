Auto-generate a sheriff emoji given a list of keywords. You can either provide a list of emoji aliases from the list [here](https://www.webpagefx.com/tools/emoji-cheat-sheet/), or provide a word like `cat' which will return all emojis with an alias including that word.

Sadly, there is not yet support for the sheriff emoji, so I'm using a policeman instead.

Also, a joke will be provided by searching for a definition on Urban Dictionary. (Warning: may be explicit and/or not funny.)

## Setup

Prerequisites: python 3.8 and the `poetry` tool.

```
$ poetry install
```

**Examples**:

```bash
$ poetry run python sheriff.py dog


   👮
  🐶🐶🐶
 🐕 🐶 🐕
👇  🌭🌭 👇
  🌭  🌭
  🌭  🌭
  👢  👢

Howdy, I'm the sheriff of dog. Not a [cat].
```

```bash
$ poetry run python sheriff.py money

   👮
  🤑🤑🤑
 💰 🤑 💰
👇  💸💸 👇
  💸  💸
  💸  💸
  👢  👢
Howdy, I'm the sheriff of money. The root of all evil].
```
