#!/usr/bin/env python3
"""Caching in python"""
import base_caching
import collections


class FIFOCache(base_caching.BaseCaching):
    """Defines a FIFO cache and its methods"""

    def __init__(self):
        super().__init__()
        self.key_queue = collections.deque()

    def put(self, key, item):
        """Inserts or updates a cache"""
        if key and item:
            self.cache_data.update({key: item})
            self.key_queue.append(key)
            if len(self.cache_data) > super().MAX_ITEMS:
                discard = self.key_queue.popleft()
                self.cache_data.pop(discard)
                print(f"DISCARD: {discard}")

    def get(self, key):
        """Retrieves from the cache"""
        return self.cache_data.get(key, None)
