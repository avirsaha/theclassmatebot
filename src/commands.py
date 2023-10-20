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
"""# Commands module
This module has the implementation of various commands.

## Note:
- This should not be executed as a script.
- Utmost care should be taken while modification of this module.
  Any casuallities may impact user experience.
## Metadata
- `Author:` Aviraj Saha & Maithil Saha
- `Purpose:` This module has the implementations of the various bot commands.
"""


# PYLINT DIRECTIVES:
# pylint: disable=unused-argument
# pylint: disable=line-too-long
# pylint: disable=no-value-for-parameter
# pylint: disable=bare-except


from telegram import Update
from telegram.ext import (
    ContextTypes,
    CallbackContext,
)


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """#### Start up prompt message.
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """
    with open("bot_responses/on_start.txt", "r", encoding="utf-8") as file:
        await update.message.reply_text(file.read())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """#### Help manual for user.
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """
    with open("bot_responses/help.txt", "r", encoding="utf-8") as file:
        await update.message.reply_text(file.read())


async def activate_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """
    await update.message.reply_text("your record is started")


async def deactivate_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """
    await update.message.reply_text("Your record is paused")


async def delete_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """
    await update.message.reply_text("Your record is deleted")


async def my_class_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """
    await update.message.reply_text("This feature is under development")


async def contribute_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """
    await update.message.reply_text("This feature is under development")


async def fetchname_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """

    await update.message.reply_text("This feature is under development")


async def fetchdate_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """

    await update.message.reply_text("This feature is under development")


async def fetchrange_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """

    await update.message.reply_text("This feature is under development")


async def create_class_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """

    await update.message.reply_text("This feature is under development")


async def delete_class_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """

    await update.message.reply_text("This feature is under development")


async def join_class_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """

    await update.message.reply_text("This feature is under development")


async def leave_class_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """#### Not implimented
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """

    await update.message.reply_text("This feature is under development")


async def open_source_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """#### Open-source information
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """

    with open("bot_responses/open_source.txt", "r", encoding="utf-8") as file:
        await update.message.reply_text(file.read())


async def commands_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """#### Sends list of commands with description to the user.
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """
    with open("bot_responses/commands.txt", "r", encoding="utf-8") as file:
        await update.message.reply_text(file.read())


async def feedback_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE, callback_function
) -> None:
    """#### Function to activate feedback mode to receive feedback
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """
    callback_function("Feedback")
    # global user_message_mode
    # user_message_mode = "Feedback"
    await update.message.reply_text(
        'Please write your feedback message. You can also write "cancel" or use command /cancel to cancel. Please do not share any sensitive info like email address, usernames etc.'
    )


async def enquiry_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE, callback_function
) -> None:
    """#### Function to activate enquiry mode to receive enquiries.
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """
    # global user_message_mode
    # user_message_mode = "Enquiry"
    callback_function("Enquiry")
    await update.message.reply_text(
        'Please state your question. You can also write "cancel" or use command /cancel to cancel. Please do not share any sensitive info like email address, usernames etc.'
        " Our developers will get back to you within 1-3 working days. We apologize for any inconvenience caused in the meantime."
    )


async def dev_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """#### Developer features.
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
    """
    await update.message.reply_text("This feature is under development")


async def cancel_command(
    update: Update,
    context: CallbackContext,
    callback_function,
) -> None:
    """#### Function to serve as a global cancel to cancel /enquiry and /feedback
    - Args:
        - update (Update)
        - context (ContextTypes.DEFAULT_TYPE)
        - current_mode (str | None)
    """
    result = callback_function()
    if result:
        await update.message.reply_text("Canceled most recent interaction.")
        return
    await update.message.reply_text("No current interaction to cancel.")
