#!/usr/bin/python3
"""Defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print fish swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat message."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print bird flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish using multiple inheritance."""

    def fly(self):
        """Print flying fish flying message."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print flying fish swimming message."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print flying fish habitat message."""
        print("The flying fish lives both in water and the sky!")
