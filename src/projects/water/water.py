#!/usr/bin/env python3
"""
`water` implementation

@authors: Adam Mertzenich
"""

JUG_1_MAX = 5
JUG_2_MAX = 3


def gcd(num_one: int, num_two: int) -> int:
    """Greatest Common Denominator"""
    if not num_one % num_two:
        return num_two
    return gcd(num_two, num_one % num_two)


class State:
    """State of the jugs"""

    def __init__(self, jug_1: int, jug_2: int):
        """__init__"""
        if not isinstance(jug_1, int):
            raise TypeError("__init__() should return None, not 'NotImplementedType'")
        if not isinstance(jug_2, int):
            raise TypeError("__init__() should return None, not 'NotImplementedType'")
        if jug_1 > JUG_1_MAX:
            raise ValueError(
                "The proposed value exceeds jug 1 capacity"
            )
        if jug_2 > JUG_2_MAX:
            raise ValueError(
                "The proposed value exceeds jug 2 capacity"
            )
        self._jug_1 = jug_1
        self._jug_2 = jug_2

    def __eq__(self, other: object) -> bool:
        """__eq__"""
        if str(self) == str(other):
            return True
        return False

    def __repr__(self) -> str:
        """__repr__"""
        return f'({self._jug_1}, {self._jug_2})'

    def __str__(self) -> str:
        """__str__"""
        return f'({self._jug_1}, {self._jug_2})'

    def clone(self):
        """Copy a state"""
        return State(self._jug_1, self._jug_2)

    def fill_jug_1(self):
        """Fill jug1 to capacity from the pump"""
        self._jug_1 = JUG_1_MAX

    def fill_jug_2(self):
        """Fill jug2 to capacity from the pump"""
        self._jug_2 = JUG_2_MAX

    def empty_jug_1(self):
        """Pour the water from jug1 onto the ground"""
        self._jug_1 = 0

    def empty_jug_2(self):
        """Pour the water from jug2 onto the ground"""
        self._jug_2 = 0

    def pour_jug_1_to_jug_2(self):
        """Pour as much water as you can from jug1 to jug2 without spilling"""
        jug_one = self._jug_1
        jug_two = self._jug_2

        if jug_one + jug_two > JUG_2_MAX:
            self._jug_1 = jug_two - (JUG_2_MAX - jug_one)
            self._jug_2 = JUG_2_MAX
        elif jug_one == 0:
            pass
        else:
            self._jug_2 += jug_one
            self._jug_1 -= jug_one

    def pour_jug_2_to_jug_1(self):
        """Pour as much water as you can from jug2 to jug1 without spilling"""
        jug_one = self._jug_1
        jug_two = self._jug_2

        if jug_one + jug_two > JUG_1_MAX:
            self._jug_1 = JUG_1_MAX
            self._jug_2 = jug_one - (JUG_1_MAX - jug_two)
        elif jug_two == 0:
            pass
        else:
            self._jug_1 += jug_two
            self._jug_2 -= jug_two


def search(start_state: State, goal: State, moves_lst: list):
    """Find a sequence of states"""
    if start_state in moves_lst:
        return None
    moves_lst.append(start_state)
    if start_state == goal:
        return moves_lst

    worker = start_state.clone()
    worker.fill_jug_1()
    result = search(worker, goal, moves_lst)
    if result:
        return result

    worker = start_state.clone()
    worker.fill_jug_2()
    result = search(worker, goal, moves_lst)
    if result:
        return result

    worker = start_state.clone()
    worker.empty_jug_1()
    result = search(worker, goal, moves_lst)
    if result:
        return result

    worker = start_state.clone()
    worker.empty_jug_2()
    result = search(worker, goal, moves_lst)
    if result:
        return result

    worker = start_state.clone()
    worker.pour_jug_1_to_jug_2()
    result = search(worker, goal, moves_lst)
    if result:
        return result

    worker = start_state.clone()
    worker.pour_jug_2_to_jug_1()
    result = search(worker, goal, moves_lst)
    if result:
        return result


def main():
    """Main"""
    start = State(0, 0)
    goal = State(4, 0)
    moves = list()
    search(start, goal, moves)
    print(", ".join([str(s) for s in moves]))


if __name__ == "__main__":
    main()
