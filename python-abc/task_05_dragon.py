#!/usr/bin/python3
"""Defines SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """Mixin providing swimming capability."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying capability."""

    def fly(self):
        """Print flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon inheriting from SwimMixin and FlyMixin."""

    def roar(self):
        """Print dragon roaring message."""
        print("The dragon roars!")
