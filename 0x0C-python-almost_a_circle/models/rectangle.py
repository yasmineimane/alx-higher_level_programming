#!/usr/bin/python3
"""
Module for Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    defines Rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.validate_integer("width", value, False)
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.validate_integer("height", value, False)
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.validate_integer("x", value, False)
            self.__x = value

        @property
        def y(slef):
            return self.__y

        @y.setter
        def y(self, value):
            self.validate_integer("y", value, False)
            self.__y = value

        def validate_integer(self, name, value, eq=True):
            '''Method for validating the value.'''
            if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
            if eq and value < 0:
                raise ValueError("{} must be >= 0".format(name))
            elif not eq and value <= 0:
                raise ValueError("{} must be > 0".format(name))
