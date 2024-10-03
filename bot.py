from dotenv import load_dotenv
import telebot
import os
# * This app receives text and sends qr code as a response
# Load environment variables from the .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(
        message, "I can generate QR codes for you. Just send me the text you want to convert to QR code.")


bot.infinity_polling()
