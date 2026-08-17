#!/usr/bin/python3
"""Unittests for Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for testing Square."""

    def test_square_init(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_str(self):
        s = Square(5, 2, 1, 10)
        self.assertEqual(str(s), "[Square] (10) 2/1 - 5")


if __name__ == "__main__":
    unittest.main()
