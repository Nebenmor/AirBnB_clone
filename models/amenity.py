#!/usr/bin/python3
"""
This is Public class attributes that inherit from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class represent an amenity

    Attributes:
        name (str): This is the name of the amenity
    """

    name = ""
