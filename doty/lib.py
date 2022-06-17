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


def populate(dry_run: bool = False) -> None:
    log.fatal(
        DotyNotImplementedException,
        "populate not implemented yet",
        data={"dry_run": dry_run},
    )


def health() -> None:
    log.fatal(DotyNotImplementedException, "health not implemented yet")


def encryptfiles(*files: str, dry_run: bool = False) -> None:
    log.fatal(
        DotyNotImplementedException,
        "encryptfile not implemented yet",
        data={"files": files, "dry_run": dry_run},
    )


def decryptfiles(*files: str, dry_run: bool = False) -> None:
    log.fatal(
        DotyNotImplementedException,
        "decryptfile not implemented yet",
        data={"files": files, "dry_run": dry_run},
    )
