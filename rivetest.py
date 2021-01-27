import re
from rivescript import RiveScript

bot = RiveScript(utf8=True, debug=False)
bot.unicode_punctuation = re.compile(r'[.,!?;:]')
bot.load_directory("rive")
bot.sort_replies()
def response(text):
    
    return reply

input_text = input()
reply_text = bot.reply("localuser", input_text)
print ("Bot: " + str(reply_text))