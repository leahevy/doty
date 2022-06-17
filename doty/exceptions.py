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

from dataclasses import dataclass
from typing import Any


@dataclass
class DotyException(Exception):
    msg: str
    data: dict[str, Any] | None = None
    type: str = "DotyException"

    def __post_init__(self) -> None:
        if self.data is None:
            self.data = {}

    def __str__(self) -> str:
        s = []
        s.append(self.type)
        s.append(": ")
        s.append(self.msg)
        if self.data:
            s.append(f", {self.data}")
        return "".join(s)


class DotyNotImplementedException(DotyException, NotImplementedError):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.type = "not implemented"


class DotyCliException(DotyException):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.type = "cli"


class DotyLibException(DotyException):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.type = "library"
