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

"""Project Template for Python Command Line Tools: Command Line Interface"""

import os
import logging

import click
import click_log

import pptcli.group1.commands
import pptcli.group2.commands

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger()
click_log.basic_config(logger)


@click.group()
@click_log.simple_verbosity_option(logger)
@click.version_option("0.1.0")
def main():
    """Project Template for Python Command Line Tools"""
    logger.debug(main.__doc__)


main.add_command(pptcli.group1.commands.group1)
main.add_command(pptcli.group2.commands.group2)
main.add_command(pptcli.group1.commands.command1)
main.add_command(pptcli.group1.commands.command2)
main.add_command(pptcli.group2.commands.command1)
main.add_command(pptcli.group2.commands.command2)

if __name__ == "__main__":
    main()
