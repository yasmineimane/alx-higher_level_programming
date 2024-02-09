#!/usr/bin/python3
"""
Module for Rectangle class.
"""


class Rectangle:
    """
    Defines Rectangle class.
    """
    def __init__(self, width=0, height=0):
        """
        Constructor

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Property for the width of a rectangle.

        Raises:
            TypeError: If width is not an integer.
            valueError: If width is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Property for the height of a rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Method that calculates the area of a rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method that calculate the perimeter of a rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """
        String method.
        """
        result = ""
        if self.__width != 0 and self.__height != 0:
            result += "\n" .join("#" * self.__width
                                 for i in range(self.__height))
        return result

    def __repr__(self):
        """
        Method that returns a string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
