#!/usr/bin/python3
"""
This module serves as a basement for future modules to inherit from.
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ This class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes attributes"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    self.__dict__[key] = value
            self.__dict__["created_at"] = datetime.strptime(self.created_at,
                                                            "%Y-%m-%dT%H:"
                                                            "%M:%S.%f")
            self.__dict__["updated_at"] = datetime.strptime(self.updated_at,
                                                            "%Y-%m-%dT%H:" +
                                                            "%M:%S.%f")

    def __str__(self):
        """Yields readable string of the instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        self.__dict__["__class__"] = type(self).__name__
        self.__dict__["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:" +
                                                               "%M:%S.%f")
        self.__dict__["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:" +
                                                               "%M:%S.%f")
        return self.__dict__
