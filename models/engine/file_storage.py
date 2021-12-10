#!/usr/bin/python3
"""
This module defines a FileStorage class that performs JSON operations.
"""


import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
