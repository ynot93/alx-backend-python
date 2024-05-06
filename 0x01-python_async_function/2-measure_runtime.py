#!/usr/bin/env python3
"""
This module tests the basics of async coroutines

"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n, max_delay):
    """
    This function measures the time executing wait_n takes
    
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    
    total_time = end_time - start_time
        
    return total_time / n
