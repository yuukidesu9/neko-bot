import asyncio
import discord
import random
import os
import aiml

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
      if ("d6" in text.content == True):
         number = random.randint(1, 7)
         await client.send_message(text.channel, random.choice(rolltext).format(number))
         return
      #Rolling a d20:
      elif ("d20" in text.content == True):
         number = random.randint(1, 21)
         await client.send_message(text.channel, random.choice(rolltext).format(number))
         return
      #Rolling two d20:
      elif ("2d20" in text.content == True):
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
      #Here's the old code:
      #if text.content.startswith("Hello") or text.content.startswith("Hey"):
      #     await client.send_message(text.channel, random.choice(hellotext))
      #     return
      #if text.content.startswith("ping") or text.content.startswith("Ping"):
      #     await client.send_message(text.channel, random.choice(pongs))
      #     return
client.run('NTA2ODg1MzQ3OTk3Nzc3OTIy.DrpEog.fLjlzw02rXw5j68iEZuU7s0ZiI8')
