#!/usr/bin/python3
"""
    This module contains a class called Review that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class extends the BaseModel class to accomodated reviews"""

    place_id = ""
    user_id = ""
    text = ""
