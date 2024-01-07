#!/usr/bin/python3
""" A module for printing a square """


def print_square(size):
    """
    A function for printing a square
    Args:
        size: size of the square
    Raises:
         TypeError: If size is not an integer
         ValueError: If size less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
