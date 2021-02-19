#!/usr/bin/env python3

first_keyboard = {
    3: ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
    2: ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
    1: ["z", "x", "c", "v", "b", "n", "m"]
}


second_keyboard = {
    3: ("q", "w", "e", "r", "t", "y", "u", "i", "o", "p"),
    2: ("a", "s", "d", "f", "g", "h", "j", "k", "l"),
    1: ("z", "x", "c", "v", "b", "n", "m")
}


third_keyboard = {
    "q": 3, "w", "e", "r", "t", "y", "u", "i", "o", "p"
    # 3: ("q", "w", "e", "r", "t", "y", "u", "i", "o", "p"),
    # 2: ("a", "s", "d", "f", "g", "h", "j", "k", "l"),
    # 1: ("z", "x", "c", "v", "b", "n", "m")
}

def find_axis(key: str):
    """Find X Axis of a Character"""
    for i in second_keyboard:
        if key in second_keyboard[i]:
            return second_keyboard[i].index(key), i
    return False

print(find_axis("w"))
