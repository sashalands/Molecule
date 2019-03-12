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


class GroupXV:
    pass


class N(Element, PeriodII, GroupXV):
    @property
    def atomic_number(self):
        return 7

    @property
    def atomic_mass(self):
        return 14.00643

    @property
    def electronegativity(self):
        return 3.04

    @property
    def common_isotope(self):
        return 14

    @property
    def max_isotope(self):
        return 15

    @property
    def min_isotope(self):
        return 14

    @property
    def common_valences(self):
        return (3, 1),

    @property
    def valences_exceptions(self):
        return ((0, 1, ((1, 'O'),)),
                (0, 1, ((2, 'O'),)),
                (0, 1, ((2, 'O'), (2, 'O'))))


class Bi(Element, PeriodVI, GroupXVII):
    @property
    def atomic_number(self):
        return 83

    @property
    def atomic_mass(self):
        return 208.9804

    @property
    def electronegativity(self):
        return 2.02

    @property
    def common_isotope(self):
        return 209

    @property
    def max_isotope(self):
        return 210

    @property
    def min_isotope(self):
        return 205

    @property
    def common_valences(self):
        return (3, 1),

    @property
    def valences_exceptions(self):
        return ((0, 1, ((2, 'O'),)),
                (0, 1, ((2, 'O'), (2, 'O'), (1, 'O'))))


class Mc(Element, PeriodVII, GroupXVII):
    @property
    def atomic_number(self):
        return 115

    @property
    def atomic_mass(self):
        return 289

    @property
    def electronegativity(self):
        return None

    @property
    def common_isotope(self):
        return 289

    @property
    def max_isotope(self):
        return 289

    @property
    def min_isotope(self):
        return 289

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupXVII', 'N', 'Bi', 'Mc']