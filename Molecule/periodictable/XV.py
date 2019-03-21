# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
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


class GroupXV:
    pass


class P(Element, PeriodIII, GroupXV):
    @property
    def atomic_number(self):
        return 15

    @property
    def atomic_mass(self):
        return 31

    @property
    def electronegativity(self):
        return 2.19

    @property
    def common_isotope(self):
        return 31

    @property
    def max_isotope(self):
        return 33

    @property
    def min_isotope(self):
        return 31

    @property
    def common_valences(self):
        return (0, 1), (3, 1), (5, 1)

    @property
    def valences_exceptions(self):
        return ()


class As(Element, PeriodIII, GroupXV):
    @property
    def atomic_number(self):
        return 33

    @property
    def atomic_mass(self):
        return 75

    @property
    def electronegativity(self):
        return 2.18

    @property
    def common_isotope(self):
        return 75

    @property
    def max_isotope(self):
        return 77

    @property
    def min_isotope(self):
        return 73

    @property
    def common_valences(self):
        return (0, 1), (3, 1), (5, 1)

    @property
    def valences_exceptions(self):
        return ()


class Sb(Element, PeriodIII, GroupXV):
    @property
    def atomic_number(self):
        return 51

    @property
    def atomic_mass(self):
        return 123

    @property
    def electronegativity(self):
        return 2.05

    @property
    def common_isotope(self):
        return 123

    @property
    def max_isotope(self):
        return 127

    @property
    def min_isotope(self):
        return 119

    @property
    def common_valences(self):
        return (0, 1), (3, 1), (5, 1)

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupXV', 'P', 'As', 'Sb']
