#!/usr/bin/python3
"""Define class square"""


class Square:
    """Initialization of an instance
    with size attribute
    """
    def __init__(self, size=0):
        self.__size = size
        """ size(self) - retrievess the private attribute size (gitter)"""
    @property
    def size(self):
        return self.__size

        """def size(self, value): setter for
        private attribute size (setter) """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """Area: returns area of a square """
    def area(self):
        return self.__size * self.__size
