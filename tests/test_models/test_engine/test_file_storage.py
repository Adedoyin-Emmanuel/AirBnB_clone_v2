#!/usr/bin/python3
"""
    Unit test file for storage class model.
"""
import unittest
import models
import os
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


class TestStorageClassMethods(unittest.TestCase):
    """Tests the storage class methods"""
    @classmethod
    def setUp(self):
        """Method to execute before testing"""
        try:
            os.rename("file.json", "test.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Method to execute after testing is done"""
        try:
            os.remove("file.json")
        except IOError:
            pass

        """Rename the file.json"""
        try:
            os.rename("test.json", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage_objects = {}

    def test_all_method(self):
        """Tests the all method of the FileStorage object"""
        self.assertTrue(type(models.storage.all()) is dict)
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        """Test the new method of the FileStorage object"""
        base_model = BaseModel()
        self.assertIn("BaseModel." + base_model.id,
                      models.storage.all().keys())
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_reload_method(self):
        """Tests the reload method of the FileStorage object"""
        base_model = BaseModel()
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, obj)

        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_save_method(self):
        """Test the save method of the FileStorage object"""
        base_model = BaseModel()
        models.storage.save()

        with open("file.json", "r") as json_file:
            text_to_save = json_file.read()
            self.assertIn("BaseModel." + base_model.id, text_to_save)

        with self.assertRaises(TypeError):
            models.storage.save(None)


if __name__ == '__main__':
    unittest.main()
