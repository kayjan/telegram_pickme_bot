import logging
import os

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          MessageHandler, filters)

from src.services.default_service import get_reply

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def _start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = get_reply("/start")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


async def _choices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = get_reply("/choices")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


async def _toto_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = get_reply("/toto_number")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


async def _4d_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = get_reply("/4d_number")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


async def normal_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store info provided by user and ask for the next category."""
    text = update.message.text
    if text.startswith("Choose "):
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    reply = get_reply(text)
    await update.message.reply_text(reply)


if __name__ == "__main__":
    application = ApplicationBuilder().token(os.getenv("API_TOKEN")).build()

    for command in ["start", "choices", "toto_number", "4d_number"]:
        application.add_handler(CommandHandler(command, eval(f"_{command}")))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, normal_text)
    )

    application.run_polling()
