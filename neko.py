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
    hellotext = [
        'Oh, hi!',
        'Hey there! o/',
        'Hello! ^-^',
        'Hey, what\'s up?',
        'Henllo owo',
        'Um... hi? \'-.-',
    ]
    greet = [
         'Hello',
         'Hi',
         'Hewwo',
         'Henllo',
         'Hey',
         'Hullo',
    ]
    command = [
         'Ping',
         'Roll',
         'Hug',
    ]
    if(text.author.id == 'BOT ID'): return
    else:
         messagetext = text.content
         if messagetext in greet:
              await client.send_message(random.choice(possible_responses))
              return
         if messagetext in command:
              await client.send_message(text.channel, "Pong, I guess?")
              return
client.run('NTA2ODg1MzQ3OTk3Nzc3OTIy.DrpEog.fLjlzw02rXw5j68iEZuU7s0ZiI8')
