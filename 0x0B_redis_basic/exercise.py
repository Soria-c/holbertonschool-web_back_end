#!/usr/bin/env python3
"""Python Redis"""

from redis import Redis
import uuid
from typing import Union


class Cache:
    """Redis class"""
    def __init__(self):
        """Constructor"""
        self._redis: Redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Sets a key value pair"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
