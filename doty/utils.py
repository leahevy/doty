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

import importlib.resources as pkg_resources
import shutil


def is_installed(name: str) -> bool:
    return shutil.which(name) is not None


def get_package_file(filename: str) -> str:
    package_name = ".".join(__name__.split(".")[:-1])
    filepath = str(pkg_resources.path(package_name, filename))
    assert filepath
    return filepath
