#!/usr/bin/python3
"""Serializes instances to JSON file and deserializes JSON file to instances"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity


class FileStorage:
    """Serializes instances and deserializes JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects to the obj with key <obk class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file(path:__file_path)"""
        obj_dict = {key: obj.to_dict()
                    for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserialize the JSON file to __objects, otherwise, do nothing"""
        try:
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as f:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        cls_name = value["__class__"]
                        del value["__class__"]
                        self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            return
