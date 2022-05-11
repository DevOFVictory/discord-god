import discord as dc
from discord_slash import SlashCommand
from discord.ext import commands

import server_differences
import setup
import on_reaction_add
import c_general
import c_gamble
import c_info
import c_crowns
import c_inventory
import c_basar_1
import c_basar_2
import c_bank
import c_give


@setup.client.event
async def on_ready():
    print("Der Bot ist online")


setup.client.run(server_differences.token)
