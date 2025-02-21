import discord
from discord.ext import commands
from utils.loadConfig import loadConfig

class joins(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = loadConfig()

    @commands.Cog.listener()
    async def on_guild_join(self, joinGuild):
        guild = self.client.get_guild(self.config["primaryGuild"])
        channel = guild.get_channel(self.config["join-leave-logs"])
        await channel.send(embed = discord.Embed(title = "Bot Joined", description=f"Bot has joined {joinGuild.name}.", color = discord.Color.green()))

    @commands.Cog.listener()
    async def on_guild_remove(self, leaveGuild):
        guild = self.client.get_guild(self.config["primaryGuild"])
        channel = guild.get_channel(self.config["join-leave-logs"])
        await channel.send(embed = discord.Embed(title = "Bot Left", description=f"Bot has left {leaveGuild.name}.", color = discord.Color.red()))

async def setup(client):
    await client.add_cog(joins(client))