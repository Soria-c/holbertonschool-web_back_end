#!/usr/bin/env python3
""" Using annotations """
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns first element if possible"""
    if lst:
        return lst[0]
    else:
        return None
