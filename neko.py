# Running on Discord
import discord
# ...and on telegram...
import telebot
# ...at the same time!
from multiprocessing import Process
import sys
# For random number fun.
import random
# Logging, maybe?
import os
# For a good chatting.
import aiml
# Well, this here is my settings file. It's private!
import config
# Also, some cool phrases :3
import phrases

# Initializing our AIML kernel...
kernel = aiml.Kernel()
# ...our Discord bot...
client = discord.Client()
# ...and our telegram bot.
bot = telebot.TeleBot(config.tgtoken)

# Some text for roll.
rolltext = [
    "I've rolled a {number}.",
    "Rolled a {number} right now.",
    "I've got a {number} here.",
]

if os.path.isfile("brain.brn"):
   kernel.bootstrap(brainFile = "brain.brn")
   # Me has brain
else:
   # Me has no brain
   kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml")
   kernel.saveBrain("brain.brn")
   # Me gained brain

def rundiscord():
   client.run(config.discordtoken)
   #Running our Discord bot.

def runtelegram():
   bot.polling()
   #Running our telegram bot.

# ---------------------------------------------------------- #
# Here is the Discord part of the code.                      #
# ---------------------------------------------------------- #
# Am I ready?
@client.event
async def on_ready():
      print("I'm online, and... ready to... rock! Yay!")
      print("I mean, I'm up and running!")
      # Yes, I am!

@client.event
async def on_message(message):
   # Oh, a message!
      if message.author == client.user:
         # Shucks, I won't talk to myself!
         return
      # Let's put some AIML in here! Also, some more code!
      # Yay for me!
      #if (message.author == (client.user.id == '291936579847716866')):
      #   await message.channel.send("Yuuki-sama! \\o/")
      #   return
      # H-HEWWO?
      if (message.content.startswith("Hello")):
         await message.channel.send(random.choice(phrases.hellotext))
         return
      # Ping... Pong?
      elif (message.content.startswith("Ping")):
         await message.channel.send(random.choice(phrases.pongs))
         return
      # Rolling a d6:
      elif (message.content.startswith("/d6")):
         number = random.randint(1, 7)
         await message.channel.send(random.choice(rolltext).format(number))
         return
      # Rolling a d20:
      elif (message.content.startswith("/d20")):
         number = random.randint(1, 21)
         await message.channel.send(random.choice(rolltext).format(number))
         return
      # Rolling two d20s:
      elif (message.content.startswith("/2d20")):
         number1 = random.randint(1, 21)
         number2 = random.randint(1, 21)
         await message.channel.send("I've got a {}...".format(number1))
         await message.channel.send("and a {}. Is it good or bad?".format(number2))
         return
      # Wait up! I'll answer you!
      else:
         response = kernel.respond(str(message).lower())
         await message.channel.send(response)
         return
# -------------------------------------------------------- #
# And here is the telegram part of our bot.                #
# -------------------------------------------------------- #
@bot.message_handler(commands=['start'])
def send_hello(message):
   bot.send_message(message.chat.id, u'Hewwo! UwU\nI\'m Yuuma, but you can call me Neko!')
   # H-HEWWO?

@bot.message_handler(func=lambda message: True, content_types=['text'])
def answer(message):
   kernel.setPredicate('name', message.chat.first_name, message.chat.id)
   response2 = kernel.respond(message.text.lower(), message.chat.id)
   bot.send_message(message.chat.id, response2)
   # Imma answer you!


# Run them both at once!
if __name__ == "__main__":
   p1 =Process(target=rundiscord)
   p1.start()
   p2 = Process(target=runtelegram)
   p2.start()