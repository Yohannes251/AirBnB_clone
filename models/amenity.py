#!/usr/bin/python3
"""
    This module contains a class called Amenity that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class extends the BaseModel class to accomodated amenities"""

    name = ""
