import argparse
import os
import random
from datetime import datetime

import discord
from API.qrcode.qr_creator import create_code
from discord.ext import commands
from discord.ext.commands import CommandNotFound

from .etc.config import PREFIX, ESCAPE


# todo:
#  IQAir, BoredAPI implement


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
            return await ctx.send("Command/API nicht gefunden.")

    @commands.Command
    async def create(self, ctx, *args):  # argparse function

        def converter(list):
            return (*list, )

        colores = []
        bgcolores = []

        color = (0, 0, 0)
        bgcolor = (255, 255, 255)
        box = 6
        data = None

        options = ['b', 'c', 'bg', 'd']

        async def parser(rounds, option, validate):
            var = 0
            while var != rounds:
                var += 1
                try:
                    val = int(args[args.index(f'{ESCAPE}{option}') + var].strip(','))
                except ValueError:
                    await ctx.send('Ein argument ist kein Integer')
                    break

                if type(val) == int:  # Double check
                    validate.append(val)
                else:
                    break

            return converter(validate)

        for option in options:
            if f'{ESCAPE}{option}' in list(args):
                if 'c' == option:  # color argparser
                    color = await parser(3, 'c', colores)

                elif 'bg' == option:  # back-color argparser
                    bgcolor = await parser(3, 'bg', bgcolores)

                elif 'd' == option:
                    pass

                elif 'b' == option:  # box-size argparser
                    try:
                        coggers_box = int(args[args.index(f'{ESCAPE}{option}') + 1].strip(','))
                        if coggers_box >= 100:
                            await ctx.send('Das Box argument ist zu Groß, bitte wähle eine Zahl die unter 100 liegt')
                            break
                        else:
                            box = coggers_box

                    except ValueError:
                        await ctx.send(ValueError)
                        break

        if data is not None:
            now = f'etc/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), random.randint(1, 9999999)}.png'

            create_code(str(vdata), now, color, bgcolor, box)
            await ctx.send(file=discord.File(now))

            os.remove(now)


def setup(bot):
    bot.add_cog(Interaction(bot))
