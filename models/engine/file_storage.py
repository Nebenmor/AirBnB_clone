#!/usr/bin/python3
"""
This module is for serializing and deserializing data
"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
import json
import os
from models.state import State
from models.review import Review
from models.city import City


class FileStorage:
    """
    This FileStorage class is for storing, serializing 
    and deserializing data
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method Returns the __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """This method sets an object in the __objects dictionary"""
        id = obj.to_dict()["id"]
        className = obj.to_dict()["__class__"]
        keyName = className+"."+id
        FileStorage.__objects[keyName] = obj

    def save(self):
        """This method serializes the __objects dictionary"""
        filepath = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(filepath, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """This method deserializes the JSON file"""
        filepath = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(filepath):
            try:
                with open(filepath) as f:
                    for key, value in json.load(f).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
                        if "User" in key:
                            data[key] = User(**value)
                        if "Place" in key:
                            data[key] = Place(**value)
                        if "State" in key:
                            data[key] = State(**value)
                        if "City" in key:
                            data[key] = City(**value)
                        if "Amenity" in key:
                            data[key] = Amenity(**value)
                        if "Review" in key:
                            data[key] = Review(**value)
            except Exception:
                pass
