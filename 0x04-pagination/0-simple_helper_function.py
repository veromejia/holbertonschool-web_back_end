#!/usr/bin/env python3
"""Defines function index_range"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """turn a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to
    return in a list for those particular pagination parameters"""
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
