#!/usr/bin/env python3
"""
Module for working with comprehensive 
"""

import asyncio
import random

async def async_generator():
    """
    Function that yied random number between 0 and 19 using random Module
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


