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

        self.parser = argparse.ArgumentParser(description='Create QR Code arguments!')
        self.args = self.parser.parse_args()

        self.parser.add_argument('-bg', '--bgcolor', type=str, help='Enter BG Color behind the Argument!')
        self.parser.add_argument('-c', '--color', type=str, help='Enter Color behind the Argument!')


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ready at {datetime.now().strftime("%H:%M:%S")}')

    @commands.Cog.listener()
    async def on_message(self, message):
        data = []
        d = {'s': self.create}

        def decode(foo):
            return foo



        # msg = message.content
        # self.parser.parse_args(msg.split())

        # await message.channel.send('ego death', self.args.bg)

            # for option in d:
            #     print(option)
            #     if f'-{option}' in msg:
            #         if 's' == option:
            #             return

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            return await ctx.send("Command/API nicht gefunden.")


    @commands.Command
    async def create(self, ctx, *args):
        print(args)


def setup(bot):
    bot.add_cog(Interaction(bot))
