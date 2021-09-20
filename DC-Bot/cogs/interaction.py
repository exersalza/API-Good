import argparse
import os
import random
from datetime import datetime

import discord
from API.qrcode.qr_creator import create_code
from discord.ext import commands
from discord.ext.commands import CommandNotFound

from .etc.config import PREFIX


# todo:


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
        # print(message.content)
        data = []
        d = {'s': self.create}

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
        options = ['-c', '-b', '-bg']

        arg1 = []
        arg2 = []
        arg3 = []
        count1 = 0
        count2 = 0
        count3 = 0

        for option in options:
            print(option, '|-', args)
            if f'-{option}' in args:
                print('cog')
                if 'b' == option:
                    print(option, '||')
                    return

        if [x for x in args if x == '-b'] and count1 != 1:
            var = 0

            while var != 1:
                if args[args.index('-b') + var].isdigit():
                    print('debuggen macht noch mehr spaß')
                    var += 1
                    arg1.append(args[args.index('-b') + var])
                    count1 += 1
                else:
                    await ctx.send(f'{PREFIX}create can only take numbers as Argument')
                    var = 1

        if [x for x in args if x == '-c'] and count2 != 3:
            var = 0
            while var != 3:
                if args[args.index('-c') + var].isdigit():
                    print('debuggen macht noch mehr spaß')
                    arg2.append(args[args.index('-c') + var].strip(','))
                    var += 1
                    count2 += 1
                else:
                    await ctx.send('create can only take numbers as Argument')
                    var = 4
        return

        now = f'etc/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), random.randint(1, 10000)}.png'

        create_code(str(args), now)
        await ctx.send(file=discord.File(now))

        os.remove(now)


def setup(bot):
    bot.add_cog(Interaction(bot))
