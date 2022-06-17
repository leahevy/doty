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

import doty.log as log
from doty.exceptions import DotyCoreException, DotyNotImplementedException
from doty.utils import get_package_file, is_installed


def build(
    dry_run: bool = False,
    config_file: str | None = None,
    preserve_tmp: bool = False,
    key_file: str | None = None,
) -> None:
    log.debug(
        "build",
        dry_run=dry_run,
        config_file=config_file,
        preserve_tmp=preserve_tmp,
        key_file=key_file,
    )
    log.fatal(DotyNotImplementedException, "build not implemented yet")


def populate(
    dry_run: bool = False,
    config_file: str | None = None,
    preserve_tmp: bool = False,
    key_file: str | None = None,
) -> None:
    log.debug(
        "populate",
        dry_run=dry_run,
        config_file=config_file,
        preserve_tmp=preserve_tmp,
        key_file=key_file,
    )
    log.fatal(DotyNotImplementedException, "populate not implemented yet")


def health(config_file: str | None = None, quiet: bool = False) -> None:
    log.debug("health", config_file=config_file)
    if not quiet:
        log.info("Dotys health 💊:")

    has_error = False

    with open(get_package_file("required-programs.txt"), "r") as f:
        required_programs = [
            line.strip()
            for line in f.read().strip().split("\n")
            if not line.startswith("#") and line.strip()
        ]

    for program in required_programs:
        if not is_installed(program):
            has_error = True
            if not quiet:
                log.error(
                    "  - ‼️ {program} is not installed.", program=program
                )
        else:
            if not quiet:
                log.info("  - ✅️ {program} available.", program=program)
    if has_error:
        raise DotyCoreException("Health-check failed.")
    elif not quiet:
        log.info("[green] => 😎 Everything fine[/green]")
