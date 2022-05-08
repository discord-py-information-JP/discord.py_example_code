# discord.ext.commandの一番最低限なBot

import discord
from discord.ext import commands
import random

description = '''discord.ext.commandの一番最低限なBot'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
  await ctx.send("pong")

bot.run('token')
