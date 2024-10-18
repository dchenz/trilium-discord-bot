from discord import app_commands, Interaction
from discord.ext import commands


class Notes(commands.Cog):

    @app_commands.command(name="list", description="Lists notes")
    async def getList(self, interaction: Interaction):
        await interaction.response.send_message("Not implemented")


async def setup(bot: commands.Bot):
    await bot.add_cog(Notes())
