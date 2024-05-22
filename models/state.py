#!/usr/bin/python3
"""Class State that inherits from BaseModel"""

from models.base_model import BaseModel

class State(BaseModel):
    """Class State that inherits from BaseModel

    Attributes:
        name(str): Name of the state
    """
    name = ""
