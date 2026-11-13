# Contributing to MAG.PY

## Who can help?
Start here. Ask Charles or a bot exec on Discord for setup, bot tokens, or if you're stuck:
- @cq0776 (Charles)
- @silverdefault. (Gary)
- @conc4veh3ad (Zakery)
- @dimpl3 (Weikai)
- @hawllowed (Jade)

## Where do I start?
1. Pick a small item from the Planned list in the [README](README.md). Or if you have a new idea, bring it to Charles
2. Post what you're working on in the discord-bot-dev channel in UCSEC Planning.
3. Create a branch (or fork the repo), then open a pull request and wait for a review before merging.

## What's a cog?
A cog is a Python file that adds commands to the bot, and groups related commands together. When the bot starts, it loads every cog listed in `EXTENSIONS` in `bot.py` and runs its code.

## Adding a New Command

Each feature lives in its own cog:

To add a command:
1. Create `my_feature.py` in the `cogs` folder. Copy `qr_code.py` as a template.
2. Add `"cogs.my_feature"` to `EXTENSIONS` in `bot.py`.