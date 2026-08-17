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
