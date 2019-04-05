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


class GroupXII:
    pass


class Zn(Element, PeriodIV, GroupXII):
    @property
    def atomic_number(self):
        return 30

    @property
    def atomic_mass(self):
        return 65.38

    @property
    def electronegativity(self):
        return 1.65

    @property
    def common_isotope(self):
        return 64

    @property
    def max_isotope(self):
        return 72

    @property
    def min_isotope(self):
        return 64

    @property
    def common_valences(self):
        return (0, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ((-4, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # Zn[(OH)6]4-
                (-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # Zn[(OH)4]2-
                (-2, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Zn[(CN)4]2-
                (-1, 1, ((1, 'C'), (1, 'C'), (1, 'C'))),  # Zn[(CN)3]-
                (-2, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # Zn[(NCS)4]2-
                (-2, 1, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))))  # Zn[(SCN)4]2-


class Cd(Element, PeriodV, GroupXII):
    @property
    def atomic_number(self):
        return 48

    @property
    def atomic_mass(self):
        return 112.411

    @property
    def electronegativity(self):
        return 1.69

    @property
    def common_isotope(self):
        return 114

    @property
    def max_isotope(self):
        return 116

    @property
    def min_isotope(self):
        return 106

    @property
    def common_valences(self):
        return (0, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ((-4, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))), # Cd[(OH)6]4-
                (-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # Cd[(OH)4]2-
                (-2, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Cd[(CN)4]2-
                (-1, 1, ((1, 'C'), (1, 'C'), (1, 'C'))),   # Cd[(CN)3]-
                (-2, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # Cd[(NCS)4]2-
                (-2, 1, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))))  # Cd[(SCN)4]2-


class Hg(Element, PeriodVI, GroupXII):
    @property
    def atomic_number(self):
        return 80

    @property
    def atomic_mass(self):
        return 200.592

    @property
    def electronegativity(self):
        return 2.00

    @property
    def common_isotope(self):
        return 200

    @property
    def max_isotope(self):
        return 204

    @property
    def min_isotope(self):
        return 194

    @property
    def common_valences(self):
        return (0, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ((-2, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # Hg[(CN)4]2-
                (-1, 1, ((1, 'C'), (1, 'C'), (1, 'C'))),  # Hg[(CN)3]-
                (-2, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # Hg[(NCS)4]2-
                (-2, 1, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # Hg[(SCN)4]2-
                (0, 2, ((1, 'O'),)),  # Hg2O
                (0, 2, ((1, 'Cl'),)),  # HgCl
                (0, 2, ((1, 'Br'),)))  #HgBr


class Cn(Element, PeriodVII, GroupXII):
    @property
    def atomic_number(self):
        return 112

    @property
    def atomic_mass(self):
        return 285

    @property
    def electronegativity(self):
        return None

    @property
    def common_isotope(self):
        return 285

    @property
    def max_isotope(self):
        return 285

    @property
    def min_isotope(self):
        return 285

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupXII', 'Zn', 'Cd', 'Hg', 'Cn']
