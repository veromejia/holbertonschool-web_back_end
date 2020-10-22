#!/usr/bin/env python3
"""measure_runtime"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return time of 4 async gather calls"""
    tasks = []
    total_time = time.time()
    for _i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    return time.time() - total_time
