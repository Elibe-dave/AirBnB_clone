#!/usr/bin/python3
"""This is the  BaseModel for the AirBnB Project."""
import uuid
from models import storage
from datetime import datetime


class BaseModel():
    """class to define all common attributes/methods"""
    def __init__(self, *args, **kwargs):
        """Initialiazes an instace of BaseModel.

        Arguments:
            *args (tuple): Arguments from instance initialization.
            **kwargs (dictionary): Arguments as key-value pairs.
        """
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for arg in kwargs:
                if arg == "created_at":
                    va = datetime.strptime(kwargs[arg], '%Y-%m-%dT%H:%M:%S.%f')
                    self.created_at = va
                elif arg == "updated_at":
                    va = datetime.strptime(kwargs[arg], '%Y-%m-%dT%H:%M:%S.%f')
                    self.updated_at = va
                elif arg != "__class__":
                    setattr(self, arg, kwargs[arg])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Provides a human-readable string representation for an object.

        Returns:
            A string containing the object's class name, ID, and attributes.
        """
        s_name = type(self).__name__
        s_id = self.id
        s_dict = str(self.__dict__)
        return "[{}] ({}) {}".format(s_name, s_id, s_dict)

    def save(self):
        """Updates the object's timestamp and persists
        the data into the JSON file.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object
        for JSON serialization.
        """
        base_dictionary = {}
        for item in self.__dict__:
            base_dictionary[item] = self.__dict__[item]
        base_dictionary["__class__"] = type(self).__name__
        base_dictionary["created_at"] = self.created_at.isoformat()
        base_dictionary["updated_at"] = self.updated_at.isoformat()
        return base_dictionary
