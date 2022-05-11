import random
import setup


@setup.slash.slash(description="Lass dir den Ping ausgeben", guild_ids=setup.guild_ids)
async def ping(ctx):
    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den ping Befehl ausgeführt")
    clock_emojis = ["🕐", "🕙", "🕥", "🕚", "🕦", "🕛", "🕧", "🕜", "🕑", "🕝", "🕒", "🕞", "🕓", "🕟", "🕔", "🕠", "🕕",
                    "🕡", "🕖", "🕢", "🕗", "🕣", "🕘", "🕤"]
    ce_1, ce_2 = random.choice(clock_emojis), random.choice(clock_emojis)
    await ctx.send(f"{ce_1} **Bot Ping - {round(setup.client.latency* 1000)}ms** {ce_2}")


@setup.slash.slash(description="Frag die Magische Miesmuschel etwas", guild_ids=setup.guild_ids)
async def mmm(ctx, question):
    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den mmm Befehl ausgeführt")
    responses = ["Ja",
                 "Auf jeden Fall",
                 "Gewiss",
                 "Nein",
                 "Auf keinen Fall",
                 "Lieber nicht",
                 "Vielleicht",
                 "Keine Ahnung"]
    await ctx.send(f"**Frage von {ctx.author.name}:** {question}\n**Antwort:** {random.choice(responses)}")


@setup.slash.slash(description="Frag die Magische Miesmuschel etwas", guild_ids=setup.guild_ids)
async def coinflip(ctx):
    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den coinflip Befehl ausgeführt")
    responses = ["Kopf", "Zahl"]
    await ctx.send(f"**{ctx.author.name} hat eine Münze geworfen. :coin: Das Ergebnis war:**\n"
                   f" **{random.choice(responses)}**")


@setup.slash.slash(description="Reich einen Vorschlag ein", guild_ids=setup.guild_ids)
async def suggestion(ctx, vorschlag):
    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den suggestion Befehl ausgeführt")
    with open(f"Datenbank/{ctx.channel.guild.id}/vorschläge.txt", mode="a", encoding="utf-8") as suggestions:
        suggestions.write(f"{ctx.author.name} hat vorgeschlagen: {vorschlag}\n\n")
    await ctx.send(f"**{ctx.author.name}**, du hast den Vorschlag erfolgreich eingereicht.")
