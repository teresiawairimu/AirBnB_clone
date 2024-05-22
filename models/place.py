#!/usr/bin/python3
"""Class Place inherits from BaseModel"""

from models.base_model import BaseModel

class Place(BaseModel):
    """class Place inherits from BaseModel

    Attributes:
        city_id(str): The id of the city
        user_id(str): The id of the user
        name(str): The name of the place
        description(str): The name of the description
        number_rooms(int): The number of rooms
        number_bathrooms(int): THe number of bathrooms
        max_guest(int): The maximum number of guests
        price_by_night(int): The price of staying a night
        latitude(float): The latitude of the place
        longitude(float): The longitude of the place
        amenity_ids(list of string): list of amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

