import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print("Borex is UP and running")

@client.command()
async def ping(ctx):
	await ctx.send(f'{round(client.latency*1000)} ms')

@client.command(aliases=['8ball'])
async def eight_ball(ctx, *, question):
	response = ['balls, in your dream retard',
				'very very gay',
				'oof',
				'very doubtful',
				'https://cdn.discordapp.com/attachments/920697181994889236/951446664558825482/1622545226719-1.mp4',
				'yay sure',
				'dorime',
				'balls in your jaws',
				'shut the fuck up porn addict'
				]

	await ctx.send(f'Question -> {question}\nAnswer-> {random.choice(response)}')

@client.command()
async def clear(ctx, amount=1):
	await ctx.channel.purge(limit=amount)
	await ctx.send(f'{amount} messages have been deleted.')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'{member} have been kicked from the server.\nReason: {reason}')

# ban command
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'{member} have been banned from the server.\nReason: {reason}')

@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'{user.name} have been unbanned from the server.')
			return

client.run('MTAwMDAzODY4OTI0MzY2ODYyMA.GDXrrR.pxABXtCL69LjKkrC8Pu8Sgo3WHpTxktGj9ccw8')