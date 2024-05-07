#!/usr/bin/env python3
"""
This module tests understanding of Async comprehension

"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times, waits 1 sec and yields random number
    between 0 - 10

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
