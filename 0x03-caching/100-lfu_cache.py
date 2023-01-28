#!/usr/bin/env python3
"""Caching in python"""
import base_caching


class LFUCache(base_caching.BaseCaching):
    """Defines a LFU cache and its methods"""

    def __init__(self):
        """Initializes object"""
        super().__init__()
        self.usage_time_count = 0
        self.el_time = {}

    def put(self, key, item):
        """Inserts or updates a cache"""
        if key and item:
            self.cache_data.update({key: item})
            if len(self.cache_data) > super().MAX_ITEMS:
                sortd = sorted(self.el_time.items(), key=lambda x: x[1][1])
                lf = sortd[0][1][1]
                diss = []
                for i in sortd:
                    if (i[1][1] == lf):
                        diss.append(i)
                    else:
                        break
                if len(diss) == 1:
                    self.cache_data.pop(sortd[0][0])
                    self.el_time.pop(sortd[0][0])
                    print(f"DISCARD: {sortd[0][0]}")
                else:
                    dis = sorted(diss, key=lambda x: x[1][0])[0][0]
                    self.el_time.pop(dis)
                    self.cache_data.pop(dis)
                    print(f"DISCARD: {dis}")
            if self.el_time.get(key, None):
                self.el_time[key][1] += 1
                self.el_time[key][0] = self.usage_time_count
            else:
                self.el_time.update({key: [self.usage_time_count, 1]})
            self.usage_time_count += 1

    def get(self, key):
        """Retrieves from the cache"""
        el = self.cache_data.get(key, None)
        if el:
            self.el_time[key][1] += 1
            self.el_time[key][0] = self.usage_time_count
            self.usage_time_count += 1
        return el
