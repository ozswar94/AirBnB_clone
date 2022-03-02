# AirBnB Clone
This repository is a project for Holberton School. It is a clone of AirBnB. It contains:
models:
	[__init__.py]:
		__init__(self, *args, **kwargs):
			you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
			*args won’t be used
			if kwargs is not empty:
				each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
				each value of this dictionary is the value of this attribute name
				Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
			otherwise:
				create id and created_at as you did previously (new instance)
		import file_storage.py
		create the variable storage, an instance of FileStorage
		call reload() method on this variable

	[models/base_model.py]:
		Public instance attributes:
			id: string - assign with an uuid when an instance is created:
				you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
				the goal is to have unique id for each BaseModel
			created_at: datetime - assign with the current datetime when an instance is created
			updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
		__str__: should print: [<class name>] (<self.id>) <self.__dict__>
		Public instance methods:
			save(self): updates the public instance attribute updated_at with the current datetime
			to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
				by using self.__dict__, only instance attributes set will be returned
				a key __class__ must be added to this dictionary with the class name of the object
				created_at and updated_at must be converted to string object in ISO format:
					format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
					you can use isoformat() of datetime object
				This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel
		import the variable storage
		in the method save(self):
		call save(self) method of storage
		__init__(self, *args, **kwargs):
			if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage

	[models/engine]:
		[models/engine/file_storage.py]
		Private class attributes:
			__file_path: string - path to the JSON file (ex: file.json)
			__objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
		Public instance methods:
			all(self): returns the dictionary __objects
			new(self, obj): sets in __objects the obj with key <obj class name>.id
			save(self): serializes __objects to the JSON file (path: __file_path)
			reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
	[models.amenity.py]:
		Public class attributes:
			name: string - empty string

	[models.city.py]:
		Public class attributes:
			state_id: string - empty string: it will be the State.id
			name: string - empty string

	[models.place.py]:
		Public class attributes:
			city_id: string - empty string: it will be the City.id
			user_id: string - empty string: it will be the User.id
			name: string - empty string
			description: string - empty string
			number_rooms: integer - 0
			number_bathrooms: integer - 0
			max_guest: integer - 0
			price_by_night: integer - 0
			latitude: float - 0.0
			longitude: float - 0.0
			amenity_ids: list of string - empty list: it will be the list of Amenity.id later

	[models.review.py]:
		Public class attributes:
			place_id: string - empty string: it will be the Place.id
			user_id: string - empty string: it will be the User.id
			text: string - empty string

	[models.state.py]:
		Public class attributes:
			name: string - empty string

	[models/user.py]:
		Public class attributes:
			email: string - empty string
			password: string - empty string
			first_name: string - empty string
			last_name: string - empty string
-test_base_model.py
