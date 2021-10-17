import time

import nextcord
from nextcord.ext import commands


class Troll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Command
    async def monkie(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client = nextcord.utils.get(self.bot.voice_clients, guild=guild)
        audio_source = nextcord.FFmpegPCMAudio('E:\python\API-Goose\DC-Bot\cogs\etc\sound\Monkie.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
            time.sleep(1)
            await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(Troll(bot))
