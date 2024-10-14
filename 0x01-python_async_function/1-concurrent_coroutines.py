#!/usr/bin/env python3
"""
Module for working with Async functions
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> [float]:
    """Return a list of n random floats between n and max_delay"""
    a_delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(a_delays)
