#!/usr/bin/python3
"""
This program 'console.py' contains the entry point of 
the command line interpreter
Contains properly imported modules, classes, methods, and functions
"""
import cmd
import ast
import re
import shlex
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel
from models.review import Review
from models.state import State
from models import storage
from models.user import User
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """Custom console class"""
    prompt = "(hbnb) "

    all_class = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

    attr_str = ["name", "amenity_id", "place_id", "state_id",
                "user_id", "city_id", "description", "text",
                "email", "password", "first_name", "last_name"]
    attr_int = ["number_rooms", "number_bathrooms",
                "max_guest", "price_by_night"]
    attr_float = ["latitude", "longitude"]

    def emptyline(self):
        """Performs no action whenever an empty line is entered"""
        pass

    def do_EOF(self, arg):
        """End of File signal to quit the program (Ctrl+D)"""
        return True

    def do_quit(self, arg):
        """Helps to exit the program by handling the quit command"""
        return True

    def do_create(self, arg):
        """
        This reates a new instance of BaseModel 
        and then save it to the JSON file
        """
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        if self.valid(arg):
            args = arg.split()
            if args[0] in classes:
                new = classes[args[0]]()
            storage.save()
            print(new.id)

    def do_show(self, arg):
        """Displays the string representation of an instance"""
        if self.valid(arg, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            print(storage.all()[_key])

    def do_destroy(self, arg):
        """Helps to delete an instance based on the class name and id"""
        if self.valid(arg, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            del storage.all()[_key]
            storage.save()

    def do_all(self, arg):
        """
        This method displays the string of all instances 
        or a specific class
        """
        args = arg.split()
        _len = len(args)
        my_list = []
        if _len >= 1:
            if args[0] not in HBNBCommand.all_class:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if args[0] in key:
                    my_list.append(str(value))
        else:
            for key, value in storage.all().items():
                my_list.append(str(value))
        print(my_list)

    def do_update(self, arg):
        """
        Helps update an instance by either adding 
        or updating an attribute
        """
        if self.valid(arg, True, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            if args[3].startswith('"'):
                match = re.search(r'"([^"]+)"', arg).group(1)
            elif args[3].startswith("'"):
                match = re.search(r'\'([^\']+)\'', arg).group(1)
            else:
                match = args[3]
            if args[2] in HBNBCommand.attr_str:
                setattr(storage.all()[_key], args[2], str(match))
            elif args[2] in HBNBCommand.attr_int:
                setattr(storage.all()[_key], args[2], int(match))
            elif args[2] in HBNBCommand.attr_float:
                setattr(storage.all()[_key], args[2], float(match))
            else:
                setattr(storage.all()[_key], args[2], self.casting(match))
            storage.save()

    def count(self, arg):
        """
        This method counts and retrieves the 
        number of instances of a class
        """
        count = 0
        for key in storage.all():
            if arg[:-1] in key:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
