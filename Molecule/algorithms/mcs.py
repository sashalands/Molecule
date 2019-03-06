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
from collections import defaultdict
from itertools import product, permutations, combinations
from typing import Dict, List, Set, Hashable


def clique(graph: Dict[Hashable, Set[Hashable]]) -> List[Hashable]:
    clique_atoms = set()
    roots = sorted(graph, key=lambda x: len(graph[x]), reverse=True)
    for i in roots:
        neighbours = graph[i] - clique_atoms
        if not neighbours:
            continue
        neighbours_root = neighbours.copy()
        neighbours_root.add(i)
        for j in neighbours:
            n_n = set(graph[j])
            n_n.add(j)
            if not n_n.issuperset(neighbours_root):
                break
        else:
            yield list(neighbours_root)
            clique_atoms.update(neighbours_root)


class MCS:
    def mcs_mapping(self, other) -> Dict[int, int]:
        p = {}
        a1 = defaultdict(set)
        for (s, v1), (o, v2) in product(self._atoms.items(), other._atoms.items()):
            if v1 == v2:
                p[(s, o)] = set()
                a1[s].add(o)
        for (s1, v1), (s2, v2) in combinations(a1.items(), 2):
            for o1, o2 in product(v1, v2):
                if o1 != o2:
                    k1 = (s1, o1)
                    k2 = (s2, o2)
                    p[k1].add(k2)
                    p[k2].add(k1)
        print(next(clique(p)))



