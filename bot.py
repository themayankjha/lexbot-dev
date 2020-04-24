import discord
from discord.ext import commands
from tokenkey import tokenkey

client = commands.Bot(command_prefix= '$')

@client.event
async def on_ready():
    print("Hi, I'm Online and ready to funtion.")
@client.command()
async def ping(ctx):
    await ctx.send('pong')
@client.command()
async def bruh(ctx):
    await ctx.send("Bruh")

client.run(tokenkey)