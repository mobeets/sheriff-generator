
Auto-generate a sheriff emoji given a list of keywords. You can either provide a list of emoji aliases from the list [here](https://www.webpagefx.com/tools/emoji-cheat-sheet/), or provide a word like `cat' which will return all emojis with an alias including that word.

Sadly, there is not yet support for the sheriff emoji, so I'm using a policeman instead.

Also, a joke will be provided by searching for a definition on Urban Dictionary. (Warning: may be explicit and/or not funny.)

__Examples__:

```bash
$ python sheriff.py dog


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
$ python sheriff.py :cactus: :heart:

   👮
  🌵🌵🌵
 🌵 🌵 🌵
👇  ❤❤ 👇
  ❤  ❤
  ❤  ❤
  👢  👢  
Howdy, I'm the sheriff of cactus. Dead, not functioning.
```

__Install requirements__:

```
pip install emoji
pip install urbandictionary
```
