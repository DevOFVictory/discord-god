import setup
import server_differences
import create_dino_embeds as cde
import open_close_stuff as ocs


@setup.slash.slash(description="Verkaufe einen Dino an den Basar", guild_ids=setup.guild_ids)
async def sell_bank(ctx, dino_nummer):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den sell_bank Befehl ausgeführt")
    message_author = ctx.author.mention.replace("!", "")

    inventories = ocs.open_inv(ctx)
    users_crowns = ocs.open_crowns(ctx)
    dinos = ocs.open_dinos()

    bank_prices = {
        "gewöhnlich": 40,
        "ungewöhnlich": 60,
        "selten": 90,
        "episch": 220,
        "legendär": 800,
    }

    try:
        chosen_dino = inventories[message_author][int(dino_nummer) - 1]  # str name des Dinos
        del inventories[message_author][int(dino_nummer) - 1]

    except IndexError:
        await ctx.send(f"Ungültige Dino-Nummer **{ctx.author.name}**!")
        return

    if dinos[chosen_dino][0] not in bank_prices:
        await ctx.send(f"Dieser Gegenstand ist nicht verkaufbar, **{ctx.author.name}**")
        return

    crown_reward = bank_prices[dinos[chosen_dino][0]]
    users_crowns[message_author] += crown_reward
    dino_name = cde.create_dino_embed(chosen_dino, "187 über allem")[1]

    ocs.close_crowns(ctx, users_crowns)
    ocs.close_inv(ctx, inventories)

    await ctx.send(f"**{ctx.author.name}**, du hast erfolgreich **{dino_name}** für **{crown_reward}** "
                   f"{server_differences.kk} verkauft!")
