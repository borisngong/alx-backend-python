#!/usr/bin/env python3
""""
Module for working with time of execution in async
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Function responsible for returning the toal runtime of asyncio """
    startTime = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        )
    endTime = time.perf_counter()
    recordTime = endTime - startTime
    return recordTime