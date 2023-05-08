import os

import telegram

TOKEN = os.getenv("API_TOKEN")  # token from BotFather
BOT_USERNAME = "pickme_bot"  # bot username
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
DEPLOY_URL = "https://kayjan.fly.dev"

bot = telegram.Bot(token=TOKEN)
# bot.setWebhook(f"{DEPLOY_URL}/{TOKEN}")
