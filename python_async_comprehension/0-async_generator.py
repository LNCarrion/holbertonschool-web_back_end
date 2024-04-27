#!/usr/bin/env python3
""" Async basics, random tasks """

import asyncio
import random
from typing import AsyncGenerator, Generator


async def async_generator() -> AsyncGenerator[float, None]:
    """Async generator that yields random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
