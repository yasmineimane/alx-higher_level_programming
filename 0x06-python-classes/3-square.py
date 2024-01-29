#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of a side of a square.

        Raises:
            TypeError: if size is not an intger.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Area of this square.
    Returns:
        The size squared.
    """
    def area(self):
        return self.__size**2
