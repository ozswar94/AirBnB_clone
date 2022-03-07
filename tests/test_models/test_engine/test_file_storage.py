#!/usr/bin/python3
""" test class FileStorage """


import unittest
import os
import sys
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test class FileStorage """

    def test_all(self):
        """ test return type of method all """
        storage = FileStorage()
        test_type = storage.all()
        self.assertEqual(type(test_type), dict)

    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_save_exist_file(self):
        """ test if json file exixt """
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_read_json(self):
        """ test json is readable """
        storage = FileStorage()
        storage.save()

        with open("file.json", 'r') as json_file:
            content = json.load(json_file)

        self.assertTrue(type(content), dict)

    def test_reaload_without_file(self):
        """ test method reload """
        storage = FileStorage()
        try:
            storage.reload()
            self.assertTrue(True)
        except TypeError:
            self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
