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

"""This module contains internal commands."""

import os
import sys

import typer

import doty.internal as internal
import doty.log as log
from doty.cli.cli import (
    add_cmd_to_args,
    command,
    update_state,
    version_callback,
)
from doty.log import LogLevel

internal_app = typer.Typer()


@command(internal_app, name="run-configure")
def run_configure(
    script_path: str = typer.Argument(..., help="Path to the script to run"),
    commands: list[str] = typer.Argument(
        ..., help="Commands to run on the script"
    ),
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
    dry_run: bool = typer.Option(
        False,
        "-n",
        "--dry-run",
        help="Only print the changes. Don't do anything.",
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
    Upgrades the installed packages
    """
    internal.run_configure(
        script_path, *commands, dry_run=dry_run, config_file=config_file
    )


@internal_app.callback(invoke_without_command=True)
def internal_callback(
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
        config_file=config_file,
    )
    if ctx.invoked_subcommand is None:
        cmdline = add_cmd_to_args(sys.argv, "--help")
        log.debug(f"Exec {cmdline}")
        os.execv(sys.argv[0], cmdline)
