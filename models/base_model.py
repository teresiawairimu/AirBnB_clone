#!/usr/bin/python3
"""This module defines all common attributes and methods"""

from datetime import datetime
import uuid


class BaseModel:
    """This class defines common attributes and methods for the other classes

    Attributes:
        id(str): Unique identifier of the instance
        name(str): Name of the instance
        created_at(datetime): The datetime when the instance was created
        updated_at(datetime): The datetime when the instance was last updated
    """

    def __init__(self, name=""):
        """Initializes a new BaseModel object

        Args:
            id(str): Unique identifier of the instance
            name(str): Name of the instance created
            created_at(datetime): The datetime when the instance was created
            updated_at(datetime): Datetime when the instance was last updated
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """Updates updated-at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary containing keys/values of instance's __dict__"""
        model_data = self.__dict__.copy()
        model_data['__class__'] = self.__class__.__name__
        model_data['created_at'] = self.created_at.isoformat()
        model_data['updated_at'] = self.updated_at.isoformat()
        return model_data

    def __str__(self):
        """Return a tring representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
