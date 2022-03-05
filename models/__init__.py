#!/usr/bin/python3
"""
Create an unique FileStorage instance for read and write in JSON file
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
