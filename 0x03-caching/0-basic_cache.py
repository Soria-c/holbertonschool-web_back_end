#!/usr/bin/env python3
"""Caching in python"""
import base_caching


class BasicCache(base_caching.BaseCaching):
    """Defines a basic cache and its methods"""
    def put(self, key, item):
        """Inserts or updates a cache"""
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """Retrieves from the cache"""
        return self.cache_data.get(key, None)
