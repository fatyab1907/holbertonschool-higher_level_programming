#!/usr/bin/python3
"""Defines a CountedIterator class that tracks iteration count."""


class CountedIterator:
    """Iterator wrapper that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)
        self.__count = 0

    def get_count(self):
        """Return the current count of iterated items."""
        return self.__count

    def __next__(self):
        """Fetch next item and increment counter."""
        item = next(self.iterator)
        self.__count += 1
        return item

    def __iter__(self):
        """Return self as an iterator."""
        return self
