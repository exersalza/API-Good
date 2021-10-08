import os
import discord
import time

from discord_components import DiscordComponents
from discord.ext import commands
from cogs.etc.config import TOKEN, PREFIX, FLASK
from cogs.etc.flask_server import start_server
from cogs.interaction import notcomplete, Interaction


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents,
                   help_command=None, description="Created by exersalza. Project: API-Goose")

DiscordComponents(bot)

for filename in os.listdir("cogs"):
    if filename.endswith(".py") and filename != "__init__.py" and filename != "playground.py":
        bot.load_extension(f"cogs.{filename[:-3]}")

# bot.load_extension('help')

animation = [
  "[        ]",
  "[=       ]",
  "[===     ]",
  "[====    ]",
  "[=====   ]",
  "[======  ]",
  "[======= ]",
  "[========]",
  "[ =======]",
  "[  ======]",
  "[   =====]",
  "[    ====]",
  "[     ===]",
  "[      ==]",
  "[       =]",
  "[        ]",
  "[        ]"
  ]

i = 0
Interaction.function('function')
for i in range(1, 20):
    print(animation[i % len(animation)], end='\r')
    time.sleep(.2)

if __name__ == '__main__':
  if FLASK:
    start_server()
  bot.run(TOKEN)
