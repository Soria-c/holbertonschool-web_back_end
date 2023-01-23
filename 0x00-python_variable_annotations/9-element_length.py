#!/usr/bin/env python3
""" Using annotations """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuple"""
    return [(i, len(i)) for i in lst]
