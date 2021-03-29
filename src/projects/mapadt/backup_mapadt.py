#!/usr/bin/env python3
"""
`mapadt` implementation

@author: Adam Mertzenich
"""


from typing import Any, List, Tuple


class HashMap:
    """Class HashMap"""

    def __init__(self, size_init: int = 16):
        """
        Initialize HashTable

        @param size_init: size of the map
        """
        self._size: int = size_init
        self._keys: List = [None] * self._size
        self._values: List = [None] * self._size

    def __setitem__(self, key: int, value: Any) -> None:
        """
        Setter

        @param key: key of the item in the collection
        @param value: new value to be added to (updated in) the collection
        """
        self._put(key, value)

    def _put(self, key: int, value: Any) -> None:
        """
        Setter

        @param key: key of the item in the collection
        @param value: new value to be added to (updated in) the collection
        """
        hash_value = self._hash(key)

        if self._keys[hash_value] is None:
            self._keys[hash_value] = key
            self._values[hash_value] = value
        else:
            if self._keys[hash_value] == key:
                self._values[hash_value] = value  # replace
            else:
                next_slot = self._rehash(hash_value, len(self._keys))
                while (
                    self._keys[next_slot] is not None
                    and self._keys[next_slot] != key
                ):
                    next_slot = self._rehash(next_slot, len(self._keys))

                if self._keys[next_slot] is None:
                    self._keys[next_slot] = key
                    self._values[next_slot] = value
                else:
                    self._values[next_slot] = value

    def __getitem__(self, key: int) -> Any:
        """
        Getter

        @param key: key of the new item in the collection
        """
        return self.get(key)

    def get(self, key: int) -> Any:
        """
        Getter

        @param key: key of the new item in the collection
        """
        start_slot = self._hash(key)

        position = start_slot
        while self._keys[position] is not None:
            if self._keys[position] == key:
                return self._values[position]
            position = self._rehash(position, len(self._keys))
            if position == start_slot:
                return None

    def __len__(self) -> int:
        """
        Map size

        @return a number of key-value pairs stored in the collection
        """
        return len(self._keys)

    def __contains__(self, key: int) -> bool:
        """
        key in HashMap

        Check if the key is in the collection
        @param key: key of an item in the collection
        @return True if the key is found, False otherwise
        """
        if key in self._keys:
            return True
        return False

    def __str__(self) -> str:
        """
        String representation of the collection

        @return collections as a string
        """
        output = {}
        for count, i in enumerate(self._keys):
            if i is not None:
                output[self._keys[count]] = self._values[count]
        return str(output)

    def _hash(self, key: int) -> int:
        """
        Hash function

        Simple remainder
        @param key: key of an element
        """
        return key % self._size

    def _rehash(self, old_hash: int, step: int = 1) -> int:
        """
        Rehash function

        Use quadratic probing
        @param old_hash: old hash value
        @param step: step (1 by default)
        @return new hash
        """
        return (old_hash + step) % self._size

    def keys(self) -> List[int]:
        """
        Keys in the collection

        @return all keys
        """
        raise NotImplementedError

    def values(self) -> List[Any]:
        """
        Values in the collection

        @return all values
        """
        raise NotImplementedError

    def items(self) -> List[Tuple[int, Any]]:
        """
        Items (key: value) in the collections

        @return all items
        """
        raise NotImplementedError


def main():
    """main"""
    hash_map = HashMap(11)
    hash_map[0] = 1
    hash_map[7] = 'carrot'
    hash_map[3] = True
    print(hash_map)


if __name__ == "__main__":
    main()
