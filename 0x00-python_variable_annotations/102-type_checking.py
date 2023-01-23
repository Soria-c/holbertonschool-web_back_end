#!/usr/bin/env python3
""" Using annotations """
from typing import Tuple, TypeVar, List
T = TypeVar("T")


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms an array by a given value"""
    zoomed_in: Tuple = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return list(zoomed_in)


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
