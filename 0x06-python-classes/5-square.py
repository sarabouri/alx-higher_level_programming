#!/usr/bin/python3

"""Define Class Square"""


class Square:
    """initialization of an instance with size attribute
    """
    def __init__(self, size):
        self.size = size
    """ size(self) - retrievess the private attribute size (gitter)"""
    @property
    def size(self):
        """set the actual size of  the square"""
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

    def my_print(self):
        """this prints the suare with # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
