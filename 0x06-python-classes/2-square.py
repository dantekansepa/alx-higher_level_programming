#!/usr/bin/python3
"""module contains class Square"""

class Sqaure:
    """validates the size of a square
    """
    def __init__(self, size=0):
        """Instantiation with optional size: def __init__(self, size=0):
           size must be an integer, otherwise raise a TypeError exception 
           with the message size must be an integer
           if size is less than 0, raise a ValueError 
           exception with the message size must be >= 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
