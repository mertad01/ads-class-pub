#!/usr/bin/env python3
"""
Touchscreen Keyboard
"""

from collections import OrderedDict
import operator

# keyboard = {
#     3: {
#         "q": 0, "w": 1, "e": 2, "r": 3, "t": 4, "y": 5, "u": 6, "i": 7,
#         "o": 8, "p": 9
#         },
#     2: {
#         "a": 0, "s": 1, "d": 2, "f": 3, "g": 4, "h": 5, "j": 6, "k": 7,
#         "l": 8
#     },
#     1: {
#         "z": 0, "x": 1, "c": 2, "v": 3, "b": 4, "n": 5, "m": 6
#     }
# }


# Dictionary containing the distance between a key and every other key.
# Generated using the commented out find_axis and word_distance code
pre_keyboard = {
    'a': {
        'a': 0, 'b': 5, 'c': 3, 'd': 2, 'e': 3, 'f': 3, 'g': 4, 'h': 5, 'i': 8,
        'j': 6, 'k': 7, 'l': 8, 'm': 7, 'n': 6, 'o': 9, 'p': 10, 'q': 1,
        'r': 4, 's': 1, 't': 5, 'u': 7, 'v': 4, 'w': 2, 'x': 2, 'y': 6, 'z': 1
    },
    'b': {
        'a': 5, 'b': 0, 'c': 2, 'd': 3, 'e': 4, 'f': 2, 'g': 1, 'h': 2, 'i': 5,
        'j': 3, 'k': 4, 'l': 5, 'm': 2, 'n': 1, 'o': 6, 'p': 7, 'q': 6, 'r': 3,
        's': 4, 't': 2, 'u': 4, 'v': 1, 'w': 5, 'x': 3, 'y': 3, 'z': 4
    },
    'c': {
        'a': 3, 'b': 2, 'c': 0, 'd': 1, 'e': 2, 'f': 2, 'g': 3, 'h': 4, 'i': 7,
        'j': 5, 'k': 6, 'l': 7, 'm': 4, 'n': 3, 'o': 8, 'p': 9, 'q': 4, 'r': 3,
        's': 2, 't': 4, 'u': 6, 'v': 1, 'w': 3, 'x': 1, 'y': 5, 'z': 2
    },
    'd': {
        'a': 2, 'b': 3, 'c': 1, 'd': 0, 'e': 1, 'f': 1, 'g': 2, 'h': 3, 'i': 6,
        'j': 4, 'k': 5, 'l': 6, 'm': 5, 'n': 4, 'o': 7, 'p': 8, 'q': 3, 'r': 2,
        's': 1, 't': 3, 'u': 5, 'v': 2, 'w': 2, 'x': 2, 'y': 4, 'z': 3
    },
    'e': {
        'a': 3, 'b': 4, 'c': 2, 'd': 1, 'e': 0, 'f': 2, 'g': 3, 'h': 4, 'i': 5,
        'j': 5, 'k': 6, 'l': 7, 'm': 6, 'n': 5, 'o': 6, 'p': 7, 'q': 2, 'r': 1,
        's': 2, 't': 2, 'u': 4, 'v': 3, 'w': 1, 'x': 3, 'y': 3, 'z': 4
    },
    'f': {
        'a': 3, 'b': 2, 'c': 2, 'd': 1, 'e': 2, 'f': 0, 'g': 1, 'h': 2, 'i': 5,
        'j': 3, 'k': 4, 'l': 5, 'm': 4, 'n': 3, 'o': 6, 'p': 7, 'q': 4, 'r': 1,
        's': 2, 't': 2, 'u': 4, 'v': 1, 'w': 3, 'x': 3, 'y': 3, 'z': 4
    },
    'g': {
        'a': 4, 'b': 1, 'c': 3, 'd': 2, 'e': 3, 'f': 1, 'g': 0, 'h': 1, 'i': 4,
        'j': 2, 'k': 3, 'l': 4, 'm': 3, 'n': 2, 'o': 5, 'p': 6, 'q': 5, 'r': 2,
        's': 3, 't': 1, 'u': 3, 'v': 2, 'w': 4, 'x': 4, 'y': 2, 'z': 5
    },
    'h': {
        'a': 5, 'b': 2, 'c': 4, 'd': 3, 'e': 4, 'f': 2, 'g': 1, 'h': 0, 'i': 3,
        'j': 1, 'k': 2, 'l': 3, 'm': 2, 'n': 1, 'o': 4, 'p': 5, 'q': 6, 'r': 3,
        's': 4, 't': 2, 'u': 2, 'v': 3, 'w': 5, 'x': 5, 'y': 1, 'z': 6
    },
    'i': {
        'a': 8, 'b': 5, 'c': 7, 'd': 6, 'e': 5, 'f': 5, 'g': 4, 'h': 3, 'i': 0,
        'j': 2, 'k': 1, 'l': 2, 'm': 3, 'n': 4, 'o': 1, 'p': 2, 'q': 7, 'r': 4,
        's': 7, 't': 3, 'u': 1, 'v': 6, 'w': 6, 'x': 8, 'y': 2, 'z': 9
    },
    'j': {
        'a': 6, 'b': 3, 'c': 5, 'd': 4, 'e': 5, 'f': 3, 'g': 2, 'h': 1, 'i': 2,
        'j': 0, 'k': 1, 'l': 2, 'm': 1, 'n': 2, 'o': 3, 'p': 4, 'q': 7, 'r': 4,
        's': 5, 't': 3, 'u': 1, 'v': 4, 'w': 6, 'x': 6, 'y': 2, 'z': 7
    },
    'k': {
        'a': 7, 'b': 4, 'c': 6, 'd': 5, 'e': 6, 'f': 4, 'g': 3, 'h': 2, 'i': 1,
        'j': 1, 'k': 0, 'l': 1, 'm': 2, 'n': 3, 'o': 2, 'p': 3, 'q': 8, 'r': 5,
        's': 6, 't': 4, 'u': 2, 'v': 5, 'w': 7, 'x': 7, 'y': 3, 'z': 8
    },
    'l': {
        'a': 8, 'b': 5, 'c': 7, 'd': 6, 'e': 7, 'f': 5, 'g': 4, 'h': 3, 'i': 2,
        'j': 2, 'k': 1, 'l': 0, 'm': 3, 'n': 4, 'o': 1, 'p': 2, 'q': 9, 'r': 6,
        's': 7, 't': 5, 'u': 3, 'v': 6, 'w': 8, 'x': 8, 'y': 4, 'z': 9
    },
    'm': {
        'a': 7, 'b': 2, 'c': 4, 'd': 5, 'e': 6, 'f': 4, 'g': 3, 'h': 2, 'i': 3,
        'j': 1, 'k': 2, 'l': 3, 'm': 0, 'n': 1, 'o': 4, 'p': 5, 'q': 8, 'r': 5,
        's': 6, 't': 4, 'u': 2, 'v': 3, 'w': 7, 'x': 5, 'y': 3, 'z': 6
    },
    'n': {
        'a': 6, 'b': 1, 'c': 3, 'd': 4, 'e': 5, 'f': 3, 'g': 2, 'h': 1, 'i': 4,
        'j': 2, 'k': 3, 'l': 4, 'm': 1, 'n': 0, 'o': 5, 'p': 6, 'q': 7, 'r': 4,
        's': 5, 't': 3, 'u': 3, 'v': 2, 'w': 6, 'x': 4, 'y': 2, 'z': 5
    },
    'o': {
        'a': 9, 'b': 6, 'c': 8, 'd': 7, 'e': 6, 'f': 6, 'g': 5, 'h': 4, 'i': 1,
        'j': 3, 'k': 2, 'l': 1, 'm': 4, 'n': 5, 'o': 0, 'p': 1, 'q': 8, 'r': 5,
        's': 8, 't': 4, 'u': 2, 'v': 7, 'w': 7, 'x': 9, 'y': 3, 'z': 10
    },
    'p': {
        'a': 10, 'b': 7, 'c': 9, 'd': 8, 'e': 7, 'f': 7, 'g': 6, 'h': 5,
        'i': 2, 'j': 4, 'k': 3, 'l': 2, 'm': 5, 'n': 6, 'o': 1, 'p': 0, 'q': 9,
        'r': 6, 's': 9, 't': 5, 'u': 3, 'v': 8, 'w': 8, 'x': 10, 'y': 4,
        'z': 11
    },
    'q': {
        'a': 1, 'b': 6, 'c': 4, 'd': 3, 'e': 2, 'f': 4, 'g': 5, 'h': 6, 'i': 7,
        'j': 7, 'k': 8, 'l': 9, 'm': 8, 'n': 7, 'o': 8, 'p': 9, 'q': 0, 'r': 3,
        's': 2, 't': 4, 'u': 6, 'v': 5, 'w': 1, 'x': 3, 'y': 5, 'z': 2
    },
    'r': {
        'a': 4, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 1, 'g': 2, 'h': 3, 'i': 4,
        'j': 4, 'k': 5, 'l': 6, 'm': 5, 'n': 4, 'o': 5, 'p': 6, 'q': 3, 'r': 0,
        's': 3, 't': 1, 'u': 3, 'v': 2, 'w': 2, 'x': 4, 'y': 2, 'z': 5
    },
    's': {
        'a': 1, 'b': 4, 'c': 2, 'd': 1, 'e': 2, 'f': 2, 'g': 3, 'h': 4, 'i': 7,
        'j': 5, 'k': 6, 'l': 7, 'm': 6, 'n': 5, 'o': 8, 'p': 9, 'q': 2, 'r': 3,
        's': 0, 't': 4, 'u': 6, 'v': 3, 'w': 1, 'x': 1, 'y': 5, 'z': 2
    },
    't': {
        'a': 5, 'b': 2, 'c': 4, 'd': 3, 'e': 2, 'f': 2, 'g': 1, 'h': 2, 'i': 3,
        'j': 3, 'k': 4, 'l': 5, 'm': 4, 'n': 3, 'o': 4, 'p': 5, 'q': 4, 'r': 1,
        's': 4, 't': 0, 'u': 2, 'v': 3, 'w': 3, 'x': 5, 'y': 1, 'z': 6
    },
    'u': {
        'a': 7, 'b': 4, 'c': 6, 'd': 5, 'e': 4, 'f': 4, 'g': 3, 'h': 2, 'i': 1,
        'j': 1, 'k': 2, 'l': 3, 'm': 2, 'n': 3, 'o': 2, 'p': 3, 'q': 6, 'r': 3,
        's': 6, 't': 2, 'u': 0, 'v': 5, 'w': 5, 'x': 7, 'y': 1, 'z': 8
    },
    'v': {
        'a': 4, 'b': 1, 'c': 1, 'd': 2, 'e': 3, 'f': 1, 'g': 2, 'h': 3, 'i': 6,
        'j': 4, 'k': 5, 'l': 6, 'm': 3, 'n': 2, 'o': 7, 'p': 8, 'q': 5, 'r': 2,
        's': 3, 't': 3, 'u': 5, 'v': 0, 'w': 4, 'x': 2, 'y': 4, 'z': 3
    },
    'w': {
        'a': 2, 'b': 5, 'c': 3, 'd': 2, 'e': 1, 'f': 3, 'g': 4, 'h': 5, 'i': 6,
        'j': 6, 'k': 7, 'l': 8, 'm': 7, 'n': 6, 'o': 7, 'p': 8, 'q': 1, 'r': 2,
        's': 1, 't': 3, 'u': 5, 'v': 4, 'w': 0, 'x': 2, 'y': 4, 'z': 3
    },
    'x': {
        'a': 2, 'b': 3, 'c': 1, 'd': 2, 'e': 3, 'f': 3, 'g': 4, 'h': 5, 'i': 8,
        'j': 6, 'k': 7, 'l': 8, 'm': 5, 'n': 4, 'o': 9, 'p': 10, 'q': 3,
        'r': 4, 's': 1, 't': 5, 'u': 7, 'v': 2, 'w': 2, 'x': 0, 'y': 6, 'z': 1
    },
    'y': {
        'a': 6, 'b': 3, 'c': 5, 'd': 4, 'e': 3, 'f': 3, 'g': 2, 'h': 1, 'i': 2,
        'j': 2, 'k': 3, 'l': 4, 'm': 3, 'n': 2, 'o': 3, 'p': 4, 'q': 5, 'r': 2,
        's': 5, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 6, 'y': 0, 'z': 7
    },
    'z': {
        'a': 1, 'b': 4, 'c': 2, 'd': 3, 'e': 4, 'f': 4, 'g': 5, 'h': 6, 'i': 9,
        'j': 7, 'k': 8, 'l': 9, 'm': 6, 'n': 5, 'o': 10, 'p': 11, 'q': 2,
        'r': 5, 's': 2, 't': 6, 'u': 8, 'v': 3, 'w': 3, 'x': 1, 'y': 7, 'z': 0
    }
}


def spell_check(filename: str) -> None:
    """Rank words by their proximity to the target"""
    # Take input from file and put it in a dictionary working_dict
    file = open(filename, "rt")
    test_cases = file.readline().strip()
    working_dict: dict = {}
    for i in range(int(test_cases)):
        count_init = file.readline().strip().split()
        working_dict[count_init[0]] = {}
        for k in range(int(count_init[1])):
            working_dict[count_init[0]][file.readline().strip()] = 0
    file.close()

    # Sort working_dict by number and alphabetically into ordered_dict
    ordered_dict = OrderedDict()
    for i in working_dict:
        for item in working_dict[i]:
            working_dict[i][item] = word_distance(i, item)
        wd_items = working_dict[i].items()
        sorted_keys = sorted(wd_items, key=operator.itemgetter(1, 0))
        ordered_dict[i] = sorted_keys

    # Outputs the sorted list in the format required
    for i in ordered_dict:
        for k in ordered_dict[i]:
            print(k[0], k[1])


# def find_axis(key: str):
#     """Find X Axis of a Character"""
#     for i in keyboard:
#         if key in keyboard[i]:
#             return keyboard[i][key], i
#     return False


def word_distance(first_word: str, second_word: str):
    """Find the distance between each character of the word provided."""
    result = 0
    for count, i in enumerate(first_word):
        # axis_one = find_axis(i)
        # axis_two = find_axis(second_word[count])
        # output = abs(axis_one[0] - axis_two[0]) + abs(axis_one[1] - axis_two[1])
        output = abs(pre_keyboard[i][second_word[count]])
        result += output
    return result


def main():
    """Entry point"""
    spell_check("../../../data/projects/keyboard/all_firsthalf.in")
    # print(pre_keyboard['z']['p'])


if __name__ == "__main__":
    main()
