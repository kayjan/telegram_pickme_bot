import os

import httpx
import telegram

TOKEN = os.getenv("API_TOKEN")  # token from BotFather
BOT_USERNAME = "pickme_bot"  # bot username
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
DEPLOY_URL = "https://telegrampickmebot.fly.dev"

bot = telegram.Bot(token=TOKEN)
client = httpx.AsyncClient()
