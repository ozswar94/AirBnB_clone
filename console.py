#!/usr/bin/python3

import cmd, sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB console"""
    prompt = '(hbnb) '
    file = None
    class_exist = {"BaseModel": BaseModel()}

    def do_EOF(self,arg):
        return True

    def do_quit(self, arg):
        return True

    def do_create(self, arg):
        if arg in self.class_exist.keys():
            obj = self.class_exist[arg]
            print(obj.id)
            obj.save()
        elif len(arg) == 0:
            print("** class name missing **")
            return False
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        if arg in self.class_exist.keys():
            obj = self.class_exist[arg]
        elif len(arg) == 0:
            print("** class name missing **")
            return False
        elif len(arg) < 2:
            print("** instance id missing **")
            return False
        elif arg[2] is not obj.id:
            print("** no instance found **")
            return False
        elif arg[1] is not BaseModel or arg[1] is not BaseModel.__subclasses__
            print("** class doesn't exist **")
            return False
        else:
            print(self.__str__)

    def destroy(self, arg):
        if arg in self.class_exist.keys():
            obj = self.class_exist[arg]
            obj.load()
        elif len(arg) == 0:
            print("** class name missing **")
            return False
        elif len(arg) < 2:
            print("** instance id missing **")
            return False
        elif arg[2] is not obj.id:
            print("** no instance found **")
            return False
        elif arg[1] is not BaseModel or arg[1] is not BaseModel.__subclasses__:
            print("** class doesn't exist **")
            return False

    def do_emptyline(self):
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
