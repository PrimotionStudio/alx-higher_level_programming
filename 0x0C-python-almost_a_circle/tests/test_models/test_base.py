#!/usr/bin/python3
"""
Unittest functions for base.py.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Im tired
    """

    def test_init_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id + 1, obj2.id)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty_list(self):
        data = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        result = Base.to_json_string(data)
        self.assertIn('"id": 1', result)
        self.assertIn('"name": "John"', result)

    def test_from_json_string_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_non_empty_string(self):
        data_str = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        result = Base.from_json_string(data_str)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['id'], 1)
        self.assertEqual(result[1]['name'], 'Jane')

    def test_create_rectangle(self):
        rectangle = Base.create(id=1, width=2, height=3)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)

    def test_create_square(self):
        square = Base.create(id=2, size=4)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 4)


if __name__ == '__main__':
    unittest.main()
