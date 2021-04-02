#!/usr/bin/env python3

# Project Template for Python Command Line Tools
# Copyright (C) 2021 Patrick Baker

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Test Project Template for Python Command Line Tools: Command Line Interface"""


from click.testing import CliRunner

import pptcli.cli


def test_preview():
    runner = CliRunner()
    result = runner.invoke(pptcli.cli.main, ["preview"])

    assert result.exit_code == 0
    assert result.output == "preview\n"
