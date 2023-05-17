#!/usr/bin/python3
"""
Base class for the storage model
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State

class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the class __objects property
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, mode='w') as json_file:
            dictionary_storage = {}
            for key, value in self.__objects.items():
                dictionary_storage[key] = value.to_dict()
            json.dump(dictionary_storage, json_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, encoding="utf-8") as json_file:
                for object in json.load(json_file).values():
                    self.new(eval(object["__class__"])(**object))
        except FileNotFoundError:
            return
