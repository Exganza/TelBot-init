import telebot
import time

# API_TOKEN
bot_token = '*******************************'
bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    pass


@bot.message_handler(commands=['help'])
def send_welcome(message):
    pass

# Handle normal messages
@bot.message_handler(func=lambda msg: msg.text is not None)
def at_bot(message):
    text = message.text
    
    
    
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)