#!/usr/bin/env python3
"""Docstring"""

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

bing_bong = {
    'ifpv': {
        'iopc': 0,
        'icpc': 0,
        'gcpc': 0
    },
    'edc': {
        'wsx': 0,
        'edc': 0,
        'rfv': 0,
        'plm': 0,
        'qed': 0
    }
}

# file = open("../../../data/projects/keyboard/sample.in", "rt")
# test_cases = file.readline().strip()
# working_dict = {
#     file.readline().strip().split()[0]: {
#         file.readline().strip(): 0,
#         file.readline().strip(): 0,
#         file.readline().strip(): 0
#     },
#     file.readline().strip().split()[0]: {
#         file.readline().strip(): 0,
#         file.readline().strip(): 0,
#         file.readline().strip(): 0,
#         file.readline().strip(): 0,
#         file.readline().strip(): 0,
#     }
# }
# print(working_dict)
# file.close()

file = open("../../../data/projects/keyboard/sample.in", "rt")

test_cases = file.readline().strip()
working_dict = {}
for i in range(int(test_cases)):
    count_init = file.readline().strip().split()
    working_dict[count_init[0]] = {}
    for k in range(int(count_init[1])):
        working_dict[count_init[0]][file.readline().strip()] = 0

print(working_dict)
file.close()

    # new = {content[1]: (content[2], content[3], content[4])}
    # new_two = {content[5]: (content[6], content[7], content[8], content[9], content[10])}
    # print(new)
    # print(new_two)
# content = file.read().splitlines()
# test_cases = int(content[0])
# for i in range(test_cases):
#     print(content[1])

# for i in content[1:]:
#     if i[-2::].replace(" ", "").isdigit():
#         next_lines = int(i[-2::].replace(" ", ""))
#         print(next_lines)
