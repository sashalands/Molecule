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
from abc import ABC, abstractmethod
from typing import Optional, Tuple


class Element(ABC):
    def __init__(self, charge: int = 0, isotope: Optional[int] = None, multiplicity: Optional[int] = None):
        """
        Element object with specified charge, isotope and multiplicity

        :param charge: formal charge of atom
        :param isotope: the isotope number of element, if isotope not entered most common isotope will be used
        :param multiplicity: multiplicity of atom
        """
        if isinstance(charge, int):
            if self.min_charge <= charge <= self.max_charge:
                self.__charge = charge
            else:
                raise ValueError('charge should be in range of {} to {}'.format(self.min_charge, self.max_charge))
        else:
            raise TypeError('integer required')

        if isotope is None:
            self.__isotope = self.common_isotope
        else:
            if isinstance(isotope, int):
                if self.min_isotope <= isotope <= self.max_isotope:
                    self.__isotope = isotope
                else:
                    raise ValueError('isotope value should be in range of {} to {}'.format(self.min_isotope,
                                                                                           self.max_isotope))
            else:
                raise TypeError('integer required')

        if multiplicity is None:
            self.__multiplicity = multiplicity
        elif isinstance(multiplicity, int):
            if 1 <= multiplicity <= self.max_multiplicity:
                self.__multiplicity = multiplicity
            else:
                raise ValueError('multiplicity should be in range of 1 to {}'.format(self.max_multiplicity))
        else:
            raise TypeError('integer required')

    @property
    def charge(self):
        return self.__charge

    @property
    def isotope(self):
        return self.__isotope

    @property
    def multiplicity(self):
        return self.__multiplicity

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.charge == other.charge and self.isotope == other.isotope \
               and self.multiplicity == other.multiplicity

    def __hash__(self):
        """
        7bit | 9bit | 3bit | 4bit
        """
        return (self.atomic_number << 16) | (self.isotope << 7) | (self.charge << 4) | (self.multiplicity or 0)

    @property
    @abstractmethod
    def atomic_number(self) -> int:
        """
        Element number
        """

    @property
    @abstractmethod
    def common_valences(self) -> Tuple[Tuple[int, int], ...]:
        """
        Returns tuple of tuples of common valences and matching multiplicity of element
        :return ((valence1: int, multiplicity1: int), (valence2: int, multiplicity2: int), ...)
        """


    @property
    @abstractmethod
    def valences_exceptions(self) -> Tuple[Tuple[int, int, Tuple[Tuple[int, str], ...]]]:
        """
        Returns tuple of tuples of exceptions in charges and matching multiplicity of element. If there no
        exceptions in valencies, returns empty tuple.
        :return (charge: int, multiplicity: int, ((bond1: int, atom1: str), (bond2: int, atom2: str), ...))
        """

    @property
    @abstractmethod
    def common_isotope(self) -> int:
        """
        elements common isotope on Earth
        """

    @property
    @abstractmethod
    def min_isotope(self) -> int:
        """
        elements lightest isotope on Earth
        """

    @property
    @abstractmethod
    def max_isotope(self) -> int:
        """
        elements heaviest isotope on Earth
        """

    @property
    @abstractmethod
    def electronegativity(self) -> float:
        """
        electronegativity of atom
        """

    @property
    @abstractmethod
    def atomic_mass(self) -> float:
        """
        elements atomic mass
        """
