#!/usr/bin/env python3
"""
`recursion` implementation

@author:
"""
# function from fractions.py:
def old_gcd(num_a: int, num_b: int) -> int:
    """
    Greatest Common Denominator of two integers

    Helper function to simplify fractions
    """
    while num_a % num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_b


def gcd(num_one: int, num_two: int) -> int:
    """Greatest Common Denominator"""
    if not num_one % num_two:
        return num_two
    return gcd(num_two, num_one % num_two)


def diamond_ite(levels: int) -> None:
    """Print a diamond"""
    raise NotImplementedError


def diamond_rec(levels: int) -> None:
    """Print a diamond"""
    raise NotImplementedError


def hourglass_ite(levels: int) -> None:
    """Print an hourglass"""
    raise NotImplementedError


def hourglass_rec(levels: int) -> None:
    """Print an hourglass"""
    raise NotImplementedError


def main():
    """Main"""


if __name__ == "__main__":
    main()
