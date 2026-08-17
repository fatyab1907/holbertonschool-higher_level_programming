#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class MetaBaseGeometry(type):
    """Meta class for BaseGeometry."""

    def __dir__(cls):
        """Control dir() output for the class."""
        return [a for a in super().__dir__() if a != '__init_subclass__']


class BaseGeometry(metaclass=MetaBaseGeometry):
    """Represent base geometry."""

    def __dir__(self):
        """Control dir() output for instances."""
        return [a for a in super().__dir__() if a != '__init_subclass__']

    def area(self):
        """Raise an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
