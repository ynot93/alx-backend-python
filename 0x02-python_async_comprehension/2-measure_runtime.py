#!/usr/bin/env python3
"""
This module tests understanding of Async comprehension
in Python

"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure time it takes to run 4 parallel comprehensions

    """
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()

    measure_runtime = end_time - start_time

    return measure_runtime
