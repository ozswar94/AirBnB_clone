#!/usr/bin/python3
""" class review description """
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """ class review
        Attribute:
            place_id: Place.id()
            user_id: User.id()
            test: test(string)
    """
    place_id = ""
    user_id = ""
    test = ""
