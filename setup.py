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
    author='Patrick Baker',
    author_email='patrick@patrickbaker.dev',
    maintainer='Patrick Baker',
    maintainer_email='patrick@patrickbaker.dev',
    url='',
    summary='',
    description='',
    long_description=open('README.md').read(),
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',

    ],
    keywords=[],
    license='AGPLv3+',
    license_files=('LICENSE',),
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    py_modules=['booker'],
    entry_points={"console_scripts": ["pptcli = pptcli.cli:main"]},
    install_requires=[
        "click-log==0.3.2",  # TODO
        "click==7.1.2",  # TODO
        'colorama==0.4.4', # BSD
    ],
    setup_require=[
        'bandit==1.7.0' # Apache 2.0
        'black==20.8b1', # MIT
        'flake8==3.9.0', # MIT
        'isort==5.8.0', # MIT
        'mypy==0.812', # MIT
        'pylint==2.7.4', # GPLv2+
    ],
    tests_require=[
        'pytest==6.2.2', # MIT
        'pytest-snapshot==0.5.0', # MIT
        # 'pytest-cov',
        # 'pytest-depends',
        # 'pytest-env',
        # 'pytest-profiling',
        # 'vulture==2.3',
    ],
)
