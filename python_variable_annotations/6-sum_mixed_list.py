#!/usr/bin/env python3
"""sum of mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of integers and floats ina a mix list"""
    return sum(mxd_lst)
