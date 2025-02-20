import discord
from discord.ext import commands
import re

def parseDuration(duration):
    match = re.match(r"(\d+)([dwmos])", duration)
    if not match:
        return 0
    value = int(match.group(1))
    unit = match.group(value)


    refs = {
        "d": 86400,
        "w": 604800,
        "m": 2592000,
        "o": 31536000
    }

    return value * refs[unit]
