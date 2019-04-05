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
        return ((-1, 1, ((1, 'Cl'), (1, 'Cl'))),  # CuCl2^-
                (-3, 1, ((1, 'S'), (1, 'S'))),  # CuS2^3- - это характерный комплекс для одновалентной меди
                (-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # Cu(OH)4^2-
                (-4, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # Cu(OH)6^4-
                (-2, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # CuCl4^2-
                (-2, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))))  # Cu(CN)4^2-


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
        return ((-1, 1, ((1, 'Cl'), (1, 'Cl'))),  # AgCl2^1-
                (-1, 1, ((1, 'O'), (1, 'O'))),  # Ag(OH)2^1-
                (-1, 1, ((1, 'S'), (1, 'S'))),  # AgS2^1-
                (-1, 1, ((1, 'C'), (1, 'C'))))  # Ag(CN)2^1-


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
        return ((-1, 1, ((1, 'Cl'), (1, 'Cl'))),  # AuCl2^1-
                (-1, 1, ((1, 'S'), (1, 'S'))),  # AuS2^1-
                (-1, 1, ((1, 'C'), (1, 'C'))),  # Au(CN)^1-
                (3, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # Au(NH3)4^3+
                (-1, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # Au(OH)4^1-
                (-1, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Au(CN)4^1-
                (-2, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Au(CN)5^2-
                (-3, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Au(CN)6^3-
                (-1, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))))  # AuCl4^1-


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
