#!/usr/bin/python3
"""
Initializes package
"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

classes = {"BaseModel": BaseModel}

storage = FileStorage()
FileStorage.reload(storage)
