#!/usr/bin/python3
"""
city unit test
"""
import unittest
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """
    City class unit test
    """
    def test_city_obj(self):
        """
        Test City creation
        """
        from models.city import City
        obj = City()
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.state_id, "")
