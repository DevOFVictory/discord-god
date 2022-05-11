import setup
import discord as dc
import server_differences


@setup.slash.slash(description="Erfahre mehr über Raritäten von Dinos", guild_ids=setup.guild_ids)
async def rarities(ctx):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den rarities Befehl ausgeführt")
    kk = server_differences.kk

    description = f"**Gewöhnlich :white_circle:**\n " \
                  f"Sie sind für **40** {kk} an die Bank verkaufbar. Die Wahrscheinlichkeit einen zu ziehen " \
                  f"liegt bei **45%**.\n\n" \
                  f"**Ungewöhnlich :green_circle:**\n" \
                  f"Sie sind für **60** {kk} an die Bank verkaufbar. Die Wahrscheinlichkeit einen zu ziehen " \
                  f"liegt bei **25%**.\n\n" \
                  f"**Selten :blue_circle:**\n" \
                  f"Sie sind für **90** {kk} an die Bank verkaufbar. Die Wahrscheinlichkeit einen zu ziehen " \
                  f"liegt bei **20%**.\n\n" \
                  f"**Episch :purple_circle:**\n" \
                  f"Sie sind für **220** {kk} an die Bank verkaufbar. Die Wahrscheinlichkeit einen zu ziehen " \
                  f"liegt bei **7,5%**.\n\n" \
                  f"**Kjell Kronen {kk}**\n" \
                  f"Mit einer **2%** chance ziehst du **600** Kjell Kronen anstatt eines Dinos.\n\n" \
                  f"**Legendär :star:**\n" \
                  f"Sie sind für **800** {kk} an die Bank verkaufbar. Die Wahrscheinlichkeit einen zu ziehen " \
                  f"liegt bei **0,5%**.\n\n" \
                  f"**Sonderrang :secret:**\n" \
                  f"Sie sind nicht an die Bank verkaufbar. Man kann sie nicht ziehen, nur durch Events " \
                  f"erhalten. Jedes gibt es nur einmal."

    embed = dc.Embed(title="Infos über die Raritäten", colour=dc.Colour(0x6d3619), description=description)
    await ctx.send(embed=embed)


@setup.slash.slash(description="Die Grundlagen des Bots", guild_ids=setup.guild_ids)
async def help_bot(ctx):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den help_bot Befehl ausgeführt")
    kk = server_differences.kk

    description = f"Der Bot zu dem diese Nachricht gehört wurde von github.com/onishrimp Erschaffen.\n\n" \
                  f"**Die Funktionen**\n" \
                  f"Primär verfügt der Bot über ein Gacha System. In diesem kann man sich Täglich mit /daily " \
                  f"sogennante Kjell Kronen {kk} abholen. Mit diesen kann man dann mit /gamble Dinos gewinnen und " \
                  f"diese dann sammeln und tauschen.\n\n" \
                  f"**Die Befehle**\n" \
                  f"Wenn ihr ein Slash eingebt seht ihr wenn ihr auf das Bot Icon geht über was der Bot so " \
                  f"verfügt. Dazu gibt es dann eine kurze Beschreibung und gegebenenfalls müsst ihr dem Befehl noch " \
                  f"Parameter hinzufügen. Aber das schafft ihr schon." \

    embed = dc.Embed(title="Der Discord Bot", colour=dc.Colour(0x6d3619), description=description)

    icon = "https://cdn.discordapp.com/attachments/912362937077891132/914146351548338216/KK_real.png"
    embed.set_thumbnail(url=icon)

    await ctx.send(embed=embed)
