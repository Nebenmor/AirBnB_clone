#!/usr/bin/python3
"""
This is public class attributes that inherit from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class User handles users' information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
