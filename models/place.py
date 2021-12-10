#!/usr/bin/python3
"""
    This module contains a class called Place that inherits from BaseModel
"""


class Place(BaseModel):
    """This class extends the BaseModel class to accomodated places"""

    city_id = ""
    user_id = ""
    name = ""
    descreption = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
