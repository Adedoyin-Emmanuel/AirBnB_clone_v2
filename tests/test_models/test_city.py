#!/usr/bin/python3
"""Test cases for the City class"""
import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_attrs_are_class_attrs(self):
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.city, attr)), str)
            self.assertFalse(bool(getattr(self.city, attr)))

    def test_city_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))
