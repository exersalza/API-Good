import nextcord
from nextcord.ext import commands
from nextcord.errors import HTTPException

# todo:
#   Voice troll option


class Troll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['MONKEY', 'Monkie'])
    async def monkie(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.Command
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()


    @commands.Command
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(Troll(bot))
