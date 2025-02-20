from discord.ext import commands
import discord
import os
import json
from utils.permissionChecks import staffCommandCheck, guildOwnerCheck
import asyncio
from utils.parsers import parseDuration

class moderationCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name = "kick", description = "Kick a user from the server.", with_app_command=True)
    async def kick(self, ctx, user: discord.Member, *, reason = "No reason provided"):
        if ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.ban_members or ctx.author.guild_permissions.administrator:
            await user.kick(reason = reason)
            await ctx.reply(f"{user.mention} has been kicked for **{reason}**.")
        else:
            msg = await ctx.reply("You have insufficient permissions to run this command, you require the `Ban Members`, `Kick Members`, or `Administrator` permission.")
            await msg.delete(delay = 5)
            await ctx.message.delete(delay = 5)

    @commands.hybrid_command(name = "ban", description = "Ban a user from the server.", with_app_command=True)
    async def ban(self, ctx, user: discord.Member, duration, *, reason = "No reason provided"):
        if ctx.author.guild_permissions.ban_members or ctx.author.guild_permissions.administrator:
            await user.ban(reason = reason)
            await ctx.reply(f"{user.mention} has been banned for **{reason}**.")
            newDuration = parseDuration(duration)
            if newDuration:
                await asyncio.sleep(newDuration)
                await ctx.guild.unban(user, reason = "Temporary ban duration expired.")
            else:
                await ctx.reply("Invalid duration provided, please provide a valid duration.")
        else:
            msg = await ctx.reply("You have insufficient permissions to run this command, you require the `Ban Members` or `Administrator` permission.")
            await msg.delete(delay = 5)
            await ctx.message.delete(delay = 5)

    
    @commands.hybrid_command(name = "unban", description = "Unban a user from the server.", with_app_command=True)
    async def unban(self, ctx, user: discord.User, *, reason = "No reason provided"):
        if ctx.author.guild_permissions.ban_members or ctx.author.guild_permissions.administrator:
            await ctx.guild.unban(user, reason = reason)
            await ctx.reply(f"{user.mention} has been unbanned for **{reason}**.")
        else:
            msg = await ctx.reply("You have insufficient permissions to run this command, you require the `Ban Members` or `Administrator` permission.")
            await msg.delete(delay = 5)
            await ctx.message.delete(delay = 5)

    @commands.hybrid_command(name = "mute", aliases=['to', 'timeout'], description = "Mute a user in the server.", with_app_command=True)
    async def mute(self, ctx: discord.ext.commands.Context, user: discord.Member, duration, *, reason = 'No reason provided'):
        if ctx.author.guild_permissions.mute_members or ctx.author.guild_permissions.administrator:
            await user.timeout(parseDuration(duration), reason = reason)
            await ctx.reply(f"{user.mention} has been muted for **{reason}**.")
        else:
            msg = await ctx.reply("You have insufficient permissions to run this command, you require the `Mute Members` or `Administrator` permission.")
            await msg.delete(delay = 5)
            await ctx.message.delete(delay = 5)

    @commands.hybrid_command(name = "unmute", aliases=['rto', 'untimeout', 'ut', 'removetimeout'], description = "Unmute a user in the server.", with_app_command=True)
    async def unmute(self, ctx, user: discord.Member, *, reason = 'No reason provided'):
        if ctx.author.guild_permissions.mute_members or ctx.author.guild_permissions.administrator:
            await user.timeout(None, reason = reason)
            await ctx.reply(f"{user.mention} has been unmuted for **{reason}**.")
        else:
            msg = await ctx.reply("You have insufficient permissions to run this command, you require the `Mute Members` or `Administrator` permission.")
            await msg.delete(delay = 5)
            await ctx.message.delete(delay = 5)

async def setup(client):
    await client.add_cog(moderationCommands(client))