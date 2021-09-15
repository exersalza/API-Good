import os
import sys
import argparse

from switch import Switch
from datetime import datetime

from discord.ext import commands
from discord.ext.commands import CommandNotFound

from API import main

Main = main.Main


class Interaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ready at {datetime.now().strftime("%H:%M:%S")}')

    @commands.Cog.listener()
    async def on_message(self, message):
        data = []
        d = {'s': self.create}

        msg = message.content
        if '-' in msg:
            for option in d:
                if f'-{option}' in msg:  # if any in d
                    d[option]()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            return await ctx.send("Command/API nicht gefunden.")


    @commands.Command
    async def create(self, ctx):
        print('coggers')


def setup(bot):
    bot.add_cog(Interaction(bot))
