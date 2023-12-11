#!/usr/bin/python3
"""
File Storage class unit test
"""
from unittest import TestCase
from uuid import uuid4
from models.engine.file_storage import FileStorage


class TestFileStorage(TestCase):
    """
    File Storage class module unit test
    """

    def test_reload(self):
        """ reload method test """
        obj = FileStorage()
        objects = obj.all()
        self.assertTrue(len(objects) > 0)
