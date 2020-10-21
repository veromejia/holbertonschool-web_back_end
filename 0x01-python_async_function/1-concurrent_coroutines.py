#!/usr/bin/env python3
"""Defines function wait_n"""


from asyncio import as_completed
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays in ascending order"""
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in as_completed(delays)]
