import discord
import youtube_dl
from discord.ext import commands


# todo:
#   Voice troll option


class Troll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def monkie(self, ctx):
        if ctx.author.voice is None:
            await ctx.send('Your not in a Voice channel!')

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def play(self, ctx, url):
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}

        vc = ctx.voice_client
        print(1)

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            print(2)
            url2 = info['formats'][0]['url']
            print(3)
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            print(4)
            vc.play(source)
            print(5)

    @commands.command()
    async def join(self, ctx):
        print('joiuner')
        channel = ctx.author.voice.channel
        print(channel)
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(Troll(bot))
