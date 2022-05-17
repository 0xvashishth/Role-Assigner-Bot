import os
import discord
from replit import db

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'
        .format(client))

my_secret = os.environ['TOKEN']
client.run(my_secret)