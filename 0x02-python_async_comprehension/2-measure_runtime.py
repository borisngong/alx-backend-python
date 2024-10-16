#!/usr/bin/env python3
"""
Module for working with time of execution in async tasks.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Function responsible for returning the total runtime of
    asyncio tasks
    """
    startTime = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    endTime = time.perf_counter()
    recordTime = endTime - startTime
    return recordTime
