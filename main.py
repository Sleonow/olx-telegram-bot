import telebot
from flask import Flask, request
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = 8042965148:AAHjoSaOopUau4CiaDEcov0uimtvGwm8Dlc
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

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
