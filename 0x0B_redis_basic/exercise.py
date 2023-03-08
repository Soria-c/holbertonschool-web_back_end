#!/usr/bin/env python3
"""Redis"""

from redis import Redis
import uuid


class Cache():
    """Redis class"""
    def __init__(self):
        """Constructor"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """Sets a key value pair"""
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
