#!/usr/bin/env python3
"""
This module tests the basics of async coroutines

"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """
    Returns a asyncio.Task object

    """
    return asyncio.create_task(wait_random(max_delay))
