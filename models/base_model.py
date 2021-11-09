#!/usr/bin/python3
"""
This module serves as a basement for future modules to inherit from.
"""


from uuid import uuid4
from datetime import datetime, date


class BaseModel:
    """ This class defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initializes attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Yields readable string of the instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        self.__dict__["__class__"] = type(self).__name__
        self.__dict__["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return self.__dict__
