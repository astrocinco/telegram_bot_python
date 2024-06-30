import os
from dotenv import load_dotenv
import telebot
from respuestas import *


# Setup
print("free_code_camp_bot.py corriendo")
respuestas = load_respuestas()
load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)



# Todos los comandos que Arturito reconoce
@bot.message_handler(commands=['comienzo'])
def send_welcome(message):
    bot.reply_to(message, respuestas["comienzo"])

@bot.message_handler(commands=['arturito'])
def send_welcome(message):
    bot.reply_to(message, respuestas["arturito"])

@bot.message_handler(commands=['calendario'])
def send_welcome(message):
    bot.reply_to(message, respuestas["calendario"])

@bot.message_handler(commands=['departamentos'])
def send_welcome(message):
    bot.reply_to(message, respuestas["departamentos"])

@bot.message_handler(commands=['deportes'])
def send_welcome(message):
    bot.reply_to(message, respuestas["deportes"])

@bot.message_handler(commands=['faq'])
def send_welcome(message):
    bot.reply_to(message, respuestas["faq"])

@bot.message_handler(commands=['aulas'])
def send_welcome(message):
    bot.reply_to(message, respuestas["aulas"])

@bot.message_handler(commands=['apuntes'])
def send_welcome(message):
    bot.reply_to(message, respuestas["apuntes"])

@bot.message_handler(commands=['bugs'])
def send_welcome(message):
    bot.reply_to(message, respuestas["bugs"])



# Respuesta default si el comando no es reconocido
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, respuestas["comienzo"])


# loop
bot.infinity_polling()