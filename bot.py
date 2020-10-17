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
@client.command()
async def hello(ctx):
    await ctx.send("Hello World!")
@client.command()
async def bye(ctx):
    await ctx.send("Ciao")
@client.command()
async def kill(ctx):
    await ctx.send("Thats illegal man")
client.run(tokenkey)
