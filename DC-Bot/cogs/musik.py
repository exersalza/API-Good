import nextcord
from nextcord.ext import commands
from nextcord.utils import get
import asyncio
import spotdl
import youtube_dl
from nextcord.errors import ClientException

from .etc.config import db, CUR


class Musik(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Command
    async def pause(self, ctx):
        ctx.voice_client.pause()

        await ctx.send('Paused.')


    @commands.Command
    async def play(self, ctx, url):

        channel = ctx.author.voice.channel
        try:
            await channel.connect()
        except ClientException:
            await ctx.send('The bot is can only play in one channel!')

        guild = ctx.guild
        voice_client = nextcord.utils.get(self.bot.voice_clients, guild=guild)


        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)

            if not voice_client.is_playing():
                url2 = info['formats'][0]['url']
                audio_source = await nextcord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                voice_client.play(audio_source)
            else:
                await ctx.send(f'A song is Already Playing.\r Channel: {channel}, Song: {info["title"]}')

    @commands.Command
    async def resume(self, ctx):

        voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
        print(self.bot.voice_channel)

        if ctx.author.voice_channel == self.bot.voice_channel:

            ctx.voice_client.resume()
            await ctx.send('Resumed.')
        else:
            print('Äc')

    @commands.Command
    async def stop(self, ctx):
        ctx.voice_client.stop()
        await ctx.send('Stoped.')


def setup(bot):
    bot.add_cog(Musik(bot))
