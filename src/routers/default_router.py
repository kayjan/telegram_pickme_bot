import time
# import urllib.parse
from typing import Any, Dict

from fastapi import APIRouter, Request

from src.app_context import BASE_URL, DEPLOY_URL, bot, client
from src.services.default_service import get_reply

app = APIRouter(prefix="")


@app.get("/")
def welcome_message():
    return {"message": "Welcome to pickme_bot"}


@app.post("/local_webhook", response_model=str)
def local_webhook(text: str):
    reply = get_reply(text)
    return reply


@app.get("/prod_webhook", response_model=bool)
def get_prod_webhook():
    return True


@app.post("/prod_webhook", response_model=str)
async def prod_webhook(request: Request):
    data = await request.json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"].encode("utf-8").decode()
    msg_id = data["message"]["message_id"]

    reply = get_reply(text)
    bot.sendChatAction(chat_id=chat_id, action="typing")
    time.sleep(1.5)
    bot.sendMessage(
        chat_id=chat_id,
        text=reply,
        reply_to_message_id=msg_id,
    )
    return reply


@app.post("/dummy_webhook/")
async def dummy_webhook(request: Request):
    data = await request.json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"]
    await client.get(f"{BASE_URL}/sendMessage?chat_id={chat_id}&text={text}")
    return data


@app.get("/set_webhook", response_model=Dict[str, Any])
async def set_webhook():
    webhook = f"{DEPLOY_URL}/prod_webhook"
    # webhook_encoded = urllib.parse.quote(webhook, safe="")
    status = await bot.setWebhook(webhook)
    return {"status": status}
