#!/usr/bin/python3
''' A Python3 Module '''

from base_caching import BaseCaching
# base_caching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    ''' inherits from BaseCaching and is a caching system '''
    def __init__(self):
        ''' instance of the class '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' put method '''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_item)

    def get(self, key):
        ''' get method '''
        return self.cache_data.get(key, None)
