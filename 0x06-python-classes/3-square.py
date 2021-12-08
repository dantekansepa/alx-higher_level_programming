#!/usr/bin/python3
"""Module with an empty class"""


class Sqaure:
     """has public instance area"""
    def __init__(self, size=0):
        """validates the value and type of size
        Args:
        size: size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
            
    def area(self):
         """Returns the area of the current square"""
        return self.__size * self.__size
