#!/usr/bin/env python3
"""
Module to measure execution time of wait_n
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Function to measure total execution time of wait_n """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    #Calc the average time per coroutine total elapsed time and return
    total_time = end_time - start_time
    return total_time / n
