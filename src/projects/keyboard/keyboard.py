#!/usr/bin/env python3
"""
Touchscreen Keyboard
"""

keyboard = {
    3: ("q", "w", "e", "r", "t", "y", "u", "i", "o", "p"),
    2: ("a", "s", "d", "f", "g", "h", "j", "k", "l"),
    1: ("z", "x", "c", "v", "b", "n", "m")
}


def spell_check(filename: str) -> None:
    """Rank words by their proximity to the target"""


def find_axis(key: str):
    """Find X Axis of a Character"""
    for i in keyboard:
        if key in keyboard[i]:
            return keyboard[i].index(key), i
    return False


def word_distance(first_word: str, second_word: str):
    """Find Result"""

    first_list = list(first_word)
    second_list = list(second_word)
    result = 0

    for count, i in enumerate(first_list):
        axis_one = find_axis(i)
        axis_two = find_axis(second_list[count])
        output = (axis_one[0] - axis_two[0]) + (axis_one[1] - axis_two[1])
        result += output

    return abs(result)



def main():
    """Entry point"""
    # spell_check("data/projects/keyboard/sample.in")
    print(word_distance("ifpv", "icpc"))


if __name__ == "__main__":
    main()
