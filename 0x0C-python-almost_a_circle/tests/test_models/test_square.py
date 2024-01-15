#!/usr/bin/python3
"""
Im so bored
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    13 reasons why
    """

    def test_init_with_valid_values(self):
        square = Square(3, 2, 2, 8)
        self.assertEqual(square.id, 8)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)

    def test_init_with_invalid_values(self):
        with self.assertRaises(ValueError):
            Square(-3, 2, 2, 8)

    def test_area(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)

if __name__ == '__main__':
    unittest.main()
