#!/usr/bin/python3
"""
Initializes package
"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User

classes = {"BaseModel": BaseModel, "User": User}

storage = FileStorage()
FileStorage.reload(storage)
