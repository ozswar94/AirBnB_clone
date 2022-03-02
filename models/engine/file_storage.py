#!/usr/bin/python3
""" define FileStorage Class """


from models.base_model import BaseModel
import json


class FileStorage:
    """ class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the objects """
        return self.__objects

    def new(self, obj):
        """ set up object with id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ save object in JSON """
        with open(self.__file_path, 'w') as json_file:
            output = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(output, json_file)

    def reload(self):
        """ reload file in JSON """
        try:
            with open(self.__file_path, "r") as json_file:
                list_obj = json.load(json_file)
                for val_obj in list_obj.values():
                    name = val_obj["__class__"]
                    del val_obj["__class__"]
                    self.new(eval(name)(**val_obj))
        except:
            return
