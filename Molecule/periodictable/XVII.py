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


class GroupXVII:
    pass


class F(Element, PeriodII, GroupXVII):
    @property
    def atomic_number(self):
        return 9

    @property
    def atomic_mass(self):
        return 18.998403

    @property
    def electronegativity(self):
        return 3.98

    @property
    def common_isotope(self):
        return 19

    @property
    def max_isotope(self):
        return 19

    @property
    def min_isotope(self):
        return 19

    @property
    def common_valences(self):
        return (1, 2),

    @property
    def valences_exceptions(self):
        return ()


class Cl(Element, PeriodIII, GroupXVII):
    @property
    def atomic_number(self):
        return 17

    @property
    def atomic_mass(self):
        return 35.450

    @property
    def electronegativity(self):
        return 3.16

    @property
    def common_isotope(self):
        return 35

    @property
    def max_isotope(self):
        return 37

    @property
    def min_isotope(self):
        return 35

    @property
    def common_valences(self):
        return (1, 2),

    @property
    def valences_exceptions(self):
        return ((0, 6, ((2, 'O'), (2, 'O'), (1, 'O'))),
                (0, 4, ((2, 'O'), (1, 'O'))),
                (0, 8, ((2, 'O'), (2, 'O'), (2, 'O'), (1, 'O'))),
                (0, 5, ((2, 'O'), (2, 'O'))),
                (-1, 7, ((2, 'O'), (2, 'O'), (1, 'O'))))


class Br(Element, PeriodIV, GroupXVII):
    @property
    def atomic_number(self):
        return 35

    @property
    def atomic_mass(self):
        return 79.905

    @property
    def electronegativity(self):
        return 2.96

    @property
    def common_isotope(self):
        return 79

    @property
    def max_isotope(self):
        return 81

    @property
    def min_isotope(self):
        return 79

    @property
    def common_valences(self):
        return (1, 2),

    @property
    def valences_exceptions(self):
        return ((0, 6, ((2, 'O'), (2, 'O'), (1, 'O'))),
                (0, 4, ((2, 'O'), (1, 'O'))),
                (0, 8, ((2, 'O'), (2, 'O'), (2, 'O'), (1, 'O'))))


__all__ = ['GroupXVII', 'F', 'Cl', 'Br']