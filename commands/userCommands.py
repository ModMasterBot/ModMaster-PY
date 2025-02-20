import discord
from discord.ext import commands

class userCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name = "whois", aliases = ['w'], description = "Get information about a user.", with_app_command=True)
    async def whois(self, ctx, user: discord.Member):
        userEmbed = discord.Embed()
        userEmbed.set_author(name = f"@{user.name}", icon_url = user.avatar.url)
        userEmbed.set_thumbnail(url = user.avatar.url)
        flags = '\n '.join([str(flag).split('.')[1].split(':')[0] for flag in user.public_flags.all()])
        userEmbed.description = f"{flags}"
        userEmbed.add_field(name = "Member Information", value = f":ampersand: {user.mention}\n:user: {user.name}\n:id: {user.id}\n:calendar: {user.created_at.strftime('%d/%m/%Y')}\n:inbox_tray: {user.joined_at.strftime('%d/%m/%Y')}", inline = False)
        userEmbed.add_field(name = "Roles", value = f"{', '.join([role.mention for role in reversed(user.roles) if role.name != '@everyone'])}", inline = False)
        userEmbed.set_footer(text = f"ID: {ctx.author.id}")
        userEmbed.timestamp = ctx.message.created_at
        await ctx.reply(embed = userEmbed)


async def setup(client):
    await client.add_cog(userCommands(client))