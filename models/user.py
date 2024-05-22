#!/usr/bin/python3
"""Class User that inherits from BaseModel"""

from models.base_model import BaseModel

class User(BaseModel):
    """Class User that inherits from BaseModel

    Attributes:
        email(str): User's email.
        password(str): User's password.
        first_name(str): User's first_name
        last_name(str): User's last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
