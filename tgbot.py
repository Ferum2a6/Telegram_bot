import telebot
from telebot import types
from config_1 import *
from random import *

bot = telebot.TeleBot(token) # BotFather!!

@bot.message_handler(commands=['start'])
def bot_start(message):
    message_bot = bot.send_message(message.chat.id, choice(cmds_hello))
    message_bot = bot.send_message(message.chat.id, text_commands)
    
@bot.message_handler(commands=['hello'])
def bot_hello(message):
    message_bot = bot.send_message(message.chat.id, choice(cmds_hello))
    
@bot.message_handler(commands=['skills'])
def bot_skills(message):
    message_bot = bot.send_message(message.chat.id, text_commands)

@bot.message_handler(commands=['random_number'])
def button_message(message):
    mk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton('1 - 10')
    b2 = types.KeyboardButton('1 - 20')
    b3 = types.KeyboardButton('1 - 30')
    mk.add(b1, b2, b3)
    bot.send_message(message.chat.id, 'Select range', reply_markup=mk)

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == '1 - 10':
        bot.send_message(message.chat.id, f'Your number: {randint(1, 10)}') # import random!!
    elif message.text == '1 - 20':
        bot.send_message(message.chat.id, f'Your number: {randint(1, 20)}') # import random!!
    elif message.text == '1 - 30':
        bot.send_message(message.chat.id, f'Your number: {randint(1, 30)}') # import random!!
    


"""Start"""
bot.polling(non_stop=True)
