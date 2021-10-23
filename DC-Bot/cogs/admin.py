from datetime import datetime
from itertools import cycle

import nextcord
from nextcord.ext import commands, tasks

from .etc.config import query, CUR, ESCAPE, EMBED_COLOR, db


#todo:
#   Ban, Kick, Mute,

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.cycle_shit = []
        query(self.cycle_shit)
        self.status = cycle(self.cycle_shit)

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
        options = ['rm', 'add', 'sh', 'rl']  # remove, add, update, showlist
        for option in options:
            if f'{ESCAPE}{option}' in list(args):
                if 'rm' == option:
                    try:
                        id_ = args[args.index(f'{ESCAPE}rm') + 1]
                    except IndexError:
                        await ctx.send('Please enter a ID to delete')
                        break
                    CUR.execute(f"DELETE FROM roll_text WHERE ID=?", id_)
                    db.commit()
                    await ctx.send(f"Die ID: `{id_}` wurde Gelöscht!")

                elif 'add' == option:
                    try:
                        ind = args.index(f'{ESCAPE}add')
                        entry = ' '.join(args[ind + 1:])
                    except IndexError:
                        await ctx.send('Please NOTHING')
                        break
                    CUR.execute(f"INSERT INTO roll_text(Text, Name) VALUES (?, 'API-Goose')", entry)
                    db.commit()
                    await ctx.send(f"Der Eintrag: `{entry}` wurde erstellt!")

                elif 'sh' == option:
                    embed = nextcord.Embed(title='Show cycle Options!', color=EMBED_COLOR, timestamp=datetime.utcnow())

                    CUR.execute("SELECT ID, Text FROM roll_text WHERE Name='API-Goose';")
                    fetcher = CUR.fetchall()

                    id_ = [item[0] for item in fetcher]
                    value = [item[1] for item in fetcher]

                    CUR.execute("SELECT roll_txt_val FROM tokens WHERE name='API-Goose';")
                    counter = CUR.fetchone()

                    for i in range(counter[0]):  # here we was
                        embed.add_field(name=f'Value: `{value[i]}`',
                                        value=f'**ID: `{id_[i]}`**', inline=False)

                    await ctx.send(embed=embed)

                elif 'rl' == option:
                    for i in self.cycle_shit:
                        self.cycle_shit.remove(i)

                    embed = nextcord.Embed(title='Realoading...', color=EMBED_COLOR)

                    query(self.cycle_shit)
                    self.status = cycle(self.cycle_shit)

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

        embed = nextcord.Embed(title=poll_query[0], color=EMBED_COLOR, timestamp=datetime.utcnow())

        await ctx.send('You\'r current Poll looks like', embed=embed)

    ## Moderation ##

    @commands.Command
    async def kick(self, ctx, member: nextcord.Member, *, reason='No Reason Provided'):
        await member.kick(reason=reason)
        embed = nextcord.Embed(title="User Kicked!",
                              description="**{0}** was kicked by **{1}**! \r\nReason **{2}**".format(member,
                                                                                                     ctx.message.author,
                                                                                                     reason),
                              color=EMBED_COLOR)
        await ctx.send(embed=embed)

    @commands.Command
    async def ban(self, ctx, member: nextcord.Member, *, reason='No Reason Provided'):
        await member.ban(reason=reason)

        embed = nextcord.Embed(title="User Banned!", color=EMBED_COLOR)
        embed.add_field(name='', value='', inline=False)

        await ctx.send(embed=embed)

    @commands.Command
    async def unban(self, ctx, *args):
        pass

    @commands.Command
    async def mute(self, ctx, *args):
        pass

    @commands.Command
    async def warning(self, ctx, *args):
        pass


def setup(bot):
    bot.add_cog(Admin(bot))
