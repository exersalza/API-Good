import random
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

        option = {1: {'path': 'E:\python\API-Goose\DC-Bot\cogs\etc\sound\Monkie.wav', 'time': 1}, 2: {'path': 'E:\\python\\API-Goose\\DC-Bot\\cogs\\etc\\sound\\two, four.mp3', 'time': 4}}

        guild = ctx.guild
        voice_client = nextcord.utils.get(self.bot.voice_clients, guild=guild)

        if random.randint(0, 1):
            audio_source = nextcord.FFmpegPCMAudio(option[1]['path'])
            time_ = option[1]['time']

        else:
            audio_source = nextcord.FFmpegPCMAudio(option[2]['path'])
            time_ = option[2]['time']

        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
            time.sleep(time_)
            await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(Troll(bot))
