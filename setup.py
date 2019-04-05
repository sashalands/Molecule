# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Dayana Bashirova <dayana.bashirova@yandex.ru>
#  This file is part of Molecule.
#
#  Molecule is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, see <https://www.gnu.org/licenses/>.
#
from setuptools import setup
from pathlib import Path

setup (
    name='Molecule',
    version='0.1.0',
    packages=['Molecule', 'Molecule.algorithms', 'Molecule.containers', 'Molecule.periodictable'],
    url='http://github.com/cimm-kzn/Molecule',
    license='LGPLv3',
    author='Ramil Nugmanov',
    author_email='stsouko@live.ru',
    python_requires='>=3.7.0',
    zip_safe=True,
    long_descripts=(Path(__file__).parent / 'README.md').open().read(),
)
