#!/usr/bin/python3
"""class Review inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class Review inherits from BaseModel

    Attributes:
        place_id(str): its the place_id
        user_id(str): its the user.id
        text(str): text
    """
    place_id = ""
    user_id = ""
    text = ""
