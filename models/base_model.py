#!/usr/bin/python3
"""
Base class declaration module for other classes
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class model declaration
    """

    def __init__(self, *args, **kwargs):
        """
            public instance attributes
            id: (string) assign with an uuid when an instance is created
            created_at: (datetime) assign with the current datetime
            when an instance is created
            updated_at: (datetime) assign with the current datetime
            when an instance is created
            and it will be updated every time you change your object
        """
        if not kwargs:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            storage.new(self)
        else:
            if '__class__' in kwargs:
                del kwargs['__class__']
            for value in ('created_at', 'updated_at'):
                if value in kwargs:
                    kwargs[value] = datetime.fromisoformat(
                        kwargs[value])
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Returns the string representation of the Base class model.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns the dict representation of the Base class model.
        """
        custom_dict = {}
        custom_dict.update(self.__dict__)
        custom_dict.update({'__class__': type(self).__name__})
        custom_dict['created_at'] = self.created_at.isoformat()
        custom_dict['updated_at'] = self.updated_at.isoformat()
        return custom_dict
