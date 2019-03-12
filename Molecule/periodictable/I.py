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


class GroupI:
    pass


class H(Element, PeriodI, GroupI):
    @property
    def atomic_number(self):
        return 1

    @property
    def atomic_mass(self):
        return 1.00784

    @property
    def electronegativity(self):
        return 2.2

    @property
    def common_isotope(self):
        return 1

    @property
    def max_isotope(self):
        return 3

    @property
    def min_isotope(self):
        return 1

    @property
    def common_valences(self):
        return (0, 2), (1, 1)

    @property
    def valences_exceptions(self):
        return ()


class Li(Element, PeriodII, GroupI):
    @property
    def atomic_number(self):
        return 3

    @property
    def atomic_mass(self):
        return 6.938

    @property
    def electronegativity(self):
        return 0.98

    @property
    def common_isotope(self):
        return 6

    @property
    def max_isotope(self):
        return 13

    @property
    def min_isotope(self):
        return 3

    @property
    def common_valences(self):
        return (0, 1), (1, 1)

    @property
    def valences_exceptions(self):
        return ()


class Na(Element, PeriodIII, GroupI):
    @property
    def atomic_number(self):
        return 11

    @property
    def atomic_mass(self):
        return 22.989

    @property
    def electronegativity(self):
        return 0.93

    @property
    def common_isotope(self):
        return 23

    @property
    def max_isotope(self):
        return 37

    @property
    def min_isotope(self):
        return 18

    @property
    def common_valences(self):
        return (0, 1), (1, 1)

    @property
    def valences_exceptions(self):
        return ()


class K(Element, PeriodIV, GroupI):
    @property
    def atomic_number(self):
        return 19

    @property
    def atomic_mass(self):
        return 39.0983

    @property
    def electronegativity(self):
        return 0.82

    @property
    def common_isotope(self):
        return 39

    @property
    def max_isotope(self):
        return 56

    @property
    def min_isotope(self):
        return 32

    @property
    def common_valences(self):
        return (0, 1), (1, 1)

    @property
    def valences_exceptions(self):
        return ()


class Rb(Element, PeriodV, GroupI):
    @property
    def atomic_number(self):
        return 37

    @property
    def atomic_mass(self):
        return 85.4678

    @property
    def electronegativity(self):
        return 0.82

    @property
    def common_isotope(self):
        return 85

    @property
    def max_isotope(self):
        return 103

    @property
    def min_isotope(self):
        return 71

    @property
    def common_valences(self):
        return (0, 1), (1, 1)

    @property
    def valences_exceptions(self):
        return ()


class Cs(Element, PeriodVI, GroupI):
    @property
    def atomic_number(self):
        return 55

    @property
    def atomic_mass(self):
        return 132.90545

    @property
    def electronegativity(self):
        return 0.79

    @property
    def common_isotope(self):
        return 133

    @property
    def max_isotope(self):
        return 151

    @property
    def min_isotope(self):
        return 112

    @property
    def common_valences(self):
        return (0, 1), (1, 1)

    @property
    def valences_exceptions(self):
        return ()


class Fr(Element, PeriodVII, GroupI):
    @property
    def atomic_number(self):
        return 87

    @property
    def atomic_mass(self):
        return 223.0197

    @property
    def electronegativity(self):
        return 0.7

    @property
    def common_isotope(self):
        return 223

    @property
    def max_isotope(self):
        return 233

    @property
    def min_isotope(self):
        return 199

    @property
    def common_valences(self):
        return (0, 1), (1, 1)

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupI', 'H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
