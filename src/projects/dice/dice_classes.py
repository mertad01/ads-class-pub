#!/usr/bin/env python3
"""
Dice game(s) simulator
"""

import random
from typing import Sequence

random.seed(42)


class Die:
    """Class Die"""

    def __init__(self, possible_values: Sequence) -> None:
        """Class Die constructor"""
        self._all_values = possible_values
        self._value = random.choice(self._all_values)

    @property
    def value(self):
        """Get the die value"""
        return self._value

    @value.setter
    def value(self, _):
        """Value property setter"""
        raise ValueError("You must roll the die to change its value") # pylint: disable=no-self-use

    def __str__(self):
        """__str__ override"""
        return f"{self._value}"

    def roll(self):
        """Roll the die"""
        self._value = random.choice(self._all_values)
        return self._value


class FrozenDie(Die):
    """A die that cannot be rolled"""

    def __init__(self, possible_values: Sequence) -> None:
        """Class FrozenDie constructor"""
        super().__init__(possible_values)
        self._frozen = False

    @property
    def frozen(self) -> bool:
        """Frozen property getter"""
        return self._frozen

    @frozen.setter
    def frozen(self, new_value: bool) -> None:
        """Frozen property setter"""
        self._frozen = new_value

    def roll(self):
        """Roll the die"""
        if self._frozen:
            return self._value
        super().roll()
        return self._value


class Cup:
    """Class Cup"""

    def __init__(self, num_dice: int, num_sides: int = 6) -> None:
        """Class FrozenDie constructor"""
        self._num_dice = num_dice
        self._num_sides = num_sides
        self._dice = [Die(range(1, self._num_sides + 1)) for _ in range(self._num_dice)]

    def __iter__(self):
        """Cup iterator"""
        return iter(self._dice)

    def __str__(self) -> str:
        """__str__ override"""
        return f"[{', '.join([str(i) for i in self._dice ])}]"

    def shake(self) -> None:
        """Shake a cup"""
        self._dice = [Die(range(1, self._num_sides + 1)) for _ in range(self._num_dice)]

    def add(self, die: object) -> None:
        """Add a die to the cup"""
        self._dice.append(die)

    def remove(self, idx: int):
        """Remove a die from the cup"""
        return self._dice.pop(idx)

    def roll(self, *args) -> None:
        """Roll specific dice"""
        for arg in args:
            self._dice[arg - 1] = Die(range(1, self._num_sides + 1))
