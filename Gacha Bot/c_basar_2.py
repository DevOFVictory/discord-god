import setup
import server_differences
import create_dino_embeds as cde
import open_close_stuff as ocs


@setup.slash.slash(description="Verkaufe einen Dino an den Basar", guild_ids=setup.guild_ids)
async def sell_basar(ctx, preis, dino_nummer):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den sell_basar Befehl ausgeführt")
    message_author = ctx.author.mention.replace("!", "")

    try:
        preis = int(preis)
    except ValueError:
        await ctx.send(f"Ungültige Preisangabe, **{ctx.author.name}**!")
        return

    if preis < 0:
        preis = 250
    elif preis > 10000:
        preis = 10000

    the_basar = ocs.open_bas(ctx)
    inventories = ocs.open_inv(ctx)

    try:
        chosen_dino = inventories[message_author][int(dino_nummer) - 1]
    except IndexError:
        await ctx.send(f"Ungültige Dino-Nummer, **{ctx.author.name}**!")
        return

    the_basar["basar"].append([chosen_dino, preis, message_author])
    del inventories[message_author][int(dino_nummer) - 1]

    ocs.close_basar(ctx, the_basar)
    ocs.close_inv(ctx, inventories)

    dino_name = cde.create_dino_embed(chosen_dino, "nur fürs Embed notwendig")[1]
    await ctx.send(f"**{ctx.author.name}**, du hast erfolgreich **{dino_name}** für **{preis}** "
                   f"{server_differences.kk} auf den Basar gestellt!")


@setup.slash.slash(description="Hol dir einen deiner Dinos wieder aus dem Basar ab", guild_ids=setup.guild_ids)
async def claim(ctx, dino_nummer):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den claim Befehl ausgeführt")
    message_author = ctx.author.mention.replace("!", "")

    the_basar = ocs.open_bas(ctx)
    inventories = ocs.open_inv(ctx)

    try:
        chosen_dino_ls = the_basar["basar"][int(dino_nummer) - 1]
    except IndexError:
        await ctx.send(f"Ungültige Dino-Nummer, **{ctx.author.name}**!")
        return

    if not chosen_dino_ls[2] == message_author:
        await ctx.send(f"Das ist nicht dein Dino, **{ctx.author.name}**!")
        return

    del the_basar["basar"][int(dino_nummer) - 1]
    inventories[message_author].append(chosen_dino_ls[0])

    ocs.close_basar(ctx, the_basar)
    ocs.close_inv(ctx, inventories)

    dino_name = cde.create_dino_embed(chosen_dino_ls[0], "nur fürs Embed notwendig")[1]
    await ctx.send(f"**{ctx.author.name}**, du hast erfolgreich **{dino_name}** aus dem Basar abgeholt!")


@setup.slash.slash(description="Kauf einen Dino aus dem Basar", guild_ids=setup.guild_ids)
async def buy(ctx, dino_nummer):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den buy Befehl ausgeführt")
    message_author = ctx.author.mention.replace("!", "")

    the_basar = ocs.open_bas(ctx)
    inventories = ocs.open_inv(ctx)
    users_crowns = ocs.open_crowns(ctx)

    try:
        chosen_dino_ls = the_basar["basar"][int(dino_nummer) - 1]
    except IndexError:
        await ctx.send(f"Ungültige Dino-Nummer, **{ctx.author.name}**!")
        return

    if users_crowns[message_author] < int(chosen_dino_ls[1]):
        await ctx.send(f"Du hast nicht genug Kjell Kronen um das zu kaufen, **{ctx.author.name}**!")
        return

    users_crowns[message_author] -= int(chosen_dino_ls[1])
    users_crowns[chosen_dino_ls[2]] += int(chosen_dino_ls[1])
    del the_basar["basar"][int(dino_nummer) - 1]
    inventories[message_author].append(chosen_dino_ls[0])

    ocs.close_basar(ctx, the_basar)
    ocs.close_inv(ctx, inventories)
    ocs.close_crowns(ctx, users_crowns)

    dino_name = cde.create_dino_embed(chosen_dino_ls[0], "nur fürs Embed notwendig")[1]

    if message_author == chosen_dino_ls[2]:
        await ctx.send(f"**{ctx.author.name}**, du hast deinen eigenen Dino vom Basar gekauft... Dafür hättest du auch "
                       f"einfach **/claim** nutzen können...")
        return

    await ctx.send(f"**{ctx.author.name}**, du hast erfolgreich **{dino_name}** von {chosen_dino_ls[2]} für "
                   f"**{chosen_dino_ls[1]}** {server_differences.kk} gekauft!")
