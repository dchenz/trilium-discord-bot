import os
import sys

from discord import Intents
from discord.ext import commands

if __name__ == "__main__":
    token = os.getenv("TOKEN")
    if not token:
        sys.exit("Missing TOKEN environment variable")

    bot_intents = Intents.default()
    bot_intents.messages = True
    bot_intents.message_content = True
    bot = commands.Bot(command_prefix="=", intents=bot_intents)

    @bot.event
    async def on_command_error(_, error):
        if isinstance(error, commands.CommandNotFound):
            return
        raise error

    bot.run(token)
