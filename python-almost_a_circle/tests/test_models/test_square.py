#!/usr/bin/python3
"""Unittests for Square class."""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for testing Square class."""

    def test_square_exists(self):
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        self.assertIsNotNone(s1)

    def test_save_to_file(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")


if __name__ == "__main__":
    unittest.main()
