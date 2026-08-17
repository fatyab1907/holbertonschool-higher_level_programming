#!/usr/bin/python3
"""Defines Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of Square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
