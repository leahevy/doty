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

from enum import Enum
from typing import Any, Type


class LogLevel(str, Enum):
    info = "info"
    warn = "warn"
    debug = "debug"


LEVEL = LogLevel.info


def info(msg: str, *args: Any, **kwargs: Any) -> None:
    pass


def warn(msg: str, *args: Any, **kwargs: Any) -> None:
    pass


def error(msg: str, *args: Any, **kwargs: Any) -> None:
    pass


def fatal(
    exceptiontype: Type[Exception], msg: str, *args: Any, **kwargs: Any
) -> None:
    raise exceptiontype(msg, *args, **kwargs)
