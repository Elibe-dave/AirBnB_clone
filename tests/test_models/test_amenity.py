#!/usr/bin/python3
"""
amenity unit tests
"""
import unittest
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """
    Amenity class tests
    """
    def test_amenity_obj(self):
        """
        Test amenity creation
        """
        from models.amenity import Amenity
        obj = Amenity()
        self.assertEqual(obj.name, "")
