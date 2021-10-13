from itertools import cycle
from datetime import datetime

import discord as discord
from discord import Message
from discord.ext import commands, tasks

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

	@commands.Command
	async def poll(self, ctx, *args):
		poll_query = []

		await ctx.send('**Welcome to the Poll-Wizard**\nPlease enter your title below')
		msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
		poll_query.append(msg.content)

		await ctx.send(f'**Your new title is: `{msg.content}`**\nPlease enter if the Poll is should be Anonym (True or False)')

		check = True
		while check:
			msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)

			if msg.content.lower() == 'true':
				poll_query.append(msg.content)
				await ctx.send('**The Poll is Anonym**\nPlease enter the Columns for the Poll')
				break

			elif msg.content.lower() == 'false':
				poll_query.append(msg.content)
				await ctx.send('**The Poll is not Anonym**\nPlease enter the Columns for the Poll, you can write it line for line. With `end` can you stop the input')
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



		#
		#
		#	USE DISCORD COMPONENTs
		#	
		#
def setup(bot):
    bot.add_cog(Admin(bot))
