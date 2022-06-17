# Copyright (C) 2022 Leah Lackner
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This module contains the functions for encryption in the CLI."""

import typer
from rich import print

import doty.lib

crypto_app = typer.Typer()
file_app = typer.Typer()
crypto_app.add_typer(file_app, name="file")


@file_app.command()
def encrypt() -> None:
    """
    Encrypts a file.
    """
    print("encryptfile")


@file_app.command()
def decrypt() -> None:
    """
    Decrypts a file.
    """
    print("decryptfile")
