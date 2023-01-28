#!/usr/bin/env python3
"""Caching in python"""
import base_caching
import collections


class LIFOCache (base_caching.BaseCaching):
    """Defines a LIFO cache and its methods"""

    def __init__(self):
        super().__init__()
        self.key_queue = collections.deque()

    def put(self, key, item):
        """Inserts or updates a cache"""
        if key and item:
            self.cache_data.update({key: item})
            if len(self.cache_data) > super().MAX_ITEMS:
                discard = self.key_queue.pop()
                self.cache_data.pop(discard)
                print(f"DISCARD: {discard}")
            self.key_queue.append(key)

    def get(self, key):
        """Retrieves from the cache"""
        return self.cache_data.get(key, None)
