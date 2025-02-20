from discord.ext import commands
import os
import json
from utils.loadConfig import loadConfig
    
def staffCommandCheck():
    async def predicate(ctx):
        config = loadConfig()
        guild = ctx.bot.get_guild(config['primaryGuild'])
        target = guild.get_member(ctx.author.id)
        for role in target.roles:
            if role.id in config['staffRoles']:
                return True
        return False
    return commands.check(predicate)

def guildOwnerCheck():
    async def predicate(ctx):
        if ctx.author.id == ctx.guild.owner_id:
            return True
        return False
    return commands.check(predicate)