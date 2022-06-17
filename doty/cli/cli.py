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

import functools
import os.path
import sys
from typing import Any

import typer
from rich import print

from doty.__version__ import __version__
from doty.log import LogLevel, set_log_level

state: dict[str, Any] = {
    "verbose": False,
    "dry_run": False,
    "log_level": LogLevel.info,
    "key_file": None,
    "config_file": None,
    "preserve_tmp": False,
}


def update_state(
    verbose: bool | None = None,
    dry_run: bool | None = None,
    log_level: LogLevel | None = None,
    key_file: str | None = None,
    config_file: str | None = None,
    preserve_tmp: bool | None = None,
) -> None:
    if verbose:
        log_level = LogLevel.debug

    if log_level is not None:
        state["log_level"] = log_level
        set_log_level(log_level)
    if dry_run is not None:
        state["dry_run"] = dry_run
    if config_file is not None:
        state["config_file"] = config_file
    if preserve_tmp is not None:
        state["preserve_tmp"] = preserve_tmp
    if key_file is not None:
        state["key_file"] = key_file


from typing import Callable, TypeVar

RT = TypeVar("RT")  # return type


def command(
    app: typer.Typer,
) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
    def decorator(f: Callable[..., RT]) -> Callable[..., RT]:
        @functools.wraps(f)
        def inner_cmd(
            *args: list[Any],
            verbose: bool | None = None,
            version: bool | None = None,
            log_level: LogLevel | None = None,
            key_file: str | None = None,
            preserve_tmp: bool | None = None,
            config_file: str | None = None,
            dry_run: bool | None = None,
            **kwargs: dict[str, Any],
        ) -> RT:
            update_state(
                verbose=verbose,
                dry_run=dry_run,
                log_level=log_level,
                key_file=key_file,
                preserve_tmp=preserve_tmp,
                config_file=config_file,
            )
            argsnames = f.__code__.co_varnames
            if "dry_run" in argsnames:
                kwargs["dry_run"] = state["dry_run"]
            if "log_level" in argsnames:
                kwargs["log_level"] = state["log_level"]
            if "key_file" in argsnames:
                kwargs["key_file"] = state["key_file"]
            if "config_file" in argsnames:
                kwargs["config_file"] = state["config_file"]
            if "preserve_tmp" in argsnames:
                kwargs["preserve_tmp"] = state["preserve_tmp"]
            return f(
                *args,
                **kwargs,
            )

        inner_cmd_click = app.command()(inner_cmd)
        return inner_cmd_click

    return decorator


def version_callback(value: bool) -> None:
    """
    Prints the version.
    """
    if value:
        print(
            f"[green]{os.path.basename(sys.argv[0])}:[/green]"
            f" [blue]v{__version__}[/blue]"
        )
        raise typer.Exit()


def add_cmd_to_args(args: list[str], cmd: str) -> list[str]:
    result = []
    appended = False
    for arg in args[1:][::-1]:
        if not appended and not arg.startswith("-"):
            result.append(cmd)
            appended = True
        result.append(arg)
    if not appended:
        result.append(cmd)
    result.append(args[0])

    result = result[::-1]
    return result


def move_global_args(args: list[str]) -> list[str]:
    result = []
    result.append(args[0])
    global_options = []
    arg_found = False

    for arg in args[1:]:
        if not arg_found and arg.startswith("-"):
            global_options.append(arg)
        else:
            arg_found = True
            result.append(arg)
            result.extend(global_options)
            global_options = []
    result.extend(global_options)
    return result
