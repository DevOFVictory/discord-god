import setup
import server_differences
import open_close_stuff as ocs


@setup.slash.slash(description="Verschenke etwas. Nur vom Admin nutzbar", guild_ids=setup.guild_ids)
async def give(ctx, verschenktes, adressat):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den give Befehl auf {adressat} ausgeführt")
    message_author = ctx.author.mention.replace("!", "")
    adressat = adressat.replace("!", "")

    if not message_author == "<@insert admin id>":
        await ctx.send(f"**DU BIST NICHT MEIN MEISTER 👺**")
        return

    try:
        verschenktes = int(verschenktes)
        crowns = True

    except ValueError:
        crowns = False

    if crowns:
        users_crowns = ocs.open_crowns(ctx)

        if adressat not in users_crowns:
            users_crowns[adressat] = 300

        users_crowns[adressat] += verschenktes
        ocs.close_crowns(ctx, users_crowns)

        await ctx.send(f"Du hast erfolgreich {adressat} **{verschenktes}** {server_differences.kk} gegeben, Meister!")

    else:
        inventories = ocs.open_inv(ctx)
        dinos = ocs.open_dinos()

        if verschenktes not in dinos:
            await ctx.send(f"Unbekannter Dino Meister")
            return

        if adressat not in inventories:
            inventories[adressat] = []

        inventories[adressat].append(verschenktes)
        ocs.close_inv(ctx, inventories)

        await ctx.send(f"Du hast erfolgreich {adressat} einen Dino gegeben, Meister!")


@setup.slash.slash(description="Gib jemandem Kronen", guild_ids=setup.guild_ids)
async def pay(ctx, kronen_menge, adressat):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den pay Befehl auf {adressat} ausgeführt")
    message_author = ctx.author.mention.replace("!", "")
    adressat = adressat.replace("!", "")

    try:
        kronen_menge = int(kronen_menge)

    except ValueError:
        await ctx.send(f"Invalide Kronen-menge, **{ctx.author.name}**!")
        return

    users_crowns = ocs.open_crowns(ctx)

    if adressat not in users_crowns:
        await ctx.send(f"Den Adressat **gibt es nicht** oder er hat noch **keine Kronen besessen**, "
                       f"**{ctx.author.name}**!")
        return

    if users_crowns[message_author] < kronen_menge:
        await ctx.send(f"Du hast **nicht genug Kronen** um so viel zu vergeben, **{ctx.author.name}**!")
        return

    users_crowns[message_author] -= kronen_menge
    users_crowns[adressat] += kronen_menge

    ocs.close_crowns(ctx, users_crowns)

    await ctx.send(f"**{ctx.author.name}**, du hast erfolgreich {adressat} **{kronen_menge}** {server_differences.kk} "
                   f"überwiesen!")
