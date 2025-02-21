import dotenv
from discord.ext import commands
import discord
import os
from utils.loadConfig import loadConfig
dotenv.load_dotenv()

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.config = loadConfig()

    async def setup_hook(self) -> None:
        for file in os.listdir('commands'):
            if file.endswith('.py') and ("command" in file.lower()):
                print(file)
                await self.load_extension(f'commands.{file[:-3]}')

        
        for file in os.listdir('events'):
            if file.endswith('.py'):
                print(file)
                await self.load_extension(f'events.{file[:-3]}')

    async def on_ready(self):
        config = loadConfig()
        guild = self.get_guild(config['primaryGuild'])
        channel = guild.get_channel(config['bot-logs'])
        await channel.send(f"<:Online:1342066679638921266> ModMaster started up successfully.")



client = Client()


client.run(os.getenv("TOKEN"))
            


