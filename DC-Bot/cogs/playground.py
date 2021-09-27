from discord.ext import commands
import argparse


class Playground(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.parser = argparse.ArgumentParser(description='Create QR Code arguments!')
        self.args = self.parser.parse_args()

        self.parser.add_argument('-bg', '--bgcolor', type=str, help='Enter BG Color behind the Argument!')
        self.parser.add_argument('-c', '--color', type=str, help='Enter Color behind the Argument!')

    @commands.Cog.listener()
    async def on_ready(self):
        print("Playground starts")


def setup(bot):
    bot.add_cog(Playground(bot))
