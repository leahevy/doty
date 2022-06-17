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

"""This is the main module docstring.

Some description comes here.
"""

import os
import os.path
import sys
import traceback

import typer
from click.exceptions import Abort, BadArgumentUsage, NoSuchOption, UsageError
from rich import print

# Allow running the main python script without installing the package
if __name__ == "__main__":
    import os as _os
    import sys as _sys

    _sys.path.append(_os.path.join(_os.path.dirname(__file__), "..", ".."))

import doty.core as core
import doty.log as log
from doty.cli.cli import (
    add_cmd_to_args,
    command,
    move_global_args,
    state,
    update_state,
    version_callback,
)
from doty.cli.config import config_app
from doty.cli.crypto import crypto_app
from doty.cli.pkgs import pkgs_app
from doty.log import LogLevel

DEFAULT_COMMAND = "build"

app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})


@command(app)
def health(
    version: bool = typer.Option(
        False,
        "-v",
        "--version",
        help="Prints the version",
        callback=version_callback,
        is_eager=True,
    ),
    log_level: LogLevel = typer.Option(
        None,
        "-l",
        "--log-level",
        help="Sets the log level.",
    ),
    config_file: str = typer.Option(
        None,
        "-c",
        "--config-file",
        help="Overwrites the search path for the configuration.",
    ),
    verbose: bool = typer.Option(
        False,
        "-V",
        "--verbose",
        help="Prints debug output.",
    ),
) -> None:
    """
    Checks if everything is set-up correctly and all required programs are available.
    """
    core.health(config_file=config_file)


@command(app)
def build(
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
    preserve_tmp: bool = typer.Option(
        None,
        "-p",
        "--preserve-tmp",
        help="Preserves the tmp dir (can be combined with --dry-run to check the generated files manually without populating)",
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
    core.build(
        dry_run=dry_run,
        config_file=config_file,
        preserve_tmp=preserve_tmp,
        key_file=key_file,
    )


@command(app)
def populate(
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
    preserve_tmp: bool = typer.Option(
        None,
        "-p",
        "--preserve-tmp",
        help="Preserves the tmp dir (can be combined with --dry-run to check the generated files manually without populating)",
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
    core.populate(
        dry_run=dry_run,
        config_file=config_file,
        preserve_tmp=preserve_tmp,
        key_file=key_file,
    )


@app.callback(invoke_without_command=True)
def main_callback(
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
    preserve_tmp: bool = typer.Option(
        None,
        "-p",
        "--preserve-tmp",
        help="Preserves the tmp dir (can be combined with --dry-run to check the generated files manually without populating)",
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
        preserve_tmp=preserve_tmp,
    )
    if ctx.invoked_subcommand is None:
        cmdline = [sys.argv[0], DEFAULT_COMMAND] + sys.argv[1:]
        log.debug(f"Exec {cmdline}")
        os.execv(sys.argv[0], cmdline)


app.add_typer(crypto_app, name="crypto")
app.add_typer(config_app, name="config")
app.add_typer(pkgs_app, name="pkg")


def main() -> None:
    try:
        app(standalone_mode=False)
    except (Abort, KeyboardInterrupt):
        debug = state["log_level"] == LogLevel.debug
        if debug:
            print(traceback.format_exc(), file=sys.stderr)
        print(
            "[red]Aborted by user...[/red]",
            file=sys.stderr,
        )
        sys.exit(1)
    except (NoSuchOption, BadArgumentUsage, UsageError) as e:
        debug = state["log_level"] == LogLevel.debug
        if debug:
            print(traceback.format_exc(), file=sys.stderr)
        print(
            f"[red]{str(e)}[/red]",
            file=sys.stderr,
        )
        sys.exit(2)
    except Exception as e:
        debug = state["log_level"] == LogLevel.debug
        if debug:
            print(traceback.format_exc(), file=sys.stderr)
        print(
            f"[red]{str(e)}[/red]",
            file=sys.stderr,
        )
        sys.exit(3)
    sys.exit(0)


if __name__ == "__main__":
    main()
