import telebot
from telebot import types
import time

def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton("but1")
    btn2 = types.KeyboardButton("but2")
    btn3 = types.KeyboardButton("but3")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3)

    return keyboard


# API_TOKEN
bot_token = '*******************************'
bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, text="Start command message here", reply_markup=main_keyboard())


@bot.message_handler(commands=['help'])
def send_welcome(message):
    pass


@bot.message_handler(func=lambda msg: msg.text is not None)
def at_bot(message):
    text = message.text
    
    
    
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)