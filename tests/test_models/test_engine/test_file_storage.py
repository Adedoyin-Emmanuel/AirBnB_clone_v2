#!/usr/bin/python3
"""
    Unit test file for storage class model.
"""
import unittest
import models
from models import base_model
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestStorageClassModel(unittest.TestCase):
    """Unit test class for the storage class model"""

    def test_storage_init(self):
        """Test storage in __init__.py"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_file_path_is_private_attribute(self):
        """Tests if the file_path is a private class attribute"""
        self.assertTrue(not hasattr(FileStorage(), "__file_path"))

    def test_object_is_private_attribute(self):
        """Tests if the object is a private class attribute"""
        self.assertTrue(not hasattr(FileStorage(), "__objects"))

    def test_init_with_argument(self):
        """Tests the initilization with argument"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_init_without_argument(self):
        """Test the initilization without argument"""
        self.assertEqual(type(FileStorage()), FileStorage)


if __name__ == '__main__':
    unittest.main()
