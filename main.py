bot.remove_webhook()
bot.set_webhook(url="https://olx-telegram-bot.onrender.com/YOUR_TOKEN")


if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}")
    app.run(host="0.0.0.0", port=10000)
