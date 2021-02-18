#!/usr/bin/env python3
"""String search"""

THE_STRING = "aaab"


def find_non_repeat(a_string: str) -> str:
    """Find the first unique character in a string"""
    for i in a_string:
        if (a_string.count(i) == 1):
            return i
        return "None"



def main():
    """Main function"""
    print(find_non_repeat(THE_STRING))


if __name__ == "__main__":
    main()
