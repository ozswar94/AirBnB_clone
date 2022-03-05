#!/usr/bin/python3
""" define Class HBNBCommand """

import cmd
import sys
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNB console"""
    prompt = '(hbnb) '
    file = None
    class_exist = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "State": State,
        "Place": Place,
        "Review": Review,
        "Amenity": Amenity
    }
    typeof_attribut = {
        "Integer": [
            "number_rooms",
            "number_bathrooms",
            "max_guest",
            "price_by_night"
            ],
        "Float": ["latitude", "longitude"],
    }

    def do_EOF(self, arg):
        """EOF command to exit with and of file
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_create(self, arg):
        """Create command for create a new instance
        create <class name>
        """
        if arg in self.class_exist.keys():
            obj = self.class_exist[arg]()
            print(obj.id)
            obj.save()
        elif len(arg) == 0:
            print("** class name missing **")
            return False
        else:
            print("** class doesn't exist **")
            return False

    def emptyline(self):
        pass

    def do_show(self, arg):
        """Show command to print instance
        show <class name> <id>
        """
        args = arg.split()
        if len(arg) == 1:
            print("** class id missing")
        elif len(arg) == 0:
            print("** class name missing")
        else:
            key_to_search = "{}.{}".format(args[0], args[1])
            if key_to_search in storage.all():
                print(storage.all()[key_to_search])
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """All command to print all instance or all instance by class name
        all | all <class name>
        """
        if arg not in self.class_exist:
            print("** class doesn't exist **")
        if len(arg) == 0:
            for key, value in storage.all().items():
                print(storage.all()[key])
        else:
            for key, value in storage.all().items():
                class_name = key.split('.')
                if class_name[0] == arg:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroy command to remove instance
        destroy <class name> <id>
        """
        args = arg.split()
        if len(arg) == 1:
            print("** class id missing")
        elif len(arg) == 0:
            print("** class name missing")
        else:
            key_to_search = "{}.{}".format(args[0], args[1])
            if key_to_search in storage.all():
                del storage.all()[key_to_search]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Update command to modify instance and save it
        update <class name> <id> <attribute name> <attribute value>
        """
        args = arg.split()

        if len(args) != 0:
            if args[0] in self.class_exist:
                if len(args) >= 2:
                    k = "{}.{}".format(args[0], args[1])
                    if k in storage.all():
                        if len(args) >= 3:
                            if len(args) == 4:
                                value = args[3].strip('"')
                                if args[2] in self.typeof_attribut["Integer"]:
                                    try:
                                        value = int(value)
                                    except ValueError:
                                        value = 0
                                    setattr(storage.all()[k], args[2], value)
                                elif args[2] in self.typeof_attribut["Float"]:
                                    try:
                                        value = float(value)
                                    except ValueError:
                                        value = 0.0
                                    setattr(storage.all()[k], args[2], value)
                                else:
                                    setattr(storage.all()[k], args[2], value)
                                storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist *")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
