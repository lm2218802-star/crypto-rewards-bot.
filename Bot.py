import telebot

TOKEN =8776680739:AAEYMf2_79qRwUX4qJQ5GLV2lM79bDPd9D0

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "👋 ¡Hola!")

bot.infinity_polling()
