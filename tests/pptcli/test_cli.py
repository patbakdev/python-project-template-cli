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


def test_default():
    runner = CliRunner()
    result = runner.invoke(pptcli.cli.main)

    expected = """Usage: main [OPTIONS] COMMAND [ARGS]...

  Project Template for Python Command Line Tools

Options:
  -v, --verbosity LVL  Either CRITICAL, ERROR, WARNING, INFO or DEBUG
  --version            Show the version and exit.
  --help               Show this message and exit.

Commands:
  G1C1    Command Number One (Group One)
  G1C2    Command Number Two (Group One)
  G2C1    Command Number One (Group Two)
  G2C2    Command Number Two (Group Two)
  group1  Group One Command Group
  group2  Group Two Command Group
"""

    assert result.exit_code == 0
    assert result.output == expected


def test_help():
    runner = CliRunner()
    result = runner.invoke(pptcli.cli.main, ["--help"])

    expected = """Usage: main [OPTIONS] COMMAND [ARGS]...

  Project Template for Python Command Line Tools

Options:
  -v, --verbosity LVL  Either CRITICAL, ERROR, WARNING, INFO or DEBUG
  --version            Show the version and exit.
  --help               Show this message and exit.

Commands:
  G1C1    Command Number One (Group One)
  G1C2    Command Number Two (Group One)
  G2C1    Command Number One (Group Two)
  G2C2    Command Number Two (Group Two)
  group1  Group One Command Group
  group2  Group Two Command Group
"""

    assert result.exit_code == 0
    assert result.output == expected


def test_version():
    runner = CliRunner()
    result = runner.invoke(pptcli.cli.main, ["--version"])

    expected = "main, version 0.1.0\n"

    assert result.exit_code == 0
    assert result.output == expected
