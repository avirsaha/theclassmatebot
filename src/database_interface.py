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
"This module interacts with the database"

# PYLINT DIRECTIVES:
# pylint: disable=line-too-long

__version__ = "0.1.0-alpha"
__all__ = []

import pyodbc


def connection(
    username: str, address: str, passwd: str, database: str = None
) -> tuple[bool, pyodbc.Connection | str]:
    try:
        connection: pyodbc.Connection = pyodbc.connect(
            f"DRIVER={{SQL Server}};SERVER={address};DATABASE={database};UID={username};PWD={passwd}"
        )
        return True, connection

    except pyodbc.Error as e:
        return False, e


CONN = connection(
    username="theclassmatebot",
    address="theclassmatebot.mysql.pythonanywhere-services.com",
    passwd="cliX1234",
    database="theclassmatebot$masterdb",
)
cursor = CONN.cursor()
result = cursor.execute("show tables;")
print(result)
# def search_record()
