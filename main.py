import telebot
import os
from flask import Flask
import threading

# Aapka Bot Token yahan nahi, Render ke Secrets mein daalna hai
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Flask App (ye hai keep_alive ka part)
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    # Port 0.0.0.0 par run karna zaroori hai
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "hello me bot hu tata")
def run_bot():
    print("Bot polling started...")
    bot.polling(none_stop=True)

# Dono ko ek saath chalane ka tareeka
if __name__ == "__main__":
    # Flask server ko ek alag thread mein chalao
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Bot ko main thread mein chalao
    run_bot()
    
