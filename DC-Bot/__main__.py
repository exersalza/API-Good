import os
import nextcord
import platform
from multiprocessing import Process

from time import sleep
from threading import Thread
from alive_progress import alive_bar
from pyfiglet import Figlet

from discord_components import DiscordComponents
from nextcord.ext import commands
from cogs.etc.config import TOKEN, PREFIX, FLASK
from cogs.etc.Flask_setup.start_server import start_server


intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents,
                   help_command=None, description="Created by exersalza. Project: API-Goose")

DiscordComponents(bot)

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


def reload():
    with alive_bar(count) as bar:
        for filename in os.listdir("cogs"):
            if filename.endswith(".py") and filename != "__init__.py" and filename != "playground.py":
                bot.unload_extension(f"cogs.{filename[:-3]}")
                bar()

    with alive_bar(count) as bar:
        for filename in os.listdir("cogs"):
            if filename.endswith(".py") and filename != "__init__.py" and filename != "playground.py":
                bot.load_extension(f"cogs.{filename[:-3]}")
                bar()


def ask_input(active=bool(True)):
    while active:
        ask = input('reload?: ')
        if ask == 'y':
            return reload()


''' def askinput(): # it doenst work for now
    while True:
        choice = input('1: Reload the Objects\n2: All alive Threads')
        if choice == '1':
            pass
        if choice == '2':
            pass
        else:
            return 0
        return 1 '''


if __name__ == '__main__':
    platform = platform.system()

    if platform == 'Windows':
        clear = lambda: os.system('cls')
        clear()
    elif platform == 'Linux':
        clear = lambda: os.system('clear')
        clear()

    print(f'\u001b[36m{Figlet(font="slant").renderText("API-Goose")}\u001b[0m')
    load()
    if FLASK:
        print('\u001b[32m/----------[ FLASK ]----------\\\u001b[0m'.center(80))
        start_server()
    sleep(.5)
    if FLASK:
        print('\u001b[32m\\----------[ FLASK ]----------/\u001b[0m'.center(80))

    Client = Process(target=bot.run(TOKEN) and ask_input(True))
    Client.start()
    # asker = Process(target=ask_input(True))
    # asker.start()

    
    
