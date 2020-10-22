#!/usr/bin/env python3
"""async generator"""


import random
from typing import List
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from generator, return them"""
    return [i async for i in async_generator()]
