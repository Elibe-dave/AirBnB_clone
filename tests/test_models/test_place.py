#!/usr/bin/python3
"""
place unit test
"""
import unittest
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """
    Place class unit test
    """
    def test_place_obj(self):
        """
        Test Place creation
        """
        from models.place import Place
        obj = Place()
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])
