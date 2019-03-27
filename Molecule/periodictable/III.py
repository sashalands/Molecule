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


class GroupIII:
    pass


class Sc(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 21

    @property
    def atomic_mass(self):
        return 44.956

    @property
    def electronegativity(self):
        return 1.36

    @property
    def common_isotope(self):
        return 45

    @property
    def max_isotope(self):
        return 48

    @property
    def min_isotope(self):
        return 45

    @property
    def common_valences(self):
        return (0, 2), (3, 1)

    @property
    def valences_exceptions(self):
        return (-3, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),


class Y(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 39

    @property
    def atomic_mass(self):
        return 88.906

    @property
    def electronegativity(self):
        return 1.22

    @property
    def common_isotope(self):
        return 89

    @property
    def max_isotope(self):
        return 87

    @property
    def min_isotope(self):
        return 91

    @property
    def common_valences(self):
        return (0, 2), (3, 1)

    @property
    def valences_exceptions(self):
        return ()


class La(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 57

    @property
    def atomic_mass(self):
        return 138.9055

    @property
    def electronegativity(self):
        return 1.1

    @property
    def common_isotope(self):
        return 139

    @property
    def max_isotope(self):
        return 139

    @property
    def min_isotope(self):
        return 137

    @property
    def common_valences(self):
        return (0, 2), (3, 1)

    @property
    def valences_exceptions(self):
        return ()


class Ce(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 58

    @property
    def atomic_mass(self):
        return 140.12

    @property
    def electronegativity(self):
        return 1.12

    @property
    def common_isotope(self):
        return 140

    @property
    def max_isotope(self):
        return 144

    @property
    def min_isotope(self):
        return 134

    @property
    def common_valences(self):
        return (0, 3), (3, 2)

    @property
    def valences_exceptions(self):
        return ((0, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),
                (0, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),
                (0, 1, ((2, 'O'), (2, 'O'))))


class Pr(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 59

    @property
    def atomic_mass(self):
        return 140.9077

    @property
    def electronegativity(self):
        return 1.13

    @property
    def common_isotope(self):
        return 141

    @property
    def max_isotope(self):
        return 143

    @property
    def min_isotope(self):
        return 141

    @property
    def common_valences(self):
        return (0, 4), (3, 3)

    @property
    def valences_exceptions(self):
        return ((0, 2, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 2, ((2, 'O'), (2, 'O'))))


class Nd(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 60

    @property
    def atomic_mass(self):
        return 144.242

    @property
    def electronegativity(self):
        return 1.14

    @property
    def common_isotope(self):
        return 142

    @property
    def max_isotope(self):
        return 150

    @property
    def min_isotope(self):
        return 142

    @property
    def common_valences(self):
        return (0, 5), (3, 4)

    @property
    def valences_exceptions(self):
        return ((0, 5, ((1, 'O'), (1, 'O'))),
                (0, 5, ((1, 'F'), (1, 'F'))),
                (0, 5, ((1, 'Cl'), (1, 'Cl'))),
                (0, 5, ((1, 'Br'), (1, 'Br'))),
                (0, 5, ((1, 'I'), (1, 'I'))),
                (0, 5, ((1, 'F'), (1, 'Cl'))),
                (0, 5, ((1, 'F'), (1, 'Br'))),
                (0, 5, ((1, 'F'), (1, 'I'))),
                (0, 5, ((1, 'C'), (1, 'C'))),
                (0, 5, ((1, 'H'), (1, 'H'))),
                (0, 5, ((2, 'O'),)),
                (0, 3, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))))


class Pm(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 61

    @property
    def atomic_mass(self):
        return 144.9127

    @property
    def electronegativity(self):
        return 1.13

    @property
    def common_isotope(self):
        return 145

    @property
    def max_isotope(self):
        return 147

    @property
    def min_isotope(self):
        return 145

    @property
    def common_valences(self):
        return (0, 6), (3, 5)

    @property
    def valences_exceptions(self):
        return ()


class Sm(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 62

    @property
    def atomic_mass(self):
        return 150.36

    @property
    def electronegativity(self):
        return 1.17

    @property
    def common_isotope(self):
        return 152

    @property
    def max_isotope(self):
        return 154

    @property
    def min_isotope(self):
        return 144

    @property
    def common_valences(self):
        return (0, 7), (3, 6)

    @property
    def valences_exceptions(self):
        return ((0, 7, ((1, 'O'), (1, 'O'))),
                (0, 7, ((1, 'F'), (1, 'F'))),
                (0, 7, ((1, 'Cl'), (1, 'Cl'))),
                (0, 7, ((1, 'Br'), (1, 'Br'))),
                (0, 7, ((1, 'I'), (1, 'I'))),
                (0, 7, ((1, 'F'), (1, 'Cl'))),
                (0, 7, ((1, 'F'), (1, 'Br'))),
                (0, 7, ((1, 'F'), (1, 'I'))),
                (0, 7, ((1, 'C'), (1, 'C'))),
                (0, 7, ((1, 'H'), (1, 'H'))),
                (0, 7, ((2, 'O'),)))


class Eu(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 63

    @property
    def atomic_mass(self):
        return 151.964

    @property
    def electronegativity(self):
        return 1.2

    @property
    def common_isotope(self):
        return 153

    @property
    def max_isotope(self):
        return 155

    @property
    def min_isotope(self):
        return 150

    @property
    def common_valences(self):
        return (0, 8), (3, 7)

    @property
    def valences_exceptions(self):
        return ((0, 8, ((1, 'O'), (1, 'O'))),
                (0, 8, ((1, 'F'), (1, 'F'))),
                (0, 8, ((1, 'Cl'), (1, 'Cl'))),
                (0, 8, ((1, 'Br'), (1, 'Br'))),
                (0, 8, ((1, 'I'), (1, 'I'))),
                (0, 8, ((1, 'F'), (1, 'Cl'))),
                (0, 8, ((1, 'F'), (1, 'Br'))),
                (0, 8, ((1, 'F'), (1, 'I'))),
                (0, 8, ((1, 'C'), (1, 'C'))),
                (0, 8, ((1, 'H'), (1, 'H'))),
                (0, 8, ((2, 'O'),)))


class Gd(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 64

    @property
    def atomic_mass(self):
        return 157.25

    @property
    def electronegativity(self):
        return 1.2

    @property
    def common_isotope(self):
        return 158

    @property
    def max_isotope(self):
        return 160

    @property
    def min_isotope(self):
        return 148

    @property
    def common_valences(self):
        return (0, 9), (3, 8)

    @property
    def valences_exceptions(self):
        return ()


class Tb(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 65

    @property
    def atomic_mass(self):
        return 158.9254

    @property
    def electronegativity(self):
        return 1.1

    @property
    def common_isotope(self):
        return 159

    @property
    def max_isotope(self):
        return 159

    @property
    def min_isotope(self):
        return 157

    @property
    def common_valences(self):
        return (0, 6), (3, 5)

    @property
    def valences_exceptions(self):
        return ((0, 4, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 4, ((2, 'O'), (2, 'O'))))


class Dy(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 66

    @property
    def atomic_mass(self):
        return 162.5

    @property
    def electronegativity(self):
        return 1.22

    @property
    def common_isotope(self):
        return 162

    @property
    def max_isotope(self):
        return 164

    @property
    def min_isotope(self):
        return 154

    @property
    def common_valences(self):
        return (0, 5), (3, 4)

    @property
    def valences_exceptions(self):
        return ((0, 3, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 3, ((2, 'O'), (2, 'O'))))


class Ho(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 67

    @property
    def atomic_mass(self):
        return 164.93

    @property
    def electronegativity(self):
        return 1.23

    @property
    def common_isotope(self):
        return 165

    @property
    def max_isotope(self):
        return 166

    @property
    def min_isotope(self):
        return 163

    @property
    def common_valences(self):
        return (0, 4), (3, 3)

    @property
    def valences_exceptions(self):
        return ((0, 4, ((1, 'O'), (1, 'O'))),
                (0, 4, ((1, 'F'), (1, 'F'))),
                (0, 4, ((1, 'Cl'), (1, 'Cl'))),
                (0, 4, ((1, 'Br'), (1, 'Br'))),
                (0, 4, ((1, 'I'), (1, 'I'))),
                (0, 4, ((1, 'F'), (1, 'Cl'))),
                (0, 4, ((1, 'F'), (1, 'Br'))),
                (0, 4, ((1, 'F'), (1, 'I'))),
                (0, 4, ((1, 'C'), (1, 'C'))),
                (0, 4, ((1, 'H'), (1, 'H'))),
                (0, 4, ((2, 'O'),)))


class Er(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 68

    @property
    def atomic_mass(self):
        return 167.26

    @property
    def electronegativity(self):
        return 1.24

    @property
    def common_isotope(self):
        return 166

    @property
    def max_isotope(self):
        return 172

    @property
    def min_isotope(self):
        return 160

    @property
    def common_valences(self):
        return (0, 3), (3, 2)

    @property
    def valences_exceptions(self):
        return ()


class Tm(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 69

    @property
    def atomic_mass(self):
        return 168.93

    @property
    def electronegativity(self):
        return 1.25

    @property
    def common_isotope(self):
        return 169

    @property
    def max_isotope(self):
        return 171

    @property
    def min_isotope(self):
        return 167

    @property
    def common_valences(self):
        return (0, 2), (3, 1)

    @property
    def valences_exceptions(self):
        return ((0, 2, ((1, 'O'), (1, 'O'))),
                (0, 2, ((1, 'F'), (1, 'F'))),
                (0, 2, ((1, 'Cl'), (1, 'Cl'))),
                (0, 2, ((1, 'Br'), (1, 'Br'))),
                (0, 2, ((1, 'I'), (1, 'I'))),
                (0, 2, ((1, 'F'), (1, 'Cl'))),
                (0, 2, ((1, 'F'), (1, 'Br'))),
                (0, 2, ((1, 'F'), (1, 'I'))),
                (0, 2, ((1, 'C'), (1, 'C'))),
                (0, 2, ((1, 'H'), (1, 'H'))),
                (0, 2, ((2, 'O'),)))


class Yb(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 70

    @property
    def atomic_mass(self):
        return 173.05

    @property
    def electronegativity(self):
        return 1.1

    @property
    def common_isotope(self):
        return 174

    @property
    def max_isotope(self):
        return 176

    @property
    def min_isotope(self):
        return 166

    @property
    def common_valences(self):
        return (0, 1), (3, 1)

    @property
    def valences_exceptions(self):
        return ((0, 1, ((1, 'O'), (1, 'O'))),
                (0, 1, ((1, 'F'), (1, 'F'))),
                (0, 1, ((1, 'Cl'), (1, 'Cl'))),
                (0, 1, ((1, 'Br'), (1, 'Br'))),
                (0, 1, ((1, 'I'), (1, 'I'))),
                (0, 1, ((1, 'F'), (1, 'Cl'))),
                (0, 1, ((1, 'F'), (1, 'Br'))),
                (0, 1, ((1, 'F'), (1, 'I'))),
                (0, 1, ((1, 'C'), (1, 'C'))),
                (0, 1, ((1, 'H'), (1, 'H'))),
                (0, 1, ((2, 'O'),)))


class Lu(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 71

    @property
    def atomic_mass(self):
        return 174.97

    @property
    def electronegativity(self):
        return 1.27

    @property
    def common_isotope(self):
        return 175

    @property
    def max_isotope(self):
        return 176

    @property
    def min_isotope(self):
        return 173

    @property
    def common_valences(self):
        return (0, 2), (3, 1)

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupIII', 'Sc', 'Y',
           'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']
