#!/usr/bin/env python3
"""itinerating"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a llist of tuples"""
    return [(i, len(i)) for i in lst]
