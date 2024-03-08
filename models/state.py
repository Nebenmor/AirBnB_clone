#!/usr/bin/python3
"""
This is public class attributes that inherit from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This present a state.

    Attributes:
        name (str): This is the name of the state.
    """

    name = ""
