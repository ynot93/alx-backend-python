#!/usr/bin/env python3
"""
This module tests understanding of Async comprehension
in Python

"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects and returns 10 numbers using async comprehension

    """
    return [i async for i in async_generator()]
