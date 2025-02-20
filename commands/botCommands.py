import discord
from discord.ext import commands
from utils.permissionChecks import staffCommandCheck, guildOwnerCheck
from utils.loadConfig import loadConfig

class TestingCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name = "sync")
    @staffCommandCheck()
    async def sync(self, ctx):
        await ctx.reply("Syncing commands...")
        await self.client.tree.sync()
        await ctx.reply("Sync complete.")

        config = loadConfig()
        guild = ctx.client.get_guild(config['primaryGuild'])
        channel = guild.get_channel(config['bot-logs'])
        await channel.send(f"{ctx.author.mention} has synced the commands.")


async def setup(client):
    await client.add_cog(TestingCommand(client))    