#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User}

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_object = self.classes[class_name]()
        new_object.save()
        print(new_object.id)

    def do_show(self, args):
        """Prints instance's string representation based on class name and id"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        object_id = args[1]
        key = f"{class_name}.{object_id}"
        if key not in models.storage.all():
            print("** no instance found **")
            return 
        print(models.storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on class name and id"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        object_id = args[1]
        key = f"{class_name}.{object_id}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, args):
        """Prints all instances' representation based or not on class name"""
        args = args.split()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        if args:
            class_name = args[0]
            print([str(value) for key, value in objects.items() if key.startswith(class_name)])
        else:
            print([str(value) for value in objects.values()])

    def do_update(self, args):
        """Updates instance based on classname & id by adding/updating attribute"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        object_id = args[1]
        key = f"{class_name}.{object_id}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        object_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        object_value = args[3]
        instance = models.storage.all()[key]
        try:
            casted_value = eval(object_value)
        except (SyntaxError, NameError):
            casted_value = object_value
        setattr(instance, object_name, casted_value)
        instance.save()

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
