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

state = {
    "verbose": False,
    "dry_run": False,
    "log_level": LogLevel.info,
}


def update_state(
    verbose: bool | None = None,
    dry_run: bool | None = None,
    log_level: LogLevel | None = None,
) -> None:
    if verbose:
        log_level = LogLevel.debug

    if log_level is not None:
        state["log_level"] = log_level
        set_log_level(log_level)
    if dry_run is not None:
        state["dry_run"] = dry_run


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
            dry_run: bool | None = None,
            **kwargs: dict[str, Any],
        ) -> RT:
            update_state(
                verbose=verbose,
                dry_run=dry_run,
                log_level=log_level,
            )
            return f(
                *args,
                dry_run=state["dry_run"],
                log_level=state["log_level"],
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
