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

import subprocess

import doty.log as log
from doty.exceptions import DotyConfigException, DotyNotImplementedException
from doty.utils import get_package_file


def run_configure(
    file: str,
    *commands: str,
    dry_run: bool = False,
    config_file: str | None = None
) -> None:
    assert len(commands) > 0  # TODO: implement this correctly
    log.debug(
        "run-configure",
        dry_run=dry_run,
        config_file=config_file,
        file=file,
        commands=commands,
    )

    subprocess.call(
        [get_package_file("run-configure-script.sh"), file] + list(commands)
    )

    log.fatal(DotyNotImplementedException, "run-configure not implemented yet")
