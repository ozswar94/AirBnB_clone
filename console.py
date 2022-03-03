#!/usr/bin/python3

import cmd, sys
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
    class_exist = {"BaseModel": BaseModel}

    storage = FileStorage()
    storage.reload()



    def do_EOF(self,arg):
        return True

    def do_quit(self, arg):
        return True

    def do_create(self, arg):
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

    def do_emptyline(self):
        return False


    def do_show(self, arg):
        args = arg.split()
        if len(arg) == 1:
            print("** class id missing")
        elif len(arg) == 0:
            print("** class name missing")
        else:
            key_to_search = "{}.{}".format(args[0],args[1])
            """if not key_to_search in storage.all():"""
            print(storage.all()[key_to_search])
            """else:
                print("**class doesn't exist **")"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
