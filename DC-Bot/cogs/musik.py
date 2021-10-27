import nextcord
from nextcord.ext import commands
import asyncio
import spotdl
import youtube_dl


class Musik(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Command
    async def play(self, ctx, url):
        try:
            await ctx.voice_client.stop()
        except Exception:
            pass
        channel = ctx.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client = nextcord.utils.get(self.bot.voice_clients, guild=guild)


        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}

        if not voice_client.is_playing():
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                audio_source = await nextcord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                voice_client.play(audio_source)


    @commands.Command
    async def pause(self, ctx):
        ctx.voice_client.pause()

        await ctx.send('Paused.')

    @commands.Command
    async def resume(self, ctx):
        ctx.voice_client.resume()

        await ctx.send('Resumed.')

    @commands.Command
    async def stop(self, ctx):
        ctx.voice_client.stop()

        await ctx.send('Stoped.')


def setup(bot):
    bot.add_cog(Musik(bot))
