#/usr/bin/python3
"""
This module defines a FileStorage class that performs JSON operations
"""


import json


class FileStorage:
    """This class handles serialization and deserialization of objects"""

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """Returns the dictionary which holds the objects"""
        return self.__objects

    def new(self, obj):
        """Populates the __objects dictionary with new insatnces"""
        key = type(obj).__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file (storage.json)"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            data = open(self.__file_path,)
            __objects = json.load(data)
        except Exception:
            pass



