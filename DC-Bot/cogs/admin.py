from datetime import datetime
from itertools import cycle

import nextcord
from nextcord.errors import Forbidden, NotFound
from nextcord.ext import commands, tasks

from .etc.config import query, CUR, ESCAPE, EMBED_COLOR, db


# todo:
#   Mute

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
        options = ['rm', 'add', 'sh', 'rl', 'h']  # remove, add, update, showlist, reload
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

                    for i in range(len(id_)):  # here we was
                        embed.add_field(name=f'Value: `{value[i]}`',
                                        value=f'**ID: `{id_[i]}`**', inline=False)

                    await ctx.send(embed=embed)

                elif 'h' == option:
                    embed = nextcord.Embed(title='Cycle Help site!', color=EMBED_COLOR, timestamp=datetime.utcnow()) \
                        .add_field(name=f'{ESCAPE}add', value=f'Usage: {ESCAPE}add [ARG], ARG can take up to 50 Char',
                                   inline=False) \
                        .add_field(name=f'{ESCAPE}rm', value=f'Usage: {ESCAPE}rm [ID], the ID is shown by {ESCAPE}sh',
                                   inline=False) \
                        .add_field(name=f'{ESCAPE}sh', value=f'Usage: {ESCAPE}sh', inline=False) \
                        .add_field(name=f'{ESCAPE}rl', value=f'Usage: {ESCAPE}rl', inline=False)

                    await ctx.send(embed=embed)

                elif 'rl' == option:
                    for i in self.cycle_shit:
                        self.cycle_shit.remove(i)

                    query(self.cycle_shit)
                    self.status = cycle(self.cycle_shit)

                    await ctx.send('**Reloaded!**')

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
        default = 'No Reason Provided'
        try:
            await member.kick(reason=reason)
            embed = nextcord.Embed(title="User Kicked!",
                                   color=EMBED_COLOR, timestamp=datetime.utcnow()) \
                .add_field(name=f'Kicked User: {member}, Reason: {reason if reason != default else "**-**"}',
                           value=f'Kicked by {ctx.message.author}',
                           inline=False)

            await ctx.send(embed=embed)
        except (Forbidden, NotFound):
            await ctx.send('No Permission to Kick a Member!')

    @commands.Command
    async def ban(self, ctx, member: nextcord.Member, *, reason='No Reason Provided'):
        try:
            await member.ban(reason=reason)

            embed = nextcord.Embed(title="User Banned!", color=EMBED_COLOR, timestamp=datetime.utcnow())
            embed.add_field(name=f'Banned User: {member}, Reason: {reason}', value=f'Banned by {ctx.message.author}',
                            inline=False)

            await ctx.send(embed=embed)
        except (Forbidden, NotFound):
            await ctx.send('No Permission to Ban a Member!')

    @commands.Command
    async def unban(self, ctx, member):
        try:
            user = await self.bot.fetch_user(member.strip('<@! >'))
            await ctx.guild.unban(user)

            embed = nextcord.Embed(title="User Unbanned!", color=EMBED_COLOR, timestamp=datetime.utcnow())
            embed.add_field(name=f'Unbanned User: {user}', value=f'Banned by {ctx.message.author}',
                            inline=False)

            await ctx.send(embed=embed)
        except (Forbidden, NotFound):
            await ctx.send('No Permission to Ban a Member or Member was not Found!')

    @commands.Command
    async def mute(self, ctx, *args):
        pass

    @commands.Command
    async def warn(self, ctx, member: nextcord.Member, *, reason='Just a warn'):
        count = 0
        CUR.execute(f"SELECT Warnings, ServerID, UserID FROM users WHERE UserID={int(member.id)};")
        out = CUR.fetchone()
        if out:
            if not out[1:] == (ctx.author.guild.id, member.id):
                print('cogers nicht da')

                query_ = "INSERT INTO users (BotName, UserID, ServerID, Bans, Warnings) VALUES (%s, %s, %s, %s, %s)"
                val = ('API-Goose', int(member.id), int(ctx.author.guild.id), 0, 1)

                CUR.execute(query_, val)

                CUR.execute(
                    f"INSERT INTO Warnings (UserID, ServerID, Warning_msg) VALUES ('{member.id}', '{ctx.author.guild.id}', '{reason}')")
            else:
                print('ist da')
                CUR.execute(f"SELECT Warnings FROM users WHERE UserID='{member.id}', ServerID={ctx.author.guild.id};")
                count = CUR.fetchone()[0] + 1

                CUR.execute(
                    f"UPDATE users SET Warnings='{count}' WHERE UserID='{member.id}', ServerID={ctx.author.guild.id};")
                CUR.execute(
                    f"INSERT INTO Warnings (UserID, ServerID, Warning_msg) VALUES ('{member.id}', {ctx.author.guild.id}, '{reason}')")

        db.commit()

        embed = nextcord.Embed(title='<= Warning =>', timestamp=datetime.now(), color=EMBED_COLOR) \
            .add_field(name=f'**User: ** {member}', value=f'Current warnings: {count + 1}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
