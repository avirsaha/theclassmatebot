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
    with open("bot_responses/help.txt", "r") as file:
        await update.message.reply_text(file.read())


async def activate_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("your record is started")


async def deactivate_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text("Your record is paused")


async def delete_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Your record is deleted")


async def my_class_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This feature is under development")


async def contribute_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text("This feature is under development")


async def fetchname_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This feature is under development")


async def fetchdate_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This feature is under development")


async def fetchrange_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text("This feature is under development")


async def create_class_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text("This feature is under development")


async def delete_class_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text("This feature is under development")


async def join_class_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text("This feature is under development")


async def leave_class_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text("This feature is under development")


async def open_source_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text("This feature is under development")


async def commands_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This feature is under development")


async def feedback_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This feature is under development")


async def enquary_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This feature is under development")


async def dev_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This feature is under development")


# Response Manager
def handle_response(text: str) -> str:
    processed_text = text.strip().lower()

    return "Sorry, This bot is still unable to respond on messages. try typing '/' before your commands"


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
    app.add_handler(CommandHandler("activate", activate_command))
    app.add_handler(CommandHandler("deactivate", deactivate_command))
    app.add_handler(CommandHandler("delete", delete_command))
    app.add_handler(CommandHandler("my_class", my_class_command))
    app.add_handler(CommandHandler("contribute", contribute_command))
    app.add_handler(CommandHandler("fetchname", fetchname_command))
    app.add_handler(CommandHandler("fetchdate", fetchdate_command))
    app.add_handler(CommandHandler("fetchrange", fetchrange_command))
    app.add_handler(CommandHandler("create_class", create_class_command))
    app.add_handler(CommandHandler("delete_class", delete_class_command))
    app.add_handler(CommandHandler("join_class", join_class_command))
    app.add_handler(CommandHandler("leave_class", leave_class_command))
    app.add_handler(CommandHandler("open_source", open_source_command))
    app.add_handler(CommandHandler("commands", commands_command))
    app.add_handler(CommandHandler("feedback", feedback_command))
    app.add_handler(CommandHandler("enquary", enquary_command))
    app.add_handler(CommandHandler("dev", dev_command))

    # Message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handlers
    app.add_error_handler(error)

    # Polling
    warning("Bot is currently polling.{}".format(str(datetime.now())))
    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    main()
