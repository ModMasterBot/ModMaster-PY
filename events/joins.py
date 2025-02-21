import discord
from discord.ext import commands

class joins(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f"Bot has joined {guild.name}.")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f"Bot has left {guild.name}.")

async def setup(client):
    await client.add_cog(joins(client))