#!/usr/bin/python3
"""Test cases for the user class in models.user"""
import unittest
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the user class model"""

    def test_attrs_are_class_attrs(self):
        """Test the the attributes are class attributes"""
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_user_is_a_subclass_of_basemodel(self):
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_class_attrs(self):
        user = User()
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name), str)
        self.assertTrue(user.first_name == "")
        self.assertTrue(user.last_name == "")
