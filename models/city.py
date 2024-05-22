#!/usr/bin/python3
"""Class City inherits from BaseModel"""

from models.base_model import BaseModel

class City(BaseModel):
    """Class City inherits from BaseModel

    Attributes:
        state_id(str): the state id.
        name(str): the name of the city
    """
    state_id = ""
    name = ""
