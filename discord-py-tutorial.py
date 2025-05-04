import discord
from discord import app_commands
import os

TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=912361242985918464))
    print(f'Logged in as {client.user}')


@tree.command(
    name="ping",
    description="Gives bot latency",
    guild=discord.Object(912361242985918464)
)
async def ping(interaction):
    await interaction.response.send_message(f'My ping is {client.latency} ms')


client.run(TOKEN)
