#!/usr/bin/python3
"""
This is lame
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Jude OC
    """

    def test_init_with_valid_values(self):
       rectangle = Rectangle(2, 4, 1, 1, 5)
        self.assertEqual(rectangle.id, 5)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 1)

    def test_init_with_invalid_values(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 4, -1, 1, 5)

    def test_area(self):
        rectangle = Rectangle(3, 5)
        self.assertEqual(rectangle.area(), 15)

if __name__ == '__main__':
    unittest.main()
