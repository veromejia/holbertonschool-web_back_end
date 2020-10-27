#!/usr/bin/python3
"""BasicCache module"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """defining Basic Cache that inherits from
       BaseCaching"""

    def put(self, key, item):
        """ Add key and value pair to cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return value stored in key of cache."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
