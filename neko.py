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
bot.sort_replies()
# ...our Discord bot...
client = discord.Client()
# ...and our telegram bot.
bot = telebot.TeleBot(config.tgtoken)

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
         await channel.send(random.choice(phrases.hellotext))
         return
      # Ping... Pong?
      elif (message.content.startswith('Ping')):
         await channel.send(random.choice(phrases.pongs))
         return
      # Sending from Discord to Telegram:
      elif (message.content.startswith('$sendtotg')):
         msgtotg = message.content
         await postFromDiscord(msgtotg)
         await channel.send('Message sent to Telegram!')
      # Wait up! I'll answer you!
      else:
         response = bot.reply("localuser", message.content)
         await channel.send(response)
         return

# -------------------------------------------------------- #
# And here is the telegram part of our bot.                #
# -------------------------------------------------------- #
@bot.message_handler(commands=['start'])
def send_hello(message):
   bot.send_message(message.chat.id, u'Hewwo! UwU\nI\'m Yuuma, but you can call me Neko!')
   # H-HEWWO?

@bot.message_handler(commands=['d6'])
def roll_d6(message):
   d6 = random.randint(1, 7)
   bot.send_message(message.chat.id, random.choice(phrases.rolltext).format(d6))
   # Rolled a d6.

@bot.message_handler(commands=['d20'])
def roll_d20(message):
   d20 = random.randint(1, 21)
   bot.send_message(message.chat.id, random.choice(phrases.rolltext).format(d20))
   # Rolled a d20.

@bot.message_handler(commands=['2d20'])
def roll_2d20(message):
   d20_1 = random.randint(1, 21)
   d20_2 = random.randint(1, 21)
   bot.send_message(message.chat.id, 'I\'ve got a {} '.format(d20_1) + 'and a {}.'.format(d20_2))

@bot.message_handler(func=lambda message: True, content_types=['text'])
def answer(message):
   kernel.setPredicate('name', message.chat.first_name, message.chat.id)
   response2 = bot.reply("localuser", message.text)
   bot.send_message(message.chat.id, response2)
   # Imma answer you!
def postFromDiscord(message):
   bot.send_message(message.chat.id, message.text)


# Run them both at once!
if __name__ == '__main__':
   p1 =Process(target=rundiscord)
   p1.start()
   p2 = Process(target=runtelegram)
   p2.start()