import random

from discord.ext import commands


class Ip_module(bot):
  def __init__(bot):
    self.bot = bot

  @commands.command(aliases=['createip', 'cip'])
  async def get_ip(self, ctx, *args):
    await ctx.send(f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}')


def setup(bot):
  bot.add_cog(Ip_module(bot))