# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Tagir Akhmetshin <tagirshin@gmail.com>
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


class GroupVII:
    pass


class Mn(Element, PeriodIV, GroupVII):
    @property
    def atomic_number(self):
        return 25

    @property
    def atomic_mass(self):
        return 54.938045

    @property
    def electronegativity(self):
        return 1.55

    @property
    def common_isotope(self):
        return 55

    @property
    def max_isotope(self):
        return 55

    @property
    def min_isotope(self):
        return 52

    @property
    def common_valences(self):
        return (0, 6), (5, 1), (7, 1)

    @property
    def valences_exceptions(self):
        return ((0, 4, ((2, 'O'), (2, 'O'))),  # MnO2
                (0, 6, ((2, 'O'),)),  # MnO
                (0, 5, ((2, 'O'), (1, 'O'))),  # Mn2O3
                (-3, 5, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # Mn(OH)6^3-
                (0, 6, ((1, 'C'), (1, 'C'))),  # Mn(CN)2
                (0, 6, ((2, 'S'),)),  # MnS
                (0, 4, ((2, 'S'), (2, 'S'))),  # MnS2
                (-3, 5, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Mn(CN)6^3-
                (-2, 4, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Mn(CN)6^2-
                (-4, 6, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Mn(CN)6^3-
                (0, 4, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (-1, 4, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # MnF5^-
                (-2, 4, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # MnF6^2-
                (-4, 5, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),
                (0, 2, ((2, 'O'), (2, 'O'), (1, 'O'), (1, 'O'))),  # MnO4^2-
                (0, 3, ((2, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # MnO4^3-
                (0, 4, ((2, 'O'), (1, 'O'), (1, 'O'))),  # MnO3^2-
                (0, 5, ((1, 'O'), (1, 'O'), (1, 'O'))))  # Mn2O5^4-


class Tc(Element, PeriodV, GroupVII):
    @property
    def atomic_number(self):
        return 43

    @property
    def atomic_mass(self):
        return 97.9072

    @property
    def electronegativity(self):
        return 1.9

    @property
    def common_isotope(self):
        return 99

    @property
    def max_isotope(self):
        return 99

    @property
    def min_isotope(self):
        return 95

    @property
    def common_valences(self):
        return (0, 6), (5, 1), (7, 1)

    @property
    def valences_exceptions(self):
        return ((0, 4, ((2, 'O'), (2, 'O'))),  # TcO2
                (0, 4, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # Tc(OH)4
                (0, 4, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # TcCl4
                (-5, 7, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Tc(CN)6^5-
                (0, 6, ((2, 'S'),)),  # TcS
                (0, 4, ((2, 'S'), (2, 'S'))))  # TcS2


class Re(Element, PeriodVI, GroupVII):
    @property
    def atomic_number(self):
        return 75

    @property
    def atomic_mass(self):
        return 186.207

    @property
    def electronegativity(self):
        return 1.9

    @property
    def common_isotope(self):
        return 187

    @property
    def max_isotope(self):
        return 187

    @property
    def min_isotope(self):
        return 183

    @property
    def common_valences(self):
        return (0, 6), (5, 1), (7, 1)

    @property
    def valences_exceptions(self):
        return ((0, 4, ((2, 'O'), (2, 'O'))),  # ReO2
                (0, 5, ((2, 'O'), (1, 'O'))),  # Re2O3
                (0, 4, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # Re(OH)4
                (0, 4, ((1, 'O'), (1, 'O'), (2, 'O'))),  # ReO3^2-
                (0, 4, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # ReO4^4-
                (-4, 6, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Re(CN)6^4-
                (-5, 7, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Re(CN)6^5-
                (-6, 8, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Re(CN)6^6-
                (-3, 5, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Re(CN)6^3-
                (0, 6, ((2, 'S'),)),  # ReS
                (0, 4, ((2, 'S'), (2, 'S'))))  # ReS2


class Bh(Element, PeriodVII, GroupVII):
    @property
    def atomic_number(self):
        return 107

    @property
    def atomic_mass(self):
        return 267

    @property
    def electronegativity(self):
        return None

    @property
    def common_isotope(self):
        return 267

    @property
    def max_isotope(self):
        return 267

    @property
    def min_isotope(self):
        return 267

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupVII', 'Mn', 'Tc', 'Re', 'Bh']
