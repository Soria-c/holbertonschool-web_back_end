#!/usr/bin/env python3
""" Using annotations """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns sum of a list"""
    return tuple([k, v * v])
