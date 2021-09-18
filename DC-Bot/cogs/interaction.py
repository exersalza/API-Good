import argparse
from datetime import datetime

import discord
from API.qrcode.qr_creator import create_code
from discord.ext import commands
from discord.ext.commands import CommandNotFound


#todo:
# !create localfile delete after send

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

        print('cogs')

        # options = ['-c', '-b', '-bg']
        # # await ctx.send(f'{args[args.index("-c") + var]} is not an Number!')
        #
        # arg = []
        #
        # if [x for x in args if x == '-c']:
        #     var = 1
        #     while var != 4:
        #         if args[args.index('-c') + var].isdigit():
        #             arg.append(args[args.index('-c') + var])
        #             var += 1
        #         else:
        #             await ctx.send('!create can only take numbers as Argument')
        #             var = 4

        # return
        create_code('coggörs')
        await ctx.send(file=discord.File('test.png'))


def setup(bot):
    bot.add_cog(Interaction(bot))
