#!/usr/bin/python3
"""Defines Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle."""
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle."""
        self.__height = value

    @property
    def x(self):
        """Get x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x coordinate."""
        self.__x = value

    @property
    def y(self):
        """Get y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y coordinate."""
        self.__y = value
