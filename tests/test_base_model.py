#!/usr/bin/env python
"""Unit test file for the BaseModel class."""
import unittest
import os
from time import sleep
from datetime import datetime
from uuid import uuid4

from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """
    BaseModel class testing methods.
    """

    def test_base_model_instance_id(self):
        """
        Test for the id property of a new model instance.
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))

    def test_base_id_uniqueness(self):
        """
        Test for the uniqueness of a new model instance id.
        """
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_base_string_representation(self):
        """
        Test if string representation of a new model instance
        is appropriate.
        """
        base_model = BaseModel()
        self.assertTrue(str(base_model), "[BaseModel] ({}) {}".format(
            base_model.id, base_model.__dict__))

    def test_id_is_type_of_str(self):
        """
        Test if the id is a type of str.
        """
        base_model = BaseModel()
        self.assertTrue(type(base_model.id), str)

    def test_created_at_is_type_datetime(self):
        """
        Test if the created_at property is a type of datetime.
        """
        base_model = BaseModel()
        self.assertTrue(type(base_model.created_at), datetime.datetime)

    def test_updated_at_is_type_datetime(self):
        """
        Test if the updated_at property is a type of datetime.
        """
        base_model = BaseModel()
        self.assertTrue(type(base_model.updated_at), datetime.datetime)

    def test_updated_at_is_equal_to_created_at_initially(self):
        """
        Test if the updated_at is equal to the created_at initially.
        """
        base_model = BaseModel()
        self.assertTrue(base_model.updated_at, base_model.created_at)


if __name__ == '__main__':
    unittest.main()
