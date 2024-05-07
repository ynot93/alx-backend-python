#!/usr/bin/env python3
"""
This module tests understanding of Async comprehension

"""
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loops 10 times, waits 1 sec and yields random number
    between 0 - 10

    """
    for i in range(1, 11):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
