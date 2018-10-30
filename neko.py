import asyncio
import discord
import random
import os

client = discord.Client()

@client.event
async def on_ready():
     print("I'm on!")

async def on_message(text):
     hello_a = "Oh, hi!"
     hello_b = "Hey there!"
     hello_c = "Hello!"
     hello_d = "Hey, what's up?"
     hello_e = "Hewwo :3"
     hello_f = "Um... hi?"
     if(text.author.id == 'BOT ID'): return
     else:
          if text.content.startswith("Hello") or text.content.startswith("hello") or text.content.startswith("hullo") or text.content.startswith("Hullo") or text.content.startswith("Hi") or text.content.startswith("hi"):
               answer = random.choice([hello_a, hello_b, hello_c, hello_d, hello_e, hello_f])
               await client.send_message(text.channel, answer)
               return
          if text.content.startswith("Ping") or text.content.startswith("ping"):
               await client.send_message(text.channel, "Pong, I guess?")
               return
client.run('NTA2ODg1MzQ3OTk3Nzc3OTIy.DrpEog.fLjlzw02rXw5j68iEZuU7s0ZiI8')
