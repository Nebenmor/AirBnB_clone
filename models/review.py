#!/usr/bin/python3
"""
This is public class attributes that inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
