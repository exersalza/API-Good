import random

from discord.ext import commands


class IpModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['createip', 'cip'])
    async def get_ip(self, ctx, *args):
        await ctx.send(
            f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}')


def setup(bot):
    bot.add_cog(IpModule(bot))
