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
    for i in result[::-1]:
        result.append(i)
    result.pop(levels)
    for i in result:
        print(i)


def diamond_rec(levels: int) -> None:
    """Print a diamond"""
    diamond_rec_results(0, levels-1, (2*levels)-1)


def diamond_rec_results(front, center, back):
    """Print results of diamond_rec"""
    if front < back:
        if front < center:
            stars = '*' * ((front * 2) + 1)
            formatter = '{:^' + str(back) + '}'
            print(formatter.format(stars))
        else:
            stars = '*' * (((back - front) * 2) - 1)
            formatter = '{:^' + str(back) + '}'
            print(formatter.format(stars))
        diamond_rec_results(front+1, center, back)



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
    for i in result[::-1]:
        result.append(i)
    result.pop(levels)
    for i in result:
        print(i)


def hourglass_rec(levels: int) -> None:
    """Print an hourglass"""
    hourglass_rec_results(0, levels-1, (2*levels)-1)


def hourglass_rec_results(front, center, back):
    """Print results of diamond_rec"""
    if front < back:
        if front <= center:
            stars = '*' * (back - (2 * front))
            formatter = '{:^' + str(back) + '}'
            print(formatter.format(stars))
        else:
            stars = '*' * ((front - center) * 2 + 1)
            formatter = '{:^' + str(back) + '}'
            print(formatter.format(stars))
        hourglass_rec_results(front+1, center, back)


def main():
    """Main"""
    hourglass_rec(5)


if __name__ == "__main__":
    main()
