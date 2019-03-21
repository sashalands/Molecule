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
from .element import Element
from .periods import *


class GroupXIV:
    pass


class Sn(Element, PeriodV, GroupXIV):
    @property
    def atomic_number(self):
        return 50

    @property
    def atomic_mass(self):
        return 118.710

    @property
    def electronegativity(self):
        return 1.96

    @property
    def common_isotope(self):
        return 120

    @property
    def max_isotope(self):
        return 126

    @property
    def min_isotope(self):
        return 112

    @property
    def common_valences(self):
        return (0, 1), (2, 1), (4, 1)

    @property
    def valences_exceptions(self):
        return ((-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),
                (-4, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))))


class Pb(Element, PeriodVI, GroupXIV):
    @property
    def atomic_number(self):
        return 82

    @property
    def atomic_mass(self):
        return 207.2

    @property
    def electronegativity(self):
        return 2.33

    @property
    def common_isotope(self):
        return 208

    @property
    def max_isotope(self):
        return 210

    @property
    def min_isotope(self):
        return 202

    @property
    def common_valences(self):
        return (0, 1), (2, 1), (4, 1)

    @property
    def valences_exceptions(self):
        return ((-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),
                (-4, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),
                (0, 2, ((1, 'C'), (1, 'C'), (1, 'C'))))


class Fl(Element, PeriodVII, GroupXIV):
    @property
    def atomic_number(self):
        return 114

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


__all__ = ['GroupXIV', 'Sn', 'Pb', 'Fl']
