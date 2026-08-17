#!/usr/bin/python3
"""Unittests for Base class."""
import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for Base class."""

    def test_id_auto(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_custom(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{'id': 12}])


if __name__ == "__main__":
    unittest.main()
