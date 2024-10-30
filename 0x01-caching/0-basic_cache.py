#!/usr/bin/python3
''' A Python3 Module '''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' This BasicCache inherits from BaseCaching (parent class)
      - It uses self.cache_data, a dictionary from the parent class
      - This caching system doesn’t have limit
    '''
    def put(self, key, item):
        ''' Assigns item as a value to the dictionary self.cache_data's key
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        ''' Returns the value in self.cache_data linked to key
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
