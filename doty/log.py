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

import logging
import os
import sys
from enum import Enum
from typing import Any, Type

from rich import print
from rich.text import Text


class LogLevel(str, Enum):
    debug = "debug"
    info = "info"
    warning = "warning"
    error = "error"
    critical = "critical"


class CustomLogHandler(logging.Handler):
    def emit(self, log_record: logging.LogRecord) -> None:
        log_level = log_record.levelname

        color = "white"
        file = sys.stdout
        underline = False
        unformated = False
        match log_level.lower():
            case LogLevel.debug.name:
                color = "yellow"
                file = sys.stderr
            case LogLevel.info.name:
                color = "green"
                unformated = True
            case LogLevel.warning.name:
                color = "cyan"
                file = sys.stderr
            case LogLevel.error.name:
                color = "red"
                file = sys.stderr
            case LogLevel.critical.name:
                color = "red"
                file = sys.stderr
                underline = True

        if unformated:
            log_message = log_record.msg
        else:
            log_message = self.format(log_record)

        log_message = f"[{color}]{log_message}[/{color}]"
        if underline:
            log_message = f"[underline]{log_message}[/underline]"
        print(log_message, file=file)
        file.flush()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(os.path.basename(sys.argv[0]))
formatter = logging.Formatter(
    fmt="(%(levelname)s)"
    " [magenta]([italic]%(asctime)s)[/italic]"
    "[/magenta][white]:[/white]"
    " %(message)s",
    datefmt="%H:%M",
)
handler = CustomLogHandler()
handler.setFormatter(formatter)
logger.handlers = [handler]
logger.propagate = False


def set_log_level(log_level: LogLevel) -> None:
    logger.setLevel(log_level.name.upper())


def _format_text(text: str, *args: Any, **kwargs: Any) -> str:
    text = text.format(*args, **kwargs)
    return text


def debug(msg: str, *args: Any, **kwargs: Any) -> None:
    logger.debug(_format_text(msg, *args, **kwargs))


def info(msg: str, *args: Any, **kwargs: Any) -> None:
    logger.info(_format_text(msg, *args, **kwargs))


def warning(msg: str, *args: Any, **kwargs: Any) -> None:
    logger.warning(_format_text(msg, *args, **kwargs))


def error(msg: str, *args: Any, **kwargs: Any) -> None:
    logger.error(_format_text(msg, *args, **kwargs))


def critical(msg: str, *args: Any, **kwargs: Any) -> None:
    logger.critical(_format_text(msg, *args, **kwargs))


def fatal(
    exceptiontype: Type[Exception], msg: str, *args: Any, **kwargs: Any
) -> None:
    raise exceptiontype(msg, *args, **kwargs)
