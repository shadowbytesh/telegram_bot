import telebot
import os

BOT_TOKEN = os.getenv("7945623788:AAFCdKDVxVM4RiYVog9YJd2Oo7P7T0Yvmig")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Salom! Men echo botman. Nima yozsang, shuni qaytaraman!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Siz yozdingiz: {message.text}")

bot.polling()
