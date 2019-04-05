# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Alexander Nikanshin <17071996sasha@gmail.com>
#  Copyright 2019 Tagir Akhmetshin <tagirshin@gmail.com>
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


class GroupV:
    pass


class V(Element, PeriodIV, GroupV):
    @property
    def atomic_number(self):
        return 23

    @property
    def atomic_mass(self):
        return 50.9415

    @property
    def electronegativity(self):
        return 1.63

    @property
    def common_isotope(self):
        return 51

    @property
    def max_isotope(self):
        return 51

    @property
    def min_isotope(self):
        return 48

    @property
    def common_valences(self):
        return (0, 4), (3, 1), (5, 1)

    @property
    def valences_exceptions(self):
        return ((0, 4, ((1, 'F'), (1, 'F'))),
                (0, 2, ((2, 'O'), (2, 'O'))),
                (-4, 4, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))))  # V(CN)6^4-


class Nb(Element, PeriodV, GroupV):
    @property
    def atomic_number(self):
        return 41

    @property
    def atomic_mass(self):
        return 92.90638

    @property
    def electronegativity(self):
        return 1.6

    @property
    def common_isotope(self):
        return 93

    @property
    def max_isotope(self):
        return 91

    @property
    def min_isotope(self):
        return 95

    @property
    def common_valences(self):
        return (0, 5), (5, 1)

    @property
    def valences_exceptions(self):
        return ((0, 4, ((1, 'Br'), (1, 'Br'))),
                (0, 3, ((1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 2, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))))


class Ta(Element, PeriodVI, GroupV):
    @property
    def atomic_number(self):
        return 73

    @property
    def atomic_mass(self):
        return 180.9478

    @property
    def electronegativity(self):
        return 1.5

    @property
    def common_isotope(self):
        return 181

    @property
    def max_isotope(self):
        return 183

    @property
    def min_isotope(self):
        return 179

    @property
    def common_valences(self):
        return (0, 4), (3, 1), (5, 1)

    @property
    def valences_exceptions(self):
        return ()


class Db(Element, PeriodVII, GroupV):
    @property
    def atomic_number(self):
        return 105

    @property
    def atomic_mass(self):
        return 268

    @property
    def electronegativity(self):
        return None

    @property
    def common_isotope(self):
        return 268

    @property
    def max_isotope(self):
        return 268

    @property
    def min_isotope(self):
        return 268

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupV', 'V', 'Nb', 'Ta', 'Db']
