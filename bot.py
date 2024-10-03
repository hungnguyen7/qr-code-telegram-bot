from dotenv import load_dotenv
import telebot
import os
from utils.qrcode import generate_qr_code

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

@bot.message_handler(func=lambda message: True)
def generate_qr(message):
    qr_code = generate_qr_code(message.text, "qr_code.png")
    bot.send_photo(message.chat.id, open(qr_code, "rb"))

bot.infinity_polling()
