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
"""# Modes module
This module has the implementation of various modes and their respective actions.

## Note:
This should not be executed as a script.

## Metadata
- `Author:` Aviraj Saha & Maithil Saha
- `Purpose:` This module has the implementations of the various modes.
"""


# PYLINT DIRECTIVES:
# pylint: disable=line-too-long
# pylint: disable=unused-argument

from typing import Final
import json
from datetime import datetime
from telegram import Update
from telegram.ext import CallbackContext


# Reading paths from JSON file
with open("data/json/paths.json", "r", encoding="utf-8") as path_file:
    data = path_file.read()
PATHS: dict[str:str] = json.loads(data)

# Path alias
# EVENT_LOG_PATH: Final[str] = PATHS["events_log"]  # Uncomment when needed.
FEEDBACK_LOG_PATH: Final[str] = PATHS["feedback_file"]
ENQUIRY_LOG_PATH: Final[str] = PATHS["enquiry_file"]


# Mode functions
async def feedback_receive(
    update: Update, context: CallbackContext, callback_function, user_message
) -> None:
    """#### Function to record user feedback and store it in feedback.txt in user_messages folder
    - Args:
        - update (Update)
        - context (CallbackContext)
    """
    match user_message.strip().lower():
        case "cancel":
            await update.message.reply_text(
                "Canceled feedback. Please feel free to share your thoughts and feedback on the bot so we can continue to improve and deliver best possible services."
            )
        case _:
            with open(FEEDBACK_LOG_PATH, "a", encoding="utf-8") as feedback_file:
                feedback_file.write(f"\n{str(datetime.now())}: " + user_message)
                await update.message.reply_text("Thank you for your valuable feedback.")

    callback_function(None)


async def enquiry_receive(
    update: Update, context: CallbackContext, callback_function, user_message
) -> None:
    """#### Function to record user enquiries and store it in enquiry.txt in user_messages folder
    - Args:
        - update (Update)
        - context (CallbackContext)
    """
    # user_message = update.message.text
    match str.lower(user_message):
        case "cancel":
            await update.message.reply_text(
                "Canceled enquiry. Please feel free to reach out to us if you have any queries."
            )
        case _:
            with open(ENQUIRY_LOG_PATH, "a", encoding="utf-8") as enquiry_file:
                enquiry_file.write(
                    f"\n{str(datetime.now())}: {update.message.chat.username}: "
                    + user_message
                )
            await update.message.reply_text(
                "Your enquiry has been noted. We will get back to you soon."
            )

    callback_function(None)
