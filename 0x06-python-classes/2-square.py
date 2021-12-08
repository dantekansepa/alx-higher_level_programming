#!/usr/bin/python3
"""module contains class Square"""

class Sqaure:
    """validates the size of a square"""
    def __init__(self, size=0):
        """validates the type of size
        Args:
        size: int type square size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
