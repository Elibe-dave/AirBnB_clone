#!/usr/bin/python3
"""
Unittests for state class
"""
import unittest
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """
    Test cases for State class
    """
    def test_state_obj(self):
        """
        Test creation of state instance
        """
        from models.state import State
        obj = State()
        self.assertEqual(obj.name, "")
