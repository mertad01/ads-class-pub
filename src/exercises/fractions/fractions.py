#!/usr/bin/env python3
"""
Implementation of the class Fraction
"""

import math


def gcd(num_a: int, num_b: int) -> int:
    """
    Greatest Common Denominator of two integers

    Helper function to simplify fractions
    """
    while num_a % num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_b


class Fraction:
    """Class Fraction"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initializer"""
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be an integer number")
        if not isinstance(denominator, int):
            raise TypeError("Denominator must be an integer number")
        self._num = numerator
        self._den = denominator

    def get_numerator(self) -> int:
        """Return fraction numerator"""
        return self._num

    numerator = property(get_numerator)

    def get_denominator(self) -> int:
        """Return fraction denominator"""
        return self._den

    denominator = property(get_denominator)

    def __str__(self) -> str:
        """Object as a string"""
        common = gcd(self._num, self._den)
        new_num = self._num // common
        new_den = self._den // common

        if new_num > new_den:
            new_test = new_num // new_den
            new_decimal = math.modf(new_num / new_den)[0]
            nd_as_int = new_decimal.as_integer_ratio()
            if new_test > 0:
                return f"{new_test} {nd_as_int[0]}/{nd_as_int[1]}"
            return f"{new_decimal.as_integer_ratio()[0]}/{new_decimal.as_integer_ratio()[1]}"
        if new_num == new_den:
            return "1"
        return f"{self._num // common}/{self._den // common}"

    def __repr__(self) -> str:
        """Object representation"""
        common = gcd(self._num, self._den)
        return f"Fraction({self._num // common}, {self._den // common})"

    def __eq__(self, other: object) -> bool:
        """Equality comparison"""
        if isinstance(other, Fraction):
            first_num = self._num * other.denominator
            second_num = other.numerator * self._den

            return first_num == second_num
        raise TypeError("Can only compare Fractions")

    def __gt__(self, other: object) -> bool:
        """Greater than comparison"""
        if isinstance(other, Fraction):
            first_num = self._num * other.denominator
            second_num = other.numerator * self._den

            return first_num > second_num
        raise TypeError("Can only compare Fractions")

    def __ge__(self, other: object) -> bool:
        """Greater than or equal comparison"""
        if isinstance(other, Fraction):
            return self._num / self._den >= other.numerator / other.denominator
        raise TypeError("Can only compare Fractions")

    def __add__(self, other: object) -> object:
        """Add two fractions"""
        if isinstance(other, Fraction):
            new_num = self._num * other.denominator + self._den * other.numerator
            new_den = self._den * other.denominator
            return Fraction(new_num, new_den)
        raise TypeError("Can only add two Fractions")

    def __sub__(self, other: object) -> object:
        """Subtract two fractions"""
        if isinstance(other, Fraction):
            new_num = self._num * other.denominator - self._den * other.numerator
            new_den = self._den * other.denominator
            return Fraction(new_num, new_den)
        raise TypeError("Can only subtract two Fractions")

    def __mul__(self, other: object) -> object:
        """Multiply two fractions"""
        if isinstance(other, Fraction):
            new_num = self._num * other.numerator
            new_den = self._den * other.denominator
            return Fraction(new_num, new_den)
        raise TypeError("Can only multiply two Fractions")

    def __truediv__(self, other: object) -> object:
        """Divide two fractions"""
        if isinstance(other, Fraction):
            new_num = self._num * other.denominator
            new_den = self._den * other.numerator
            return Fraction(new_num, new_den)
        raise TypeError("Can only divide two Fractions")


def main():
    """Main function"""
    print("Working with Classes")
    fraction1 = Fraction(10, 4)
    print(f"Fraction 1 is {fraction1}")
    fraction2 = Fraction(10, 12)
    print(f"Fraction 2 is {fraction2}")
    fraction3 = Fraction(3, 4)
    print(f"Fraction 3 is {fraction3}")
    print(f"Its id is {id(fraction3)}")
    fraction4 = Fraction(3, 4)
    print(f"Fraction 4 is {fraction4}")
    print(f"Its id is {id(fraction4)}")

    print("Comparison")
    if fraction3 == fraction4:
        print(f"{fraction3} and {fraction4} are equal!")
    else:
        print(f"{fraction3} and {fraction4} are different!")

    print(f"{fraction1} + {fraction2} = {fraction1 + fraction2}")

    print("repr " + repr(Fraction(6, 4)))

    print(f"{Fraction(3, 2)}")

    print(f"{Fraction(1, 3) > Fraction(1, 4)}")
    print(f"{Fraction(1, 2) > Fraction(2, 3)}")

    print(f"{Fraction(1, 2)}")


if __name__ == "__main__":
    main()
