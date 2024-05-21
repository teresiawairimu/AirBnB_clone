#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF commmand to exit the program"""
        return True

    def emptyline(self):
        """Should not execute anything"""
        pass

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
