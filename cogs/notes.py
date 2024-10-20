import logging
from io import BufferedIOBase, StringIO

import markdown2
import Paginator
from bs4 import BeautifulSoup
from discord import Attachment, Embed, File, Interaction, app_commands
from discord.ext import commands

import trilium
from trilium_client.trilium_client.models import CreateAttachment, CreateNoteDef, Note
from utils import partitionList
from utils.discord import findMessage

logger = logging.getLogger(__name__)

NOTES_RESULTS_PAGE_SIZE = 10


def createNoteResultsEmbed(notes: list[Note], title: str) -> Embed:
    """
    Creates a Discord embed that displays a list of notes clearly.
    """
    embed = Embed(title=title)
    for note in notes:
        name = f"`{'+'.join(note.parent_note_ids or [])} / {note.note_id}`"
        value = f"**{note.title}**\nModified: {note.date_modified}"
        embed.add_field(name=name, value=value, inline=False)
    return embed


async def addAttachmentToNote(attachment: Attachment, noteId: str):
    data = await attachment.read()

    if attachment.content_type and attachment.content_type.startswith("image/"):
        role = "image"
    else:
        role = "file"

    response = trilium.client.post_attachment(
        CreateAttachment(
            ownerId=noteId,
            content="",
            role=role,
            mime=attachment.content_type,
            title=attachment.filename,
        )
    )
    if response.attachment_id:
        trilium.setAttachmentContents(response.attachment_id, data)


class Notes(commands.Cog):
    group = app_commands.Group(name="notes", description="Manage your notes.")

    @group.command(name="search", description="Search for notes based on the provided criteria.")
    @app_commands.describe(
        query="The query string to search for, which can be full text, exact match, "
        "or with labels.",
        includecontents="Search for keywords in the note contents too.",
        includearchived="Include archived notes in the search results.",
        ancestorid="Specify the ancestor noteId to limit search to its subtree.",
        ancestordepth="Specify the depth to search from the ancestor node.",
        orderby="Specify the property/label to order the results by.",
        orderdirection="Specify the order direction (asc, desc).",
        limit="Limit the number of results returned.",
    )
    @app_commands.choices(
        orderdirection=[
            app_commands.Choice(name="Ascending", value="asc"),
            app_commands.Choice(name="Descending", value="desc"),
        ],
        orderby=[
            app_commands.Choice(name="Title", value="title"),
            app_commands.Choice(name="dateCreated", value="dateCreated"),
        ],
    )
    async def searchNotes(
        self,
        interaction: Interaction,
        query: str,
        includecontents: bool = False,
        includearchived: bool = False,
        ancestorid: str | None = None,
        ancestordepth: str | None = None,
        orderby: str | None = None,
        orderdirection: str = "asc",
        limit: int | None = None,
    ):
        if (not ancestorid or ancestorid == "root") and ancestordepth:
            await interaction.response.send_message(
                "`ancestordepth` has no effect if `ancestorid` is `root`", ephemeral=True
            )
            return

        options = {
            "fast_search": not includecontents,
            "include_archived_notes": includearchived,
            "ancestor_note_id": ancestorid,
            "ancestor_depth": ancestordepth,
            "order_by": orderby,
            "order_direction": orderdirection,
            "limit": limit,
        }
        response = trilium.client.search_notes(query, **options)
        notes = [n for n in response.results if n.note_id != "_hidden"]
        pages = [
            createNoteResultsEmbed(page, f"Page {i+1}")
            for i, page in enumerate(partitionList(notes, NOTES_RESULTS_PAGE_SIZE))
        ]
        await Paginator.Simple(ephemeral=True).start(interaction, pages=pages)

    @group.command(name="contents", description="Returns the contents of a note by ID")
    async def getNoteContents(self, interaction: Interaction, noteid: str):
        try:
            contents = trilium.client.get_note_content(noteid)
        except Exception as e:
            await interaction.response.send_message(str(e), ephemeral=True)
            return
        soup = BeautifulSoup(contents, "html.parser")
        contents = soup.prettify()
        f: BufferedIOBase = StringIO(contents)  # type: ignore
        await interaction.response.send_message(
            file=File(f, filename="message.txt"), ephemeral=True
        )

    @group.command(name="create-from-message", description="Creates a new note")
    @app_commands.describe(
        messageid="ID of the Discord message used to create the note",
        title="Title of the note",
        ancestorid="ID of the note to create this new note under",
    )
    async def createNote(
        self,
        interaction: Interaction,
        messageid: str,
        title: str = "new note",
        ancestorid: str = "root",
    ):
        try:
            messageIdInt = int(messageid)
        except ValueError:
            await interaction.response.send_message(
                f"Invalid message ID `{messageid}`", ephemeral=True
            )
            return

        noteMsg = await findMessage(messageIdInt, interaction)
        if not noteMsg:
            await interaction.response.send_message(
                f"Unable to find message ID `{messageIdInt}`", ephemeral=True
            )
            return

        response = trilium.client.create_note(
            CreateNoteDef(
                parentNoteId=ancestorid,
                title=title,
                type="text",
                content=markdown2.markdown(noteMsg.content),
            )
        )
        if response.note and response.note.note_id:
            for attachment in noteMsg.attachments:
                await addAttachmentToNote(attachment, response.note.note_id)
            await interaction.response.send_message(
                f"Created note with ID `{response.note.note_id}`", ephemeral=True
            )

    @group.command(name="delete", description="Deletes a note.")
    async def deleteNote(self, interaction: Interaction, noteid: str):
        trilium.client.delete_note_by_id(noteid)
        await interaction.response.send_message("Deleted", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Notes())
