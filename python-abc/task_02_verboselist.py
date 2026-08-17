#!/usr/bin/python3
"""Extending the Python List with Notifications."""


class VerboseList(list):
    """Custom list class that prints notifications when modified."""

    def append(self, item):
        """Append item and print notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extend list and print notification."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Remove item and print notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and print notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
