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



"""Start"""
bot.polling(non_stop=True)