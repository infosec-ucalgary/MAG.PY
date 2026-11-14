# MAG.PY General Function Discord Bot
MAG.PY is a **privacy-focused** general-purpose Discord bot, organized by the tech team at University of Calgary Cybersecurity Club. It goal is to offer server admins a bot that requires minimal user data and omits any after the fact, with (hopefully) clear and robust user terms of service surrounding user data storage practices. Currently, MAG.PY does not store any user-data outside of Discord's own first-party data storage practices.

## Current Features
- Converts strings to basic mono-tone QR codes

### Improvements
- [`/cogs/qr_code.py`](cogs/qr_code.py)
  - URL input sanitation
  - Automatic `https://` prefixing for URLs missing a scheme
  - QR code style selection

### Planned features
- Automatic CVE feed
- Role assigning feature
- Audio bot
- Per-server birthday record-keeper
- Robust error logging
- User-data storage disclosure