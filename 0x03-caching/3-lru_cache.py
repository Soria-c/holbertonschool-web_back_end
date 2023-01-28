#!/usr/bin/env python3
"""Caching in python"""
import base_caching
import collections


class LRUCache  (base_caching.BaseCaching):
    """Defines a LRU cache and its methods"""

    def __init__(self):
        """Initializes object"""
        super().__init__()
        self.usage_time_count = 0
        self.el_time = {}

    def put(self, key, item):
        """Inserts or updates a cache"""
        if key and item:
            self.cache_data.update({key: item})
            self.el_time.update({key: self.usage_time_count})
            if len(self.cache_data) > super().MAX_ITEMS:
                dis = sorted(self.el_time.items(), key=lambda x: x[1])[0][0]
                self.cache_data.pop(dis)
                self.el_time.pop(dis)
                print(f"DISCARD: {dis}")
            self.usage_time_count += 1

    def get(self, key):
        """Retrieves from the cache"""
        el = self.cache_data.get(key, None)
        if el:
            self.el_time.update({key: self.usage_time_count})
        return el
