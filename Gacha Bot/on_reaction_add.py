import server_differences
import create_dino_embeds as cde
import setup
import json
import discord as dc
import open_close_stuff as ocs


@setup.client.event
async def on_reaction_add(reaction, user):

    message_author = user.mention.replace("!", "")

    if message_author == server_differences.bot_id:
        return

    if not (reaction.emoji == "▶️") and not (reaction.emoji == "◀️") and not (reaction.emoji == "🔄"):
        return

    embed_list = reaction.message.embeds

    if not embed_list:
        return

    basar_requested = False

    # falls die Reaktion an das Inventar oder Basar Embed geht
    if not embed_list[0].title == f"**Inventar von {user.name}**":
        basar_requested = True
        if not embed_list[0].title == "**Der aktuelle Basar**":
            return

    page_int = 1
    if reaction.emoji == "◀️":
        page_int = -1
    elif reaction.emoji == "🔄":
        page_int = 0
    page = int(embed_list[0].footer.text.split(" ", maxsplit=1)[1]) + page_int
    if page <= 0:
        page = 1

    description = ""
    dino_range = 25 * (page - 1)

    if not basar_requested:  # Wenn es das Inventar ist

        inventory_index = 1
        user_dinos = []

        with open(f"Datenbank/{reaction.message.channel.guild.id}/inv.txt", mode="r", encoding="utf-8") as inv_load:
            inventories = json.load(inv_load)

        if message_author not in inventories:
            description = "Du hast noch keine Gegenstände besessen!"

        elif not inventories[message_author]:
            description = "Dein Inventar ist leer!"

        else:
            for d in inventories[message_author]:
                title = f"Eigentum von {user.name}"
                user_dinos.append(f"**{inventory_index}** - {cde.create_dino_embed(d, title)[1]}\n")
                inventory_index += 1

            for d in range(1, 26):
                try:
                    d += dino_range
                    description += user_dinos[d - 1]
                except IndexError:
                    break

        if description == "":
            description = "Auf dieser Seite befindet sich nichts!"

        embed_title = f"**Inventar von {user.name}**"

    else:  # Also wenn es der Basar ist
        basar_index = 1
        basar_dinos = []

        with open(f"Datenbank/{reaction.message.channel.guild.id}/basar.txt", mode="r", encoding="utf-8") as bas_load:
            the_basar = json.load(bas_load)

        if not the_basar["basar"]:
            description = "Der Basar ist leer!"

        else:
            for d in the_basar["basar"]:
                d_name = cde.create_dino_embed(d[0], "Der aktuelle Basar")[1]
                basar_dinos.append(f"**{basar_index}** - {d_name} - {d[1]} {server_differences.kk} - von {d[2]}\n")
                basar_index += 1

        for d in range(1, 26):
            try:
                d += dino_range
                description += basar_dinos[d - 1]
            except IndexError:
                break

        if description == "":
            description = "Auf dieser Seite befindet sich nichts!"

        embed_title = "**Der aktuelle Basar**"

    embed = dc.Embed(title=embed_title, colour=dc.Colour(0x485885), description=description)
    embed.set_footer(text=f"Seite {page}")

    await reaction.remove(user)
    await reaction.message.edit(embed=embed)
