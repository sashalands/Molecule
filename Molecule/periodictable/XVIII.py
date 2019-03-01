# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
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
from .element import Element
from .periods import *


class GroupXVIII:
    pass


class He(Element, PeriodI, GroupXVIII):
    pass


class Rn(Element, PeriodVI, GroupXVIII):
    @property
    def atomic_number(self):
        return 86

    @property
    def atomic_mass(self):
        return 222.0176

    @property
    def electronegativity(self):
        return 2.2

    @property
    def common_isotope(self):
        return 222

    @property
    def max_isotope(self):
        return 222

    @property
    def min_isotope(self):
        return 222

    @property
    def common_valences(self):
        return (0, 1)

    @property
    def valences_exeptions(self):
        return ()


class Og(Element, PeriodVII, GroupXVIII):
    @property
    def atomic_number(self):
        return 118

    @property
    def atomic_mass(self):
        return 294

    @property
    def electronegativity(self):
        return None

    @property
    def common_isotope(self):
        return 294

    @property
    def max_isotope(self):
        return 294

    @property
    def min_isotope(self):
        return 294

    @property
    def common_valences(self):
        return (0, 1)

    @property
    def valences_exeptions(self):
        return ()

__all__ = ['GroupXVIII', 'He', 'Rn', 'Og']
