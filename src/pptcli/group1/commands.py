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

"""Project Template for Python Command Line Tools: Group One Commands"""

import logging

import click

logger = logging.getLogger()


@click.group()
def group1():
    """Group One Command Group"""
    logger.debug(group1.__doc__)


@group1.command("G1C1")
def command1():
    """Command Number One (Group One)"""
    logger.debug(command1.__doc__)


@group1.command("G1C2")
def command2():
    """Command Number Two (Group One)"""
    logger.debug(command2.__doc__)
