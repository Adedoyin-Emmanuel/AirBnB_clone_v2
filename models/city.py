#!/usr/bin/python3
"""The City model extending the BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Declare the city model"""
    state_id = ""
    name = ""

