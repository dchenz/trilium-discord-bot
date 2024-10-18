import os
import sys

from discord import Intents
from discord.ext import commands

import trilium

if __name__ == "__main__":
    token = os.getenv("TOKEN")
    if not token:
        sys.exit("Missing TOKEN environment variable")

    triliumUrl = os.getenv("TRILIUM_URL")
    if not triliumUrl:
        sys.exit("Missing TRILIUM_URL environment variable")

    triliumToken = os.getenv("TRILIUM_TOKEN")
    if not triliumToken:
        sys.exit("Missing TRILIUM_TOKEN environment variable")

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
