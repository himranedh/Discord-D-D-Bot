import discord
import os
import random
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

client = discord.Client()

d20 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return
    
  if message.content.startswith('!commands'):
    await message.channel.send('!d20 = Rolls a D20 \n !roll = Rolls dice of your choosing')

  if message.content.startswith('!d20'):
    await message.channel.send('You rolled: ' + random.choice(d20))

  if message.content.startswith('!roll'):
    
    return

keep_alive()
client.run(my_secret)