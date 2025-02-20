import discord
from discord.ext import commands
from utils.permissionChecks import staffCommandCheck

class TestingCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name = "test")
    @staffCommandCheck()
    async def test(self, ctx):
        await ctx.reply("ModMaster up and running!")

async def setup(client):
    await client.add_cog(TestingCommand(client))    