import telebot
import os

# Ye line Render ke secret section se token ko secure tareeke se legi
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Bot ko initialize karein
bot = telebot.TeleBot(BOT_TOKEN)

# Jab koi /start bhejega to ye function chalega
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, main kaam kar raha hoon!")

# Bot ko hamesha messages sunne ke liye start kar dein
print("Bot is running...")
bot.polling()
