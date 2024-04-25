#!/usr/bin/env python3
"""identifiying truples and floats"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int,float]) -> Tuple[str, float]:
    """return a tuple with the string k and the scquare of v as a float"""
    return k, float(v) ** 2
