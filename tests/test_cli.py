#!/usr/bin/env python
#
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

from types import ModuleType

import pytest


class TestCoreCli:
    def test_cli_main_build(self, doty: ModuleType) -> None:
        with pytest.raises(doty.exceptions.DotyException):
            doty.cli.main.build()

    def test_cli_main_populate(self, doty: ModuleType) -> None:
        with pytest.raises(doty.exceptions.DotyException):
            doty.cli.main.populate()

    def test_cli_main_health(self, doty: ModuleType) -> None:
        doty.cli.main.health()


class TestCryptoCli:
    def test_cli_crypto_file_encrypt(self, doty: ModuleType) -> None:
        with pytest.raises(doty.exceptions.DotyException):
            doty.cli.crypto.encrypt("testfile")

    def test_cli_crypto_file_decrypt(self, doty: ModuleType) -> None:
        with pytest.raises(doty.exceptions.DotyException):
            doty.cli.crypto.decrypt("testfile.encrypted")

    def test_cli_crypto_modify(self, doty: ModuleType) -> None:
        with pytest.raises(doty.exceptions.DotyException):
            doty.cli.crypto.modify(".")


class TestConfigCli:
    def test_cli_config_show(self, doty: ModuleType) -> None:
        with pytest.raises(doty.exceptions.DotyException):
            doty.cli.config.show()


class TestPkgsCli:
    def test_cli_pkgs_status(self, doty: ModuleType) -> None:
        with pytest.raises(doty.exceptions.DotyException):
            doty.cli.pkgs.status()

    def test_cli_pkgs_upgrade(self, doty: ModuleType) -> None:
        with pytest.raises(doty.exceptions.DotyException):
            doty.cli.pkgs.upgrade()


class TestInternalCli:
    def test_cli_internal_runconfigure(self, doty: ModuleType) -> None:
        with pytest.raises(doty.exceptions.DotyException):
            doty.cli.internal.run_configure("Testfile.sh", "pre-populate")
