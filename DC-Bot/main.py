import os
import nextcord as discord
import platform

from time import sleep
from threading import Thread
from alive_progress import alive_bar
from pyfiglet import Figlet

# from discord_components import DiscordComponents
from nextcord.ext import commands
from cogs.etc.config import TOKEN, PREFIX, FLASK
from cogs.etc.Flask_setup.start_server import start_server


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents,
                   help_command=None, description="Created by exersalza. Project: API-Goose")

# DiscordComponents(bot)

count = 0

for f in os.listdir('cogs'):
    if f.endswith(".py") and f != "__init__.py" and f != "playground.py":
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
    platform = platform.system()

    if platform == 'Windows':
        clear = lambda: os.system('cls')
        clear()
    elif platform == 'Linux':
        clear = lambda: os.system('clear')
        clear()

    print(Figlet(font='slant').renderText('API-Goose'))
    load()
    if FLASK:
        print('/----------[ FLASK ]----------\\')
        start_server()
    sleep(.5)
    if FLASK:
        print('\\----------[ FLASK ]----------/')
    bot.run(TOKEN)
