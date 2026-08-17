#!/usr/bin/python3
"""Unittests for Square class."""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for testing Square class."""

    def test_square_init(self):
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        s4 = Square(1, 2, 3, 4)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(5, 2, 1, 10)
        self.assertEqual(str(s), "[Square] (10) 2/1 - 5")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 10, 'x': 2, 'y': 1})

    def test_update_args(self):
        s = Square(10, 10, 10, 10)
        s.update()
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 1)
        self.assertEqual(s.size, 1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create(self):
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)
        s2 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s2.size, 1)
        s3 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s3.x, 2)
        s4 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s4.y, 3)

    def test_save_to_file(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_load_from_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([Square(1)])
        self.assertEqual(len(Square.load_from_file()), 1)


if __name__ == "__main__":
    unittest.main()
