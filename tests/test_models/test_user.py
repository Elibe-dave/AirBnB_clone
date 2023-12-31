#!/usr/bin/python3
"""User Class Module unit test
"""
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Base Model test
    """
    def test_init_no_arg(self):
        """create user with no arguments
        """
        tmp = User()
        n_list = []
        check_list = [
                'id', 'created_at',
                'updated_at', '__class__'
                ]
        for key in tmp.to_dict():
            n_list.append(key)
        self.assertEqual(n_list, check_list)

    def test_init_kwargs_args(self):
        """create user with kwargs arguments
        """
        tmp_wa = User(name='wina', age=26, time='now')
        n_list_wa = []
        check_list_wa = [
                'id', 'created_at', 'updated_at',
                'name', 'age', 'time', '__class__'
                ]
        for key in tmp_wa.to_dict():
            n_list_wa.append(key)
        self.assertEqual(n_list_wa, check_list_wa)

    def test_init_args_args(self):
        """create user with args arguments
        """
        tmp_args = User(16, "new", "anything", 36.50)
        nlist_args = []
        check_list = [
                'id', 'created_at',
                'updated_at', '__class__'
                ]
        for key in tmp_args.to_dict():
            nlist_args.append(key)
        self.assertEqual(nlist_args, check_list)

    def test_init_args_and_kwargs(self):
        """create user with args and kwargs
        """
        tmp_args_kwargs = User("every", "new", 26, name="wina", age=16)
        list_ak = []
        check_list = [
                'id', 'created_at', 'updated_at',
                'name', 'age', '__class__'
                ]
        for key in tmp_args_kwargs.to_dict():
            list_ak.append(key)
        self.assertEqual(list_ak, check_list)

    def test_str(self):
        tmp_str = User()
        s_name = type(tmp_str).__name__
        s_id = tmp_str.id
        s_dict = str(tmp_str.__dict__)
        output = "[{}] ({}) {}".format(s_name, s_id, s_dict)
        self.assertEqual(str(tmp_str), output)

    def test_email_attribute(self):
        """
        Test class attributes
        """
        usr = User()
        self.assertEqual(usr.email, "")
        self.assertEqual(usr.password, "")
        self.assertEqual(usr.first_name, "")
        self.assertEqual(usr.last_name, "")


if __name__ == '__main__':
    unittest.main()
