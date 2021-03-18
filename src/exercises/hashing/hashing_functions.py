#!/usr/bin/env python3
"""
Exercise `hashing` implementation

@author: Adam Mertzenich
"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    return key % size


def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    first = str(key**2)
    cleaned = '{:0>4}'.format(first)
    middle_digits = int(cleaned[1:-1])
    return middle_digits % size


# changed key to str from int
def hash_folding(key: int, size: int) -> int:
    """Find hash using folding method"""
    item = key.replace('-', '')
    seperated = [item[i:i+2] for i in range(0, len(item), 2)]
    seperated = [int(i) for i in seperated]
    return sum(seperated) % size


def hash_str(key: str, size: int) -> int:
    """Find string hash using simple sum-of-values method"""
    agg = 0
    for i in key:
        agg += ord(i)
    return agg % size


def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    agg = 0
    for count, i in enumerate(key):
        agg += ord(i) * (count)
    return agg % size
