import argparse
import os
import random
from datetime import datetime
from itertools import cycle

import discord
from API.qrcode.qr_creator import create_code
from discord.ext import commands
from discord.ext.commands import CommandNotFound

from .etc.config import ESCAPE, cycle_query


# todo:
#  IQAir, BoredAPI implement
global notcomplete
notcomplete = True

class Interaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.parser = argparse.ArgumentParser(description='Create QR Code arguments!')
        self.args = self.parser.parse_args()

        self.parser.add_argument('-bg', '--bgcolor', type=str, help='Enter BG Color behind the Argument!')
        self.parser.add_argument('-c', '--color', type=str, help='Enter Color behind the Argument!')

        self.cycle = cycle(cycle_query)

    async def function(function):
      print(function)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ready at {datetime.now().strftime("%H:%M:%S")}')
        notcomplete = False

    @commands.Cog.listener()
    async def on_message(self, message):  # help for lonely commands :(
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
            return await ctx.send("Command/API not found.")

    @commands.Command
    async def createqr(self, ctx, *args):  # argparse function

        colores = []
        bgcolores = []
        vdata = []

        color = (0, 0, 0)
        bgcolor = (255, 255, 255)
        box = 6

        options = ['b', 'c', 'bg', 'd', 'h']

        async def parser(rounds, option, validate, limit):
            var = 0
            while var != rounds:
                var += 1
                try:
                    val = int(args[args.index(f'{ESCAPE}{option}') + var].strip(','))
                except ValueError:
                    await ctx.send('One Argument is not an Integer')
                    break

                if type(val) == int and not val >= limit + 1:  # Double check
                    validate.append(val)
                else:
                    await ctx.send(f'One Argument is not under or {limit}')
                    break

            def converter(list):
                return (*list,)

            return converter(validate)

        for option in options:
            if f'{ESCAPE}{option}' in list(args):
                if 'c' == option:  # color argparser
                    color = await parser(3, 'c', colores, 255)

                elif 'bg' == option:  # back-color argparser
                    bgcolor = await parser(3, 'bg', bgcolores, 255)

                elif 'd' == option:  # data argparser
                    for i in args[args.index(f'{ESCAPE}d') + 1:]:
                        if not [i for t in options if f'{ESCAPE}{t}' == i]:
                            vdata.append(i)
                        else:
                            break

                elif 'b' == option:  # box-size argparser
                    try:
                        coggers_box = int(args[args.index(f'{ESCAPE}{option}') + 1].strip(','))
                        if coggers_box >= 100:
                            await ctx.send('The box Argument is too Large, please take a Number under 100')
                            break
                        else:
                            box = coggers_box

                    except ValueError:
                        await ctx.send(ValueError)
                        break

                elif 'h' == option or 'help' == option:
                    embed = discord.Embed(title=f'Help site for the Qr Code generator',
                                          timestamp=datetime.utcnow(),
                                          color=0x3498DB) \
                        .add_field(name=f'{ESCAPE}d | Data Argument',
                                   value=f'Usage: {ESCAPE}d Data*',
                                   inline=False) \
                        .add_field(name=f'{ESCAPE}c | Color Argument',
                                   value=f'Usage: {ESCAPE}c Num, Num, Num',
                                   inline=False) \
                        .add_field(name=f'{ESCAPE}bg | Background Color Argument',
                                   value=f'Usage: {ESCAPE}bg Num, Num, Num',
                                   inline=False) \
                        .set_thumbnail(url='https://cdn.discordapp.com/attachments/887032886006530111/894227663072395284/embed_pic.png')

                    await ctx.send(embed=embed)

        if len(vdata):
            data = str(vdata).translate({ord(i): None for i in "[',]"})
            now = f'etc/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), random.randint(1, 9999999)}.png'

            create_code(str(data), now, color, bgcolor, box)
            await ctx.send(file=discord.File(now))

            os.remove(now)


def setup(bot):
    bot.add_cog(Interaction(bot))
