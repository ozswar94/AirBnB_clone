#!/usr/bin/python3
""" class place definition """
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


class Place(BaseModel):
    """ class Place that inherits from Base 
        Attribute:
            city_id: City.id()
            user_id: User.id()
            name: name (string)
            description: description of Place
            number_rooms: int number of rooms
            number_bathrooms: int number of bathrooms
            max_guest: int max guest
            price_by_night: price
            latitude: latitude (float)
            longitude: longitude (float)
            amenity_ids: Amenity.id()
            """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
