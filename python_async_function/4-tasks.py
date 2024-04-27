#!/usr/bin/env python3
""" Async basics, tasks """

from asyncio import Task, create_task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Return a task """
    return create_task(wait_random(max_delay))
