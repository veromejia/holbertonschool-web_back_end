#!/usr/bin/python3
"""FIFOCache module"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Class LIFOCache """

    def __init__(self):
        """Initialize class instance."""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add key/value pair to cache data using LIFO"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """Get an item by key using LIFO"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None