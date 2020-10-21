#!/usr/bin/env python3
"""Define task_wait_n"""


from asyncio import as_completed
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return array of delays from async function"""
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in as_completed(delays)]
