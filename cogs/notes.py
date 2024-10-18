from discord import app_commands, Interaction
from discord.ext import commands
import trilium
import json


def prettyJson(obj) -> str:
    return f"```\n{json.dumps(obj, indent=2)}\n```"


class Notes(commands.Cog):

    @app_commands.command(
        name="search", description="Search for notes based on the provided criteria."
    )
    @app_commands.describe(
        query="The query string to search for, which can be full text, exact match, or with labels.",
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
        ancestordepth: int | None = None,
        orderby: str | None = None,
        orderdirection: str = "asc",
        limit: int | None = None,
    ):
        options = {
            "query": query,
            "fast_search": not includecontents,
            "include_archived_notes": includearchived,
            "ancestor_note_id": ancestorid,
            "ancestor_depth": ancestordepth,
            "order_by": orderby,
            "order_direction": orderdirection,
            "limit": limit,
        }
        response = trilium.client.search_note(query, **options)
        await interaction.response.send_message(
            prettyJson(
                [
                    {
                        "noteId": n["noteId"],
                        "title": n["title"],
                        "dateCreated": n["dateCreated"],
                    }
                    for n in response["results"]
                    if n["noteId"] != "_hidden"
                ]
            )
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Notes())
