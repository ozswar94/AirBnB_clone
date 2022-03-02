#!/usr/bin/python3
""" class city definition """
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """ class City that inherits from Base """

    state_id = ""
    name = ""
