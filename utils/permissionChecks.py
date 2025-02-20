from discord.ext import commands
import os
import json

def loadConfig():
    with open("config.json", "r") as configFile:
        return json.load(configFile)
    
def staffCommandCheck():
    async def predicate(ctx):
        config = loadConfig()
        print(ctx.author.roles)
        print(config['staffRoles'])
        for role in ctx.author.roles:
            if role.id in config['staffRoles']:
                print(role.id)
                return True
            return False
    return commands.check(predicate)