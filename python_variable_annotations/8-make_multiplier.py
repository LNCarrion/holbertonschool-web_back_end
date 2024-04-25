#!/usr/bin/env python3
"""making a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies floats"""
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
