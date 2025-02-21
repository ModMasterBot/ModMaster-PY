import discord
from discord.ext import commands
from utils.loadConfig import loadConfig

class onMessage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx,  error):
        if isinstance(error, commands.CheckFailure):
            await ctx.reply("Insufficient permissions.")
        else:
            await ctx.reply(f"An error occurred: {error}")

            config = loadConfig()
            guild = self.client.get_guild(config["primaryGuild"])
            channel = guild.get_channel(config["error-logs"])
            await channel.send(embed = discord.Embed(title = "Error", description=f"An error occurred in {ctx.command.name if ctx.command.name is not None else "unknown command"}:\n```{error}```", color = discord.Color.red()))
        

async def setup(client):
    await client.add_cog(onMessage(client))