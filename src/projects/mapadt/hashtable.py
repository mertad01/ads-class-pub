#!/usr/bin/env python3

class HashTable:
    def __init__(self):
        self._size = 11
        self._keys = [None] * self._size
        self._values = [None] * self._size

    def put(self, key, value):
        hash_value = self.hash_function(key, len(self._keys))

        if self._keys[hash_value] is None:
            self._keys[hash_value] = key
            self._values[hash_value] = value
        else:
            if self._keys[hash_value] == key:
                self._values[hash_value] = value  # replace
            else:
                next_slot = self.rehash(hash_value, len(self._keys))
                while (
                    self._keys[next_slot] is not None
                    and self._keys[next_slot] != key
                ):
                    next_slot = self.rehash(next_slot, len(self._keys))

                if self._keys[next_slot] is None:
                    self._keys[next_slot] = key
                    self._values[next_slot] = value
                else:
                    self._values[next_slot] = value

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self._keys))

        position = start_slot
        while self._keys[position] is not None:
            if self._keys[position] == key:
                return self._values[position]
            else:
                position = self.rehash(position, len(self._keys))
                if position == start_slot:
                    return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)
