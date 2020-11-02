# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


def get_some_text():
    f = open('testText.txt', "r")
    text = f.readlines()
    f.close
    return text


def write_some_text():
    f = open('testText.txt', "a")
    f.write("Extra Line")
    f.close()


client= commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready. ')

@client.command()
async def respond(ctx):
    await ctx.send('hello from the other side')

@client.command()
async def test(ctx):
    await ctx.send(get_some_text())

@client.command()
async def testWrite(ctx):
    write_some_text()


client.run(TOKEN)
