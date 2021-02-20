#!/usr/bin/env python3
"""
Touchscreen Keyboard
"""

from collections import OrderedDict
from timeit import Timer
import operator

keyboard = {
    3: {
        "q": 0, "w": 1, "e": 2, "r": 3, "t": 4, "y": 5, "u": 6, "i": 7,
        "o": 8, "p": 9
        },
    2: {
        "a": 0, "s": 1, "d": 2, "f": 3, "g": 4, "h": 5, "j": 6, "k": 7,
        "l": 8
    },
    1: {
        "z": 0, "x": 1, "c": 2, "v": 3, "b": 4, "n": 5, "m": 6
    }
}


def spell_check(filename: str) -> None:
    """Rank words by their proximity to the target"""
    file = open(filename, "rt")
    test_cases = file.readline().strip()
    working_dict = {}
    for i in range(int(test_cases)):
        count_init = file.readline().strip().split()
        working_dict[count_init[0]] = {}
        for k in range(int(count_init[1])):
            working_dict[count_init[0]][file.readline().strip()] = 0
    file.close()

    ordered_dict = OrderedDict()
    for i in working_dict:
        for item in working_dict[i]:
            working_dict[i][item] = word_distance(i, item)
        wd_items = working_dict[i].items()
        sorted_keys = sorted(wd_items, key=operator.itemgetter(1, 0))
        ordered_dict[i] = sorted_keys

    for i in ordered_dict:
        for k in ordered_dict[i]:
            print(k[0], k[1])


def find_axis(key: str):
    """Find X Axis of a Character"""
    for i in keyboard:
        if key in keyboard[i]:
            return keyboard[i][key], i
    return False


def word_distance(first_word: str, second_word: str):
    """Find Result"""
    result = 0
    for count, i in enumerate(first_word):
        axis_one = find_axis(i)
        axis_two = find_axis(second_word[count])
        output = abs(axis_one[0] - axis_two[0]) + abs(axis_one[1] - axis_two[1])
        result += output

    return result


def main():
    """Entry point"""
    spell_check("../../../data/projects/keyboard/all_firsthalf.in")
    # t1 = Timer("spell_check('../../../data/projects/keyboard/sample.in')", "from __main__ import spell_check")
    # print(f"{t1.timeit(number=1000):15.2f} milliseconds")


if __name__ == "__main__":
    main()

"""
    # for i in working_dict:
    #     sorted_dict = {}
    #     sorted_keys = sorted(working_dict[i], key=working_dict[i].get)
    #     for k in sorted_keys:
    #         sorted_dict[k] = working_dict[i][k]
    #     working_dict[i] = sorted_dict

    # sorted_keys = sorted(working_dict["ifpv"], key=working_dict["ifpv"].get)
    # for k in sorted_keys:
    #     sorted_dict[k] = working_dict["ifpv"][k]

    # working_dict["ifpv"] = sorted_dict

    # working_dict = {
    #     "ifpv": {
    #         "iopc": 0,
    #         "icpc": 0,
    #         "gcpc": 0
    #     },
    #     "edc": {
    #         "wsx": 0,
    #         "edc": 0,
    #         "rfv": 0,
    #         "plm": 0,
    #         "qed": 0
    #     }
    # }
"""
