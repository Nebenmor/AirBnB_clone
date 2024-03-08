#!/usr/bin/python3
"""
The public class attributes that inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent a city.

    Attributes:
        state_id (str): This is the state id.
        name (str): This is the name of the city.
    """

    state_id = ""
    name = ""
