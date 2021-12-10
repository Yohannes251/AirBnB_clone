#!/usr/bin/python3
"""
Initializes package
"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

storage = FileStorage()
FileStorage.reload(storage)
