#!/usr/bin/env python3
"""
Module that tets understanding of async in Python

"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    """
    Executes multiple coroutines concurrently

    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    return results
