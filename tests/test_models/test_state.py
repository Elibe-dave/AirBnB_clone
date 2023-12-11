#!/usr/bin/python3
"""
state unit test
"""
import unittest
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """
    State class unit test
    """
    def test_state_obj(self):
        """
        Test State creation
        """
        from models.state import State
        obj = State()
        self.assertEqual(obj.name, "")
