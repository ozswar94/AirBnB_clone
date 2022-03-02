#!/usr/bin/python
""" define BaseModel class """


from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        self.updated_at = self.updated_at.now()

    def to_dict(self):
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
