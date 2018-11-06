import asyncio
import discord
import random
import os
import phrases

client = discord.Client()

@client.event
async def on_ready():
     print("I'm online, and... ready to... rock?")

@client.event
async def on_message(text):
    if text.author == client.user:
         return
     
    else:
         if text.content.startswith("Hello") or text.content.startswith("Hey"):
              await client.send_message(text.channel, random.choice(hellotext))
              return
         if text.content.startswith("ping") or text.content.startswith("Ping"):
              await client.send_message(text.channel, random.choice(pongs))
              return
client.run('NTA2ODg1MzQ3OTk3Nzc3OTIy.DrpEog.fLjlzw02rXw5j68iEZuU7s0ZiI8')
