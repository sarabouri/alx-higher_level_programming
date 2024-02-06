#!/usr/bin/python3
"""Define class square"""


class Square:
    """Initialization of an instance
    with size attribute
    """
    def __init__(self, size=0):
        self.__size = 0
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
