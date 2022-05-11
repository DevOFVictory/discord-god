import setup
import random
import server_differences
import create_dino_embeds as cde
import open_close_stuff as ocs


@setup.slash.slash(description="Gamble für 200 Kjell Kronen", guild_ids=setup.guild_ids)
async def gamble(ctx):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den gamble Befehl ausgeführt")
    message_author = ctx.author.mention.replace("!", "")

    users_crowns = ocs.open_crowns(ctx)
    dinos = ocs.open_dinos()
    inventory = ocs.open_inv(ctx)

    if not users_crowns[message_author] >= 200:
        await ctx.channel.send(f"**{ctx.author.name}**, du hast nicht genug {server_differences.kk} zum Gambeln!")
        return

    users_crowns[message_author] -= 200

    if message_author not in inventory:
        inventory[message_author] = []

    common = []
    uncommon = []
    rare = []
    epic = []
    legendary = []

    for k, v in dinos.items():
        if v[0] == "gewöhnlich":
            common.append(k)
        if v[0] == "ungewöhnlich":
            uncommon.append(k)
        if v[0] == "selten":
            rare.append(k)
        if v[0] == "episch":
            epic.append(k)
        if v[0] == "legendär":
            legendary.append(k)

    letter_translation_dict = {
        "A": "common",
        "B": "uncommon",
        "C": "rare",
        "D": "epic",
        "E": "KKs",
        "F": "legendary"
    }

    probabilities = ("A" * 90) + ("B" * 50) + ("C" * 40) + ("D" * 15) + ("E" * 4) + "F"
    chosen_letter = random.choice(probabilities)
    chosen_rarity = letter_translation_dict[chosen_letter]

    try:
        chosen_dino_raw = eval(chosen_rarity)  # zur Liste umwandeln
        chosen_dino = random.choice(chosen_dino_raw)  # Dino Name
        inventory[message_author].append(chosen_dino)
        embed_and_dino_name = cde.create_dino_embed(chosen_dino, f"Eigentum von {ctx.author.name}")

        await ctx.send(embed=embed_and_dino_name[0])
        await ctx.channel.send(f"Herzlichen Glückwunsch! Du hast **{embed_and_dino_name[1]}** gezogen!")

    except NameError:
        await ctx.send(f"Wow! Herzlichen Glückwunsch **{ctx.author.name}**! Du hast anstatt eines Dinos **600** "
                       f"{server_differences.kk} erhalten!")
        users_crowns[message_author] += 800

    ocs.close_crowns(ctx, users_crowns)
    ocs.close_inv(ctx, inventory)
