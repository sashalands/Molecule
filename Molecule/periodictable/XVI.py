# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Dayana Bashirova <dayana.bashirova@yandex.ru>
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


class GroupXVI:
    pass


class O(Element, PeriodII, GroupXVI):
    @property
    def atomic_number(self):
        return 8

    @property
    def atomic_mass(self):
        return 15.999

    @property
    def electronegativity(self):
        return 3.44

    @property
    def common_isotope(self):
        return 16

    @property
    def max_isotope(self):
        return 18

    @property
    def min_isotope(self):
        return 16

    @property
    def common_valences(self):
        return (2, 1),

    @property
    def valences_exceptions(self):
        return ((0, 2, ((1, 'H'),)), (0, 2, ((1, 'N'),)), (0, 2, ((1, 'O'),)), (-2, 1, ()),
                (-1, 1, ((1, 'H'),)), (-1, 1, ((1, 'O'),)),
               ((-1, 1, ((1, 'S'),)), (-1, 1, ((1, 'Se'),)), (-1, 1, ((1, 'C'),))))
    # First three tuples are exceptions when oxygen is radical, for example: hydroxyl radical or ozone
    # Other are examples of oxygen anion for example in acids or ozone


class S(Element, PeriodIII, GroupXVI):
    @property
    def atomic_number(self):
        return 16

    @property
    def atomic_mass(self):
        return 32.059

    @property
    def electronegativity(self):
        return 2.58

    @property
    def common_isotope(self):
        return 32

    @property
    def max_isotope(self):
        return 36

    @property
    def min_isotope(self):
        return 32

    @property
    def common_valences(self):
        return (2, 1), (4, 1), (6, 1)

    @property
    def valences_exceptions(self):
        return ((-1, 1, ((2, 'O'), (2, 'O'), (1, 'O'))), (-1, 1, ((2, 'O'), (2, 'O'), (1, 'S'))),
                (-1, 1, ((1, 'H'), )), (-2, 1, ()), (-1, 1, ((1, 'C'), )), (-1, 1, ((2, 'O'), (2, 'O'), (1, 'C'))))


class Se(Element, PeriodIV, GroupXVI):
    @property
    def atomic_number(self):
        return 34

    @property
    def atomic_mass(self):
        return 78.96

    @property
    def electronegativity(self):
        return 2.55

    @property
    def common_isotope(self):
        return 80

    @property
    def max_isotope(self):
        return 82

    @property
    def min_isotope(self):
        return 72

    @property
    def common_valences(self):
        return (2, 1), (4, 1), (6, 1)

    @property
    def valences_exceptions(self):
        return ()


class Po(Element, PeriodVI, GroupXVI):
    @property
    def atomic_number(self):
        return 84

    @property
    def atomic_mass(self):
        return 209

    @property
    def electronegativity(self):
        return 2.3

    @property
    def common_isotope(self):
        return 209

    @property
    def max_isotope(self):
        return 210

    @property
    def min_isotope(self):
        return 206

    @property
    def common_valences(self):
        return (0, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ((0, 1, ((2, 'O'), (2, 'O'), (2, 'O'))),
                (0, 1, ((2, 'O'), (2, 'O'))),
                (0, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),
                (0, 1, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))),
                (0, 1, ((1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'))),
                (0, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))))


class Lv(Element, PeriodVII, GroupXVI):
    @property
    def atomic_number(self):
        return 116

    @property
    def atomic_mass(self):
        return 293

    @property
    def electronegativity(self):
        return None

    @property
    def common_isotope(self):
        return 293

    @property
    def max_isotope(self):
        return 293

    @property
    def min_isotope(self):
        return 293

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupXVI', 'O', 'S', 'Se', 'Po', 'Lv']
