#!/usr/bin/python3
"""A  Rectangle class to define a rectangle"""


class Rectangle:
    """To represent the rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing rectangle class
        Args:
            width: to represent rectangle width
            height: to represent rectangle height
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """to retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """to retrieve height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """To return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """to return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
