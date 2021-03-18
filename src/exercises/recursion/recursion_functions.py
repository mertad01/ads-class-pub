#!/usr/bin/env python3
"""
`recursion` implementation

@author:
"""
# function from fractions.py:

def gcd(num_one: int, num_two: int) -> int:
    """Greatest Common Denominator"""
    if not num_one % num_two:
        return num_two
    return gcd(num_two, num_one % num_two)


def diamond_ite(levels: int) -> None:
    """Print a diamond"""
    runs = (2*levels)-1
    result = []
    for i in range(runs):
        out = '*'
        if i < levels:
            for k in range((2 * i)):
                out += '*'
            formatter = '{:^' + str(runs) +'}'
            result.append(formatter.format(out))
    foo = result[::-1]
    for i in result[::-1]:
        result.append(i)
    result.pop(levels)
    for i in result:
        print(i)

# output diamond_ite(5)
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *


def diamond_rec(levels: int) -> None:
    """Print a diamond"""
    diamond_rec_results(0, (levels*2)-1, levels-1)

def diamond_rec_results(begin, end, center):
    """Print results of diamond_rec"""
    if begin < end:
        if begin <= center:
            formatter = '{:^' + str(end) + '}'
            print(formatter.format("*"))
        else:
            formatter = '{:^' + str(end) + '}'
            test = begin - center
            print(formatter.format("*" * test))
        diamond_rec_results(begin+1, end, center)



def hourglass_ite(levels: int) -> None:
    """Print an hourglass"""
    runs = (2*levels)-1
    result = []
    for i in range(runs):
        output = '*'
        if i < levels:
            for k in range(runs-1):
                output += '*'
            runs -= 2
            formatter = '{:^' + str((2*levels)-1) + '}'
            result.append(formatter.format(output))
    foo = result[::-1]
    for i in result[::-1]:
        result.append(i)
    result.pop(levels)
    for i in result:
        print(i)


def hourglass_rec(levels: int) -> None:
    """Print an hourglass"""
    raise NotImplementedError


def main():
    """Main"""
    diamond_rec(5)


if __name__ == "__main__":
    main()
