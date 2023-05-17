#!/usr/bin/python3
"""
Declare the review class
extending from the BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Declare the base model class
    """
    place_id = ""
    user_id = ""
    text = ""
