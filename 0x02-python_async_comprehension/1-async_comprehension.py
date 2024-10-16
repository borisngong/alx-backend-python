#!/usr/bin/env python3
"""Module for working with Async Comprehensions"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Function responsible for returning comprehensive list """
    comprehensive = [k async for k in async_generator()]
    return comprehensive
