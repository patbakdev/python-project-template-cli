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

from setuptools import setup, find_packages

setup(
    name="pptcli",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["pptcli = pptcli.__main__:main"]},
    install_requires=[
        "click==7.1.2",  # TODO
        "click-log==0.3.2",  # TODO
        "colorama==0.4.4",  # BSD License (3 clause)
    ],
    # devtest_requires=[
    #     'black==20.8b1', # TODO
    #     'isort==5.8.0', # TODO
    #     'flake8==2.3.1', # TODO
    #     'pylint==2.7.4', # GPLv2
    #     'mypy==0.812', # TODO
    #     'bandit==1.7.0', # TODO
    #     'pytest==6.2.2', # TODO
    # ],
)
