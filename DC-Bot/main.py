import os
import discord

from discord_components import DiscordComponents
from discord.ext import commands
from cogs.etc.config import TOKEN, PREFIX
from cogs.API.main import Main

print('Modules name is: ', Main.__name__)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents,
                   help_command=None, description="Created by exersalza. Project: API-Goose")

DiscordComponents(bot)

API_Conn = Main

for filename in os.listdir("cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        print(filename)
        bot.load_extension(f"cogs.{filename[:-3]}")

# bot.load_extension('help')
bot.run(TOKEN)
