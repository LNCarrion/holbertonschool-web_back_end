#!/usr/bin/env python3
""" Async basics, random tasks """

import asyncio
from typing import List

wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of completed random delay results for n tasks with a given max_delay """

    tasks = [wait_random(max_delay) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
