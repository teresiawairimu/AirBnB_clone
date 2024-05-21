#!/usr/bin/python3
"""Serializes instances to JSON file and deserializes JSON file to instances"""

import json
import os


class FileStorage:
    """Serializes instances and deserializes JSON file""""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects to the obj with key <obk class name>.id"""
        key = f"{obj.__class__name.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file(path:__file_path)"""
        obj_dict = {key: obj.to_dict()
                    for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserialize the JSON file to __objects, otherwise, do nothing"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = key.split('.')[0]
                    cls = globals()[cls_name]
                    FileStorage.__objects[key] = cls(**value)
