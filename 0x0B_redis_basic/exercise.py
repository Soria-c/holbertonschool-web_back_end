#!/usr/bin/env python3
"""Python Redis"""

from redis import Redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int]:
        """Retrieves data saved in redis given a key"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Retrieves data and casts it to string"""
        return self.get(key, str)

    def get_str(self, key: int) -> int:
        """Retrieves data and casts it to int"""
        return self.get(key, int)
