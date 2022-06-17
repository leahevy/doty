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

import os
import sys

import typer

import doty.crypto as crypto
import doty.log as log
from doty.cli.cli import (
    add_cmd_to_args,
    command,
    update_state,
    version_callback,
)
from doty.log import LogLevel

crypto_app = typer.Typer()

file_app = typer.Typer()
crypto_app.add_typer(file_app, name="file")

keys_app = typer.Typer()
crypto_app.add_typer(keys_app, name="key")


@command(file_app)
def encrypt(
    files: list[str] = typer.Argument(..., help="Files to encrypt"),
    version: bool = typer.Option(
        False,
        "-v",
        "--version",
        help="Prints the version",
        callback=version_callback,
        is_eager=True,
    ),
    dry_run: bool = typer.Option(
        False,
        "-n",
        "--dry-run",
        help="Only print the changes. Don't do anything.",
    ),
    config_file: str = typer.Option(
        None,
        "-c",
        "--config-file",
        help="Overwrites the search path for the configuration.",
    ),
    key_file: str = typer.Option(
        None,
        "-K",
        "--key-file",
        help="Overwrites the key file path.",
    ),
    log_level: LogLevel = typer.Option(
        None,
        "-l",
        "--log-level",
        help="Sets the log level.",
    ),
    verbose: bool = typer.Option(
        False,
        "-V",
        "--verbose",
        help="Prints debug output.",
    ),
) -> None:
    """
    Encrypts a file.
    """
    crypto.encryptfiles(
        *files, dry_run=dry_run, config_file=config_file, key_file=key_file
    )


@command(file_app)
def decrypt(
    files: list[str] = typer.Argument(..., help="Files to decrypt"),
    version: bool = typer.Option(
        False,
        "-v",
        "--version",
        help="Prints the version",
        callback=version_callback,
        is_eager=True,
    ),
    dry_run: bool = typer.Option(
        False,
        "-n",
        "--dry-run",
        help="Only print the changes. Don't do anything.",
    ),
    config_file: str = typer.Option(
        None,
        "-c",
        "--config-file",
        help="Overwrites the search path for the configuration.",
    ),
    key_file: str = typer.Option(
        None,
        "-K",
        "--key-file",
        help="Overwrites the key file path.",
    ),
    log_level: LogLevel = typer.Option(
        None,
        "-l",
        "--log-level",
        help="Sets the log level.",
    ),
    verbose: bool = typer.Option(
        False,
        "-V",
        "--verbose",
        help="Prints debug output.",
    ),
) -> None:
    """
    Decrypts a file.
    """
    crypto.decryptfiles(
        *files, dry_run=dry_run, config_file=config_file, key_file=key_file
    )


@command(crypto_app)
def modify(
    directory: str = typer.Argument(".", help="Directory to modify"),
    version: bool = typer.Option(
        False,
        "-v",
        "--version",
        help="Prints the version",
        callback=version_callback,
        is_eager=True,
    ),
    dry_run: bool = typer.Option(
        False,
        "-n",
        "--dry-run",
        help="Only print the changes. Don't do anything.",
    ),
    config_file: str = typer.Option(
        None,
        "-c",
        "--config-file",
        help="Overwrites the search path for the configuration.",
    ),
    key_file: str = typer.Option(
        None,
        "-K",
        "--key-file",
        help="Overwrites the key file path.",
    ),
    log_level: LogLevel = typer.Option(
        None,
        "-l",
        "--log-level",
        help="Sets the log level.",
    ),
    verbose: bool = typer.Option(
        False,
        "-V",
        "--verbose",
        help="Prints debug output.",
    ),
) -> None:
    """
    Decrypts a file.
    """
    crypto.modify(
        directory, dry_run=dry_run, config_file=config_file, key_file=key_file
    )


@command(keys_app)
def genkey(
    output_file: str = typer.Option(
        None,
        "-o",
        "--output",
        help="Specifies the target file.",
    ),
    version: bool = typer.Option(
        False,
        "-v",
        "--version",
        help="Prints the version",
        callback=version_callback,
        is_eager=True,
    ),
    dry_run: bool = typer.Option(
        False,
        "-n",
        "--dry-run",
        help="Only print the changes. Don't do anything.",
    ),
    config_file: str = typer.Option(
        None,
        "-c",
        "--config-file",
        help="Overwrites the search path for the configuration.",
    ),
    key_file: str = typer.Option(
        None,
        "-K",
        "--key-file",
        help="Overwrites the key file path.",
    ),
    log_level: LogLevel = typer.Option(
        None,
        "-l",
        "--log-level",
        help="Sets the log level.",
    ),
    verbose: bool = typer.Option(
        False,
        "-V",
        "--verbose",
        help="Prints debug output.",
    ),
) -> None:
    """
    Generates a key.
    """
    crypto.genkey(
        output_file=output_file,
        dry_run=dry_run,
        config_file=config_file,
        key_file=key_file,
    )


@keys_app.callback(invoke_without_command=True)
def keys_callback(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "-v",
        "--version",
        help="Prints the version",
        callback=version_callback,
        is_eager=True,
    ),
    dry_run: bool = typer.Option(
        False,
        "-n",
        "--dry-run",
        help="Only print the changes. Don't do anything.",
    ),
    config_file: str = typer.Option(
        None,
        "-c",
        "--config-file",
        help="Overwrites the search path for the configuration.",
    ),
    key_file: str = typer.Option(
        None,
        "-K",
        "--key-file",
        help="Overwrites the key file path.",
    ),
    log_level: LogLevel = typer.Option(
        None,
        "-l",
        "--log-level",
        help="Sets the log level.",
    ),
    verbose: bool = typer.Option(
        False,
        "-V",
        "--verbose",
        help="Prints debug output.",
    ),
) -> None:
    update_state(
        verbose=verbose,
        dry_run=dry_run,
        log_level=log_level,
        key_file=key_file,
        config_file=config_file,
    )
    pass
    if ctx.invoked_subcommand is None:
        cmdline = add_cmd_to_args(sys.argv, genkey.__name__)
        log.debug(f"Exec {cmdline}")
        os.execv(sys.argv[0], cmdline)


@file_app.callback(invoke_without_command=True)
def file_callback(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "-v",
        "--version",
        help="Prints the version",
        callback=version_callback,
        is_eager=True,
    ),
    dry_run: bool = typer.Option(
        False,
        "-n",
        "--dry-run",
        help="Only print the changes. Don't do anything.",
    ),
    config_file: str = typer.Option(
        None,
        "-c",
        "--config-file",
        help="Overwrites the search path for the configuration.",
    ),
    key_file: str = typer.Option(
        None,
        "-K",
        "--key-file",
        help="Overwrites the key file path.",
    ),
    log_level: LogLevel = typer.Option(
        None,
        "-l",
        "--log-level",
        help="Sets the log level.",
    ),
    verbose: bool = typer.Option(
        False,
        "-V",
        "--verbose",
        help="Prints debug output.",
    ),
) -> None:
    update_state(
        verbose=verbose,
        dry_run=dry_run,
        log_level=log_level,
        key_file=key_file,
        config_file=config_file,
    )
    if ctx.invoked_subcommand is None:
        cmdline = add_cmd_to_args(sys.argv, "--help")
        log.debug(f"Exec {cmdline}")
        os.execv(sys.argv[0], cmdline)


@crypto_app.callback(invoke_without_command=True)
def crypto_callback(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "-v",
        "--version",
        help="Prints the version",
        callback=version_callback,
        is_eager=True,
    ),
    dry_run: bool = typer.Option(
        False,
        "-n",
        "--dry-run",
        help="Only print the changes. Don't do anything.",
    ),
    config_file: str = typer.Option(
        None,
        "-c",
        "--config-file",
        help="Overwrites the search path for the configuration.",
    ),
    key_file: str = typer.Option(
        None,
        "-K",
        "--key-file",
        help="Overwrites the key file path.",
    ),
    log_level: LogLevel = typer.Option(
        None,
        "-l",
        "--log-level",
        help="Sets the log level.",
    ),
    verbose: bool = typer.Option(
        False,
        "-V",
        "--verbose",
        help="Prints debug output.",
    ),
) -> None:
    update_state(
        verbose=verbose,
        dry_run=dry_run,
        log_level=log_level,
        key_file=key_file,
        config_file=config_file,
    )
    if ctx.invoked_subcommand is None:
        cmdline = add_cmd_to_args(sys.argv, "--help")
        log.debug(f"Exec {cmdline}")
        os.execv(sys.argv[0], cmdline)
