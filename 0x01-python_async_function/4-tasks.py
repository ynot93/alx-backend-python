#!/usr/bin/env python3
"""
Module that tets understanding of async in Python

"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n, max_delay):
    """
    Executes multiple coroutines concurrently

    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    results = await asyncio.gather(*tasks)

    return results
