# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Tagir Akhmetshin <tagirshin@gmail.com>
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


class GroupX:
    pass


class Ni(Element, PeriodIV, GroupX):
    @property
    def atomic_number(self):
        return 28

    @property
    def atomic_mass(self):
        return 58.6934

    @property
    def electronegativity(self):
        return 1.91

    @property
    def common_isotope(self):
        return 58

    @property
    def max_isotope(self):
        return 64

    @property
    def min_isotope(self):
        return 56

    @property
    def common_valences(self):
        return (0, 3), (2, 1)

    @property
    def valences_exceptions(self):
        return ((-2, 1, ((1, 'Ni'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Ni2(CO)6]2-
                (-2, 1, ((1, 'C'),(1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Ni(CO)6]2-
                (-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # [Ni(OH)4]2-, [Ni(NO3)4]
                (-1, 1, ((1, 'O'), (1, 'O'), (1, 'O'))),  # [Ni(NO3)3]-
                (-4, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # [Ni(NO2)6]4-
                (-2, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Ni(CN)4]2-
                (-3, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Ni(CN)5]3-
                (-4, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Ni(NCS)6]4-
                (-4, 1, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Ni(SCN)6]4-
                (-2, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Ni(NCS)4]2-
                (-2, 1, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Ni(SCN)4]2-
                (-2, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [NiF4]2-
                (-2, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [NiCl4]2-
                (-2, 1, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))),  # [NiBr4]2-
                (-3, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))), # [NiCl5]3-
                (0, 1, ((2, 'O'), (1, 'O')))) # Ni2O3


class Pd(Element, PeriodV, GroupX):
    @property
    def atomic_number(self):
        return 46

    @property
    def atomic_mass(self):
        return 106.42

    @property
    def electronegativity(self):
        return 2.20

    @property
    def common_isotope(self):
        return 106

    @property
    def max_isotope(self):
        return 110

    @property
    def min_isotope(self):
        return 102

    @property
    def common_valences(self):
        return (0, 1), (2, 1), (4, 1)

    @property
    def valences_exceptions(self):
        return ((-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # [Pd(OH)4]2-
                (-2, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Pd(CN)4]2-
                (-2, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Pd(NCS)4]2-
                (-2, 1, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Pd(SCN)4]2-
                (-2, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [PdF4]2-
                (-2, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [PdCl4]2-
                (-2, 1, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))),  # [PdBr4]2-
                (-2, 1, ((1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'))))  # [PdI4]2-


class Pt(Element, PeriodVI, GroupX):
    @property
    def atomic_number(self):
        return 78

    @property
    def atomic_mass(self):
        return 195.084

    @property
    def electronegativity(self):
        return 2.28

    @property
    def common_isotope(self):
        return 195

    @property
    def max_isotope(self):
        return 198

    @property
    def min_isotope(self):
        return 190

    @property
    def common_valences(self):
        return (0, 1), (2, 1), (4, 1)

    @property
    def valences_exceptions(self):
        return ((-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # [Pt(OH)6]2-
                (-2, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Pt(CN)4]2-
                (-2, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Pt(CN)6]2-
                (-2, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Pt(NCS)4]2-
                (-2, 1, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Pt(SCN)4]2-
                (-2, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Pt(NCS)6]4-
                (-2, 1, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Pt(SCN)6]4-
                (-2, 1, ((1, 'H'), (1, 'H'), (1, 'H'), (1, 'H'))),  # [PtH4]2-
                (-2, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [PtCl4]2-
                (-1, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'N'))),  # [Pt(NH3)Cl5]-
                (-1, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'N'))),  # [Pt(NH3)Cl3]-
                (-2, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [PtCl6]2-
                (-2, 1, ((1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'))),  # [PdI6]2-
                (0, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # PtCl3
                (0, 1, ((1, 'Br'),(1, 'Br'), (1, 'Br'))),  # PtBr3
                (0, 1, ((1, 'I'), (1, 'I'), (1, 'I'))),  # PtI3
                (0, 1, ((1, 'F'), (1, 'F'), (1, 'F'))),  # PtF3
                (0, 1, ((2, 'O'), (1, 'O'))),  # Pt2O3
                (0, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # PtF5
                (0, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # PtF6
                (0, 1, ((2, 'O'), (2, 'O'), (2, 'O'))))  # PtO3


class Ds(Element, PeriodVII, GroupX):
    @property
    def atomic_number(self):
        return 110

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
        return 271

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupX', 'Ni', 'Pd', 'Pt', 'Ds']
