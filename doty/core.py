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
from doty.exceptions import DotyNotImplementedException


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


def health(config_file: str | None = None) -> None:
    log.debug("health", config_file=config_file)
    log.fatal(DotyNotImplementedException, "health not implemented yet")
