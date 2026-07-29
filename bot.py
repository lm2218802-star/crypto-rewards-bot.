
import os
import telebot

TOKEN = os.environ["TOKEN"]

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "👋 ¡Hola!")

bot.infinity_polling()
