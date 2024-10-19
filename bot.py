import logging
import os
import sys

from discord import Intents
from discord.ext import commands

import trilium


def load_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        sys.exit(f"Missing {name} environment variable")
    return value


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    token = load_required_env("TOKEN")
    triliumUrl = load_required_env("TRILIUM_URL")
    triliumToken = load_required_env("TRILIUM_TOKEN")

    trilium.login(triliumUrl, triliumToken)

    bot_intents = Intents.default()
    bot_intents.messages = True
    bot_intents.message_content = True
    bot = commands.Bot(command_prefix="=", intents=bot_intents)

    @bot.event
    async def setup_hook():
        await bot.load_extension("cogs.notes")
        await bot.tree.sync()

    @bot.event
    async def on_command_error(_, error):
        if isinstance(error, commands.CommandNotFound):
            return
        raise error

    bot.run(token)
