#!/usr/bin/env python3
""" Using annotations """
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """Returns sum of a list"""
    return sum(input_list)
