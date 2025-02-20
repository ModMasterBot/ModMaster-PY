import dotenv
from discord.ext import commands
import discord
import os
dotenv.load_dotenv()

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=";", intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        for file in os.listdir('commands'):
            if file.endswith('.py') and ("command" in file.lower()):
                print(file)
                await self.load_extension(f'commands.{file[:-3]}')

        
        for file in os.listdir('events'):
            if file.endswith('.py'):
                print(file)
                await self.load_extension(f'events.{file[:-3]}')



client = Client()


client.run(os.getenv("TOKEN"))
            


