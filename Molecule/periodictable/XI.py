# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Alexander Nikanshin <17071996sasha@gmail.com>
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


class GroupXI:
    pass


class Cu(Element, PeriodIV, GroupXI):
    @property
    def atomic_number(self):
        return 29

    @property
    def atomic_mass(self):
        return 63.546

    @property
    def electronegativity(self):
        return 1.9

    @property
    def common_isotope(self):
        return 63

    @property
    def max_isotope(self):
        return 65

    @property
    def min_isotope(self):
        return 63

    @property
    def common_valences(self):
        return (1, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ((-1, 1, ((1, 'Cl'), (1, 'Cl'))),
                (-3, 1, ((1, 'S'), (1, 'S'))),
                (-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),
                (2, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),
                (-2, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),
                (1, 1, ((1, 'N'), (1, 'N'))),
                (-1, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))))


class Ag(Element, PeriodV, GroupXI):
    @property
    def atomic_number(self):
        return 47

    @property
    def atomic_mass(self):
        return 107.8682

    @property
    def electronegativity(self):
        return 1.93

    @property
    def common_isotope(self):
        return 107

    @property
    def max_isotope(self):
        return 106

    @property
    def min_isotope(self):
        return 109

    @property
    def common_valences(self):
        return (1, 1),

    @property
    def valences_exceptions(self):
        return ((-1, 1, ((1, 'Cl'), (1, 'Cl'))),
                (-1, 1, ((1, 'O'), (1, 'O'))),
                (-1, 1, ((1, 'S'), (1, 'S'))),
                (-1, 1, ((1, 'C'), (1, 'C'))),
                (1, 1, ((1, 'N'), (1, 'N'))))


class Au(Element, PeriodVI, GroupXI):
    @property
    def atomic_number(self):
        return 79

    @property
    def atomic_mass(self):
        return 196.966569

    @property
    def electronegativity(self):
        return 2.64

    @property
    def common_isotope(self):
        return 197

    @property
    def max_isotope(self):
        return 199

    @property
    def min_isotope(self):
        return 195

    @property
    def common_valences(self):
        return (1, 1),

    @property
    def valences_exceptions(self):
        return ((-1, 1, ((1, 'Cl'), (1, 'Cl'))),
                (-1, 1, ((1, 'S'), (1, 'S'))),
                (-1, 1, ((1, 'C'), (1, 'C'))),
                (1, 1, ((1, 'N'), (1, 'N'))),
                (3, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),
                (-1, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),
                (-1, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),
                (-2, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),
                (-3, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),
                (-1, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))))


class Rg(Element, PeriodVII, GroupXI):
    @property
    def atomic_number(self):
        return 111

    @property
    def atomic_mass(self):
        return 281

    @property
    def electronegativity(self):
        return None

    @property
    def common_isotope(self):
        return 281

    @property
    def max_isotope(self):
        return 281

    @property
    def min_isotope(self):
        return 281

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupXI', 'Cu', 'Ag', 'Au', 'Rg']
