#!/usr/bin/env python3
""" Measure runtime """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime"""
    start_time = time()
    tasks = [async_comprehension() for _ in range(4)]
    await gather(*tasks)
    end_time = time()
    return end_time - start_time
