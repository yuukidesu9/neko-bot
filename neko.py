# Running on Discord
import discord
# ...and on telegram at the same time!
import telebot
# For random number fun.
import random
# Logging, maybe?
import os
# For a good chatting.
import aiml
# For running only on business hours.
import schedule
import time
# Well, this here is my settings file. It's private!
import config

kernel = aiml.Kernel()
bot = telebot.TeleBot(config.tgtoken)
client = discord.Client()

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
# ---------------------------------------------------------- #
# Here is the Discord part of the code.                      #
# ---------------------------------------------------------- #
@client.event
async def on_ready():
      print("I'm online, and... ready to... rock! Yay!")
      print("I mean, I'm up and running!")
@client.event
async def on_message(message):
      if message.author == client.user:
         return
      #Let's put some AIML in here! Also, some roll code!
      #Rolling a d6:
      if (message.content.startswith("/d6")):
         number = random.randint(1, 7)
         await message.channel.send(random.choice(rolltext).format(number))
         return
      #Rolling a d20:
      elif (message.content.startswith("/d20")):
         number = random.randint(1, 21)
         await message.channel.send(random.choice(rolltext).format(number))
         return
      #Rolling two d20:
      elif (message.content.startswith("/2d20")):
         number1 = random.randint(1, 21)
         number2 = random.randint(1, 21)
         await message.channel.send("I've got a {}...".format(number1))
         await message.channel.send("and a {}. Is it good or bad?".format(number2))
         return
      #Answering a message:
      else:
         response = kernel.respond(message.upper())
         await message.channel.send(response)
         return
# -------------------------------------------------------- #
# And here is the telegram part of our bot.                #
# -------------------------------------------------------- #
@bot.message_handler(commands=['start'])
def send_hello(message):
   bot.send_message(message.chat.id, u'Hewwo! I\'m Yuuma, but you can call me Neko!')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def answer(message):
   kernel.setPredicate('name', message.chat.first_name, message.chat.id)
   response2 = kernel.respond(message.text.upper(), message.chat.id)
   bot.send_message(message.chat.id, response2)

# Run them both!
bot.polling()
client.run(config.discordtoken)