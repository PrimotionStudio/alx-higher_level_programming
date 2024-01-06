#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for testing the max_integer \
    function using unit tests"""

    def test_ordered(self):
        """Tests if the function returns the max \
        integer in an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_rev(self):
        """Tests if the function returns the max \
        integer in a reversed list"""
        self.assertEqual(max_integer([4,3,2,1]), 4)

    def test_rand(self):
        """Tests if the function returns the max \
        integer in a random order list"""
        self.assertEqual(max_integer([2,4,1,3]), 4)

    def test_dupl(self):
        """Tests if the function handles duplicate values correctly"""
        self.assertEqual(max_integer([3,5,5,5,3]), 5)

    def test_empty(self):
        """Tests if the function returns None for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        """Tests if the function handles a string input \
        correctly"""
        self.assertEqual(max_integer("Hello"), "o")

    def test_one_digit(self):
        """Tests if the function handles a list with a single \
        digit correctly"""
        self.assertEqual(max_integer([1]), 1)

    def test_mixed_types(self):
        """Tests if the function raises a TypeError for mixed \
        types in the list"""
        self.assertRaises(TypeError, max_integer, [1, 1.5, 'Hey'])

    def test_float(self):
        """Tests if the function handles a list of floating-point \
        numbers correctly"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_int_float(self):
        """Tests if the function handles a list with a \
        mix of integers and floats correctly"""
        self.assertEqual(max_integer([1, 1.5, 3, 3.1]), 3.1)

    def test_strings(self):
        """Tests if the function handles a list of strings correctly"""
        self.assertEqual(max_integer(["Hey", "Hi", "Hello"]), "Hi")
