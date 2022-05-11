import setup
import create_dino_embeds as cde
import discord as dc
import open_close_stuff as ocs


@setup.slash.slash(description="Lass dir einen Dino aus deinem Inventar ausgeben", guild_ids=setup.guild_ids)
async def item(ctx, dino_nummer):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den item Befehl ausgeführt")
    message_author = ctx.author.mention.replace("!", "")

    inventories = ocs.open_inv(ctx)

    try:
        chosen_dino = inventories[message_author][int(dino_nummer) - 1]  # str name des Dinos

    except IndexError:
        await ctx.send(f"Ungültige Dino-Nummer **{ctx.author.name}**!")
        return

    embed_and_dino_name = cde.create_dino_embed(chosen_dino, f"Eigentum von {ctx.author.name}")
    await ctx.send(embed=embed_and_dino_name[0])


@setup.slash.slash(description="Lass dir dein Inventar ausgeben", guild_ids=setup.guild_ids)
async def inventory(ctx):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den inventory Befehl ausgeführt")
    message_author = ctx.author.mention.replace("!", "")

    inventories = ocs.open_inv(ctx)

    description = ""
    inventory_index = 1

    if message_author not in inventories:
        description = "Du hast noch keine Gegenstände besessen!"

    elif not inventories[message_author]:
        description = "Dein Inventar ist leer!"

    else:
        for d in inventories[message_author]:
            if inventory_index <= 25:
                title = f"Eigentum von {ctx.author.name}"
                description += f"**{inventory_index}** - {cde.create_dino_embed(d, title)[1]}\n"
                inventory_index += 1

    embed = dc.Embed(title=f"**Inventar von {ctx.author.name}**", colour=dc.Colour(0x485885), description=description)
    embed.set_footer(text="Seite 1")

    await ctx.send(embed=embed)
    await ctx.message.add_reaction("◀️")
    await ctx.message.add_reaction("▶️")
    await ctx.message.add_reaction("🔄")
