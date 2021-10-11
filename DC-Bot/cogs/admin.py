from itertools import cycle
from datetime import datetime

import nextcord as discord
from nextcord.ext import commands, tasks

from .etc.config import cycle_query, CUR, ESCAPE, EMBED_COLOR


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.status = cycle(cycle_query)

    @tasks.loop(seconds=30)
    async def status_task(self):
        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.Activity(type=discord.ActivityType.playing,
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
                    e = discord.Embed(title='Show cycle Options!', color=EMBED_COLOR, timestamp=datetime.utcnow())
                    CUR.execute("SELECT * FROM roll_text WHERE Name='API-Goose'")

                    contents = []
                    for val in CUR.fetchall():
                        contents.append(val)

                    for i in contents:
                        e.add_field(name=f'Value: `{i[1]}`', value=f'**ID: `{contents.index(i)}`**', inline=False)

                    await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Admin(bot))
