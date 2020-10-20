#!/usr/bin/env python3
"""Define element_length function"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return values with the appropriate types"""
    return [(i, len(i)) for i in lst]