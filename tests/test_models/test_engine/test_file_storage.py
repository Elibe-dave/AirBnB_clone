#!/usr/bin/python3
"""
File Storage class unit test
"""
from unittest import TestCase
from uuid import uuid4
from models.engine.file_storage import FileStorage


class TestFileStorage(TestCase):
    """
    File Storage class tests
    """

    def test_reload(self):
        """Test the reload"""
        obj = FileStorage()
        objects = obj.all()
        self.assertTrue(len(objects) > 0)
