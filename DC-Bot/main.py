import os
import discord

from discord_components import DiscordComponents
from discord.ext import commands
from cogs.etc.config import TOKEN, PREFIX


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents,
                   help_command=None, description="Created by exersalza. Project: API-Goose")

DiscordComponents(bot)

for filename in os.listdir("cogs"):
    if filename.endswith(".py") and filename != "__init__.py" and filename != "playground.py":
        bot.load_extension(f"cogs.{filename[:-3]}")

# bot.load_extension('help')

if __name__ == '__main__':
    bot.run(TOKEN)
