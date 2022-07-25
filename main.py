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
	await.ctx.channel.purge(limit=amount)

client.run('MTAwMDAzODY4OTI0MzY2ODYyMA.GDXrrR.pxABXtCL69LjKkrC8Pu8Sgo3WHpTxktGj9ccw8')