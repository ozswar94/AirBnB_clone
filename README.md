# AirBnB Clone
This repository is a project for Holberton School. It is the beginning of a bigger project which will be a clone of AirBnB. It contains:
/models:
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
	/[engine]:
-/console:
	[console.py]:
		You must use the module cmd
		Your class definition must be: class HBNBCommand(cmd.Cmd):
		Your command interpreter should implement:
			quit and EOF to exit the program
			help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
			a custom prompt: (hbnb)
			an empty line + ENTER shouldn’t execute anything

		commands of console:
			create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
				If the class name is missing, print ** class name missing ** (ex: $ create)
				If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
			show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
				If the class name is missing, print ** class name missing ** (ex: $ show)
				If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
				If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
				If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
			destroy: Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
				If the class name is missing, print ** class name missing ** (ex: $ destroy)
				If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
				If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
				If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
			all: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
				The printed result must be a list of strings (like the example below)
				If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
			update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
			Usage: update <class name> <id> <attribute name> "<attribute value>"
				Only one attribute can be updated at the time
				You can assume the attribute name is valid (exists for this model)
				The attribute value must be casted to the attribute type
				If the class name is missing, print ** class name missing ** (ex: $ update)
				If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
				If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
				If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)
				If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
				If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)
				All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
				id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
				Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime
-/tests:
	[tests/tests_model]:
		__init__.py
		test_base_model.py: tests for class BaseModel
		/test_engine: tests for engine:
			.gitignore
			__init__.py
			test_file_storage.py
		test_place.py: test for class Place
		test_review.py: test for class Review
		test_user.py: test for class User
		test_amenity.py
		test_city.py
		test_state.py
-file.json
-AUTHORS
