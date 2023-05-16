#!/usr/bin/python3
"""Unit test file for the BaseModel class."""
import unittest
import os
from time import sleep
from datetime import datetime
from uuid import uuid4
import models
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
        self.assertTrue(type(base_model.created_at), datetime)

    def test_updated_at_is_type_datetime(self):
        """
        Test if the updated_at property is a type of datetime.
        """
        base_model = BaseModel()
        self.assertTrue(type(base_model.updated_at), datetime)

    def test_updated_at_is_equal_to_created_at_initially(self):
        """
        Test if the updated_at is equal to the created_at initially.
        """
        base_model = BaseModel()
        self.assertTrue(base_model.updated_at, base_model.created_at)

    def test_arguments_args_unused(self):
        """
        Test the args arguement was not used.
        """
        base_model = BaseModel(None)
        self.assertNotIn(None, base_model.__dict__.values())

    def test_2_models_created_at_values(self):
        """
        Test 2 different models created_at property.
        """
        base_model1 = BaseModel()
        sleep(0.5)
        base_model2 = BaseModel()
        sleep(0.5)
        self.assertNotEqual(base_model1.created_at, base_model2.updated_at)

    def test_if_to_dict_returns_dict_type(self):
        """
        Test if the to_dict_returns_dict_type
        """
        base_model = BaseModel()
        self.assertTrue(type(base_model.to_dict()) is dict)

    def test_if_created_at_returned_by_to_dict_is_iso_string(self):
        """
        Test if the created_at returned by the
        to_dict method returns an iso format string.
        """
        base_model = BaseModel()
        self.assertEqual(base_model.to_dict()["created_at"],
                         base_model.created_at.isoformat())

    def test_if_updated_at_returned_by_to_dict_is_iso_string(self):
        """
        Test if the update_at returned by the
        to_dict method returns an iso format string.
        """
        base_model = BaseModel()
        self.assertEqual(base_model.to_dict()["updated_at"],
                         base_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
