# Copyright 2023 Aviraj Saha & Maithil Saha
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see https://www.gnu.org/licenses/gpl-3.0.txt.
# ==============================================================================
"""# Bot Script

This module serves as the main script of the bot.

### Note: 
This should run on a server.

## Metadata
- `Author:` Aviraj Saha, Maithil Saha
- `Purpose:` This module serves as the main script of the bot.
"""

# PYLINT DIRECTIVES:
# pylint: disable=unused-argument
# pylint: disable=global-statement
# pylint: disable=line-too-long
# pylint: disable=no-value-for-parameter
# pylint: disable=wrong-import-order
# pylint: disable=bare-except
# pylint: disable=function-redefined
# pylint: disable=import-error

# Intentionally wrongly ordered import statements.
from typing import Final
import json


# Version and other meta data
__version__: str = "0.1.0-alpha"
__all__: list[str,] = []

# Reading paths from JSON file
with open("data/json/paths.json", "r", encoding="utf-8") as path_file:
    data = path_file.read()
PATHS: dict[str:str] = json.loads(data)

# Path alias
EVENT_LOG_PATH: Final[str] = PATHS["events_log"]
# FEEDBACK_LOG_PATH: Final[str] = PATHS["feedback_file"] # Uncomment when needed.
# ENQUIRY_LOG_PATH: Final[str] = PATHS["enquiry_file"]  # Uncomment when needed.


# Mode variable
user_message_mode: str = None  # Variable to switch between the different text handling modes. Currently "Feedback", "Enquiry" and regular mode


# import database_interface
from os import getenv
from datetime import datetime
from functools import partial
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from commands import (
    start_command,
    help_command,
    activate_command,
    deactivate_command,
    delete_command,
    my_class_command,
    contribute_command,
    fetchname_command,
    fetchdate_command,
    fetchrange_command,
    create_class_command,
    delete_class_command,
    join_class_command,
    leave_class_command,
    open_source_command,
    commands_command,
    feedback_command,
    enquiry_command,
    dev_command,
    cancel_command,
)
from modes import feedback_receive, enquiry_receive, activate_account
from dotenv import load_dotenv
from logging import error, warning, basicConfig, WARNING


# Config for loading .env
load_dotenv(
    dotenv_path=".env"
)  # Create your own .env file the project root directory before running this script.


# Getting API token and username from .env
TOKEN: Final[str] = getenv("api_token_telegrambot")
BOT_USERNAME: Final[str] = getenv("username_telegrambot")


# Config for logging
basicConfig(
    filename=EVENT_LOG_PATH,
    filemode="a",
    format="%(name)s - %(levelname)s - %(message)s",
    level=WARNING,
)


# Callback functions
def set_message_mode_callback(mode: str | None) -> None:
    """Sets message mode
    Args:
        mode (str | None): Specify mode.
    """
    global user_message_mode
    user_message_mode = mode


def set_message_mode_callback_cancel() -> None:
    """Sets message mode for cancelation"""
    global user_message_mode
    if user_message_mode is not None:
        user_message_mode = None
        return True
    return False


# Response Manager
def handle_response(text: str) -> str:
    """Handles responses
    Args:
        text (str): Text send by user

    Returns:
        str: Bot response
    """
    # processed_text = text.strip().lower()  # Uncomment when used.
    with open("bot_responses/default.txt", "r", encoding="utf-8") as file:
        return file.read()


# Message Manager
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles different messages
    Args:
        update (Update)
        context (ContextTypes.DEFAULT_TYPE)
    """
    text: str = update.message.text
    response: str
    # Switches between feedback mode, enquiry mode and normal text mode
    match user_message_mode:
        case "Feedback":
            await feedback_receive(update, context, set_message_mode_callback, text)
            return
        case "Enquiry":
            await enquiry_receive(update, context, set_message_mode_callback, text)
            return

        case "Activate":
            await activate_account(update, context, set_message_mode_callback, text)
            return
        case _:
            response = handle_response(text)
            warning(f"User:{ update.message.chat.id} :{text}-{str(datetime.now())}")
            await update.message.reply_text(response)


# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors
    Args:
        update (Update)
        context (ContextTypes.DEFAULT_TYPE)
    """
    error(
        f"Update {update} caused the following error {context.error}-{ str(datetime.now())}"
    )


def main() -> None:
    """This is the entry point"""
    warning(f"Bot is currently online-{str(datetime.now())}")

    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        CommandHandler(
            "activate",
            partial(activate_command, callback_function=set_message_mode_callback),
        )
    )
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
    app.add_handler(
        CommandHandler(
            "feedback",
            partial(feedback_command, callback_function=set_message_mode_callback),
        )  # Binds the command function with respective callback function/s.
    )
    app.add_handler(
        CommandHandler(
            "enquiry",
            partial(enquiry_command, callback_function=set_message_mode_callback),
        )  # Binds the command function with respective callback function/s.
    )
    app.add_handler(CommandHandler("dev", dev_command))
    app.add_handler(
        CommandHandler(
            "cancel",
            partial(
                cancel_command,
                callback_function=set_message_mode_callback_cancel,
            ),
        )  # Binds the command function with respective callback function/s.
    )

    # Message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handlers
    app.add_error_handler(error)

    # Polling
    print("bot is online...")
    warning(f"Bot is currently polling-{str(datetime.now())}")
    try:
        app.run_polling(poll_interval=3)
    except:
        error(f"Bot went offline-{str(datetime.now())}")

    error(f"Bot went offline-{str(datetime.now())}")


if __name__ == "__main__":
    main()
