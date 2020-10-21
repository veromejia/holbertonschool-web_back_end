#!/usr/bin/env python3
"""Define measure_runtime"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """return the total_time / n """
    t0 = time.time()
    asyncio.run(wait_n(n, max_delay))
    t1 = time.time()
    total_time = t1 - t0
    return total_time / n
