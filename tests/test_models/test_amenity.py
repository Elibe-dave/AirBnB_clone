#!/usr/bin/python3
"""
Unittests for amenity class
"""
import unittest
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class
    """
    def test_amenity_obj(self):
        """
        Test creation of amenity
        """
        from models.amenity import Amenity
        obj = Amenity()
        self.assertEqual(obj.name, "")
