import discord
from discord.ext import commands
from discord.errors import HTTPException
import asyncio

# todo:
#   Voice troll option


class Troll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['MONKEY', 'Monkie'])
    async def monkie(self, ctx):
        # grab the user who sent the command
        print('1')
        voice_channel = ctx.author.voice.channel
        print('1+')
        print('2')
        # only play music if user is in a voice channel
        # grab user's voice channel
        print('self.before')
        await ctx.send('User is in channel: ' + voice_channel.name)
        print('self.channel')
        # create StreamPlayer
        vc = await voice_channel.connect()
        print('3')
        ctx.play('etc/sound/Monkie.mp3')
        print('4')

        await vc.disconnect()


    @commands.Command
    async def join(self, ctx):
        print('joiuner')
        channel = ctx.author.voice.channel
        print(channel)
        await channel.connect()


    @commands.Command
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(Troll(bot))
