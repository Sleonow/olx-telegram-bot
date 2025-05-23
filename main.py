import telebot
from flask import Flask, request
import os
import sys  # Добавил импорт sys

API_TOKEN = os.getenv("API_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if not API_TOKEN or not WEBHOOK_URL:
    print("ERROR: Не заданы переменные окружения API_TOKEN или WEBHOOK_URL")
    sys.exit(1)

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route("/" + API_TOKEN, methods=["POST"])
def webhook():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "", 200

@app.route("/")
def index():
    return "Hello, this is OLX Dropshipping Bot!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Это OLX Dropshipping бот.")

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL + "/" + API_TOKEN)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

