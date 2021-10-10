import os
import discord
import time
from threading import Thread
from alive_progress import alive_bar

from discord_components import DiscordComponents
from discord.ext import commands
from cogs.etc.config import TOKEN, PREFIX, FLASK
from cogs.etc.Flask_setup.start_server import start_server
from cogs.interaction import notcomplete, Interaction


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents,
                   help_command=None, description="Created by exersalza. Project: API-Goose")

DiscordComponents(bot)

count = 0

for f in os.listdir('cogs'):
    count += 1


def load():
    with alive_bar(count) as bar:
        for filename in os.listdir("cogs"):
            if filename.endswith(".py") and filename != "__init__.py" and filename != "playground.py":
                bot.load_extension(f"cogs.{filename[:-3]}")
                bar()


def unload():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py") and filename != "__init__.py" and filename != "playground.py":
            bot.unload_extension(f"cogs.{filename[:-3]}")


if __name__ == '__main__':
    load()
    if FLASK:
        start_server()
    bot.run(TOKEN)
