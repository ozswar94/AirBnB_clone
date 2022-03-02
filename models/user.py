#!/usr/bin/python3
""" class user module """
from models.base_model import BaseModel


class User(BaseModel):
    """ class User that inherits from Base """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
