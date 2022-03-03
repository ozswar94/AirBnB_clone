#!/usr/bin/python3

import cmd, sys
import models


class HBNBCommand(cmd.Cmd):
    """HBNB console"""
    prompt = '(hbnb) '
    file = None

    def do_EOF(self,arg):
        return True

    def do_quit(self, arg):
        return True

    def do_emptyline(self):
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
