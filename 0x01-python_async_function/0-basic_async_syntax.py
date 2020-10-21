#!/usr/bin/env python3
"""basics of async"""


import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    """wait ramdom function"""
    time_delay = random.random() * max_delay
    await asyncio.sleep(time_delay)
    return time_delay
