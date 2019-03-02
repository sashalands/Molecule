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


class GroupII:
    pass


class Be(Element, PeriodII, GroupII):
    @property
    def atomic_number(self):
        return 4

    @property
    def atomic_mass(self):
        return 9.012182

    @property
    def electronegativity(self):
        return 1.57

    @property
    def common_isotope(self):
        return 9

    @property
    def max_isotope(self):
        return 10

    @property
    def min_isotope(self):
        return 7

    @property
    def common_valences(self):
        return (0, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ()


class Mg(Element, PeriodIII, GroupII):
    @property
    def atomic_number(self):
        return 12

    @property
    def atomic_mass(self):
        return 24.305

    @property
    def electronegativity(self):
        return 1.31

    @property
    def common_isotope(self):
        return 24

    @property
    def max_isotope(self):
        return 28

    @property
    def min_isotope(self):
        return 24

    @property
    def common_valences(self):
        return (0, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ()


class Ca(Element, PeriodIV, GroupII):
    @property
    def atomic_number(self):
        return 20

    @property
    def atomic_mass(self):
        return 40.078

    @property
    def electronegativity(self):
        return 1.00

    @property
    def common_isotope(self):
        return 40

    @property
    def max_isotope(self):
        return 48

    @property
    def min_isotope(self):
        return 40

    @property
    def common_valences(self):
        return (0, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ()


class Sr(Element, PeriodV, GroupII):
    @property
    def atomic_number(self):
        return 38

    @property
    def atomic_mass(self):
        return 87.62

    @property
    def electronegativity(self):
        return 0.95

    @property
    def common_isotope(self):
        return 88

    @property
    def max_isotope(self):
        return 90

    @property
    def min_isotope(self):
        return 82

    @property
    def common_valences(self):
        return (0, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ()


class Ba(Element, PeriodVI, GroupII):
    @property
    def atomic_number(self):
        return 56

    @property
    def atomic_mass(self):
        return 137.327

    @property
    def electronegativity(self):
        return 0.89

    @property
    def common_isotope(self):
        return 138

    @property
    def max_isotope(self):
        return 138

    @property
    def min_isotope(self):
        return 130

    @property
    def common_valences(self):
        return (0, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ()


class Ra(Element, PeriodVII, GroupII):
    @property
    def atomic_number(self):
        return 88

    @property
    def atomic_mass(self):
        return 226.0254

    @property
    def electronegativity(self):
        return 0.9

    @property
    def common_isotope(self):
        return 226

    @property
    def max_isotope(self):
        return 228

    @property
    def min_isotope(self):
        return 223

    @property
    def common_valences(self):
        return (0, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupII', 'Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra']
