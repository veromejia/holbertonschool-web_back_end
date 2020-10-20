#!/usr/bin/env python3
"""Define make_multipler function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier."""
    return lambda x: x * multiplier
