import discord
from discord.ext import commands
import re
from datetime import timedelta

def parseDuration(duration):
    match = re.match(r"(\d+)([dwmos])", duration)
    if not match:
        return timedelta(0)
    value = int(match.group(1))
    unit = match.group(2)

    refs = {
        "d": 86400,
        "w": 604800,
        "m": 2592000,
        "o": 31536000
    }

    return timedelta(seconds=value * refs[unit])


def flagParsers(flag):
    flags = {
        "hypesquad_balance": "HypeSquad Balance",
        "active_developer": "Active Developer",
        "hypesquad_bravery": "HypeSquad Bravery",
        "hypesquad_brilliance": "HypeSquad Brilliance",
        
    }

    return flags[flag]