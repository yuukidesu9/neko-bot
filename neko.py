# For random number fun.
import random
# Logging, maybe?
import os
# For a good chatting.
import aiml
# For running only on business hours.
import schedule
import time
# Running on telegram...
from telegram.ext import Updater, CommandHandler
# ...and Discord at the same time!
import discord
import asyncio
# Well, this here is my settings file. It's private!
import config

client = discord.Client()
kernel = aiml.Kernel()

rolltext = [
    "I've rolled a {number}.",
    "Rolled a {number} right now.",
    "I've got a {number} here.",
]

if os.path.isfile("brain.brn"):
   kernel.bootstrap(brainFile = "brain.brn")
else:
   kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml")
   kernel.saveBrain("brain.brn")

@client.event
async def on_ready():
   print("I'm online, and... ready to... rock! Yay!")
   print("I mean, I'm up and running!")

@client.event
async def on_message(text):
   message = text.content
   if text.author == client.user:
      return
   else:
      #Let's put some AIML in here! Also, some roll code!
      #Rolling a d6:
      if (text.content == "d6"):
         number = random.randint(1, 7)
         await client.send_message(text.channel, random.choice(rolltext).format(number))
         return
      #Rolling a d20:
      elif (text.content == "d20"):
         number = random.randint(1, 21)
         await client.send_message(text.channel, random.choice(rolltext).format(number))
         return
      #Rolling two d20:
      elif (text.content == "2d20"):
         number1 = random.randint(1, 21)
         number2 = random.randint(1, 21)
         await client.send_message(text.channel, "I've got a {}...".format(number1))
         await client.send_message(text.channel, "and a {}. Is it good or bad?".format(number2))
         return
      #Answering a message:
      else:
         response = kernel.respond(message.upper())
         await client.send_message(text.channel, response)
         return
updater = Updater(config.tgtoken)
client.run(config.discordtoken)