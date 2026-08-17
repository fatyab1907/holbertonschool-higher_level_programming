#!/usr/bin/python3
"""Unittests for Square class."""
import unittest
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for testing Square class."""

    def test_square_1(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_1_2(self):
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_1_2_3(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)


class TestSquare_save_to_file(unittest.TestCase):
    """Unittests for save_to_file method in Square."""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_one_square(self):
        s = Square(1, 0, 0, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual('[{"id": 1, "size": 1, "x": 0, "y": 0}]', f.read())


if __name__ == "__main__":
    unittest.main()
