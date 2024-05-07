#!/usr/bin/env python3
"""
This module tests understanding of Async comprehension

"""
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[int, None]:
    for i in range(1, 11):
        asyncio.sleep(1)
        yield random.randint(1, 10)