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

    def test_square_1_2_3_4(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_size_string(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_string(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_string(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(5, 2, 1, 10)
        self.assertEqual(str(s), "[Square] (10) 2/1 - 5")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 10, 'x': 2, 'y': 1})

    def test_update(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual(s.id, 10)

    def test_update_89(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_89_1_2(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_89_1_2_3(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_dict_id(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_dict_size(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_update_dict_x(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_update_dict_y(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create_id(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_create_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_y(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_square(self):
        Square.save_to_file([Square(1, 0, 0, 1)])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "size": 1, "x": 0, "y": 0}]')

    def test_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        Square.save_to_file([Square(1)])
        self.assertEqual(len(Square.load_from_file()), 1)


if __name__ == "__main__":
    unittest.main()
