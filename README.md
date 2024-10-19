# Trilium Discord Bot

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This is a Discord bot that interacts with Trilium ETAPI. It's designed for self-hosting and is meant to be used in a private Discord server where you're the only member.

The idea is to use Discord as a reverse proxy to access a Trilium instance hosted on your home network, without needing open router ports or a VPN. This setup is handy for taking notes directly through Discord when you're not at home.

## Requirements

- Python: 3.10.12
- Dependencies: Install with `pip install -r requirements.txt`
- You'll need your own [Discord developer account](https://discord.com/developers/applications).

## Environment variables

Before running the bot, ensure the following environment variables are set:

- `TOKEN`: Your Discord bot token.
- `TRILIUM_URL`: Your Trilium instance URL. The HTTP path must be `/etapi`.
- `TRILIUM_TOKEN`: Your Trilium ETAPI token. Create one by going to "Options > ETAPI > Create new ETAPI token".

## Running the bot

```sh
export TOKEN="your_discord_token"
export TRILIUM_URL="your_trilium_url"
export TRILIUM_TOKEN="your_trilium_token"

python3 bot.py
```

## Development

### Linting

This project uses [Ruff](https://github.com/astral-sh/ruff) for linting. You can find the configuration in `ruff.toml`.

```sh
pip install ruff

ruff check

ruff format
```

### Dependencies

This project uses [pipreqs](https://github.com/bndr/pipreqs) to generate the `requirements.txt` file.

```sh
pip install pipreqs

./scripts/generate-requirements.sh
```
