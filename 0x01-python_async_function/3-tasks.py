#!/usr/bin/env python3
"""
Module Responsible for creating a task for wait_random coroutine
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task
    """
    coroutineTasks = asyncio.create_task(wait_random(max_delay))
    return coroutineTasks
