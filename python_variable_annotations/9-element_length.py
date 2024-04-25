#!/usr/bin/env python3
"""itinerating"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """return a llist of tuples"""
    return [(i, len(i)) for i in lst]
