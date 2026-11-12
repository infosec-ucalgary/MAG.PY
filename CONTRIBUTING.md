# Contributing to MAG.PY

Thanks for helping improve MAG.PY! This guide covers how to set up the project and submit changes.

## Getting Started

1. Fork the repo and clone your fork
2. Follow the setup steps in the [README](README.md#getting-started)
3. Create a separate Discord application and bot token for testing, and invite it to a private test server

## Making Changes

1. Create a branch from `master`:
   ```bash
   git checkout -b feature/short-description
   ```
2. Make your changes and test them in your test server
3. Commit with a clear message describing what changed and why
4. Push your branch and open a pull request

## Adding a New Command

Each feature lives in its own cog:

1. Create a file in `cogs/` (e.g. `cogs/my_feature.py`)
2. Define a `commands.Cog` class with your slash commands
3. Add an async `setup(bot)` function at the bottom:
   ```python
   async def setup(bot: commands.Bot) -> None:
       await bot.add_cog(MyFeature(bot))
   ```
4. Register it in `EXTENSIONS` in `main.py`:
   ```python
   EXTENSIONS = [
       "cogs.general",
       "cogs.qr_code",
       "cogs.my_feature",
   ]
   ```

## Code Style

- Follow PEP 8
- Use type hints on function signatures
- Keep each cog focused on one feature area

## Pull Request Checklist

- [ ] The bot starts without extension load errors
- [ ] New commands have a clear `description` and `app_commands.describe` text
- [ ] The README is updated if you added a user-facing feature

## Good First Contributions

- Automatic CVE feed: the bot periodically checks for newly published CVEs (vulnerability reports) and posts them to a dedicated channel
- Automatically prefix `https://` when a URL has no scheme
- Add QR code style selection
- Add new general-purpose commands to the `general` cog