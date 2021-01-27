# Running on Discord
import discord
from multiprocessing import Process
import sys
# For random number fun.
import random
# Logging, maybe?
import os
# For a good chatting.
from rivescript import RiveScript
import re
# Well, this here is my settings file. It's private!
import config
# Also, some cool phrases :3
import phrases

# Initializing our bot instance...
neko = RiveScript(utf8=True, debug=False)
neko.unicode_punctuation = re.compile(r'[.,!?;:]')
neko.load_directory("rive")
neko.sort_replies()
# ...and our Discord bot.
client = discord.Client()

def rundiscord():
   client.run(config.discordtoken)
   #Running our Discord bot.
   print("Discord connection ok.")

# ---------------------------------------------------------- #
# Here is the Discord code.                                  #
# ---------------------------------------------------------- #
# Am I ready?
@client.event
async def on_ready():
      print('I\'m online, and... ready to... rock! Yay!')
      print('I mean, I\'m up and running!')
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
      if (message.content.startswith('Hello')):
         await message.channel.send(random.choice(phrases.hellotext))
         return
      # Ping... Pong?
      elif (message.content.startswith('Ping')):
         await message.channel.send(random.choice(phrases.pongs))
         return
      # Wait up! I'll answer you!
      else:
         response = neko.reply("localuser", message.content)
         await message.channel.send(response)
         return

# Run the bot at once!
if __name__ == '__main__':
   p1 =Process(rundiscord)
   p1.start()