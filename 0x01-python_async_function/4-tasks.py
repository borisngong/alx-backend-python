#!/usr/bin/env python3
"""
Module that defines two asynchronous functions:
task_wait_random and task_wait_n.
"""

import asyncio
import random
from typing import List


async def task_wait_random(max_delay: int) -> float:
    """Wait for a random delay between 0 and max_delay seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for n tasks to complete, each waiting for a random delay."""
    tasks = [
        asyncio.create_task(task_wait_random(max_delay))
        for _ in range(n)
    ]
    delays = await asyncio.gather(*tasks)
    return delays
