import discord
import os
TOKEN = os.getenv('TOKEN')

bot = discord.Bot()


@bot.listen()
async def on_ready():
    print('bot is ready!')


@bot.slash_command(name='hi', guild_ids=[912361242985918464])
async def hello(ctx):
    await ctx.respond(f'hello! My latency is: {bot.latency * 1000} ms')

bot.run(TOKEN)
