# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def get_some_text():
    f = open('testText.txt', "r")
    f.close()
    return f

client= commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready. ')

@client.command()
async def respond(ctx):
    await ctx.send('hello #8')

@client.command()
async def test(ctx):
    await ctx.send(get_some_text())


client.run(TOKEN)
