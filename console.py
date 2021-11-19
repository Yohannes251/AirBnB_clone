#!/usr/bin/python3
"""
This module defines classes that interprete commands
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = ("(hbnb) ")

    def do_quit(self, args):
        """ Implements Quit command that exits the program"""
        return True

    def do_EOF(self, args):
        """ Exits the program when recieving EOF signal"""
        return True

    def emptyline(self):
        """Brings next prompt when recieving Enter or empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
