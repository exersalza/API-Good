from discord.ext import commands
from datetime import datetime


class Interaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ready at {datetime.now().strftime("%H:%M:%S")}')


def setup(bot):
    bot.add_cog(Interaction(bot))
