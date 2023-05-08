from fastapi import APIRouter, Request

from src.app_context import TOKEN, bot
from src.services.default_service import get_reply

app = APIRouter(prefix="")


@app.get("/")
def welcome_message():
    return {"message": "Welcome to pickme_bot"}


@app.post("/local_test", response_model=str)
def local_webhook(text: str):
    reply = get_reply(text)
    return reply


@app.post("/{}".format(TOKEN), response_model=str)
async def webhook(request: Request):
    data = await request.json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"].encode("utf-8").decode()
    msg_id = data["message"]["message_id"]

    reply = get_reply(text)
    bot.sendMessage(
        chat_id=chat_id,
        text=reply,
        reply_to_message_id=msg_id,
    )
    return reply
