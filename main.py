from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import datetime
import random

TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

# Random jokes & quotes
jokes = [
    "😂 Why did the computer go to the doctor? Because it caught a virus!",
    "🤣 I asked my laptop for a joke… it said '404 Joke Not Found!'",
    "😜 Why was the math book sad? Because it had too many problems."
]

quotes = [
    "🌟 Believe in yourself!",
    "🚀 Dreams don’t work unless you do.",
    "🔥 Stay positive, work hard, make it happen."
]

# Start command
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📌 About Bot", callback_data='about')],
        [InlineKeyboardButton("👤 My Profile", callback_data='profile')],
        [InlineKeyboardButton("⏰ Time & Date", callback_data='time')],
        [InlineKeyboardButton("😂 Random Joke", callback_data='joke')],
        [InlineKeyboardButton("💡 Quote", callback_data='quote')],
        [InlineKeyboardButton("🔄 Restart", callback_data='restart')],
        [InlineKeyboardButton("❌ Exit", callback_data='exit')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome! Choose an option 👇", reply_markup=reply_markup)

# Button callback
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "about":
        text = "🤖 This is a simple Telegram bot with inline buttons."
    elif query.data == "profile":
        user = query.from_user
        text = f"👤 Profile:\nName: {user.full_name}\nUsername: @{user.username}\nID: {user.id}"
    elif query.data == "time":
        text = f"⏰ Current Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    elif query.data == "joke":
        text = random.choice(jokes)
    elif query.data == "quote":
        text = random.choice(quotes)
    elif query.data == "restart":
        start(query, context)
        return
    elif query.data == "exit":
        text = "❌ Bot stopped. Type /start to begin again."
    else:
        text = "⚠️ Unknown option!"

    query.edit_message_text(text=text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("
