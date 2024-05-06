#!/usr/bin/env python3
"""
This module tests the basics of async coroutines

"""
import random
import asyncio


async def wait_random(max_delay=10):
    """
    This function waits for random delay and eventually
    returns the coroutine

    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
