#!/usr/bin/python3
"""Define the user model"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Declare the user model extending the base model

    Args:
        email (string): user email
        password (string): user password
        first_name (string): user firstname
        last_name (string): user lastname
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
