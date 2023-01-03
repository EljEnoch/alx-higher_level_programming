#!/usr/bin/python3

"""
Print Square
with #

"""


def print_square(size):
    """
    Function that prints square with #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print((size * "#") + "\n", end="")
