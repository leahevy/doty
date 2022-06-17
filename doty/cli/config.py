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

"""This module contains the CLI for managing the configuration"""

import os
import sys

import typer

import doty.config as config
from doty.cli.cli import command, update_state, version_callback
from doty.log import LogLevel

config_app = typer.Typer()


@command(config_app)
def show(
    version: bool = typer.Option(
        False,
        "-v",
        "--version",
        help="Prints the version",
        callback=version_callback,
        is_eager=True,
    ),
    config_file: str = typer.Option(
        None,
        "-c",
        "--config-file",
        help="Overwrites the search path for the configuration.",
    ),
    log_level: LogLevel = typer.Option(
        LogLevel.info,
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
    config.show(config_file=config_file)


@config_app.callback(invoke_without_command=True)
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
    log_level: LogLevel = typer.Option(
        LogLevel.info,
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
        config_file=config_file,
    )
    if ctx.invoked_subcommand is None:
        os.execv(sys.argv[0], sys.argv + [show.__name__])
