import setup
import create_dino_embeds as cde
import discord as dc
import server_differences
import open_close_stuff as ocs


@setup.slash.slash(description="Lass dir einen Dino aus dem Basar ausgeben", guild_ids=setup.guild_ids)
async def basar_item(ctx, dino_nummer):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den basar_item Befehl ausgeführt")

    the_basar = ocs.open_bas(ctx)

    try:
        chosen_dino = the_basar["basar"][int(dino_nummer) - 1][0]  # str des dino Namens

    except IndexError:
        await ctx.send(f"Ungültige Dino-Nummer **{ctx.author.name}**!")
        return

    embed_and_dino_name = cde.create_dino_embed(chosen_dino, "Basargegenstand")
    await ctx.send(embed=embed_and_dino_name[0])


@setup.slash.slash(description="Lass dir den Basar ausgeben", guild_ids=setup.guild_ids)
async def basar(ctx):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den basar Befehl ausgeführt")

    the_basar = ocs.open_bas(ctx)

    description = ""
    basar_index = 1

    if not the_basar["basar"]:
        description = "Der Basar ist leer!"

    else:
        for d in the_basar["basar"]:
            if basar_index <= 25:
                d_name = cde.create_dino_embed(d[0], "das hier ist ein Osterei")[1]
                description += f"**{basar_index}** - {d_name} - {d[1]} {server_differences.kk} - von {d[2]}\n"
                basar_index += 1

    embed = dc.Embed(title="**Der aktuelle Basar**", colour=dc.Colour(0x485885), description=description)
    embed.set_footer(text="Seite 1")

    await ctx.send(embed=embed)
    await ctx.message.add_reaction("◀️")
    await ctx.message.add_reaction("▶️")
    await ctx.message.add_reaction("🔄")
