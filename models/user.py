#!/usr/bin/python3
"""User classs module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class module for User
    Arguments:
        email (str)
        password (str)
        first_name (str)
        last_name (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
