#!/usr/bin/python3
"""Abstract Animal Class and Subclasses Dog and Cat."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method sound."""
        pass


class Dog(Animal):
    """Subclass Dog."""

    def sound(self):
        """Return Bark."""
        return "Bark"


class Cat(Animal):
    """Subclass Cat."""

    def sound(self):
        """Return Meow."""
        return "Meow"
