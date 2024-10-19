from discord import Guild, Interaction, Message, NotFound
from discord.abc import Messageable


async def findMessageInChannel(
    messageId: int,
    channel: Messageable,
) -> Message | None:
    try:
        return await channel.fetch_message(messageId)
    except NotFound:
        return None


async def findMessageInGuild(messageId: int, guild: Guild) -> Message | None:
    for channel in [*guild.channels, *guild.threads]:
        if not isinstance(channel, Messageable):
            continue
        message = await findMessageInChannel(messageId, channel)
        if message:
            return message
    return None


async def findMessage(messageId: int, interaction: Interaction) -> Message | None:
    if isinstance(interaction.channel, Messageable):
        message = await findMessageInChannel(messageId, interaction.channel)
        if message:
            return message
    if interaction.guild:
        return await findMessageInGuild(
            messageId,
            interaction.guild,
        )
    return None
