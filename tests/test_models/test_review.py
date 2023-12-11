#!/usr/bin/python3
"""
review unit test
"""
import unittest
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """
    Review class unit test
    """
    def test_review_obj(self):
        """
        Test Review creation
        """
        from models.review import Review
        obj = Review()
        self.assertEqual(obj.text, "")
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
