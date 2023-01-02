#!/usr/bin/python3
"""
class Rectangle
defines rectangle
width and height
"""


class Rectangle:
    """
    define rectangle with w + h
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """get area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """get perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        """print square"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec = (self.__height * ((self.__width * str(self.print_symbol)) +
               '\n'))
        return rec[:-1]

    def __repr__(self):
        """return string representation"""
        new = (self.__width, self.__height)
        return "Rectangle" + str(new)

    def __del__(self):
        """deleting"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns biggest rectangle on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle"""
        return Rectangle(size, size)
