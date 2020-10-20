#!/usr/bin/env python3
"""Define first element of a sequence"""


from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return values with the appropriate types"""

    if lst:
        return lst[0]
    else:
        return None
