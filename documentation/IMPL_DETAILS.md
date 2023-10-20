# Implementation Details
## Table of Contents

1. [Overview](#overview)
   - [Modules](#modules)
     - [`main.py`](#mainpy)
     - [`commands.py`](#commandspy)
     - [`modes.py`](#modespy)
     - [`database-interface.py`](#database-interfacepy)
     - [`__init__.py`](#__init__py)
   - [`main.py`](#mainpy-1)
     - [Bot Script](#bot-script)
     - [Metadata](#metadata)
     - [PYLINT DIRECTIVES](#pylint-directives)
     - [Dependencies](#dependencies)
     - [Script Functionality](#script-functionality)
   - [`commands.py`](#commandspy-1)
     - [Commands Module](#commands-module)
     - [Metadata](#metadata-1)
     - [PYLINT DIRECTIVES](#pylint-directives-1)
     - [Dependencies](#dependencies-1)
     - [Implemented Functions](#implemented-functions)
   - [`modes.py`](#modespy-1)
     - [Modes Module](#modes-module)
     - [Metadata](#metadata-2)
     - [PYLINT DIRECTIVES](#pylint-directives-2)
     - [Dependencies](#dependencies-2)
     - [Implemented Functions](#implemented-functions-1)
   - [`__init__.py`](#__init__py-1)
   - [`database-interface.py`](#database-interfacepy-1)
2. [Data](#data)
3. [Environment](#environment)
4. [Pylint](#pylint)
5. [Mypy](#mypy)
6. [Tests](#tests)
7. [License](#license)

---

# Overview

This document provides a comprehensive overview of the logic and implementation details related to the code base.

## Modules

### `main.py`

This module functions as the main script expected to run on a server. It contains the necessary code for the bot to operate and connect to a server.

- **Bot Script:**
  This module serves as the main script of the bot.

#### Metadata

- **Author:** Aviraj Saha, Maithil Saha
- **Purpose:** This module serves as the main script of the bot.

#### PYLINT DIRECTIVES

```Python
# pylint: disable=unused-argument
# pylint: disable=global-statement
# pylint: disable=line-too-long
# pylint: disable=no-value-for-parameter
# pylint: disable=wrong-import-order
# pylint: disable=bare-except
# pylint: disable=function-redefined
# pylint: disable=import-error
```

#### Dependencies

```Python
from typing import Final
import json
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
from modes import feedback_receive, enquiry_receive
from dotenv import load_dotenv
from logging import error, warning, basicConfig, WARNING
```

#### Script Functionality

This script includes implementations for various functions:

- Callback functions: `set_message_mode_callback`, `set_message_mode_callback_cancel`
- Response Manager: `handle_response`
- Message Manager: `handle_message`
- Error handler: `error`
- Main function: `main`

### `commands.py`

This module contains implementations of various commands.

#### Metadata

- **Author:** Aviraj Saha & Maithil Saha
- **Purpose:** This module contains the implementations of various bot commands.

#### PYLINT DIRECTIVES

```Python
# pylint: disable=unused-argument
# pylint: disable=line-too-long
# pylint: disable=no-value-for-parameter
# pylint: disable=bare-except
```

#### Dependencies

```Python
from telegram import Update
from telegram.ext import (
    ContextTypes,
    CallbackContext,
)
```

#### Implemented Functions

- `start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Start up prompt message.
- `help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Help manual for users.
- `activate_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `deactivate_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `delete_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `my_class_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `contribute_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `fetchname_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `fetchdate_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `fetchrange_command(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `create_class_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `delete_class_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `join_class_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `leave_class_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Not implemented.
- `open_source_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Open-source information.
- `commands_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Sends a list of commands with descriptions to the user.
- `feedback_command(update: Update, context: ContextTypes.DEFAULT_TYPE, callback_function) -> None`: Function to activate feedback mode to receive feedback.
- `enquiry_command(update: Update, context: ContextTypes.DEFAULT_TYPE, callback_function) -> None`: Function to activate enquiry mode to receive enquiries.
- `dev_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None`: Developer features.
- `cancel_command(update: Update, context: CallbackContext, callback_function) -> None`: Function to serve as a global cancel to cancel any current interactions like /feedback.

### `modes.py`

This module contains the implementations of various modes and their respective actions.

#### Metadata

- **Author:** Aviraj Saha & Maithil Saha
- **Purpose:** This module contains the implementations of the various modes.

#### PYLINT DIRECTIVES

```Python
# pylint: disable=line-too-long
# pylint: disable=unused-argument
```

#### Dependencies

```Python
from typing import Final
import json
from datetime import datetime
from telegram import Update
from telegram.ext import CallbackContext
```

#### Implemented Functions

- `feedback_receive(update: Update, context: CallbackContext, callback_function, user_message) -> None`: Function to record user feedback and store it in feedback.txt in the user_messages folder.
- `enquiry_receive(update: Update, context: CallbackContext, callback_function, user_message) -> None`: Function to record user enquiries and store it in enquiry.txt in the user_messages folder.

### `__init__.py`

This module packages all components together to appear as a package for Pylint and running tests easily.

### `database-interface.py`

**Not Implemented**

## Data

This directory is expected to hold runtime data. Currently, all paths are stored in `Data/json/paths.json`.

## Environment

The `.env` file configures the environment variables for dealing with sensitive data.

## Pylint

Setup with GitHub Actions.

```yaml
name: Pylint

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10"]
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint
        pip install -r requirements.txt
    - name: Analyzing the code with pylint
      run: |
        pylint **/*.py
```

## Mypy

**Not Implemented**

## Tests

**Not Implemented**

---

© 2023 AVIRAJ SAHA & MAITHIL SAHA. THIS OPEN-SOURCE SOFTWARE IS LICENSED UNDER THE [GPLv3.0](../LICENSE) LICENSE.
