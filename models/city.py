#!/usr/bin/python3
""" class city definition """
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """ class City that inherits from Base
        Attribute:
            state_id: State.id()
            name: name
    """

    state_id = ""
    name = ""
