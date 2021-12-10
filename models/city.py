#!/usr/bin/python3
"""
    This module contains a class called City that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class extends the BaseModel class to accomodated cities"""

    state_id = ""
    name = ""
