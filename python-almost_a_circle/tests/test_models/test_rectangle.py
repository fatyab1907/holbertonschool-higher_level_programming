#!/usr/bin/python3
"""Unittests for Rectangle class."""
import unittest
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for testing Rectangle class."""

    def test_rectangle_1_2(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_1_2_3(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_1_2_3_4(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_display_without_x_and_y(self):
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_without_y(self):
        r = Rectangle(2, 2, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ##\n ##\n")

    def test_display(self):
        r = Rectangle(2, 2, 1, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")


class TestRectangle_save_to_file(unittest.TestCase):
    """Unittests for save_to_file method in Rectangle."""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(1, 2, 0, 0, 1)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]', f.read())


if __name__ == "__main__":
    unittest.main()
