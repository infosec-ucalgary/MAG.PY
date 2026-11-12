# MAG.PY General Function Discord Bot
MAG.PY is a discord bot equipped with general functions to University of Calgary club and school servers

## Current Features
| Command | Description |
|---|---|
| `/create-qr-code <url>` | Convert a URL into a QR code. The result is sent privately (only you can see it). |

## Planned Features

- Automatic CVE feed: the bot periodically checks for newly published CVEs (vulnerability reports) and posts them to a dedicated channel
- Automatic `https://` prefixing for URLs missing a scheme
- QR code style selection

## Setup

Requires Python 3.10+ and a bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

```
git clone https://github.com/infosec-ucalgary/MAG.PY
cd MAG.PY

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
py -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
DISCORD_TOKEN=your-bot-token
BOT_ERROR_CHANNEL_ID=123456789012345678   # optional, reports startup errors
```

Then run:

```bash
python bot.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).