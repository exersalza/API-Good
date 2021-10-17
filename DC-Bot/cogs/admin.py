from datetime import datetime
from itertools import cycle

import nextcord
from nextcord.ext import commands, tasks

from .etc.config import query, CUR, ESCAPE, EMBED_COLOR


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        cycle_shit = []
        query(cycle_shit)
        self.status = cycle(cycle_shit)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ready at {datetime.now().strftime("%H:%M:%S")}')

        await self.status_task.start()

    @tasks.loop(seconds=30)
    async def status_task(self):
        await self.bot.change_presence(status=nextcord.Status.idle,
                                       activity=nextcord.Activity(type=nextcord.ActivityType.watching,
                                                                 name=next(self.status)))

    @commands.command()
    async def cycle(self, ctx, *args):
        options = ['rm', 'add', 'u', 'sh']  # remove, add, update, showlist
        for option in options:
            if f'{ESCAPE}{option}' in list(args):
                if 'rm' == option:
                    try:
                        CUR.execute(f"DELETE FROM roll_text WHERE ID={args[args.index(f'{ESCAPE}rm')]}")
                        await ctx.send(f'Die ID: `{args[args.index(f"{ESCAPE}")]}`')
                    except Exception:
                        pass
                elif 'add' == option:
                    pass
                elif 'u' == option:
                    pass
                elif 'sh' == option:
                    e = nextcord.Embed(title='Show cycle Options!', color=EMBED_COLOR, timestamp=datetime.utcnow())

                    CUR.execute("SELECT ID, Text FROM roll_text WHERE Name='API-Goose'")
                    fetcher = CUR.fetchall()

                    id_ = [item[0] for item in fetcher]
                    value = [item[1] for item in fetcher]

                    for i in id_:  # here we was
                        e.add_field(name=f'Value: `{contents[contents.index(i)]}`',
                                    value=f'**ID: `{contents.index(i)}`**', inline=False)

                await ctx.send(embed=e)

    @commands.Command
    async def poll(self, ctx, *args):
        poll_query = []

        await ctx.send('**Welcome to the Poll-Wizard**\nPlease enter your title below')
        msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        poll_query.append(msg.content)

        await ctx.send(
            f'**Your new title is: `{msg.content}`**\nPlease enter if the Poll is should be Anonym (True or False)')

        check = True
        while check:
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)

            if msg.content.lower() == 'true':
                poll_query.append(msg.content)
                await ctx.send('**The Poll is Anonym**\nPlease enter the Columns for the Poll')
                break

            elif msg.content.lower() == 'false':
                poll_query.append(msg.content)
                await ctx.send(
                    '**The Poll is not Anonym**\nPlease enter the Columns for the Poll, you can write it line for line. With `end` can you stop the input')
                break

            else:
                await ctx.send(f'Please type True or False and not: `{msg.content}`')
                continue

        while check:
            print('begin')
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            if not msg.content.lower() == 'end':
                print('format')
                poll_query.append(f'{msg.content}\n')
            else:
                break

        embed = discord.Embed(title=poll_query[0], color=EMBED_COLOR, timestamp=datetime.utcnow())

        await ctx.send('You\'r current Poll looks like', embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
