#!/usr/bin/env python3
"""
Module for altering wait_n to use task_wait_random instead
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Return the list of all the delays (float) in ascending order.
    """
    delay_n = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(delay_n)
