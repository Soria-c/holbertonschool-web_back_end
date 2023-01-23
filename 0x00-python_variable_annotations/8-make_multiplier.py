#!/usr/bin/env python3
""" Using annotations """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function"""
    return lambda x: multiplier * x
