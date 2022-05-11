from discord_slash import SlashCommand
from discord.ext import commands
import server_differences

client = commands.Bot(command_prefix=",")
slash = SlashCommand(client=client, sync_commands=True)
guild_ids = ["list of int guild ids"]


def check_channel(ctx):
    if not server_differences.channel_id == str(ctx.channel.id):
        return
