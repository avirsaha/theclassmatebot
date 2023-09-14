from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from logging import debug, error, warning, basicConfig, DEBUG
from datetime import datetime


basicConfig(level=DEBUG)


# Initialization
TOKEN: Final[str] = "xxx"
BOT_USERNAME: Final[str] = "The_Classmate_Bot"


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This is what the bot says on start.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("this is help text.")


# Response Manager
def handle_response(text: str) -> str:
    processed_text = text.strip().lower()

    return "This is the response generated by the bot."


# Message Manager
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text: str = update.message.text
    response: str = handle_response(text)

    debug("User:{}, :{}-{}".format(update.message.chat.id, text, str(datetime.now())))
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    error(
        "Update {} caused the following error {}-{}".format(
            update, context.error, str(datetime.now())
        )
    )


def main() -> None:
    warning("Bot is currently online.{}".format(str(datetime.now())))

    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polling
    warning("Bot is currently polling.{}".format(str(datetime.now())))


if __name__ == "__main__":
    main()
