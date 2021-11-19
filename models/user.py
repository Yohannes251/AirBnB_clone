#!/usr/bin/python3
"""
This module defines a class named User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Implements a User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
