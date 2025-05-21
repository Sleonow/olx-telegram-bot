from config import bot

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Це webhook-базований бот :)")
