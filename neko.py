import asyncio
import discord
import random
import os

client = discord.Client()

@client.event
async def on_ready():
     print("I'm on!")

async def on_message(text):
    hellotext = [
        'Oh, hi!',
        'Hey there! o/',
        'Hello! ^-^',
        'Hey, what\'s up?',
        'Henllo owo',
        'Um... hi? \'-.-',
    ]
    pongs = [
        'Pong! ^-^',
        'Um... pong?',
        'Am I supposed to tell \'pong\'...?',
        'Pong, I... guess?'
    if(text.author.id == 'BOT ID'): return
    else:
         messagetext = text.content
         if messagetext.startswith("Hello") or messagetext.startswith("Hey"):
              await client.send_message(random.choice(hellotext))
              return
         if messagetext == "ping" or messagetext == "Ping":
              await client.send_message(random.choice(pongs))
              return
client.run('NTA2ODg1MzQ3OTk3Nzc3OTIy.DrpEog.fLjlzw02rXw5j68iEZuU7s0ZiI8')
