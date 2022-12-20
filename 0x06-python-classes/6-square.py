#!/usr/bin/python3
"""class Square"""


class Square:
    """Private instance attribute and instantation with optional"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """getting size"""
        return self.__size

    @property
    def position(self):
        """getting position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Setting size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @position.setter
    def position(self, value):
        """setting position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """area of square"""
        return self.__size ** 2

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for x in range(self.__size):
                for z in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print("")
