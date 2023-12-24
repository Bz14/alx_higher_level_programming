#!/usr/bin/python3
"""Square module"""


class Square:
    """Class for defining a square"""
    def __init__(self, size=0, position=(0, 0)):
        """This is the init function."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter function for size"""
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print()
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(self.size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()

    def __str__(self):
        """Print representation of a square."""
        if (self.__size != 0):
            [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
