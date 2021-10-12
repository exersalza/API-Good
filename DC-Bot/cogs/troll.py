import nextcord
from nextcord.ext import commands


# todo:
#   Voice troll option

class Troll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Troll(bot))
